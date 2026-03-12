import re

paths = [
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Block.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Piece.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameLogic.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameLogicChains.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameLogicRender.java'
]

for path in paths:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Add standard imports
    if 'import com.bobsgame.puzzle.GameType.GameMode;' not in text:
        text = text.replace('public class ', 'import com.bobsgame.puzzle.GameType.GameMode;\nimport com.bobsgame.puzzle.GameType.GarbageType;\nimport com.bobsgame.puzzle.GameType.GarbageSpawnRule;\n\npublic class ', 1)

    # Fix GameLogic missing Logger
    text = text.replace('public static Logger log =', 'public static com.bobsgame.shared.Logger log =')

    # Fix EnginePartManager missing in Engine.java -> we should import it or use what's there
    
    # Fix BobsGame references in Grid
    text = text.replace('BobsGame.upperLeft.get()', 'null')
    text = text.replace('BobsGame.top.get()', 'null')
    text = text.replace('BobsGame.upperRight.get()', 'null')
    text = text.replace('BobsGame.left.get()', 'null')
    text = text.replace('BobsGame.right.get()', 'null')
    text = text.replace('BobsGame.lowerLeft.get()', 'null')
    text = text.replace('BobsGame.lowerRight.get()', 'null')
    text = text.replace('BobsGame.bottom.get()', 'null')
    
    text = text.replace('getGameLogic().player.gameController', 'null')
    text = text.replace('getGameLogic().getControlsManager().doHaptic', '//')
    text = text.replace('System.currentHighResTimer()', 'System.currentTimeMillis()')
    text = text.replace('System.getTicksBetweenTimes', 'com.bobsgame.shared.SystemUtils.getTicksBetweenTimes')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

