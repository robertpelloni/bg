import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def fix_gamelogic():
    path = os.path.join(base_path, 'GameLogic.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Fix Room stub
    room_stub = """class Room {
    public float gameSpeedStart = 0.0f;
    public long lockDelayMinimum = -1;
    public long spawnDelayLimit = -1;
    public long spawnDelayMinimum = -1;
    public long totalYLockDelayLimit = -1;
    public long floorSpinLimit = -1;
    public long stackWaitLimit = -1;

    public float gameSpeedChangeRate = 0.001f;
    public float gameSpeedMaximum = 1.0f;
    public long dropDelayMinimum = -1;

    public int levelUpMultiplier = 1;
    public int levelUpCompoundMultiplier = 1;

    public float lockDelayDecreaseRate = 0;
    public float spawnDelayDecreaseRate = 0;

    public boolean endlessMode = false;

    public boolean multiplayer_DisableVSGarbage = false;
    public int multiplayer_GarbageMultiplier = 1;
    public boolean multiplayer_GarbageScaleByDifficulty = false;
    public int multiplayer_GarbageLimit = 0;
}"""
    text = re.sub(r'class Room \{.*?\}', room_stub, text, flags=re.DOTALL)

    # 2. Add NetworkPacket and missing fields at the top of the class
    missing_fields = """
    public static class NetworkPacket {
        public ArrayList<FrameState> frameStates = new ArrayList<>();
    }
    public NetworkPacket networkPacket = new NetworkPacket();
    public long randomSeed = -1;
    public Random randomGenerator = new Random();
    public boolean isNetworkPlayer = false;
    public boolean waitingForStart = false;
    public boolean waitingForReady = false;
    public boolean testing = false;
    public FrameState frameState = new FrameState();
    public ArrayList<FrameState> framesArray = new ArrayList<>();
    public long timeStarted = 0;
    public float gameSpeed = 0.0f;
    public long totalTicksPassed = 0;
    public int createdPiecesCounterForFrequencyPieces = 0;
    public boolean canPressRotateCW = true;
    public boolean canPressRotateCCW = true;
    public boolean canPressRight = true;
    public boolean canPressLeft = true;
    public boolean canPressUp = true;
    public boolean canPressDown = true;
    public boolean canPressSlam = true;
    public boolean canPressHoldRaise = true;
    public float playingFieldX0, playingFieldX1, playingFieldY0, playingFieldY1;
    public float captionX;
    public boolean forceGravityThisFrame = false;
    public long stopStackRiseTicksCounter = 0;
    public int timesToFlashBlocksQueue = 0;
    public int timesToFlashScreenQueue = 0;
    public long lockDelayTicksCounter = 0;
    public long currentLineDropSpeedTicks = 0;
    public long currentStackRiseSpeedTicks = 0;
    public long adjustedMaxLockDelayTicks = 0;
    public boolean switchedHoldPieceAlready = false;
    public int timesToFlashBlocks = 5;
    public int flashBlockSpeedTicks = 100;
    public int flashScreenSpeedTicks = 100;
    public boolean flashScreenOnOffToggle = false;
    public long flashBlocksTicksCounter = 0;
    public long flashScreenTicksCounter = 0;
    public ArrayList<Block> currentChainBlocks = new ArrayList<>();
    public int resultCaptionFontSize = 40;
    public int announcementCaptionFontSize = 20;
    public Caption garbageWaitCaption = null;
    public int queuedVSGarbageAmountFromOtherPlayer = 0;
    public int queuedVSGarbageAmountToSend = 0;
    public int garbageWaitForPiecesSetCount = 0;
    public int playingFieldGarbageValueCounter = 0;
    public int piecesMadeThisGame = 0;
    public int lastPiecesMadeThisGame = 0;
    public int blocksClearedThisGame = 0;
    public int linesClearedThisGame = 0;
    """
    
    # Replace the class content with a clean version of fields
    # I'll just find the first '{' after 'public class GameLogic' and insert there.
    insert_pos = text.find('public class GameLogic')
    insert_pos = text.find('{', insert_pos) + 1
    
    # But first, remove all existing instances of these fields to avoid duplicates
    field_names = [
        'randomSeed', 'randomGenerator', 'isNetworkPlayer', 'waitingForStart', 'waitingForReady',
        'testing', 'frameState', 'framesArray', 'timeStarted', 'gameSpeed', 'totalTicksPassed',
        'createdPiecesCounterForFrequencyPieces', 'canPressRotateCW', 'canPressRotateCCW',
        'canPressRight', 'canPressLeft', 'canPressUp', 'canPressDown', 'canPressSlam',
        'canPressHoldRaise', 'playingFieldX0', 'playingFieldX1', 'playingFieldY0', 'playingFieldY1',
        'captionX', 'forceGravityThisFrame', 'stopStackRiseTicksCounter', 'timesToFlashBlocksQueue',
        'timesToFlashScreenQueue', 'lockDelayTicksCounter', 'currentLineDropSpeedTicks',
        'currentStackRiseSpeedTicks', 'adjustedMaxLockDelayTicks', 'switchedHoldPieceAlready',
        'timesToFlashBlocks', 'flashBlockSpeedTicks', 'flashScreenSpeedTicks', 'flashScreenOnOffToggle',
        'flashBlocksTicksCounter', 'flashScreenTicksCounter', 'currentChainBlocks', 'resultCaptionFontSize',
        'announcementCaptionFontSize', 'garbageWaitCaption', 'queuedVSGarbageAmountFromOtherPlayer',
        'queuedVSGarbageAmountToSend', 'garbageWaitForPiecesSetCount', 'playingFieldGarbageValueCounter',
        'piecesMadeThisGame', 'lastPiecesMadeThisGame', 'blocksClearedThisGame', 'linesClearedThisGame',
        'lockInputCountdownTicks', 'lastPiece', 'announcementCaptions', 'infoCaptions', 'difficultyCaption',
        'gameTypeCaption', 'rulesCaption1', 'rulesCaption2', 'rulesCaption3', 'levelCaption',
        'piecesToLevelUpThisLevelCaption', 'piecesLeftToLevelUpCaption', 'linesClearedThisGameCaption',
        'blocksClearedThisGameCaption', 'piecesMadeThisGameCaption', 'totalLinesClearedCaption',
        'totalBlocksClearedCaption', 'totalPiecesMadeCaption', 'currentChainCaption', 'currentComboCaption',
        'comboChainTotalCaption', 'lineDropTicksCounter', 'lockDelayCaption', 'spawnDelayCaption',
        'lineClearDelayCaption', 'gravityCaption', 'stopCounterCaption', 'totalTicksPassedCaption',
        'holdCaption', 'nextCaption', 'winCaption', 'loseCaption', 'deadCaption', 'creditsCaption'
    ]
    
    for name in field_names:
        text = re.sub(r'public\s+.*?\s+' + name + r'\s*(=.*?)?;', '', text)
        text = re.sub(r'private\s+.*?\s+' + name + r'\s*(=.*?)?;', '', text)

    # Re-insert the clean fields
    text = text[:insert_pos] + missing_fields + text[insert_pos:]

    # 3. Fix Logger
    text = text.replace('public static Logger log = new Logger("GameLogic");', '')
    text = text[:insert_pos] + '\n    public static final org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(GameLogic.class);' + text[insert_pos:]

    # 4. Fix stubs/imports
    text = text.replace('ManagedCaption', 'Caption')
    
    # 5. Fix `e.` to `engine.`
    text = text.replace(' e.', ' engine.')
    text = text.replace('(e.', '(engine.')

    # 6. Add missing methods
    missing_methods = """
    public long ticks() { return frameState != null ? frameState.ticksPassed : 0; }
    public void waitForPressStart() {}
    public void waitForReady() {}
    public void updateCaptionFadeValues() {}
    public void updateCaptions() {}
    public void wonSequence() {}
    public void lostSequence() {}
    public void diedSequence() {}
    public void creditsSequence() {}
    public void doExtraStageEffects() {}
    public void updateSpecialPiecesAndBlocks() {}
    public void processQueuedGarbageSentFromOtherPlayer() {}
    public void checkForChain() {}
    public void handleNewChain() {}
    public void checkForFastMusic() {}
    public void updateKeyInput() {}
    public void flashChainBlocks() {}
    public void flashScreen() {}
    public void removeFlashedChainBlocks() {}
    public void updateScore() {}
    public void makeAnnouncementCaption(String s) {}
    public void makeAnnouncementCaption(String s, BobColor c) {}
    """
    
    # Remove existing stubs of these methods if any
    for m in ['ticks', 'waitForPressStart', 'waitForReady', 'updateCaptionFadeValues', 'updateCaptions', 
              'wonSequence', 'lostSequence', 'diedSequence', 'creditsSequence', 'doExtraStageEffects',
              'updateSpecialPiecesAndBlocks', 'processQueuedGarbageSentFromOtherPlayer', 'checkForChain',
              'handleNewChain', 'checkForFastMusic', 'updateKeyInput', 'flashChainBlocks', 'flashScreen',
              'removeFlashedChainBlocks', 'updateScore', 'makeAnnouncementCaption']:
        text = re.sub(r'public\s+.*?\s+' + m + r'\s*\(.*?\}\n', '', text, flags=re.DOTALL)

    text = text.rstrip().rstrip('}') + "\n" + missing_methods + "\n}\n"

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    fix_gamelogic()
