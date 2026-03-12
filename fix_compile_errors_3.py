import os

base = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'

def replace_in_file(path, old, new):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# Settings.java
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Settings.java', 'public class GameTypeLegacy', 'class GameTypeLegacy')

# GameServerTCP.java (comment out all Hikari stuff)
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'import com.zaxxer.hikari.HikariConfig;', '')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'import com.zaxxer.hikari.HikariDataSource;', '')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'static HikariDataSource', '// static HikariDataSource')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'HikariConfig', '// HikariConfig')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'amazonRDS', '// amazonRDS')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'dreamhost', '// dreamhost')

# FriendUDPConnection.java
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\network\FriendUDPConnection.java', '@Override\n\tpublic void handleMessage(String s)', 'public void handleMessage(String s)')
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\network\FriendUDPConnection.java', '@Override\r\n\tpublic void handleMessage(String s)', 'public void handleMessage(String s)')
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\network\FriendUDPConnection.java', '@Override\n        public void handleMessage(String s)', 'public void handleMessage(String s)')

