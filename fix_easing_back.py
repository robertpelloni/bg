import os

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java'

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith('.java'):
            path = os.path.join(dirpath, filename)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            new_text = text.replace('BobEasing', 'Easing')
            if new_text != text:
                print(f"Updating: {path}")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_text)
