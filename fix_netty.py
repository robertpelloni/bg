import os

def replace_in_file(path, old, new):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

base = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava'

# Fix GameClientTCP.java
old_gctcp = """                        setConnectedToServer_S(false);
                        setNotAuthorizedOnServer();
                        setServerIPAddress_S(null);

                //===============================================================================================
                @Override
                public void channelActive(ChannelHandlerContext ctx) throws Exception"""
new_gctcp = """                        setConnectedToServer_S(false);
                        setNotAuthorizedOnServer();
                        setServerIPAddress_S(null);
                }

                //===============================================================================================
                @Override
                public void channelActive(ChannelHandlerContext ctx) throws Exception"""
replace_in_file(base + r'\client\src\main\java\com\bobsgame\client\network\GameClientTCP.java', old_gctcp, new_gctcp)

# Fix IndexClientTCP.java
old_ictcp = """                pipeline.addLast("handler", new IndexClientHandler());
            }
        });

                //clientBootstrap.setOption("sendBufferSize", 65536);
                //clientBootstrap.setOption("receiveBufferSize", 65536);
                //clientBootstrap.setOption("receiveBufferSizePredictorFactory", new AdaptiveReceiveBufferSizePredictorFactory());

                //clientBootstrap.setOption("tcpNoDelay", true);
                //clientBootstrap.setOption("keepAlive", true);

                pipeline.addLast("handler", new IndexClientHandler());
            }
        });"""
new_ictcp = """                pipeline.addLast("handler", new IndexClientHandler());
            }
        });"""
replace_in_file(base + r'\server\src\main\java\com\bobsgame\server\IndexClientTCP.java', old_ictcp, new_ictcp)

# Fix STUNServerUDP.java
old_stun = """            .handler(new ChannelInitializer<DatagramChannel>() {
                @Override
                public void initChannel(DatagramChannel ch) throws Exception {
                    ChannelPipeline pipeline = ch.pipeline();

        workerGroup = new NioEventLoopGroup();"""
new_stun = """            .handler(new ChannelInitializer<DatagramChannel>() {
                @Override
                public void initChannel(DatagramChannel ch) throws Exception {
                    ChannelPipeline pipeline = ch.pipeline();
                }
            });

        workerGroup = new NioEventLoopGroup();"""
replace_in_file(base + r'\server\src\main\java\com\bobsgame\stunserver\STUNServerUDP.java', old_stun, new_stun)
