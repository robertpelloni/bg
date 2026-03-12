import re

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix static Logger log
text = text.replace('public static Logger log;', 'public static com.bobsgame.shared.Logger log = new com.bobsgame.shared.Logger("Grid");')

# Fix math min/max
text = re.sub(r'\bmax\(', 'Math.max(', text)
text = re.sub(r'\bmin\(', 'Math.min(', text)

# Fix GameLogic game = nullptr
text = text.replace('public GameLogic game = null;', 'public GameLogic game = null;')

# Fix to_string
text = text.replace('to_string(', 'String.valueOf(')

# Fix some remaining pointer syntax that was weird
text = text.replace('Piece(new Piece', 'new Piece')

# containsValue
text = text.replace('blocks.containsValue(b)', 'blocks.contains(b)')

# some other ones
text = text.replace('ArrayList<BobColor> acceptableColors;', 'ArrayList<BobColor> acceptableColors = new ArrayList<>();')

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'w', encoding='utf-8') as f:
    f.write(text)
