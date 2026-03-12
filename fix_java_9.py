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

def clean_cpp_leftovers(text):
    # Remove boost serialization
    text = re.sub(r'template.*?serialize.*?;', '', text, flags=re.DOTALL)
    text = re.sub(r'template.*?Archive.*?serialize.*?\{.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'void\s+[a-zA-Z0-9_]+\.serialize\s*\([^)]*\)\s*\{[^}]*\}', '', text, flags=re.DOTALL)
    text = re.sub(r'ar & BOOST_SERIALIZATION_NVP.*?;', '', text)
    
    # Remove operator overloads
    text = re.sub(r'boolean\s+[a-zA-Z0-9_]+\.operator.*?\)[^{]*\{.*?\}', '', text, flags=re.DOTALL)
    
    # Remove class forward declarations
    text = re.sub(r'class [a-zA-Z0-9_]+;', '', text)
    
    # Fix 'Type public methodName' to 'public Type methodName'
    text = re.sub(r'^(\s*)([a-zA-Z0-9_]+)\s+public\s+([a-zA-Z0-9_]+)\(', r'\1public \2 \3(', text, flags=re.MULTILINE)
    text = re.sub(r'^(\s*)([a-zA-Z0-9_]+)\[\]\s+public\s+([a-zA-Z0-9_]+)\(', r'\1public \2[] \3(', text, flags=re.MULTILINE)

    # Fix pointers return type 'Type* public' -> 'public Type'
    text = re.sub(r'^(\s*)([a-zA-Z0-9_]+)\*\s+public\s+([a-zA-Z0-9_]+)\(', r'\1public \2 \3(', text, flags=re.MULTILINE)
    
    # Fix float* xy = new float[2]{screenX,screenY};
    text = text.replace('float* xy = new float[2]{screenX,screenY};', 'float[] xy = new float[]{screenX,screenY};')
    text = text.replace('float* xy = getInterpolatedScreenXY(screenX, screenY);', 'float[] xy = getInterpolatedScreenXY(screenX, screenY);')
    text = text.replace('public float* getInterpolatedScreenXY', 'public float[] getInterpolatedScreenXY')
    text = text.replace('public float getInterpolatedScreenXY', 'public float[] getInterpolatedScreenXY') # fallback
    text = text.replace('public float[]* getInterpolatedScreenXY', 'public float[] getInterpolatedScreenXY') 

    # Fix pointer constructors BobColor(*color) -> new BobColor(color) or just color
    text = re.sub(r'BobColor\(\*([a-zA-Z0-9_.]+)\)', r'\1', text)
    text = re.sub(r'BobColor\(([a-zA-Z0-9_.]+)\)', r'\1', text)

    # remove bad piece/block static setups
    text = re.sub(r'PieceType\s+PieceType\.emptyPieceType.*?\;', '', text)
    text = re.sub(r'BlockType\s+BlockType\.emptyBlockType.*?\;', '', text)
    text = re.sub(r'BlockType\s+BlockType\.squareBlockType.*?\;', '', text)
    text = re.sub(r'BlockType\s+BlockType\.shotPieceBlockType.*?\;', '', text)

    return text

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = clean_cpp_leftovers(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
