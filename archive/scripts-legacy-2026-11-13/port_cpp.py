import os
import re
import sys

def remove_method(text, method_name):
    # This is a naive regex but it handles removing functions by name
    # We want to remove something like `void ClassName::serialize(...) { ... }`
    # Because braces can be nested, we should do a basic brace parser
    start_idx = text.find(method_name)
    while start_idx != -1:
        # Check if it looks like a method signature
        if '(' in text[start_idx:start_idx+100]:
            # find the opening brace
            brace_idx = text.find('{', start_idx)
            if brace_idx != -1 and brace_idx - start_idx < 200: # reasonable distance
                open_braces = 0
                end_idx = -1
                for i in range(brace_idx, len(text)):
                    if text[i] == '{':
                        open_braces += 1
                    elif text[i] == '}':
                        open_braces -= 1
                        if open_braces == 0:
                            end_idx = i
                            break
                if end_idx != -1:
                    # remove from start of line containing start_idx to end_idx
                    line_start = text.rfind('\n', 0, start_idx)
                    text = text[:line_start] + text[end_idx+1:]
                    start_idx = text.find(method_name)
                    continue
        start_idx = text.find(method_name, start_idx + len(method_name))
    return text

def convert_cpp_to_java(cpp_content_list, h_content, class_name):
    java_code = f"package com.bobsgame.puzzle;\n\nimport java.util.ArrayList;\nimport com.bobsgame.shared.BobColor;\nimport com.bobsgame.client.GLUtils;\n\npublic class {class_name} {{\n"
    
    in_class = False
    for line in h_content.split('\n'):
        if f"class {class_name}" in line:
            in_class = True
            continue
        if in_class and line.startswith('};'):
            break
        if in_class and not line.strip().startswith('//') and not 'operator==' in line and not 'serialize(' in line:
            line = line.strip()
            if line.startswith('public:') or line.startswith('private:') or line.startswith('protected:'):
                continue
            if '(' not in line and ';' in line and not line.startswith('static Logger'):
                line = re.sub(r'shared_ptr<([a-zA-Z0-9_]+)>', r'\1', line)
                line = line.replace('string', 'String').replace('bool ', 'boolean ')
                line = line.replace('long long', 'long').replace('HashMap<', 'java.util.HashMap<')
                line = re.sub(r'\s*Info .*?_Info.*;', ';', line)
                
                # handle pointers carefully
                line = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_])', r'\1 \2', line)
                line = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*([a-zA-Z_])', r'\1 \2', line)
                line = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\*\s*([a-zA-Z_])', r'\1 \2', line)
                
                if 'Info ' not in line:
                    java_code += f"    public {line}\n"

    methods_text = ""
    for cpp_content in cpp_content_list:
        methods_text += cpp_content + "\n"

    # Remove specific C++ methods
    methods_text = remove_method(methods_text, "::serialize")
    methods_text = remove_method(methods_text, "::operator")
    methods_text = remove_method(methods_text, "toBase64GZippedXML")
    methods_text = remove_method(methods_text, "fromBase64GZippedXML")

    methods_text = re.sub(r'#include.*', '', methods_text)
    methods_text = re.sub(r'Logger [a-zA-Z0-9_]+::log = Logger\(.*?\);', '', methods_text)
    
    # Method signatures
    methods_text = re.sub(rf'([a-zA-Z0-9_<>]+)\s+{class_name}::([a-zA-Z0-9_]+)\((.*?)\)', r'public \1 \2(\3)', methods_text)
    methods_text = re.sub(rf'{class_name}::([a-zA-Z0-9_]+)\((.*?)\)', r'public \1(\2)', methods_text)
    
    # Simple syntax replacements
    methods_text = re.sub(r'shared_ptr<([a-zA-Z0-9_]+)>', r'\1', methods_text)
    methods_text = methods_text.replace('string ', 'String ')
    methods_text = methods_text.replace('bool ', 'boolean ')
    methods_text = methods_text.replace('long long ', 'long ')
    methods_text = methods_text.replace('->', '.')
    methods_text = methods_text.replace('::', '.')
    methods_text = methods_text.replace('nullptr', 'null')
    
    # References in parameters
    methods_text = re.sub(r'&([a-zA-Z_])', r'\1', methods_text)
    
    # Pointers in method signatures or variable decls
    methods_text = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_])', r'\1 \2', methods_text)
    methods_text = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*([a-zA-Z_])', r'\1 \2', methods_text)
    methods_text = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\*\s*([a-zA-Z_])', r'\1 \2', methods_text)
    
    methods_text = re.sub(r'//={20,}', '', methods_text)
    
    java_code += methods_text
    java_code += "\n}\n"
    
    # Fix ifdefs
    def repl_ifdef(m):
        return m.group(1)
    java_code = re.sub(r'#ifdef blocksHashMap.*?#else(.*?)#endif', repl_ifdef, java_code, flags=re.DOTALL)
    
    # Fix specific lines
    java_code = java_code.replace('public static Block nullBlock;', 'public static Block nullBlock = new Block();')
    java_code = java_code.replace('public Block nullBlock(new Block());', '')
    java_code = java_code.replace('.removeAt(', '.remove(')
    java_code = java_code.replace('.insert(', '.add(')
    
    java_code = java_code.replace('BobColor c(48, 48, 48);', 'BobColor c = new BobColor(48, 48, 48);')
    java_code = java_code.replace('c = *BobColor.lightGray;', 'c = BobColor.lightGray;')
    java_code = java_code.replace('Piece tempPiece(new Piece', 'Piece tempPiece = new Piece')
    java_code = java_code.replace('Piece piece(new Piece', 'Piece piece = new Piece')
    
    java_code = java_code.replace('GameType public getGameType()', 'public GameType getGameType()')
    java_code = java_code.replace('GameLogic public getGameLogic()', 'public GameLogic getGameLogic()')

    # Fix multiple public
    java_code = java_code.replace('public public', 'public')

    if java_code.startswith('\ufeff'):
        java_code = java_code[1:]

    return java_code

if __name__ == '__main__':
    base_path = sys.argv[1]
    class_name = sys.argv[2]
    
    with open(f"{base_path}/{class_name}.h", 'r', encoding='utf-8') as f:
        h_content = f.read()
    
    cpp_files = []
    if len(sys.argv) > 3:
        for extra in sys.argv[3:]:
            with open(f"{base_path}/{extra}.cpp", 'r', encoding='utf-8') as f:
                cpp_files.append(f.read())
    else:
        with open(f"{base_path}/{class_name}.cpp", 'r', encoding='utf-8') as f:
            cpp_files.append(f.read())
        
    out = convert_cpp_to_java(cpp_files, h_content, class_name)
    with open(f"C:/Users/hyper/workspace/bg/bobsgameonlinejava/shared/src/main/java/com/bobsgame/puzzle/{class_name}.java", 'w', encoding='utf-8') as f:
        f.write(out)
    print(f"Generated {class_name}.java")
