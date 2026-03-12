import re

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'r', encoding='utf-8') as f:
    text = f.read()

if text.startswith('\ufeff'):
    text = text[1:]

text = text.replace('public public ', 'public ')
text = text.replace('ArrayList<BobColor*> ', 'ArrayList<BobColor> ')
text = text.replace('BobColor c(48, 48, 48);', 'BobColor c = new BobColor(48, 48, 48);')
text = text.replace('c = *BobColor.lightGray;', 'c = BobColor.lightGray;')
text = text.replace('Piece tempPiece = new Piece(getGameLogic(), this, type, blockTypes));', 'Piece tempPiece = new Piece(getGameLogic(), this, type, blockTypes);')
text = text.replace('Piece piece = new Piece(getGameLogic(), this, getRandomPieceType(pieceTypes), blockTypes));', 'Piece piece = new Piece(getGameLogic(), this, getRandomPieceType(pieceTypes), blockTypes);')
text = text.replace('GameType public getGameType()', 'public GameType getGameType()')
text = text.replace('GameLogic public getGameLogic()', 'public GameLogic getGameLogic()')

text = re.sub(r'ArrayList<BlockType>\s+&ignoreTypes', 'ArrayList<BlockType> ignoreTypes', text)
text = re.sub(r'ArrayList<BlockType>\s+&mustContainAtLeastOneTypes', 'ArrayList<BlockType> mustContainAtLeastOneTypes', text)
text = re.sub(r'ArrayList<BlockType>\s+&ignoreUnlessTouchingBreakerBlockTypes', 'ArrayList<BlockType> ignoreUnlessTouchingBreakerBlockTypes', text)
text = re.sub(r'ArrayList<BlockType>\s+&breakerBlockTypes', 'ArrayList<BlockType> breakerBlockTypes', text)
text = re.sub(r'ArrayList<PieceType>\s+&pieceTypes', 'ArrayList<PieceType> pieceTypes', text)
text = re.sub(r'ArrayList<BlockType>\s+&blockTypes', 'ArrayList<BlockType> blockTypes', text)
text = re.sub(r'ArrayList<Block>\s+&connectedBlocks', 'ArrayList<Block> connectedBlocks', text)
text = re.sub(r'ArrayList<Piece>\s+&nextPieces', 'ArrayList<Piece> nextPieces', text)
text = re.sub(r'ArrayList<PieceType>\s+&pieceArray', 'ArrayList<PieceType> pieceArray', text)
text = re.sub(r'ArrayList<BlockType>\s+&blockArray', 'ArrayList<BlockType> blockArray', text)
text = re.sub(r'ArrayList<PieceType>\s+&arr', 'ArrayList<PieceType> arr', text)
text = re.sub(r'ArrayList<BlockType>\s+&arr', 'ArrayList<BlockType> arr', text)

with open(r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java', 'w', encoding='utf-8') as f:
    f.write(text)
