import re
import os

TYPES = ['Grid', 'Block', 'Piece', 'GameLogic', 'GameType', 'BlockType', 'PieceType', 'BobColor', 'Caption', 'DifficultyType', 'Room', 'Engine', 'BobsGame', 'Sprite', 'Sound', 'Music', 'Logger', 'FrameState', 'Rotation', 'RotationSet', 'BlockOffset', 'MovementType', 'AnimationState', 'NetworkPacket']
KEYWORDS = ['int', 'float', 'double', 'long', 'boolean', 'public', 'private', 'protected', 'static', 'final', 'return', 'new', 'class', 'enum', 'if', 'while', 'for', 'else', 'case', 'break', 'continue', 'void', 'synchronized', 'volatile', 'transient', 'native', 'abstract', 'strictfp']

def translate_body(body):
    # 1. shared_ptr
    body = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', body)
    
    # 2. Pointer types (KnownType *)
    for t in TYPES:
        body = re.sub(r'\b' + t + r'\s*\*', t + ' ', body)
    
    # 3. Pointer dereference (*var)
    body = re.sub(r'\(\*([a-zA-Z0-9_.]+)\)', r'\1', body)
    
    # 4. Protect multiplication before removing other asterisks
    # Match: (non-keyword-lowercase | digit | ) ) SPACE * SPACE (lowercase | digit | ( )
    # This is still hard. Let's try to match what's NOT a pointer.
    # In this codebase, most * are multiplication except for Type* and *ptr.
    
    # Let's replace Type* first
    body = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*', r'\1 ', body)
    
    # Now, handle dereference (*ptr)
    body = re.sub(r'\(\*([a-z][a-zA-Z0-9_.]*)\)', r'\1', body)
    
    # Replace -> and ::
    body = body.replace('->', '.')
    body = body.replace('::', '.')
    body = body.replace('nullptr', 'null')
    
    # Fix common methods
    body = body.replace('.removeAt(', '.remove(')
    body = body.replace('.insert(', '.add(')
    body = body.replace('BobsGame.log.', 'log.')
    
    # Fix Math
    body = re.sub(r'\b(max|min)\(', r'Math.\1(', body)
    
    # Fix types
    body = body.replace('string ', 'String ').replace('bool ', 'boolean ').replace('long long ', 'long ')
    body = body.replace('(unsigned int)', '(int)')
    body = body.replace('const ', '')

    # Fix float* return or local
    body = body.replace('float* ', 'float[] ')

    # Fix array init: new float[2]{x, y} -> new float[]{x, y}
    body = re.sub(r'new\s+float\[\d+\]\{(.*?)\}', r'new float[]{\1}', body)

    # 6. C++ stack allocation fix
    for t in TYPES:
        body = re.sub(r'(?<=[ \t\n{])' + t + r'\s+([a-zA-Z0-9_]+)\((.*?)\);', r'' + t + r' \1 = new ' + t + r'(\2);', body)

    # 7. Cleanup preprocessor
    body = re.sub(r'#ifdef.*?#else', '', body, flags=re.DOTALL)
    body = re.sub(r'#ifdef.*?#endif', '', body, flags=re.DOTALL)
    body = re.sub(r'#ifndef.*?#endif', '', body, flags=re.DOTALL)
    body = re.sub(r'#endif', '', body)
    body = re.sub(r'#include.*', '', body)

    # 8. Fix make_shared
    body = re.sub(r'make_shared<([A-Za-z0-9_]+)>\(', r'new \1(', body)

    return body

def get_body(text, start_idx):
    brace_idx = text.find('{', start_idx)
    if brace_idx == -1: return None, -1
    open_braces = 0
    in_string = False
    in_char = False
    escape = False
    in_line_comment = False
    in_block_comment = False
    for i in range(brace_idx, len(text)):
        c = text[i]
        if in_line_comment:
            if c == '\n': in_line_comment = False
            continue
        if in_block_comment:
            if c == '*' and i+1 < len(text) and text[i+1] == '/': in_block_comment = False
            continue
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if not in_string and not in_char:
            if c == '/' and i+1 < len(text):
                if text[i+1] == '/': in_line_comment = True; continue
                if text[i+1] == '*': in_block_comment = True; continue
        if c == '"' and not in_char: in_string = not in_string
        elif c == "'" and not in_string: in_char = not in_char
        if not in_string and not in_char and not in_line_comment and not in_block_comment:
            if c == '{': open_braces += 1
            elif c == '}':
                open_braces -= 1
                if open_braces == 0: return text[brace_idx+1:i], i
    return None, -1

