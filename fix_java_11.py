import re
import os

paths = [
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Grid.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Block.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\Piece.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameLogic.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameType.java',
    r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\shared\src\main\java\com\bobsgame\puzzle\GameSequence.java'
]

def fix_code(text):
    # const String -> String
    text = text.replace('const String ', 'String ')
    text = text.replace('const string ', 'String ')
    text = text.replace('const ', ' ')
    
    # GameType.difficulty_BEGINNER -> difficulty_BEGINNER
    text = re.sub(r'([A-Za-z0-9_]+)\s+[A-Za-z0-9_]+\.([A-Za-z0-9_]+)\s*=', r'\1 \2 =', text)
    
    # long public long -> public long
    text = text.replace('long public long', 'public long')
    text = text.replace('int public int', 'public int')
    
    # string public string -> public String
    text = text.replace('string public string', 'public String')
    text = text.replace('String public String', 'public String')
    
    # &( -> (
    text = text.replace('&(', '(')
    
    # ArrayList<FrameState>() -> new ArrayList<FrameState>()
    text = re.sub(r'=\s*ArrayList<([A-Za-z0-9_]+)>\(\);', r'= new ArrayList<\1>();', text)
    
    # StringConverterHelper.fromString<long> -> Long.parseLong
    text = re.sub(r'StringConverterHelper\.fromString<long>\((.*?)\)', r'Long.parseLong(\1)', text)
    
    # catch (exception) -> catch (Exception e)
    text = text.replace('catch (exception)', 'catch (Exception e)')
    
    # Block b(this, grid, null, blockType); -> Block b = new Block(this, grid, null, blockType);
    text = re.sub(r'Block\s+([a-zA-Z0-9_]+)\((.*?)\);', r'Block \1 = new Block(\2);', text)
    
    # uniform_real_distribution<double> distribution(0.0, 1.0); -> double distribution = Math.random();
    text = text.replace('uniform_real_distribution<double> distribution(0.0, 1.0);', 'double distribution = Math.random();')
    
    # boost::uuids::random_generator generator; -> 
    text = re.sub(r'public boost::uuids::random_generator.*?;', '', text)
    
    # public importExport_gameUUIDs = gameUUIDs; -> public ArrayList<String> importExport_gameUUIDs = gameUUIDs;
    text = text.replace('public importExport_gameUUIDs', 'public ArrayList<String> importExport_gameUUIDs')
    
    # [] (GameLogic a, GameLogic b) {return a.uuid.compare(b.uuid); }
    text = re.sub(r'sort\((.*?)\.begin\(\),\s*(.*?)\.end\(\),\s*\[\]\s*\([A-Za-z0-9_]+\s+([a-zA-Z0-9_]+),\s*[A-Za-z0-9_]+\s+([a-zA-Z0-9_]+)\)\s*\{return\s+([^;]+);\s*\}\);',
                  r'\1.sort((a, b) -> \5);', text)
                  
    # remove #ifdef again just in case
    text = re.sub(r'#ifdef\s+[A-Za-z0-9_]+', '', text)
    text = re.sub(r'#endif', '', text)
    
    # remove oss1 << setfill('0')
    text = re.sub(r'[a-zA-Z0-9_]+\s*<<.*?<<.*?;', '// stringstream logic removed', text)
    
    # BobsGameLeaderBoardAndHighScoreBoard::BobsGameLeaderBoardAndHighScoreBoardEntry -> BobsGameLeaderBoardAndHighScoreBoardEntry
    text = text.replace('BobsGameLeaderBoardAndHighScoreBoard::BobsGameLeaderBoardAndHighScoreBoardEntry', 'BobsGameLeaderBoardAndHighScoreBoard.LeaderBoardScore')

    return text

for path in paths:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = fix_code(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
