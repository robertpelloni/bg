import re
import os

paths = [
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Block.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Piece.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameLogic.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameType.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameSequence.java'
]

def fix_code(text):
    # Remove forward declarations
    text = re.sub(r'public\s+class\s+[a-zA-Z0-9_]+;', '', text)
    
    # Remove #define
    text = re.sub(r'#define.*', '', text)

    # Remove destructor
    text = re.sub(r'public\s+~[a-zA-Z0-9_]+\(\)\s*\{[^{}]*\}', '', text, flags=re.DOTALL)
    text = re.sub(r'public\s+[a-zA-Z0-9_]+\.~[a-zA-Z0-9_]+\(\)\s*\{[^{}]*\}', '', text, flags=re.DOTALL)

    # Fix C++ copy constructors or stack allocations like `PieceType cursorPieceType(PieceType.oneBlockCursorPieceType);`
    # Replace with `PieceType cursorPieceType = PieceType.oneBlockCursorPieceType;`
    # Be careful not to replace actual method calls. Let's do targeted ones.
    text = re.sub(r'PieceType\s+([a-zA-Z0-9_]+)\(PieceType.([a-zA-Z0-9_]+)\);', r'PieceType \1 = PieceType.\2;', text)
    text = re.sub(r'BlockType\s+([a-zA-Z0-9_]+)\(BlockType.([a-zA-Z0-9_]+)\);', r'BlockType \1 = BlockType.\2;', text)

    # Replace make_shared
    text = re.sub(r'make_shared<([a-zA-Z0-9_]+)>\(', r'new \1(', text)
    
    # Typedefs
    text = re.sub(r'public\s+typedef.*?;', '', text)
    
    # Fix vector / chrono leftovers
    text = text.replace('long long', 'long')
    text = text.replace('(long long)', '(long)')
    
    # Repeated modifiers
    text = text.replace('public public', 'public')
    text = re.sub(r'public\s+public', 'public', text)
    
    # Remove BOM
    text = text.replace('\ufeff', '')
    
    # Pointers
    text = text.replace('BobsGame*', 'BobsGame')
    text = text.replace('GameLogic*', 'GameLogic')
    text = text.replace('Piece*', 'Piece')
    
    # b = *bp
    text = text.replace('b = *bp;', 'b = bp;')
    text = text.replace('*bp = b;', 'bp = b;')

    # Fix Random device
    text = text.replace('default_random_engine defaultRandomEngine(randomDevice());', 'java.util.Random defaultRandomEngine = new java.util.Random();')
    text = re.sub(r'randomGenerator = mt19937.*?;', 'randomGenerator = new java.util.Random((long)randomSeed);', text)

    return text

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = fix_code(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
