import os
import shutil

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'
src_main = os.path.join(root, 'src', 'main', 'java')

others = [
    os.path.join(root, 'client', 'src', 'main', 'java'),
    os.path.join(root, 'shared', 'src', 'main', 'java'),
    os.path.join(root, 'server', 'src', 'main', 'java')
]

for other in others:
    if not os.path.exists(other): continue
    for dirpath, dirnames, filenames in os.walk(other):
        for filename in filenames:
            if filename.endswith('.java'):
                full_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(full_path, other)
                target_path = os.path.join(src_main, rel_path)
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                print(f"Moving {rel_path}")
                shutil.copy2(full_path, target_path) # use copy2 to be safe
