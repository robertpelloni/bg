import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def fix_gametype():
    path = os.path.join(root, 'GameType.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Add missing enums if they aren't there
    if 'enum VSGarbageRule' not in text:
        text = text.replace('public class GameType implements Serializable {', 
                            'public class GameType implements Serializable {\n    public enum VSGarbageRule { FALL_FROM_CEILING_IN_EVEN_ROWS, RISE_FROM_FLOOR_IN_EVEN_ROWS }\n    public enum ScoreType { LINES_CLEARED, BLOCKS_CLEARED, PIECES_MADE }\n    public enum GarbageSpawnRule { NONE, TICKS, LINES_CLEARED, BLOCKS_CLEARED, PIECES_MADE }\n')
    
    # Fix references
    text = text.replace('VSGarbageDropRule', 'VSGarbageRule')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def fix_piece():
    path = os.path.join(root, 'Piece.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if 'class RotationSet' not in text:
        text = text.replace('public class Piece {', 
                            'public class Piece {\n    public static class BlockOffset implements java.io.Serializable { public int x, y; public BlockOffset(int x, int y) { this.x=x; this.y=y; } public BlockOffset() {} }\n    public static class Rotation implements java.io.Serializable { public ArrayList<BlockOffset> blockOffsets = new ArrayList<>(); public void add(BlockOffset b) { blockOffsets.add(b); } }\n    public static class RotationSet implements java.io.Serializable { public String name; public ArrayList<Rotation> rotationSet = new ArrayList<>(); public RotationSet(String name) { this.name=name; } public void add(Rotation r) { rotationSet.add(r); } public int size() { return rotationSet.size(); } public Rotation get(int i) { return rotationSet.get(i); } }\n')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

fix_gametype()
fix_piece()
print("Fixed GameType and Piece inner classes")
