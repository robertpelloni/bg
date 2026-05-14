import sys
import re
import os

def parse_cpp_methods(cpp_content):
    methods = []
    # match method signature: return_type ClassName::methodName(args)
    # improved pattern to be less restrictive about what's between ) and {
    pattern = re.compile(r'^([A-Za-z0-9_<>:*\s&]+)\s+([A-Za-z0-9_]+)::([A-Za-z0-9_~]+)\s*\((.*?)\)[^{]*\{', re.MULTILINE)
    
    pos = 0
    while True:
        match = pattern.search(cpp_content, pos)
        if not match:
            break
        
        start_idx = match.start()
        brace_idx = match.end() - 1
        
        # brace matching
        open_braces = 0
        end_idx = -1
        in_string = False
        in_char = False
        in_line_comment = False
        in_block_comment = False
        escape = False
        
        for i in range(brace_idx, len(cpp_content)):
            c = cpp_content[i]
            
            if in_line_comment:
                if c == '\n':
                    in_line_comment = False
                continue
                
            if in_block_comment:
                if c == '*' and i + 1 < len(cpp_content) and cpp_content[i+1] == '/':
                    in_block_comment = False
                    # skip next char somehow? we just let it be, '/' won't trigger anything
                continue

            if escape:
                escape = False
                continue
                
            if c == '\\':
                escape = True
                continue
                
            if not in_string and not in_char:
                if c == '/' and i + 1 < len(cpp_content):
                    if cpp_content[i+1] == '/':
                        in_line_comment = True
                        continue
                    elif cpp_content[i+1] == '*':
                        in_block_comment = True
                        continue

            if c == '"' and not in_char:
                in_string = not in_string
            elif c == "'" and not in_string:
                in_char = not in_char
                
            if not in_string and not in_char and not in_line_comment and not in_block_comment:
                if c == '{':
                    open_braces += 1
                elif c == '}':
                    open_braces -= 1
                    if open_braces == 0:
                        end_idx = i
                        break
                        
        if end_idx != -1:
            ret_type = match.group(1).strip()
            class_name = match.group(2).strip()
            method_name = match.group(3).strip()
            args = match.group(4).strip()
            body = cpp_content[brace_idx+1:end_idx].strip()
            methods.append({
                'ret_type': ret_type,
                'class_name': class_name,
                'method_name': method_name,
                'args': args,
                'body': body
            })
            pos = end_idx + 1
        else:
            pos = brace_idx + 1
            
    return methods

def translate_method_to_java(method):
    ret_type = method['ret_type']
    name = method['method_name']
    args = method['args']
    body = method['body']
    
    # Exclude destructors and serialize
    if name.startswith('~') or name == 'serialize' or name == 'operator==' or name == 'toBase64GZippedXML' or name == 'fromBase64GZippedXML':
        return ""
        
    # Translate return type
    ret_type = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', ret_type)
    ret_type = ret_type.replace('string', 'String')
    ret_type = ret_type.replace('bool', 'boolean')
    ret_type = ret_type.replace('long long', 'long')
    ret_type = ret_type.replace('*', '').replace('&', '').strip()
    
    # Construct signature
    if name == method['class_name']:
        sig = f"public {name}({args})"
    else:
        sig = f"public {ret_type} {name}({args})"
        
    # Translate args
    sig = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', sig)
    sig = sig.replace('string', 'String').replace('bool ', 'boolean ').replace('long long ', 'long ')
    sig = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_])', r'\1 \2', sig)
    sig = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*([a-zA-Z_])', r'\1 \2', sig)
    sig = re.sub(r'&([a-zA-Z_])', r'\1', sig)
    
    # Remove #ifdefs from body using regex
    body = re.sub(r'#ifdef.*?#else', '', body, flags=re.DOTALL)
    body = re.sub(r'#ifdef.*?#endif', '', body, flags=re.DOTALL)
    body = re.sub(r'#endif', '', body)
    body = re.sub(r'#ifndef.*?#endif', '', body, flags=re.DOTALL)
    
    # Translate body
    body = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', body)
    body = body.replace('string ', 'String ').replace('bool ', 'boolean ').replace('long long ', 'long ')
    body = body.replace('->', '.').replace('::', '.')
    body = body.replace('nullptr', 'null')
    body = body.replace('.removeAt(', '.remove(')
    body = body.replace('.insert(', '.add(')
    body = body.replace('BobsGame.log.error', 'log.error')
    body = body.replace('BobsGame.log.warn', 'log.warn')
    body = body.replace('BobsGame.log.info', 'log.info')
    
    # Pointer creations like `PieceType bp(new PieceType());` -> `PieceType bp = new PieceType();`
    body = re.sub(r'([A-Za-z0-9_]+)\s+([a-zA-Z0-9_]+)\(new\s+\1\((.*?)\)\);', r'\1 \2 = new \1(\3);', body)
    # General pointers `BobColor *bp = new BobColor();` -> `BobColor bp = new BobColor();`
    body = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=', r'\1 \2 =', body)
    
    # Fix references
    body = body.replace('b = *bp;', 'b = bp;')
    body = body.replace('*bp = b;', 'bp = b;')

    # More fixes
    body = body.replace('float* xy = new float[2]{screenX,screenY};', 'float[] xy = new float[]{screenX,screenY};')
    body = body.replace('float* xy = b.getInterpolatedScreenXY(bx, by);', 'float[] xy = b.getInterpolatedScreenXY(bx, by);')
    body = body.replace('return (BobsGame*)getEngine();', 'return (BobsGame)getEngine();')
    body = body.replace('const String& text', 'String text')
    body = re.sub(r'oss1.*?<<.*?\(totalTicksPassed.*?1000\);', '//', body)
    body = re.sub(r'oss2.*?<<.*?\(totalTicksPassed.*?60\);', '//', body)
    body = re.sub(r'oss3.*?<<.*?\(totalTicksPassed.*?60\);', '//', body)
    body = body.replace('ArrayList<BobColor*> acceptableColors;', 'ArrayList<BobColor> acceptableColors = new ArrayList<>();')
    body = body.replace('BobColor c(48, 48, 48);', 'BobColor c = new BobColor(48, 48, 48);')
    body = body.replace('c = *BobColor.lightGray;', 'c = BobColor.lightGray;')
    body = re.sub(r'RotationSet\s+rotations\("([^"]+)"\);', r'RotationSet rotations = new RotationSet("\1");', body)
    body = re.sub(r'RotationSet\s+rotations\(name\);', r'RotationSet rotations = new RotationSet(name);', body)
    
    # Fix generic types with asterisks `ArrayList<BobColor*>` -> `ArrayList<BobColor>`
    body = re.sub(r'ArrayList<([A-Za-z0-9_]+)\*>', r'ArrayList<\1>', body)
    
    # Fix array syntax:
    body = re.sub(r'\[\]\s*\([A-Za-z0-9_]+\s+([a-zA-Z0-9_]+),\s*[A-Za-z0-9_]+\s+([a-zA-Z0-9_]+)\)\s*\{return\s+([^;]+);\s*\}', r'( \1, \2 ) -> { return \3; }', body)

    # Some stray C++ new Piece allocations
    body = re.sub(r'PieceType\s+([a-zA-Z0-9_]+)\(new\s+PieceType\((.*?)\)\);', r'// PieceType \1 removed', body)
    body = re.sub(r'BlockType\s+([a-zA-Z0-9_]+)\(new\s+BlockType\((.*?)\)\);', r'// BlockType \1 removed', body)

    # Fix pointer getters
    sig = sig.replace('float* ', 'float[] ')
    sig = sig.replace('const String&', 'String')
    
    java_code = f"    {sig} {{\n{body}\n    }}\n"
    return java_code

