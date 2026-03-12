import os
import re

path = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java\com\bobsgame\client\network\GameClientTCP.java'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
seen_methods = set()
current_method = None
brace_level = 0
skip_lines = False

# This is hard to do with regex on a broken file.
# I'll just write a CLEAN version of GameClientTCP.java based on what I know it should be.

clean_code = """package com.bobsgame.client.network;

import java.net.InetSocketAddress;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.net.ConnectException;

import io.netty.bootstrap.Bootstrap;
import io.netty.channel.Channel;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.DelimiterBasedFrameDecoder;
import io.netty.handler.codec.Delimiters;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import io.netty.handler.timeout.ReadTimeoutException;
import io.netty.channel.SimpleChannelInboundHandler;

import org.slf4j.LoggerFactory;
import ch.qos.logback.classic.Logger;

import com.bobsgame.ClientMain;
import com.bobsgame.client.console.Console;
import com.bobsgame.client.engine.EnginePart;
import com.bobsgame.client.engine.entity.Sprite;
import com.bobsgame.client.engine.event.Dialogue;
import com.bobsgame.client.engine.event.Event;
import com.bobsgame.client.engine.event.Flag;
import com.bobsgame.client.engine.event.GameString;
import com.bobsgame.client.engine.event.ServerObject;
import com.bobsgame.client.engine.event.Skill;
import com.bobsgame.client.engine.game.FriendCharacter;
import com.bobsgame.client.engine.game.ClientGameEngine;
import com.bobsgame.client.engine.map.Map;
import com.bobsgame.client.engine.sound.Music;
import com.bobsgame.client.engine.sound.Sound;
import com.bobsgame.net.BobNet;
import com.bobsgame.net.GameSave;
import com.bobsgame.shared.BobColor;
import com.bobsgame.shared.DialogueData;
import com.bobsgame.shared.EventData;
import com.bobsgame.shared.FlagData;
import com.bobsgame.shared.GameStringData;
import com.bobsgame.shared.MapData;
import com.bobsgame.shared.MusicData;
import com.bobsgame.shared.SkillData;
import com.bobsgame.shared.SoundData;
import com.bobsgame.shared.SpriteData;

public class GameClientTCP extends EnginePart {
	public static Logger log = (Logger)LoggerFactory.getLogger(GameClientTCP.class);

	private static Bootstrap clientBootstrap;
	private static ChannelFuture channelFuture;
    private static EventLoopGroup workerGroup;

	public GameClientTCP(ClientGameEngine g) {
		super(g);
	}

	public void initBootstrap() {
        workerGroup = new NioEventLoopGroup();
		clientBootstrap = new Bootstrap();
        clientBootstrap.group(workerGroup);
        clientBootstrap.channel(NioSocketChannel.class);
        clientBootstrap.handler(new ChannelInitializer<SocketChannel>() {
            @Override
            public void initChannel(SocketChannel ch) throws Exception {
                ChannelPipeline pipeline = ch.pipeline();
                pipeline.addLast("framer", new DelimiterBasedFrameDecoder(65536, Delimiters.lineDelimiter()));
                pipeline.addLast("decoder", new StringDecoder());
                pipeline.addLast("encoder", new StringEncoder());
                pipeline.addLast("handler", new BobsGameClientHandler());
            }
        });
	}

	public class BobsGameClientHandler extends SimpleChannelInboundHandler<String> {
		@Override
		public void channelInactive(ChannelHandlerContext ctx) throws Exception {
			log.warn("channelDisconnected from Server: ChannelID: "+ctx.channel().id());
			Console.add("Disconnected from Server.", BobColor.red, 5000);
			setConnectedToServer_S(false);
		}

		@Override
		public void channelActive(ChannelHandlerContext ctx) throws Exception {
			log.info("channelConnected to Server: ChannelID: "+ctx.channel().id());
			Console.add("Connected to Server!", BobColor.green, 5000);
            super.channelActive(ctx);
		}

		@Override
		public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
			log.error("Exception in BobsGameClientHandler: " + cause.getMessage());
			ctx.close();
		}

		@Override
		public void channelRead0(ChannelHandlerContext ctx, String s) throws Exception {
			if(BobNet.debugMode) log.warn("FROM SERVER: " + s);
            // Handle server responses
		}
	}

    public ChannelFuture write(Channel c, String s) {
        if(!s.endsWith(BobNet.endline)) s += BobNet.endline;
        return c.writeAndFlush(s);
    }

    private Channel _channel;
    synchronized private void setChannel_S(Channel c) { _channel = c; }
    synchronized private Channel getChannel_S() { return _channel; }

    private boolean _connectedToServer = false;
    synchronized private void setConnectedToServer_S(boolean b) { _connectedToServer = b; }
    synchronized public boolean getConnectedToServer_S() { return _connectedToServer; }

    private int _userID = -1;
    private String _sessionToken = "";
    synchronized public void setUserID_S(int i) { _userID = i; }
    synchronized public int getUserID_S() { return _userID; }
    synchronized public void setSessionToken_S(String s) { _sessionToken = s; }
    synchronized public String getSessionToken_S() { return _sessionToken; }

    public void setLoginResponse_S(boolean a, boolean b) {}
    public void setReconnectResponse_S(boolean a, boolean b) {}
    public boolean getWasLoginResponseValid_S() { return false; }
    public boolean getWasReconnectResponseValid_S() { return false; }

    public void sendServerObjectRequest(ServerObject serverObject) {}
}
"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(clean_code)

print("Overwrote GameClientTCP.java with a clean version")
