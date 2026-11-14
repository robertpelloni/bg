import os
import shutil
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'
src_main = os.path.join(root, 'src', 'main', 'java')

others = [
    os.path.join(root, 'client', 'src', 'main', 'java'),
    os.path.join(root, 'shared', 'src', 'main', 'java'),
    os.path.join(root, 'server', 'src', 'main', 'java')
]

# 1. Move and update
for other in others:
    if not os.path.exists(other): continue
    for dirpath, dirnames, filenames in os.walk(other):
        for filename in filenames:
            if filename.endswith('.java'):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, other)
                target_path = os.path.join(src_main, rel_path)
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                if not os.path.exists(target_path):
                    shutil.move(full_path, target_path)
                else:
                    # If target exists, overwrite it with the module version
                    os.remove(target_path)
                    shutil.move(full_path, target_path)

# 2. Fix packages and common renames
for dirpath, dirnames, filenames in os.walk(src_main):
    for filename in filenames:
        if filename.endswith('.java'):
            path = os.path.join(dirpath, filename)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            changed = False
            
            # Correct package
            rel_dir = os.path.dirname(os.path.relpath(path, src_main))
            correct_package = rel_dir.replace(os.sep, '.')
            match = re.search(r'package\s+(.*?);', text)
            if match:
                actual_package = match.group(1)
                if actual_package != correct_package:
                    text = text.replace(f"package {actual_package};", f"package {correct_package};")
                    changed = True
            
            # Renames
            if 'PuzzleGameType' in text:
                text = text.replace('PuzzleGameType', 'GameType')
                changed = True
            if 'import easing.Easing;' in text:
                text = text.replace('import easing.Easing;', 'import com.bobsgame.shared.BobEasing;')
                changed = True
            if 'import com.bobsgame.shared.Easing;' in text:
                text = text.replace('import com.bobsgame.shared.Easing;', 'import com.bobsgame.shared.BobEasing;')
                changed = True
            if 'public class Easing' in text:
                text = text.replace('public class Easing', 'public class BobEasing')
                changed = True
            if 'Easing.' in text:
                text = text.replace('Easing.', 'BobEasing.')
                changed = True

            if changed:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(text)

# 3. Final renames of files
if os.path.exists(os.path.join(src_main, 'com', 'bobsgame', 'shared', 'Easing.java')):
    os.rename(os.path.join(src_main, 'com', 'bobsgame', 'shared', 'Easing.java'), os.path.join(src_main, 'com', 'bobsgame', 'shared', 'BobEasing.java'))
if os.path.exists(os.path.join(src_main, 'com', 'bobsgame', 'puzzle', 'PuzzleGameType.java')):
    os.rename(os.path.join(src_main, 'com', 'bobsgame', 'puzzle', 'PuzzleGameType.java'), os.path.join(src_main, 'com', 'bobsgame', 'puzzle', 'GameType.java'))

print("Consolidation V2 finished")
