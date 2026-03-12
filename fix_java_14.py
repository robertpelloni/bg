import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def fix_gamelogic():
    path = os.path.join(base_path, 'GameLogic.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Imports
    imports = [
        'import org.slf4j.Logger;',
        'import org.slf4j.LoggerFactory;',
        'import com.bobsgame.client.engine.text.Caption;',
        'import com.bobsgame.client.engine.text.CaptionManager;',
        'import com.bobsgame.shared.BobColor;',
        'import com.bobsgame.client.GLUtils;',
        'import com.bobsgame.puzzle.GameType.GameMode;',
        'import com.bobsgame.puzzle.GameType.GarbageSpawnRule;',
        'import com.bobsgame.puzzle.GameType.VSGarbageDropRule;'
    ]
    for imp in imports:
        if imp not in text:
            text = text.replace('package com.bobsgame.puzzle;', f'package com.bobsgame.puzzle;\n{imp}')

    # 2. Duplicate variables
    text = text.replace('public long lockInputCountdownTicks = 0;', 'public long lockInputCountdownTicks = 0;') # placeholder
    # Remove second/third occurrences
    vars_to_dedupe = [
        'public long lockInputCountdownTicks',
        'public Piece lastPiece',
        'public ArrayList<Caption> announcementCaptions',
        'public ArrayList<Caption> infoCaptions',
        'public Caption difficultyCaption',
        'public void renderBlocks()',
        'public void renderForeground()'
    ]
    
    for var_prefix in vars_to_dedupe:
        first = text.find(var_prefix)
        if first != -1:
            next_occ = text.find(var_prefix, first + len(var_prefix))
            while next_occ != -1:
                # find the end of the statement or block
                if var_prefix.endswith('()'):
                    # find the matching closing brace
                    open_brace = text.find('{', next_occ)
                    if open_brace != -1:
                        counter = 0
                        end_brace = -1
                        for i in range(open_brace, len(text)):
                            if text[i] == '{': counter += 1
                            elif text[i] == '}':
                                counter -= 1
                                if counter == 0:
                                    end_brace = i
                                    break
                        if end_brace != -1:
                            text = text[:next_occ] + text[end_brace+1:]
                else:
                    end_line = text.find('\n', next_occ)
                    text = text[:next_occ] + text[end_line+1:]
                next_occ = text.find(var_prefix, first + len(var_prefix))

    # 3. Missing fields
    missing_fields = [
        'public long randomSeed = -1;',
        'public Random randomGenerator;',
        'public float playingFieldX0, playingFieldX1, playingFieldY0, playingFieldY1;',
        'public float captionX;',
        'public boolean forceGravityThisFrame = false;',
        'public long stopStackRiseTicksCounter = 0;',
        'public int timesToFlashBlocksQueue = 0;',
        'public int timesToFlashScreenQueue = 0;',
        'public long lockDelayTicksCounter = 0;',
        'public long currentLineDropSpeedTicks = 0;',
        'public long currentStackRiseSpeedTicks = 0;',
        'public long adjustedMaxLockDelayTicks = 0;',
        'public int createdPiecesCounterForFrequencyPieces = 0;',
        'public boolean switchedHoldPieceAlready = false;',
        'public int timesToFlashBlocks = 5;',
        'public int flashBlockSpeedTicks = 100;',
        'public int flashScreenSpeedTicks = 100;',
        'public boolean flashScreenOnOffToggle = false;',
        'public long flashBlocksTicksCounter = 0;',
        'public long flashScreenTicksCounter = 0;',
        'public ArrayList<Block> currentChainBlocks = new ArrayList<>();',
        'public int resultCaptionFontSize = 40;',
        'public int announcementCaptionFontSize = 20;',
        'public Caption garbageWaitCaption = null;',
        'public int queuedVSGarbageAmountFromOtherPlayer = 0;',
        'public int queuedVSGarbageAmountToSend = 0;',
        'public int garbageWaitForPiecesSetCount = 0;',
        'public int playingFieldGarbageValueCounter = 0;'
    ]
    
    insert_pos = text.find('public class GameLogic')
    insert_pos = text.find('{', insert_pos) + 1
    for field in missing_fields:
        field_name = field.split(' ')[2].strip(';').split('=')[0].strip()
        if field_name not in text:
            text = text[:insert_pos] + f"\n    {field}" + text[insert_pos:]

    # 4. Replace ManagedCaption with Caption
    text = text.replace('ManagedCaption', 'Caption')
    
    # 5. Fix `e.` to `engine.` or `getEngine().`
    text = text.replace(' e.', ' engine.')
    text = text.replace('(e.', '(engine.')
    
    # 6. Fix `ticks()` vs `game.ticks()`
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def fix_grid():
    path = os.path.join(base_path, 'Grid.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove duplicate cellW/cellH
    text = re.sub(r'public int cellW\(\) \{ return game\.cellW\(\); \}', '', text)
    text = re.sub(r'public int cellH\(\) \{ return game\.cellH\(\); \}', '', text)
    
    # Ensure imports
    if 'import org.slf4j.Logger;' not in text:
        text = text.replace('package com.bobsgame.puzzle;', 'package com.bobsgame.puzzle;\nimport org.slf4j.Logger;\nimport org.slf4j.LoggerFactory;')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    fix_gamelogic()
    fix_grid()
