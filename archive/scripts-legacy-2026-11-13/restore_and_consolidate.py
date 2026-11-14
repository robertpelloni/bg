import os
import subprocess
import shutil

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'
src_main = os.path.join(root, 'src', 'main', 'java')

# Get list of deleted files from git
result = subprocess.run(['git', 'status', '--porcelain'], cwd=root, capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if line.startswith(' D ') or line.startswith('D  '):
        path = line[3:].strip()
        if path.endswith('.java'):
            print(f"Restoring and moving: {path}")
            subprocess.run(['git', 'restore', path], cwd=root)
            
            # Identify the new target path in src/main/java
            # The structure is module/src/main/java/com/bobsgame/...
            parts = path.split('/')
            if 'src' in parts and 'main' in parts and 'java' in parts:
                idx = parts.index('java')
                rel_path = '/'.join(parts[idx+1:])
                target_path = os.path.join(src_main, rel_path.replace('/', os.sep))
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.move(os.path.join(root, path.replace('/', os.sep)), target_path)
