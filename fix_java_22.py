import re
import os

path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\puzzle\GameLogic.java'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix player field
text = text.replace('public PuzzlePlayer* public PuzzlePlayer player = null;', 'public PuzzlePlayer player = null;')

# Fix leaderboard entry
text = text.replace('BobsGameLeaderBoardAndHighScoreBoard::BobsGameLeaderBoardAndHighScoreBoardEntry *', 'com.bobsgame.client.engine.game.nd.bobsgame.BobsGameLeaderBoardAndHighScoreBoard.LeaderBoardScore ')

# Fix static Logger
text = text.replace('public static Logger log;', '')

# Fix chrono
text = text.replace('chrono.milliseconds ms = chrono.duration_cast<chrono.milliseconds>(chrono.system_clock.now().time_since_epoch());', 'long ms = System.currentTimeMillis();')
text = text.replace('timeStarted = (long long)ms.count();', 'timeStarted = ms;')

# Fix vector
text = text.replace('vector<GameLogic > otherPlayers;', 'ArrayList<GameLogic> otherPlayers = new ArrayList<>();')
text = text.replace('otherPlayers.push_back(g2);', 'otherPlayers.add(g2);')
text = text.replace('vector<GameLogic > alivePlayers;', 'ArrayList<GameLogic> alivePlayers = new ArrayList<>();')
text = text.replace('alivePlayers.push_back(g2);', 'alivePlayers.add(g2);')
text = text.replace('alivePlayers.at(', 'alivePlayers.get(')

# Fix sort
text = re.sub(r'sort\(otherPlayers\.begin\(\), otherPlayers\.end\(\), \[\]\(GameLogic a, GameLogic b\) \{return a\.uuid\.compare\(b\.uuid\); \}\);', 'otherPlayers.sort((a, b) -> a.uuid.compareTo(b.uuid));', text)

# Fix for each
text = text.replace('for (auto g2 : otherPlayers)', 'for (GameLogic g2 : otherPlayers)')
text = text.replace('for (auto g2 : alivePlayers)', 'for (GameLogic g2 : alivePlayers)')

# Fix to_string
text = text.replace('to_string(', 'String.valueOf(')

# Fix math
text = text.replace('abs(', 'Math.abs(')
text = text.replace('ceil(', 'Math.ceil(')
text = text.replace('floor(', 'Math.floor(')
text = text.replace('pow(', 'Math.pow(')

# Fix thread
text = text.replace('packetProcessThread = thread(&GameLogic._packetProcessThreadLoop,this);', '// packetProcessThread = new Thread(() -> _packetProcessThreadLoop(this));')
text = text.replace('this_thread.sleep_for(chrono.milliseconds(100));', 'try { Thread.sleep(100); } catch (InterruptedException e) {}')
text = text.replace('this_thread.sleep_for(chrono.milliseconds(10));', 'try { Thread.sleep(10); } catch (InterruptedException e) {}')

# Fix string methods
text = text.replace('.find(', '.indexOf(')
text = text.replace('.substr(', '.substring(')

# Fix delete
text = text.replace('delete ', '// delete ')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
