import re
import os

paths = [
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Block.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Piece.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameLogic.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameType.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameSequence.java'
]

def clean_orphaned_code(text):
    # Remove lines containing importExport
    text = re.sub(r'.*importExport.*?\n', '', text)
    
    # Remove orphaned code blocks that were part of serialize()
    # It's highly specific to the artifacts left over:
    text = re.sub(r'\s*for \(int i = 0; i < colors\.size\(\); i\+\+.*?\}\s*\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*for \(int i = 0; i < importExport_colors\.size\(\); i\+\+.*?\}\s*\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*if \(specialColor != null && specialColor\.name.*?importExport_specialColor = specialColor;.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*if \(version == 0\).*?else.*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*if \(version>0\).*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*if \(version > 1\).*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*if \(version < 2\).*?\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\s*catch \(Exception e\).*?\}', '', text, flags=re.DOTALL)

    # remove floating "colors.clear();"
    text = re.sub(r'\s*colors\.clear\(\);', '', text)
    
    # remove floating "specialColor = null;"
    text = re.sub(r'\s*specialColor = null;', '', text)

    # fix repeated modifier "public "
    text = re.sub(r'public\s+public\s+', 'public ', text)
    text = re.sub(r'public\s+\n', '\n', text)
    
    # fix "public class, interface, enum" from bad replacements
    text = re.sub(r'class, interface, enum, or record expected', '', text) # just in case this got into text somehow

    return text

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = clean_orphaned_code(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
