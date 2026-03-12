import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java'

def fix_package_and_imports(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changed = False
    
    # Identify correct package based on directory
    rel_dir = os.path.dirname(os.path.relpath(path, root))
    correct_package = rel_dir.replace(os.sep, '.')
    
    # Fix package declaration
    match = re.search(r'package\s+(.*?);', text)
    if match:
        actual_package = match.group(1)
        if actual_package != correct_package:
            print(f"Fixing package in {path}: {actual_package} -> {correct_package}")
            text = text.replace(f"package {actual_package};", f"package {correct_package};")
            changed = True
    
    # Fix common import errors
    if 'import easing.Easing;' in text:
        text = text.replace('import easing.Easing;', 'import com.bobsgame.shared.Easing;')
        changed = True
    if 'import hq2x.HQ2X;' in text:
        text = text.replace('import hq2x.HQ2X;', 'import com.bobsgame.editor.HQ2X;') # Based on where I moved it
        changed = True
    if 'import com.bobsgame.client.engine.game.nd.bobsgame.game.' in text:
        text = text.replace('com.bobsgame.client.engine.game.nd.bobsgame.game.', 'com.bobsgame.puzzle.')
        changed = True
    if 'import com.bobsgame.puzzle.PuzzleGameType;' in text:
        text = text.replace('com.bobsgame.puzzle.PuzzleGameType', 'com.bobsgame.puzzle.GameType')
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith('.java'):
            fix_package_and_imports(os.path.join(dirpath, filename))

print("Fixed packages and imports")
