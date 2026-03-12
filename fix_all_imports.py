import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changed = False
    
    # Add java.util.* if needed
    if ('ArrayList' in text or 'HashMap' in text or 'Vector' in text or 'List ' in text) and 'import java.util' not in text:
        text = re.sub(r'package\s+.*?;', r'\g<0>\n\nimport java.util.*;', text)
        changed = True
        
    # Fix PuzzleGameType -> GameType
    if 'PuzzleGameType' in text:
        text = text.replace('PuzzleGameType', 'GameType')
        changed = True
        
    # Add BobColor import to puzzle package
    if 'com.bobsgame.puzzle' in text and 'BobColor' in text and 'import com.bobsgame.shared.BobColor' not in text:
        text = re.sub(r'package\s+.*?;', r'\g<0>\n\nimport com.bobsgame.shared.BobColor;', text)
        changed = True

    # Add Easing import to puzzle package
    if 'Easing.' in text and 'import com.bobsgame.shared.Easing' not in text:
        text = re.sub(r'package\s+.*?;', r'\g<0>\n\nimport com.bobsgame.shared.Easing;', text)
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith('.java'):
            fix_file(os.path.join(dirpath, filename))

print("Fixed imports and GameType references")
