import re
import os

cpp_path = r'C:\Users\hyper\workspace\bg\okgame\legacy-src\src\Puzzle\Grid.cpp'
h_path = r'C:\Users\hyper\workspace\bg\okgame\legacy-src\src\Puzzle\Grid.h'
java_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle\Grid.java'

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

def translate_body(body):
    body = body.replace('->', '.')
    body = body.replace('::', '.')
    body = body.replace('nullptr', 'null')
    # Use regex for shared_ptr to avoid breaking other templates or operators
    body = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', body)
    
    body = body.replace('.removeAt(', '.remove(')
    body = body.replace('.insert(', '.add(')
    body = body.replace('BobsGame.log.', 'log.')
    
    # Simple replacement for pointer dereference if it's (*var).
    body = re.sub(r'\(\*([a-zA-Z0-9_]+)\)', r'\1', body)
    body = body.replace('(*', '').replace('*', '') # risky but many * remain
    
    body = re.sub(r'\b(max|min)\(', r'Math.\1(', body)
    
    # Fix common C++ types
    body = body.replace('string ', 'String ')
    body = body.replace('bool ', 'boolean ')
    body = body.replace('long long ', 'long ')
    
    # Fix generic types with pointers
    body = body.replace('ArrayList<BobColor*>', 'ArrayList<BobColor>')
    body = body.replace('ArrayList<shared_ptr<BlockType>>', 'ArrayList<BlockType>')
    body = body.replace('ArrayList<shared_ptr<PieceType>>', 'ArrayList<PieceType>')
    body = body.replace('ArrayList<shared_ptr<Block>>', 'ArrayList<Block>')
    body = body.replace('ArrayList<shared_ptr<Piece>>', 'ArrayList<Piece>')

    # Fix `Type var(args);` -> `Type var = new Type(args);`
    # Be very specific to avoid matching method calls
    for t in ['Block', 'Piece', 'BobColor', 'RotationSet', 'Rotation', 'BlockOffset']:
        # This matches `Type var(args);` at start of line or after space/brace
        body = re.sub(r'(?<=[ \t\n{])' + t + r'\s+([a-zA-Z0-9_]+)\((.*?)\);', r'' + t + r' \1 = new ' + t + r'(\2);', body)

    # remove #ifdefs
    body = re.sub(r'#ifdef.*?#else', '', body, flags=re.DOTALL)
    body = re.sub(r'#ifdef.*?#endif', '', body, flags=re.DOTALL)
    body = re.sub(r'#ifndef.*?#endif', '', body, flags=re.DOTALL)
    body = re.sub(r'#endif', '', body)

    return body

with open(h_path, 'r', encoding='utf-8') as f:
    h = f.read()
with open(cpp_path, 'r', encoding='utf-8') as f:
    cpp = f.read()

# Fields from H
fields = []
in_class = False
for line in h.split('\n'):
    if 'class Grid' in line: in_class = True; continue
    if in_class and line.strip().startswith('};'): break
    if in_class:
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('public:') or line.startswith('private:') or line.startswith('#') or '(' in line or '{' in line: continue
        
        # Translate field type
        line = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', line)
        line = line.replace('string', 'String').replace('bool', 'boolean').replace('long long', 'long')
        line = line.replace('*', '') # remove pointer asterisks
        
        if line.endswith(';'): line = line[:-1]
        fields.append(f"    public {line};")

java_code = "package com.bobsgame.puzzle;\n\nimport java.util.*;\nimport com.bobsgame.shared.BobColor;\nimport com.bobsgame.client.GLUtils;\nimport org.slf4j.Logger;\nimport org.slf4j.LoggerFactory;\n\npublic class Grid {\n"
java_code += "    public static final Logger log = LoggerFactory.getLogger(Grid.class);\n"
java_code += "\n".join(fields) + "\n\n"

# Methods from CPP
pos = 0
# Improved method pattern
method_pattern = re.compile(r'^([A-Za-z0-9_<>:*\s&]+)\s+Grid::([A-Za-z0-9_~]+)\s*\((.*?)\)[^{]*\{', re.MULTILINE)
while True:
    match = method_pattern.search(cpp, pos)
    if not match: break
    
    ret_type_raw = match.group(1)
    ret_type = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', ret_type_raw)
    ret_type = ret_type.replace('*', '').replace('&', '').replace('string', 'String').replace('bool', 'boolean').replace('long long', 'long').strip()
    
    name = match.group(2)
    
    args_raw = match.group(3)
    args = re.sub(r'shared_ptr<([A-Za-z0-9_]+)>', r'\1', args_raw)
    args = args.replace('*', '').replace('&', '').replace('string', 'String').replace('bool ', 'boolean ').replace('long long', 'long').strip()
    
    body, end_idx = get_body(cpp, match.start())
    if body:
        if name != 'serialize' and not name.startswith('~'):
            sig = f"public {ret_type} {name}({args})"
            if name == 'Grid': sig = f"public Grid({args})"
            java_code += f"    {sig} {{\n{translate_body(body)}\n    }}\n\n"
        pos = end_idx + 1
    else:
        pos = match.end()

java_code += "}\n"
with open(java_path, 'w', encoding='utf-8') as f:
    f.write(java_code)
print("Ported Grid.java properly")
