import re

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix & references
text = re.sub(r'&\s*([a-zA-Z_])', r'\1', text)

# Fix multiplication that got messed up if any left
text = text.replace('  ', ' ') # careful not to break indent too much, actually let's skip

# Fix repeated modifiers
text = text.replace('public public ', 'public ')

# Fix specific lines that errored out
text = text.replace('BobColor c(48, 48, 48);', 'BobColor c = new BobColor(48, 48, 48);')
text = text.replace('c = *BobColor.lightGray;', 'c = BobColor.lightGray;')
text = text.replace('Piece tempPiece(new Piece', 'Piece tempPiece = new Piece')
text = text.replace('Piece piece(new Piece', 'Piece piece = new Piece')
text = text.replace('GameType public getGameType()', 'public GameType getGameType()')
text = text.replace('GameLogic public getGameLogic()', 'public GameLogic getGameLogic()')

# Fix array list insert/remove
text = re.sub(r'blocks\.insert\((.*?),\s*(.*?)\);', r'blocks.add(\1, \2);', text)

# Write back
with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'w', encoding='utf-8') as f:
    f.write(text)
