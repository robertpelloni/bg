import re
import os

paths = [
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Grid.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Block.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Piece.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\GameLogic.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\GameType.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\GameSequence.java'
]

def fix_code(text):
    text = re.sub(r'BlockType\s+BlockType\.([a-zA-Z0-9_]+)\(new\s+BlockType\((.*?)\)\);', r'// BlockType \1 removed', text)
    text = re.sub(r'PieceType\s+PieceType\.([a-zA-Z0-9_]+)\(new\s+PieceType\((.*?)\)\);', r'// PieceType \1 removed', text)
    
    text = text.replace('float* xy = new float[2]{screenX,screenY};', 'float[] xy = new float[]{screenX,screenY};')
    text = text.replace('float* xy = b.getInterpolatedScreenXY(bx, by);', 'float[] xy = b.getInterpolatedScreenXY(bx, by);')
    text = text.replace('float* public getInterpolatedScreenXY', 'public float[] getInterpolatedScreenXY')
    
    text = text.replace('return (BobsGame*)getEngine();', 'return (BobsGame)getEngine();')
    
    text = text.replace('const String& text', 'String text')
    text = re.sub(r'oss1.*?<<.*?\(totalTicksPassed.*?1000\);', '//', text)
    text = re.sub(r'oss2.*?<<.*?\(totalTicksPassed.*?60\);', '//', text)
    text = re.sub(r'oss3.*?<<.*?\(totalTicksPassed.*?60\);', '//', text)
    
    text = text.replace('public Block nullBlock(new Block() {', 'public Block nullBlock = new Block();')
    
    text = text.replace('ArrayList<BobColor*> acceptableColors;', 'ArrayList<BobColor> acceptableColors = new ArrayList<>();')
    
    text = text.replace('BobColor c(48, 48, 48);', 'BobColor c = new BobColor(48, 48, 48);')
    text = text.replace('c = *BobColor.lightGray;', 'c = BobColor.lightGray;')
    
    text = re.sub(r'RotationSet\s+rotations\("([^"]+)"\);', r'RotationSet rotations = new RotationSet("\1");', text)
    
    # Remove remaining serialize things
    text = re.sub(r'template\s+void\s+[a-zA-Z0-9_]+\.serialize.*?unsigned\s+int\);', '', text)
    text = re.sub(r'template\s+<typename\s+Archive>', '', text)
    
    # Specific C++isms left
    text = text.replace('default_random_engine defaultRandomEngine(randomDevice());', 'java.util.Random defaultRandomEngine = new java.util.Random();')
    text = re.sub(r'randomGenerator = mt19937\(\(unsigned int\)randomSeed\);', 'randomGenerator = new java.util.Random((long)randomSeed);', text)
    text = text.replace('(long long)', '(long)')
    
    text = re.sub(r'PieceType\s+([a-zA-Z0-9_]+)\(PieceType\.([a-zA-Z0-9_]+)\);', r'PieceType \1 = PieceType.\2;', text)
    text = re.sub(r'make_shared<Piece>\(', r'new Piece(', text)
    
    text = text.replace('vector<GameLogic*> otherPlayers;', 'ArrayList<GameLogic> otherPlayers = new ArrayList<>();')
    text = text.replace('vector<GameLogic*> alivePlayers;', 'ArrayList<GameLogic> alivePlayers = new ArrayList<>();')
    text = re.sub(r'sort\(otherPlayers\.begin\(\), otherPlayers\.end\(\), \[\]\(GameLogic\*a, GameLogic\*b\) \{return a\.uuid\.compare\(b\.uuid\); \}\);', r'otherPlayers.sort((a, b) -> a.uuid.compareTo(b.uuid));', text)
    
    text = text.replace('return &(frameState);', 'return frameState;')

    return text

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = fix_code(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
