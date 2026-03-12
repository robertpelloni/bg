import os
import re

root = r'C:\Users\hyper\workspace\bg\bobsgameonlinejava\src\main\java'

def fix_renderer():
    # Create the missing package and interface
    dir_path = os.path.join(root, 'de/matthiasmann/twl/renderer')
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, 'Renderer.java'), 'w', encoding='utf-8') as f:
        f.write("package de.matthiasmann.twl.renderer;\npublic interface Renderer { void syncViewportSize(); }\n")
    
    # Also need de.matthiasmann.twl.GUI and other classes used in constructors
    dir_path_twl = os.path.join(root, 'de/matthiasmann/twl')
    os.makedirs(dir_path_twl, exist_ok=True)
    with open(os.path.join(dir_path_twl, 'GUI.java'), 'w', encoding='utf-8') as f:
        f.write("package de.matthiasmann.twl;\nimport de.matthiasmann.twl.renderer.Renderer;\npublic class GUI { public GUI(Object widget, Renderer renderer) {} public void applyTheme(Object theme) {} }\n")

def fix_lwjglutils():
    path = os.path.join(root, 'com/bobsgame/client/LWJGLUtils.java')
    with open(path, 'r', encoding='utf-8') as f: text = f.read()
    text = text.replace('public static Object TWLrenderer = null;', 'public static de.matthiasmann.twl.renderer.Renderer TWLrenderer = null;')
    text = text.replace('public static Object TWLthemeManager = null;', 'public static Object TWLthemeManager = null;')
    with open(path, 'w', encoding='utf-8') as f: f.write(text)

def fix_pieceeditor():
    path = os.path.join(root, 'com/bobsgame/client/engine/game/gui/customGameEditor/PieceEditorPanel.java')
    with open(path, 'r', encoding='utf-8') as f: text = f.read()
    # Ensure Piece is imported
    if 'import com.bobsgame.puzzle.Piece;' not in text:
        text = text.replace('package com.bobsgame.client.engine.game.gui.customGameEditor;', 'package com.bobsgame.client.engine.game.gui.customGameEditor;\nimport com.bobsgame.puzzle.Piece;')
    with open(path, 'w', encoding='utf-8') as f: f.write(text)

fix_renderer()
fix_lwjglutils()
fix_pieceeditor()
print("Fixed Renderer and Piece issues")
