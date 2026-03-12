import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle'

def fix_all_puzzle_files():
    for filename in os.listdir(base_path):
        if filename.endswith('.java'):
            path = os.path.join(base_path, filename)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # Fix pointers in types
            text = text.replace('BobColor*', 'BobColor')
            text = text.replace('Block*', 'Block')
            text = text.replace('Piece*', 'Piece')
            text = text.replace('GameLogic*', 'GameLogic')
            text = text.replace('GameType*', 'GameType')
            text = text.replace('PieceType*', 'PieceType')
            text = text.replace('BlockType*', 'BlockType')
            
            # Fix multiple public
            text = text.replace('public public', 'public')
            
            # Fix float*
            text = text.replace('float*', 'float[]')
            
            # Fix nullptr
            text = text.replace('nullptr', 'null')
            
            # Fix ->
            text = text.replace('->', '.')
            
            # Fix ::
            text = text.replace('::', '.')
            
            # Fix multiply * that shouldn't be there
            # text = re.sub(r'\b([A-Z][a-zA-Z0-9_]*)\s*\*\s*([a-zA-Z_])', r'\1 \2', text)
            
            # Fix constructor calls PieceType(new PieceType())
            text = re.sub(r'([A-Za-z0-9_]+)\s+([a-zA-Z0-9_]+)\(new\s+\1\((.*?)\)\);', r'\1 \2 = new \1(\3);', text)

            # Fix common methods
            text = text.replace('.removeAt(', '.remove(')
            text = text.replace('.insert(', '.add(')
            
            # Remove any trailing pointers
            text = re.sub(r'\b([A-Za-z0-9_]+)\s*\*\s+', r'\1 ', text)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)

if __name__ == '__main__':
    fix_all_puzzle_files()
