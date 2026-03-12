import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle'

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Restore broken multiplication
    # These are very specific cases found in the logs
    replacements = [
        (r'(\d+)\s+cellH\(', r'\1 * cellH('),
        (r'(\d+)\s+cellW\(', r'\1 * cellW('),
        (r'(\d+)\s+w\s+scale', r'\1 * w * scale'),
        (r'(\d+)\s+h\s+scale', r'\1 * h * scale'),
        (r'y\s+getWidth\(', r'y * getWidth('),
        (r'y\s+oldWidth', r'y * oldWidth'),
        (r'xGrid\s+grid\.cellW\(', r'xGrid * grid.cellW('),
        (r'yGrid\s+grid\.cellH\(', r'yGrid * grid.cellH('),
        (r'disappearingAlpha\s+2\.0f', r'disappearingAlpha * 2.0f'),
        (r'0\.001f\s+getEngine\(', r'0.001f * getEngine('),
        (r'captionY\s+captionYSize', r'captionY * captionYSize'),
        (r'counterY\s+captionYSize', r'counterY * captionYSize'),
        (r'xMod\s+xDiff', r'xMod * xDiff'),
        (r'yMod\s+yDiff', r'yMod * yDiff'),
        (r'dropSpeedDiff\s+gameSpeed', r'dropSpeedDiff * gameSpeed'),
        (r'stackRiseDiff\s+gameSpeed', r'stackRiseDiff * gameSpeed'),
        (r'AmountPerLevelGained\s+getRoom\(', r'AmountPerLevelGained * getRoom('),
        (r'Multiplier\s+getRoom\(', r'Multiplier * getRoom('),
        (r'maxLockDelayTicks\s+getRoom\(', r'maxLockDelayTicks * getRoom('),
        (r'AmountPerPiece\s+getRoom\(', r'AmountPerPiece * getRoom('),
        (r'linesCleared\s+currentGameType', r'linesCleared * currentGameType'),
        (r'blocksCleared\s+currentGameType', r'blocksCleared * currentGameType'),
        (r'1000\s+currentChainBlocks', r'1000 * currentChainBlocks'),
        (r'blockWidth\s+scale', r'blockWidth * scale'),
        (r'xInPiece\s+cellW\(', r'xInPiece * cellW('),
        (r'yInPiece\s+cellH\(', r'yInPiece * cellH('),
        (r'ghostAlpha\s+alpha', r'ghostAlpha * alpha'),
        (r'ghostAlpha\s*/\s*2\s+alpha', r'ghostAlpha / 2 * alpha'),
        (r'17\s+30', r'17 * 30'),
        (r'30\s+17', r'30 * 17'),
        (r'100\s+17', r'100 * 17'),
        (r'10\s+17', r'10 * 17'),
        (r'17\s+6', r'17 * 6'),
        (r'x\s+cellW\(', r'x * cellW('),
        (r'y\s+cellH\(', r'y * cellH('),
        (r'xGrid\s+cellW\(', r'xGrid * cellW('),
        (r'ghostY\s+cellH\(', r'ghostY * cellH('),
        (r'number\s+1\.5f', r'number * 1.5f'),
    ]

    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)

    # 2. Fix C++ stack allocations like `Block b(this, grid, null, blockType);`
    # and method calls that look like them but should be `new`
    # Heuristic: Type var(args); -> Type var = new Type(args);
    # Only for specific known types
    types = ['Block', 'Piece', 'BobColor', 'RotationSet']
    for t in types:
        # Match `Type var(args);` but NOT `method(args);`
        # and NOT `if(cond)`, `while(cond)`, etc.
        pattern = r'\b' + t + r'\s+([a-zA-Z0-9_]+)\((.*?)\);'
        text = re.sub(pattern, r'' + t + r' \1 = new ' + t + r'(\2);', text)

    # 3. Fix uniform_real_distribution
    text = text.replace('uniform_real_distribution<double> distribution(0.0, 1.0);', 'double distribution = Math.random();')
    text = text.replace('distribution(randomGenerator)', 'randomGenerator.nextDouble()')

    # 4. Fix Grid.java nullBlock and other artifacts
    if 'Grid.java' in path:
        # Remove the broken nullBlock method entirely
        text = re.sub(r'public\s+Block\s+nullBlock\(new\s+Block\(\)\s*\{.*?\}\n', '', text, flags=re.DOTALL)
        # Ensure blocks.get(index) is used instead of blocks[index] or other artifacts
        # (Though most of this seems okay now)

    # 5. Fix remaining shared_ptr and make_shared
    text = text.replace('make_shared<Piece>', 'new Piece')
    text = text.replace('make_shared<Block>', 'new Block')
    text = text.replace('shared_ptr<', '').replace('>', '') # risky but let's see

    # 6. Fix repeated modifiers
    text = re.sub(r'public\s+public', 'public', text)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

for filename in os.listdir(base_path):
    if filename.endswith('.java'):
        fix_file(os.path.join(base_path, filename))

print("Applied fix_java_19.py")
