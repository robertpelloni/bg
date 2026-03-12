import os
import re

base = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'

def replace_in_file(path, old, new):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# Settings.java
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Settings.java', 'public class GameType\r\n', 'public class GameTypeLegacy\r\n')
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Settings.java', 'public class GameType\n', 'public class GameTypeLegacy\n')

# GameServerTCP.java
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'import com.zaxxer.hikari.HikariConfig;', '')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'import com.zaxxer.hikari.HikariDataSource;', '')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'static HikariDataSource amazonRDSConnectionPool = null;', '// static HikariDataSource amazonRDSConnectionPool = null;')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'static HikariDataSource dreamhostSQLConnectionPool = null;', '// static HikariDataSource dreamhostSQLConnectionPool = null;')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'HikariConfig amazonConfig = new HikariConfig();', '// HikariConfig amazonConfig = new HikariConfig();')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'amazonRDSConnectionPool = new HikariDataSource(amazonConfig);', '// amazonRDSConnectionPool = new HikariDataSource(amazonConfig);')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'HikariConfig dreamhostConfig = new HikariConfig();', '// HikariConfig dreamhostConfig = new HikariConfig();')
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'dreamhostSQLConnectionPool = new HikariDataSource(dreamhostConfig);', '// dreamhostSQLConnectionPool = new HikariDataSource(dreamhostConfig);')

# FriendUDPConnection.java
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\network\FriendUDPConnection.java', 'public class FriendUDPConnection extends UDPConnection implements UDPInterface', 'public class FriendUDPConnection extends UDPConnection')
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\network\FriendUDPConnection.java', 'if(s.startsWith(BobNet.STUN_Response)){incomingSTUNReply(ctx, s);return;}', 'if(s.startsWith(BobNet.STUN_Response)){incomingSTUNReply(null, s);return;}')

# GameClientTCP.java
with open(base + r'\client\src\main\java\com\bobsgame\client\network\GameClientTCP.java', 'r', encoding='utf-8') as f:
    gctcp = f.read()
if 'import java.net.ConnectException;' not in gctcp:
    gctcp = gctcp.replace('import java.net.InetSocketAddress;', 'import java.net.InetSocketAddress;\nimport java.net.ConnectException;')
with open(base + r'\client\src\main\java\com\bobsgame\client\network\GameClientTCP.java', 'w', encoding='utf-8') as f:
    f.write(gctcp)

# GameSelector.java
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\engine\game\gui\GameSelector.java', 'bg.ME.setGameSequence(seq);', '//bg.ME.setGameSequence(seq);')

# STUNServerUDP.java
with open(base + r'\server\src\main\java\com\bobsgame\stunserver\STUNServerUDP.java', 'r', encoding='utf-8') as f:
    stun = f.read()

stun = stun.replace('group = new NioEventLoopGroup();', '// group = new NioEventLoopGroup();')
stun = stun.replace('ChannelInitializer<DatagramChannel>', 'ChannelInitializer<NioDatagramChannel>')
stun = stun.replace('public void initChannel(DatagramChannel ch)', 'public void initChannel(NioDatagramChannel ch)')
if 'import io.netty.channel.ChannelOption;' not in stun:
    stun = stun.replace('import io.netty.channel.Channel;', 'import io.netty.channel.Channel;\nimport io.netty.channel.ChannelOption;')
if 'import io.netty.channel.AdaptiveRecvByteBufAllocator;' not in stun:
    stun = stun.replace('import io.netty.channel.Channel;', 'import io.netty.channel.Channel;\nimport io.netty.channel.AdaptiveRecvByteBufAllocator;')
stun = stun.replace('connectionlessBootstrap.group(group)', '// connectionlessBootstrap.group(group)')

with open(base + r'\server\src\main\java\com\bobsgame\stunserver\STUNServerUDP.java', 'w', encoding='utf-8') as f:
    f.write(stun)

