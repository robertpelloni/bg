import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java'

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    changed = False
    
    # Fix old puzzle package imports
    old_pkg = 'com.bobsgame.client.engine.game.nd.bobsgame.game'
    if old_pkg in text:
        text = text.replace(old_pkg, 'com.bobsgame.puzzle')
        changed = True
        
    # Fix Easing test name
    if 'class BobEasingTest' in text and 'EasingTest.java' in path:
        text = text.replace('class BobEasingTest', 'class EasingTest')
        changed = True
    
    # Fix constructor name in EasingTest
    if 'public BobEasingTest' in text and 'EasingTest.java' in path:
        text = text.replace('public BobEasingTest', 'public EasingTest')
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith('.java'):
            fix_file(os.path.join(dirpath, filename))

print("Fixed final imports")
