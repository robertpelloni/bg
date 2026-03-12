import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def fix_blocktype():
    path = os.path.join(root, 'BlockType.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Add aliases for backward compatibility with editor
    if 'public boolean useAsGarbage;' not in text:
        text = text.replace('public boolean useAsGarbageBlock = false;', 
                            'public boolean useAsGarbageBlock = false;\n    public boolean useAsGarbage = false;')
    if 'public boolean useAsPlayingFieldFiller;' not in text:
        text = text.replace('public boolean useAsPlayingFieldFillerBlock = false;', 
                            'public boolean useAsPlayingFieldFillerBlock = false;\n    public boolean useAsPlayingFieldFiller = false;')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def fix_piecetype():
    path = os.path.join(root, 'PieceType.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Change rotationSet to ArrayList<Piece.Rotation> for editor compatibility
    text = text.replace('public Piece.RotationSet rotationSet = new Piece.RotationSet("");', 
                        'public ArrayList<Piece.Rotation> rotationSet = new ArrayList<>();')
    text = text.replace('rotationSet = new Piece.RotationSet("");', 
                        'rotationSet = new ArrayList<Piece.Rotation>();')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def fix_gamelogic():
    path = os.path.join(root, 'GameLogic.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Add missing fields
    if 'public boolean dead = false;' not in text:
        text = text.replace('public boolean died = false;', 'public boolean died = false;\n    public boolean dead = false;')
    if 'public NetworkPacket networkPacket = new NetworkPacket();' not in text:
        text = text.replace('public static class NetworkPacket {', 'public NetworkPacket networkPacket = new NetworkPacket();\n\n    public static class NetworkPacket {')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def fix_gametype():
    path = os.path.join(root, 'GameType.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Add stub for GSON method
    if 'toBase64GZippedGSON' not in text:
        text = text.replace('public void tetsosumi() {}', 
                            'public void tetsosumi() {}\n    public String toBase64GZippedGSON() { return ""; }')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

fix_blocktype()
fix_piecetype()
fix_gamelogic()
fix_gametype()
print("Fixed final-final issues")
