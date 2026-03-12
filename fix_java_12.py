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

def clean_file(text):
    lines = text.split('\n')
    out_lines = []
    
    in_class_body = False
    
    for line in lines:
        stripped = line.strip()
        
        # Remove forward declarations like "public class Piece;"
        if re.match(r'^(public\s+)?class\s+[A-Za-z0-9_]+;$', stripped):
            continue
            
        # Remove repeated modifiers "public public"
        line = line.replace('public public', 'public')
        
        # Remove empty blocks like "for (int i = 0; i < colors.size(); i++)" that are followed by "b = bp;"
        # Actually wait, the error was "illegal start of type" because it was OUTSIDE a method!
        # Ah! The C++ file had method bodies, but some code was outside methods?
        # No, the C++ file has methods like `void Block::update() { ... }`
        # My converter `methods_text = re.sub(rf'([a-zA-Z0-9_<>]+)\s+{class_name}::([a-zA-Z0-9_]+)\((.*?)\)', r'public \1 \2(\3)', methods_text)`
        # If the C++ method was `Block::Block()`, it matched `re.sub(rf'{class_name}::([a-zA-Z0-9_]+)\((.*?)\)', r'public \1(\2)', methods_text)`.
        # But what if there are methods from other classes in the cpp file? Like `void BlockType::something()`?
        # YES! Block.cpp contains Block methods AND BlockType methods!
        # Piece.cpp contains Piece methods AND PieceType methods!
        # Grid.cpp contains only Grid methods? No, maybe other stuff!
        # GameType.cpp contains GameType methods AND DifficultyType methods!
        
        out_lines.append(line)
        
    return '\n'.join(out_lines)

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strip all BlockType methods from Block.java (we will put them in BlockType.java)
        if 'Block.java' in path:
            content = re.sub(r'public\s+[A-Za-z0-9_\[\]]+\s+BlockType\.([a-zA-Z0-9_]+)\(.*?\{.*?\n\}', '', content, flags=re.DOTALL)
            # Also remove BlockType constructors
            content = re.sub(r'public\s+BlockType\.BlockType\(.*?\{.*?\n\}', '', content, flags=re.DOTALL)
            
        # Strip all PieceType methods from Piece.java
        if 'Piece.java' in path:
            content = re.sub(r'public\s+[A-Za-z0-9_\[\]]+\s+PieceType\.([a-zA-Z0-9_]+)\(.*?\{.*?\n\}', '', content, flags=re.DOTALL)
            content = re.sub(r'public\s+PieceType\.PieceType\(.*?\{.*?\n\}', '', content, flags=re.DOTALL)
            
        # Fix difficulty type assignments that were placed outside of a method or in a constructor but parsed badly.
        # In C++, `DifficultyType* GameType::difficulty_BEGINNER = nullptr;` is a static initialization!
        # In Java, it should be `public static DifficultyType difficulty_BEGINNER = null;` inside the class.
        content = re.sub(r'DifficultyType\s+difficulty_([A-Z]+)\s*=\s*null;', r'public static DifficultyType difficulty_\1 = null;', content)

        content = clean_file(content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
