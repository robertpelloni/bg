import os
import re

base = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'

# 1. Add HikariCP to build.gradle
with open(base + r'\build.gradle', 'r', encoding='utf-8') as f:
    gradle = f.read()
if 'com.zaxxer:HikariCP' not in gradle:
    gradle = gradle.replace("implementation 'com.mchange:c3p0:0.9.5.5'", "implementation 'com.mchange:c3p0:0.9.5.5'\n    implementation 'com.zaxxer:HikariCP:5.0.1'")
with open(base + r'\build.gradle', 'w', encoding='utf-8') as f:
    f.write(gradle)

# 2. Fix STUNServerUDP.java
with open(base + r'\server\src\main\java\com\bobsgame\stunserver\STUNServerUDP.java', 'r', encoding='utf-8') as f:
    stun = f.read()

# Make group not final or EventLoopGroup
stun = stun.replace('static final EventExecutorGroup group = new DefaultEventExecutorGroup(16);', 'static EventLoopGroup group = new NioEventLoopGroup(16);')
stun = stun.replace('import io.netty.channel.socket.nio.NioDatagramChannel;', 'import io.netty.channel.socket.nio.NioDatagramChannel;\nimport io.netty.channel.socket.DatagramChannel;')

with open(base + r'\server\src\main\java\com\bobsgame\stunserver\STUNServerUDP.java', 'w', encoding='utf-8') as f:
    f.write(stun)

# 3. GameServerTCP.java uncomment Hikari stuff
with open(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'r', encoding='utf-8') as f:
    gstcp = f.read()
gstcp = gstcp.replace('// static HikariDataSource', 'static HikariDataSource')
gstcp = gstcp.replace('// HikariConfig', 'HikariConfig')
gstcp = gstcp.replace('// amazonRDS', 'amazonRDS')
gstcp = gstcp.replace('// dreamhost', 'dreamhost')
if 'import com.zaxxer.hikari.HikariConfig;' not in gstcp:
    gstcp = gstcp.replace('import java.net.InetSocketAddress;', 'import java.net.InetSocketAddress;\nimport com.zaxxer.hikari.HikariConfig;\nimport com.zaxxer.hikari.HikariDataSource;')
with open(base + r'\server\src\main\java\com\bobsgame\server\GameServerTCP.java', 'w', encoding='utf-8') as f:
    f.write(gstcp)

# 4. Settings.java
with open(base + r'\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Settings.java', 'r', encoding='utf-8') as f:
    settings = f.read()
settings = settings.replace('public class GameTypeLegacy', 'public class GameType')
with open(base + r'\client\src\main\java\com\bobsgame\client\engine\game\nd\bobsgame\game\Settings.java', 'w', encoding='utf-8') as f:
    f.write(settings)

# 5. GameSelector.java
with open(base + r'\client\src\main\java\com\bobsgame\client\engine\game\gui\GameSelector.java', 'r', encoding='utf-8') as f:
    gs = f.read()
gs = gs.replace('//bg.ME.setGameSequence(seq);', 'bg.ME.setGameSequence(seq);')
with open(base + r'\client\src\main\java\com\bobsgame\client\engine\game\gui\GameSelector.java', 'w', encoding='utf-8') as f:
    f.write(gs)
