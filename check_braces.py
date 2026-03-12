import os

def check_braces(path):
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    open_count = text.count('{')
    close_count = text.count('}')
    print(f"{os.path.basename(path)}: Open {open_count}, Close {close_count}, Balance {open_count - close_count}")

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame'
for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if filename.endswith('.java'):
            check_braces(os.path.join(dirpath, filename))
