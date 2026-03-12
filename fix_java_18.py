import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle'

def fix_all_puzzle_files():
    # List of known classes to help distinguish pointers
    classes = ['Grid', 'Block', 'Piece', 'GameLogic', 'GameType', 'PieceType', 'BlockType', 'BobColor', 'Caption', 'DifficultyType', 'Room', 'Engine', 'FrameState']
    
    for filename in os.listdir(base_path):
        if filename.endswith('.java'):
            path = os.path.join(base_path, filename)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # 1. Restore common multiplications that were broken
            # Patterns like: var var(), var var, num var, var num
            # This is hard to do perfectly, but let's look at the errors:
            # xGrid grid.cellW() -> xGrid * grid.cellW()
            # ++captionY captionYSize -> ++captionY * captionYSize
            # 0.001f getEngine() -> 0.001f * getEngine()
            
            # Simple heuristic: if we have `something something` and it's not a type decl
            # and the first one isn't a keyword like `public`, `return`, `int`, etc.
            
            # Let's fix specific common broken ones from the log first
            text = text.replace('xGrid grid.', 'xGrid * grid.')
            text = text.replace('yGrid grid.', 'yGrid * grid.')
            text = text.replace('captionY captionYSize', 'captionY * captionYSize')
            text = text.replace('0.001f getEngine', '0.001f * getEngine')
            text = text.replace('counterY captionYSize', 'counterY * captionYSize')
            text = text.replace('xMod xDiff', 'xMod * xDiff')
            text = text.replace('yMod yDiff', 'yMod * yDiff')
            text = text.replace('dropSpeedDiff gameSpeed', 'dropSpeedDiff * gameSpeed')
            text = text.replace('stackRiseDiff gameSpeed', 'stackRiseDiff * gameSpeed')
            text = text.replace('Gained getRoom', 'Gained * getRoom')
            text = text.replace('Multiplier getRoom', 'Multiplier * getRoom')
            text = text.replace('DelayTicks getRoom', 'DelayTicks * getRoom')
            text = text.replace('AmountPerPiece getRoom', 'AmountPerPiece * getRoom')
            text = text.replace('linesCleared currentGameType', 'linesCleared * currentGameType')
            text = text.replace('blocksCleared currentGameType', 'blocksCleared * currentGameType')
            text = text.replace('1000 currentChainBlocks', '1000 * currentChainBlocks')
            text = text.replace('blockWidth scale', 'blockWidth * scale')
            text = text.replace('blockHeight*scale', 'blockHeight * scale') # was already there?
            text = text.replace('3 cellW()', '3 * cellW()')
            text = text.replace('2 cellW()', '2 * cellW()')
            text = text.replace('2 cellH()', '2 * cellH()')
            text = text.replace('1 w scale', '1 * w * scale')
            text = text.replace('1 h scale', '1 * h * scale')
            text = text.replace('0.5f w scale', '0.5f * w * scale')
            text = text.replace('1 w scale', '1 * w * scale')
            text = text.replace('w scale', 'w * scale')
            text = text.replace('h scale', 'h * scale')
            text = text.replace('4 cellH()', '4 * cellH()')
            text = text.replace('xInPiece cellW()', 'xInPiece * cellW()')
            text = text.replace('yInPiece cellH()', 'yInPiece * cellH()')
            text = text.replace('6 1', '6 * 1')
            text = text.replace('6 4', '6 * 4')
            text = text.replace('height (float)', 'height * (float)')
            text = text.replace('disappearingAlpha 2.0f', 'disappearingAlpha * 2.0f')
            
            # 2. Fix remaining C++ syntax
            text = text.replace('const String&', 'String')
            text = text.replace('const string&', 'String')
            text = text.replace('string(', 'String.valueOf(')
            text = text.replace('substr(', 'substring(')
            text = text.replace('.find(', '.indexOf(')
            text = text.replace('::', '.')
            text = text.replace('->', '.')
            text = text.replace('nullptr', 'null')
            text = text.replace('make_shared<Piece>', 'new Piece')
            text = text.replace('make_shared<Block>', 'new Block')
            
            # Fix StringConverterHelper
            text = re.sub(r'StringConverterHelper\.fromString<.*?>\((.*?)\)', r'Long.parseLong(\1)', text)

            # Fix catch(exception)
            text = text.replace('catch (exception)', 'catch (Exception e)')

            with open(path, 'w', encoding='utf-8') as f:
                f.write(text)

if __name__ == '__main__':
    fix_all_puzzle_files()
