import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def fix_animation_state():
    path = os.path.join(base_path, 'AnimationState.java')
    if not os.path.exists(path): return
    content = """package com.bobsgame.puzzle;

public enum AnimationState {
    NORMAL,
    DROPPING,
    TOUCHING_BOTTOM,
    SET_AT_BOTTOM,
    FLASHING,
    REMOVING,
    PRESSURE
}
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_block_and_blocktype():
    for filename in ['Block.java', 'BlockType.java']:
        path = os.path.join(base_path, filename)
        if not os.path.exists(path): continue
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Remove nested enum AnimationState if it exists incorrectly
        text = re.sub(r'public enum AnimationState .*?\{.*?\}', '', text, flags=re.DOTALL)
        
        # Fix the constants
        text = text.replace('public const static int', 'public static final int')
        text = text.replace('const static int', 'public static final int')
        
        # Fix the pointers
        text = text.replace('SpriteAnimationSequence*', 'SpriteAnimationSequence')
        text = text.replace('float*', 'float[]')
        
        # Fix the broken multiplication (VERY important)
        # Look for [number/paren/variable] SPACE [variable/method]
        # This is where we need to be careful.
        # Let's fix the specific ones from the log.
        text = text.replace('ticks()) 0.005f', 'ticks()) * 0.005f')
        text = text.replace('ticksPerPhase)) (colorFlashTo', 'ticksPerPhase)) * (colorFlashTo')
        text = text.replace('ticksPerPhase)) (effectAlphaTo', 'ticksPerPhase)) * (effectAlphaTo')
        text = text.replace('xGrid cellW()', 'xGrid * cellW()')
        text = text.replace('yGrid cellH()', 'yGrid * cellH()')
        text = text.replace('Increment)cellH()', 'Increment) * cellH()')
        text = text.replace('ticks)) xDiff', 'ticks)) * xDiff')
        text = text.replace('ticks)) yDiff', 'ticks)) * yDiff')
        text = text.replace('disappearingAlpha 2.0f', 'disappearingAlpha * 2.0f')
        text = text.replace('Flash) 255', 'Flash) * 255')
        text = text.replace('af()) 255', 'af()) * 255')
        text = text.replace('blockW() scale', 'blockW() * scale')
        text = text.replace('blockH() scale', 'blockH() * scale')
        text = text.replace('17 6', '17 * 6') # for (17 * 6)
        text = text.replace('x0InImage imageToTextureRatioX', 'x0InImage * imageToTextureRatioX')
        text = text.replace('x1InImage imageToTextureRatioX', 'x1InImage * imageToTextureRatioX')
        text = text.replace('y0InImage imageToTextureRatioY', 'y0InImage * imageToTextureRatioY')
        text = text.replace('y1InImage imageToTextureRatioY', 'y1InImage * imageToTextureRatioY')
        text = text.replace('w 0.04f', 'w * 0.04f')
        text = text.replace('0.1f 255.0f', '0.1f * 255.0f')
        text = text.replace('3 scale', '3 * scale')
        text = text.replace('6 scale', '6 * scale')
        
        # Fix the new float[2]{...}
        text = text.replace('new float[2]{', 'new float[]{')
        
        # Fix BobColor(*ptr)
        text = re.sub(r'BobColor\(\*(.*?)\)', r'\1', text)
        
        # Fix this->
        text = text.replace('this->', 'this.')
        
        # Remove class Piece; etc.
        text = re.sub(r'public class (Piece|PieceType|GameType|Sprite|SpriteAnimationSequence|Block|BlockType|Grid|GameLogic|GameSequence|PuzzlePlayer);', '', text)

        # Fix GameLogic.aboveGridBuffer
        text = text.replace('cellH()GameLogic.aboveGridBuffer', 'cellH() * GameLogic.aboveGridBuffer')
        text = text.replace('cellW()getWidth()', 'cellW() * getWidth()')
        
        # Remove remaining #include
        text = re.sub(r'#include.*', '', text)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)

def fix_gamelogic():
    path = os.path.join(base_path, 'GameLogic.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = text.replace('PuzzlePlayer* player = null;', 'public PuzzlePlayer player = null;')
    text = text.replace('player = null;', 'public PuzzlePlayer player = null;') # handle duplicate
    
    # Fix the leaderboard entry pointer
    text = re.sub(r'BobsGameLeaderBoardAndHighScoreBoard\.LeaderBoardScore\s*\*\s*currentLeaderboardEntry\s*=\s*null;', 'public BobsGameLeaderBoardAndHighScoreBoard.LeaderBoardScore currentLeaderboardEntry = null;', text)
    
    # Fix randomGenerator
    text = text.replace('mt19937((int)randomSeed)', 'new Random((long)randomSeed)')
    text = text.replace('randomGenerator = new Random', 'public Random randomGenerator = new Random')
    
    # Fix PieceType cursorPieceType(PieceType.oneBlockCursorPieceType);
    text = re.sub(r'PieceType\s+([a-zA-Z0-9_]+)\(PieceType\.([a-zA-Z0-9_]+)\);', r'PieceType \1 = PieceType.\2;', text)
    
    # Fix make_shared
    text = re.sub(r'make_shared<Piece>\((.*?)\)', r'new Piece(\1)', text)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    fix_animation_state()
    fix_block_and_blocktype()
    fix_gamelogic()