def sync_class(cpp_file_path, java_file_path, class_name):
    with open(cpp_file_path, 'r', encoding='utf-8') as f:
        cpp_content = f.read()
        
    cpp_methods = parse_cpp_methods(cpp_content)
    
    with open(java_file_path, 'r', encoding='utf-8') as f:
        java_content = f.read()
        
    # Get existing java methods
    java_method_names = set(re.findall(r'public\s+(?:[A-Za-z0-9_<>\[\]]+\s+)?([a-zA-Z0-9_]+)\(', java_content))
    
    new_methods_code = []
    for m in cpp_methods:
        if m['class_name'] == class_name and m['method_name'] not in java_method_names:
            translated = translate_method_to_java(m)
            if translated:
                new_methods_code.append(translated)
                
    if not new_methods_code:
        print(f"No new methods to add for {class_name}")
        return
        
    # Insert new methods before the last closing brace
    last_brace_idx = java_content.rfind('}')
    if last_brace_idx != -1:
        updated_java = java_content[:last_brace_idx] + "\n".join(new_methods_code) + "\n" + java_content[last_brace_idx:]
        with open(java_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_java)
        print(f"Added {len(new_methods_code)} methods to {class_name}")
    else:
        print(f"Error: Could not find closing brace in {java_file_path}")

if __name__ == '__main__':
    base_cpp = r'C:\Users\hyper\workspace\bg\okgame\legacy-src\src\Puzzle'
    base_java = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle'
    
    classes = ['Grid', 'Block', 'Piece', 'GameLogic', 'GameSequence', 'BlockType', 'PieceType']
    
    # Force sync for Grid
    sync_class(f"{base_cpp}\\Grid.cpp", f"{base_java}\\Grid.java", 'Grid')
    sync_class(f"{base_cpp}\\Block.cpp", f"{base_java}\\Block.java", 'Block')
    sync_class(f"{base_cpp}\\Piece.cpp", f"{base_java}\\Piece.java", 'Piece')
    
    # Special handling for GameLogic - it's split across multiple files
    gamelogic_cpps = ['GameLogic', 'GameLogicChains', 'GameLogicGarbage', 'GameLogicNetwork', 'GameLogicRender']
    for extra in gamelogic_cpps:
        sync_class(f"{base_cpp}\\{extra}.cpp", f"{base_java}\\GameLogic.java", 'GameLogic')

    sync_class(f"{base_cpp}\\GameType.cpp", f"{base_java}\\PuzzleGameType.java", 'GameType')
    sync_class(f"{base_cpp}\\PuzzlePlayer.cpp", f"{base_java}\\PuzzlePlayer.java", 'PuzzlePlayer')
    sync_class(f"{base_cpp}\\GameSequence.cpp", f"{base_java}\\GameSequence.java", 'GameSequence')