def port_class(class_name, h_path, cpp_paths, java_path):
    if not os.path.exists(h_path): return
    with open(h_path, 'r', encoding='utf-8') as f: h = f.read()
    cpp_contents = []
    for p in cpp_paths:
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f: cpp_contents.append(f.read())

    fields = []
    in_class = False
    class_pattern = re.compile(r'\bclass\s+' + class_name + r'\b')
    for line in h.split('\n'):
        if class_pattern.search(line): in_class = True; continue
        if in_class and line.strip().startswith('};'): in_class = False; continue
        if in_class:
            line = line.strip()
            if not line or line.startswith('//') or line.startswith('public:') or line.startswith('private:') or line.startswith('#') or '(' in line or '{' in line or line.startswith('class '): continue
            line = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', line)
            line = line.replace('string', 'String').replace('bool', 'boolean').replace('long long', 'long').replace('const ', '')
            for t in TYPES: line = re.sub(r'\b' + t + r'\s*\*', t + ' ', line)
            if line.endswith(';'): line = line[:-1]
            fields.append(f"    public {line};")

    java_code = f"package com.bobsgame.puzzle;\n\nimport java.util.*;\nimport com.bobsgame.shared.BobColor;\nimport com.bobsgame.client.GLUtils;\nimport org.slf4j.Logger;\nimport org.slf4j.LoggerFactory;\n\npublic class {class_name} {{\n"
    java_code += f"    public static final Logger log = LoggerFactory.getLogger({class_name}.class);\n"
    java_code += "\n".join(fields) + "\n\n"

    for cpp in cpp_contents:
        pos = 0
        pattern_str = r'^([A-Za-z0-9_<>:*\s&]+)\s+' + class_name + r'::([A-Za-z0-9_~]+)\s*\((.*?)\)[^{]*\{'
        method_pattern = re.compile(pattern_str, re.MULTILINE)
        while True:
            match = method_pattern.search(cpp, pos)
            if not match: break
            ret_type = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', match.group(1))
            for t in TYPES: ret_type = re.sub(r'\b' + t + r'\s*\*', t + ' ', ret_type)
            ret_type = ret_type.replace('&', '').replace('string', 'String').replace('bool', 'boolean').replace('long long', 'long').replace('const ', '').strip()
            name = match.group(2)
            args = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', match.group(3))
            for t in TYPES: args = re.sub(r'\b' + t + r'\s*\*', t + ' ', args)
            args = args.replace('&', '').replace('string', 'String').replace('bool ', 'boolean ').replace('long long', 'long').replace('const ', '').strip()
            body, end_idx = get_body(cpp, match.start())
            if body:
                if name != 'serialize' and not name.startswith('~'):
                    sig = f"public {ret_type} {name}({args})"
                    if name == class_name: sig = f"public {class_name}({args})"
                    java_code += f"    {sig} {{\n{translate_body(body)}\n    }}\n\n"
                pos = end_idx + 1
            else: pos = match.end()
    java_code += "}\n"
    java_code = java_code.replace('public class class', 'public class').replace('public enum class', 'public enum').replace('public typedef', '// typedef').replace('public mutex', '// mutex').replace('public condition_variable', '// condition_variable').replace('public thread', '// thread')
    java_code = re.sub(r'public\s+class\s+[A-Za-z0-9_]+;', '', java_code)
    with open(java_path, 'w', encoding='utf-8') as f: f.write(java_code)
    print(f"Ported {class_name}")

if __name__ == '__main__':
    base_cpp = r'C:\Users\hyper\workspace\bg\okgame\legacy-src\src\Puzzle'
    base_java = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'
    port_class('Grid', f"{base_cpp}\\Grid.h", [f"{base_cpp}\\Grid.cpp"], f"{base_java}\\Grid.java")
    port_class('Block', f"{base_cpp}\\Block.h", [f"{base_cpp}\\Block.cpp"], f"{base_java}\\Block.java")
    port_class('Piece', f"{base_cpp}\\Piece.h", [f"{base_cpp}\\Piece.cpp"], f"{base_java}\\Piece.java")
    port_class('GameLogic', f"{base_cpp}\\GameLogic.h", [f"{base_cpp}\\GameLogic.cpp", f"{base_cpp}\\GameLogicChains.cpp", f"{base_cpp}\\GameLogicGarbage.cpp", f"{base_cpp}\\GameLogicNetwork.cpp", f"{base_cpp}\\GameLogicRender.cpp"], f"{base_java}\\GameLogic.java")
    port_class('GameType', f"{base_cpp}\\GameType.h", [f"{base_cpp}\\GameType.cpp"], f"{base_java}\\PuzzleGameType.java")
    port_class('GameSequence', f"{base_cpp}\\GameSequence.h", [f"{base_cpp}\\GameSequence.cpp"], f"{base_java}\\GameSequence.java")
    port_class('BlockType', f"{base_cpp}\\Block.h", [f"{base_cpp}\\Block.cpp"], f"{base_java}\\BlockType.java")
    port_class('PieceType', f"{base_cpp}\\Piece.h", [f"{base_cpp}\\Piece.cpp"], f"{base_java}\\PieceType.java")
    port_class('PuzzlePlayer', f"{base_cpp}\\PuzzlePlayer.h", [f"{base_cpp}\\PuzzlePlayer.cpp"], f"{base_java}\\PuzzlePlayer.java")
