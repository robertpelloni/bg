import re
import os

base_path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle'

def fix_gamelogic():
    path = os.path.join(base_path, 'GameLogic.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update Room stub
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
    public long stackWaitLimit = -1;
}"""
    # Fix the duplicate stackWaitLimit in my own string
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

    # 2. Add NetworkPacket inner class
    network_packet = """    public static class NetworkPacket {
        public ArrayList<FrameState> frameStates = new ArrayList<>();
    }
    public NetworkPacket networkPacket = new NetworkPacket();"""
    
    if 'class NetworkPacket' not in text:
        insert_pos = text.find('public class GameLogic')
        insert_pos = text.find('{', insert_pos) + 1
        text = text[:insert_pos] + "\n" + network_packet + text[insert_pos:]

    # 3. Add missing basic fields
    missing_fields = [
        'public long randomSeed = -1;',
        'public Random randomGenerator = new Random();',
        'public boolean isNetworkPlayer = false;',
        'public boolean waitingForStart = false;',
        'public boolean waitingForReady = false;',
        'public boolean testing = false;',
        'public FrameState frameState = new FrameState();',
        'public ArrayList<FrameState> framesArray = new ArrayList<>();',
        'public long timeStarted = 0;',
        'public float gameSpeed = 0.0f;',
        'public long totalTicksPassed = 0;',
        'public int createdPiecesCounterForFrequencyPieces = 0;',
        'public boolean canPressRotateCW = true;',
        'public boolean canPressRotateCCW = true;',
        'public boolean canPressRight = true;',
        'public boolean canPressLeft = true;',
        'public boolean canPressUp = true;',
        'public boolean canPressDown = true;',
        'public boolean canPressSlam = true;',
        'public boolean canPressHoldRaise = true;'
    ]
    
    insert_pos = text.find('public class GameLogic')
    insert_pos = text.find('{', insert_pos) + 1
    for field in missing_fields:
        field_name = field.split(' ')[2].split('=')[0].strip()
        if f" {field_name} " not in text and f".{field_name}" not in text:
             text = text[:insert_pos] + f"\n    {field}" + text[insert_pos:]

    # 4. Fix Logger instantiation
    text = text.replace('public static Logger log = new Logger("GameLogic");', 'public static org.slf4j.Logger log = org.slf4j.LoggerFactory.getLogger(GameLogic.class);')

    # 5. Fix duplicate variable declarations (some might have missed in previous turn)
    # Regex to find `public long lockInputCountdownTicks = 0;` and remove subsequent ones
    # text = re.sub(r'(public long lockInputCountdownTicks = 0;.*?)public long lockInputCountdownTicks = 0;', r'\1', text, flags=re.DOTALL)
    
    # 6. Fix `e.` to `engine.` (already done but let's be sure)
    
    # 7. Add `ticks()` implementation
    if 'public long ticks()' not in text:
        text = text.replace('public class GameLogic {', 'public class GameLogic {\n    public long ticks() { return frameState != null ? frameState.ticksPassed : 0; }')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def fix_settings():
    path = os.path.join(base_path, 'Settings.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # If it's the old GameType, we might need to rename it or ensure GameType.java exists.
    # The user said they have GameType.java in the puzzle directory.
    # Let's check GameType.java
    
def fix_gametype():
    path = os.path.join(base_path, 'GameType.java')
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Ensure enums are there
    enums = """    public enum GameMode { STACK, DROP }
    public enum GarbageSpawnRule { NONE, TICKS, PIECES_MADE, BLOCKS_CLEARED, LINES_CLEARED }
    public enum VSGarbageDropRule { FALL_FROM_CEILING_IN_EVEN_ROWS, RISE_FROM_FLOOR_IN_EVEN_ROWS }"""
    
    if 'enum GameMode' not in text:
        insert_pos = text.find('public class GameType')
        insert_pos = text.find('{', insert_pos) + 1
        text = text[:insert_pos] + "\n" + enums + text[insert_pos:]
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    fix_gamelogic()
    fix_gametype()
