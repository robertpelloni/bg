import os

path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\client\network\GameClientTCP.java'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
open_braces = 0
for line in lines:
    open_braces += line.count('{')
    open_braces -= line.count('}')
    out.append(line)

while open_braces > 0:
    out.append('}\n')
    open_braces -= 1

with open(path, 'w', encoding='utf-8') as f:
    f.write("".join(out))

print(f"Fixed braces in GameClientTCP.java, final balance: {open_braces}")
