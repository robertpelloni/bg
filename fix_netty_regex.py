import os
import re

base = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'

# Fix GameClientTCP.java
path = base + r'\client\src\main\java\com\bobsgame\client\network\GameClientTCP.java'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add a closing brace after setServerIPAddress_S(null);
text = re.sub(r'setServerIPAddress_S\(null\);\s*//===============================================================================================\s*@Override\s*public void channelActive',
              r'setServerIPAddress_S(null);\n\t\t}\n\n\t\t//===============================================================================================\n\t\t@Override\n\t\tpublic void channelActive', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix IndexClientTCP.java
path = base + r'\server\src\main\java\com\bobsgame\server\IndexClientTCP.java'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove the duplicate handler configuration block
text = re.sub(r'pipeline\.addLast\("handler", new IndexClientHandler\(\)\);\s*\}\s*\}\);\s*//clientBootstrap.*?pipeline\.addLast\("handler", new IndexClientHandler\(\)\);\s*\}\s*\}\);',
              r'pipeline.addLast("handler", new IndexClientHandler());\n            }\n        });', text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix STUNServerUDP.java
path = base + r'\server\src\main\java\com\bobsgame\stunserver\STUNServerUDP.java'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'if\(s\.startsWith\(BobNet\.STUN_Request\)\)\{incomingSTUNRequest\(packet, s\);return;\}\s*STUNServerMain\.totalConnections\+\+;\s*if\(s\.startsWith\(BobNet\.STUN_Request\)\) \{\s*incomingSTUNRequest\(ctx, s, packet\.sender\(\)\);\s*\}\s*\} else \{\s*// Should not happen with DatagramChannel without decoders\s*\}',
              r'if(s.startsWith(BobNet.STUN_Request)){incomingSTUNRequest(packet, s);return;}', text)

text = re.sub(r'ChannelPipeline pipeline = ch\.pipeline\(\);\s*workerGroup = new NioEventLoopGroup\(\);',
              r'ChannelPipeline pipeline = ch.pipeline();\n                }\n            });\n\n        workerGroup = new NioEventLoopGroup();', text)

# fix the method call argument mismatch for incomingSTUNRequest
text = re.sub(r'channel\.writeAndFlush\(new DatagramPacket\(\s*Unpooled\.copiedBuffer\(BobNet\.STUN_Response\+r\.userID2\+",(.*?)",\s*CharsetUtil\.UTF_8\),\s*r\.userIP1\)\);',
              r'writeToAddress(channel, BobNet.STUN_Response+r.userID2+","\1", r.userIP1);', text, flags=re.DOTALL)
text = re.sub(r'channel\.writeAndFlush\(new DatagramPacket\(\s*Unpooled\.copiedBuffer\(BobNet\.STUN_Response\+r\.userID1\+",(.*?)",\s*CharsetUtil\.UTF_8\),\s*r\.userIP2\)\);',
              r'writeToAddress(channel, BobNet.STUN_Response+r.userID1+","\1", r.userIP2);', text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
