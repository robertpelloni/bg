import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java'

def fix_lwjglutils():
    path = os.path.join(root, 'com/bobsgame/client/LWJGLUtils.java')
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace('import de.matthiasmann.twl.input.lwjgl.LWJGLInput;', '')
    text = text.replace('import de.matthiasmann.twl.renderer.lwjgl.LWJGLRenderer;', '')
    text = text.replace('public static LWJGLInput twlInput;', 'public static Object twlInput;')
    text = text.replace('public static LWJGLRenderer TWLrenderer = null;', 'public static Object TWLrenderer = null;')
    text = text.replace('TWLrenderer = new LWJGLRenderer();', 'TWLrenderer = null;')
    text = text.replace('twlInput = (LWJGLInput)TWLrenderer.getInput();', 'twlInput = null;')
    with open(path, 'w', encoding='utf-8') as f: f.write(text)

def fix_friendudp():
    path = os.path.join(root, 'com/bobsgame/client/network/FriendUDPConnection.java')
    with open(path, 'r', encoding='utf-8') as f: text = f.read()
    text = text.replace('incomingSTUNReply(ctx, s)', 'incomingSTUNReply(s)')
    with open(path, 'w', encoding='utf-8') as f: f.write(text)

def fix_blockeditor():
    path = os.path.join(root, 'com/bobsgame/client/engine/game/gui/customGameEditor/BlockEditorPanel.java')
    with open(path, 'r', encoding='utf-8') as f: text = f.read()
    if 'import java.util.ArrayList;' not in text:
        text = text.replace('package com.bobsgame.client.engine.game.gui.customGameEditor;', 'package com.bobsgame.client.engine.game.gui.customGameEditor;\nimport java.util.ArrayList;\nimport java.util.Arrays;')
    with open(path, 'w', encoding='utf-8') as f: f.write(text)

def fix_pieceeditor():
    path = os.path.join(root, 'com/bobsgame/client/engine/game/gui/customGameEditor/PieceEditorPanel.java')
    with open(path, 'r', encoding='utf-8') as f: text = f.read()
    text = text.replace('new ArrayList<Rotation>()', 'new Piece.RotationSet("")')
    text = text.replace('new ArrayList<Piece.Rotation>()', 'new Piece.RotationSet("")')
    with open(path, 'w', encoding='utf-8') as f: f.write(text)

fix_lwjglutils()
fix_friendudp()
fix_blockeditor()
fix_pieceeditor()
print("Fixed last 10 errors")
