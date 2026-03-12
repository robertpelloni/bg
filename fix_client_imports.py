import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\client'

def add_puzzle_import(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if ('GameLogic' in text or 'GameType' in text or 'GameSequence' in text or 'Block' in text or 'Piece' in text or 'Grid' in text) and 'import com.bobsgame.puzzle' not in text:
        print(f"Adding puzzle import to: {path}")
        text = re.sub(r'package\s+.*?;', r'\g<0>\n\nimport com.bobsgame.puzzle.*;', text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith('.java'):
            add_puzzle_import(os.path.join(dirpath, filename))

print("Added puzzle imports to client classes")
