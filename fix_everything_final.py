import os
import re

src_root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java'

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changed = False
    
    # 1. Fix old puzzle package imports and references
    old_pkg = 'com.bobsgame.client.engine.game.nd.bobsgame.game'
    if old_pkg in text:
        text = text.replace(old_pkg, 'com.bobsgame.puzzle')
        changed = True
    
    # 2. Fix PuzzleGameType -> GameType
    if 'PuzzleGameType' in text:
        text = text.replace('PuzzleGameType', 'GameType')
        changed = True
        
    # 3. Fix inner class references for Piece
    for cls in ['Rotation', 'RotationSet', 'BlockOffset', 'RotationType']:
        # if `class` followed by SPACE and `cls` is NOT found (i.e. not the definition)
        # and `Piece.cls` is NOT found
        if re.search(r'\b' + cls + r'\b', text) and not re.search(r'\bPiece\.' + cls + r'\b', text) and not re.search(r'class\s+' + cls, text):
            # and if we aren't in Piece.java
            if 'Piece.java' not in path:
                print(f"Adding Piece prefix to {cls} in {path}")
                text = re.sub(r'\b' + cls + r'\b', 'Piece.' + cls, text)
                changed = True

    # 4. Fix inner class references for BlockType
    if 'TurnFromBlockTypeToType' in text and 'BlockType.TurnFromBlockTypeToType' not in text and 'BlockType.java' not in path:
        text = text.replace('TurnFromBlockTypeToType', 'BlockType.TurnFromBlockTypeToType')
        changed = True

    # 5. Fix Easing imports
    if 'import easing.Easing;' in text:
        text = text.replace('import easing.Easing;', 'import com.bobsgame.shared.Easing;')
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

# Delete problematic files
to_delete = [
    os.path.join(src_root, 'com/bobsgame/client/engine/game/nd/bobsgame/game/Settings.java'),
    os.path.join(src_root, 'com/bobsgame/puzzle/TurnFromBlockTypeToType.java')
]
for p in to_delete:
    if os.path.exists(p):
        print(f"Deleting {p}")
        os.remove(p)

for dirpath, dirnames, filenames in os.walk(src_root):
    for filename in filenames:
        if filename.endswith('.java'):
            fix_file(os.path.join(dirpath, filename))

print("Fixed final issues")
