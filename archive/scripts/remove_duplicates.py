import os

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'
src_main = os.path.join(root, 'src', 'main', 'java')

others = [
    os.path.join(root, 'client', 'src', 'main', 'java'),
    os.path.join(root, 'shared', 'src', 'main', 'java'),
    os.path.join(root, 'server', 'src', 'main', 'java')
]

for dirpath, dirnames, filenames in os.walk(src_main):
    for filename in filenames:
        if filename.endswith('.java'):
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, src_main)
            
            # Special case: KEEP the puzzle files I just wrote in src/main/java
            if 'com\\bobsgame\\puzzle' in rel_path:
                continue
                
            for other in others:
                other_full = os.path.join(other, rel_path)
                if os.path.exists(other_full):
                    print(f"Deleting duplicate: {rel_path}")
                    os.remove(full_path)
                    break
