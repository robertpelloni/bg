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

    # Import fix: we don't need GameMode if we fully qualify it or define it in GameType
    text = text.replace('public static com.bobsgame.shared.Logger log =', 'public static org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(Grid.class);')
    text = text.replace('public static org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(Grid.class); new com.bobsgame.shared.Logger("GameLogic");', 'public static org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(GameLogic.class);')
    text = text.replace('public static org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(Grid.class); new com.bobsgame.shared.Logger("Grid");', 'public static org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(Grid.class);')

    if 'import org.slf4j.Logger;' not in text:
        text = text.replace('package com.bobsgame.puzzle;\n', 'package com.bobsgame.puzzle;\nimport org.slf4j.Logger;\nimport org.slf4j.LoggerFactory;\n')

    # Quick fix for GameType.GameMode ambiguity - replace GameMode. with GameType.GameMode.
    text = re.sub(r'(?<!GameType\.)\bGameMode\.', 'GameType.GameMode.', text)
    text = re.sub(r'(?<!GameType\.)\bGarbageSpawnRule\.', 'GameType.GarbageSpawnRule.', text)
    text = re.sub(r'(?<!GameType\.)\bGarbageType\.', 'GameType.GarbageType.', text)

    # Remove the imports of them if they exist
    text = text.replace('import com.bobsgame.puzzle.GameType.GameMode;\n', '')
    text = text.replace('import com.bobsgame.puzzle.GameType.GarbageType;\n', '')
    text = text.replace('import com.bobsgame.puzzle.GameType.GarbageSpawnRule;\n', '')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

