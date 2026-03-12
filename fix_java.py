import re

# Read original sources to completely regenerate Java code properly
with open(r'C:\Users\hyper\workspace\bg\okgame\legacy-src\src\Puzzle\Grid.cpp', 'r', encoding='utf-8') as f:
    cpp_text = f.read()

with open(r'C:\Users\hyper\workspace\bg\okgame\legacy-src\src\Puzzle\Grid.h', 'r', encoding='utf-8') as f:
    h_text = f.read()

import sys
sys.path.append(r'C:\Users\hyper\workspace\bg')
from port_cpp import convert_cpp_to_java

java_code = convert_cpp_to_java(cpp_text, h_text, 'Grid')

# Targeted replacements instead of dumb ones
java_code = java_code.replace('shared_ptr<Block>', 'Block')
java_code = java_code.replace('shared_ptr<Piece>', 'Piece')
java_code = java_code.replace('shared_ptr<BlockType>', 'BlockType')
java_code = java_code.replace('shared_ptr<PieceType>', 'PieceType')

# Fix pointer types like `BobColor *color` -> `BobColor color`
java_code = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_])', r'\1 \2', java_code)
java_code = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*([a-zA-Z_])', r'\1 \2', java_code)

# Fix references `&name`
java_code = re.sub(r'&([a-zA-Z_])', r'\1', java_code)

# Fix #ifdef
def repl_ifdef(m):
    return m.group(1)
java_code = re.sub(r'#ifdef blocksHashMap.*?#else(.*?)#endif', repl_ifdef, java_code, flags=re.DOTALL)

# Fix method signatures for constructor
java_code = java_code.replace('Grid::Grid', 'Grid')

# Some syntax fixes
java_code = java_code.replace('public static Block nullBlock;', 'public static Block nullBlock = new Block();')
java_code = java_code.replace('public Block nullBlock(new Block());', '')
java_code = java_code.replace('.removeAt(', '.remove(')
java_code = java_code.replace('.insert(', '.add(')
java_code = java_code.replace('::', '.')
java_code = java_code.replace('->', '.')
java_code = java_code.replace('nullptr', 'null')
java_code = java_code.replace('GameLogic game = null;', 'public GameLogic game = null;')

# Output
with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'w', encoding='utf-8') as f:
    f.write(java_code.lstrip('\ufeff'))
