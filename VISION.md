# VISION: bob's game — The Ultimate Omni-Engine

## The Dream

**bob's game** is not just a game. It is the **Omni-Engine** — a massively multiplayer game creation platform that transcends the boundaries between engine, editor, and game. The player plays games *inside* the game (on the "nD" virtual handheld console), creates games *with* the game (using built-in editors), and shares games *through* the game (via an online community hub).

The world of bob's game is a **100×100 tile MMO overworld** where every player exists simultaneously. NPCs have full AI, dialogue trees, and schedules. Buildings are enterable and contain unique interiors. The world persists. The economy persists. Friendships persist. Tournaments persist. Everything is connected.

## Core Concept: The nD (n-Dimensional Console)

Every player carries an **nD** — a virtual handheld game console visible in-game as a 3D object. The nD is a **window into every game ever created**. It contains:

- **Puzzle Mode**: The original "bob's game" — a Tetris-style puzzle game with 9 game types, 7 difficulties, multiplayer (local + online), tournaments, leaderboards, replays, and ELO ratings.
- **Mini-Games**: Ping (Pong), Ramio (Breakout), and user-created games via the Custom Game Editor.
- **Emulator Core**: Libretro-based emulation running natively in the nD screen (C++/JNI) and via WASM (web).
- **Audio Visualizer**: libprojectM music visualization running inside the nD screen.

The nD zooms in/out with **parabolic bounce easing** — a signature animation that makes opening it feel like a physical device unfolding in your hands.

## The Six Engine Superset

The Omni-Engine aims to be a **strict superset** of six major 2D game engines:

1. **Defold → ECS Architecture**: Entity-Component-System with state history, rollback netcode, and hot message passing.
2. **LÖVE → Raw Power**: Immediate-mode GPU access, shader programming, raw drawing hooks, audio graph manipulation.
3. **Phaser → Web-Native**: Multi-threaded WebWorkers, WebGPU rendering, fractionally-zoomed multi-target cameras.
4. **Construct → Visual Scripting**: Omni-Event Sheet system that compiles visual node blocks into optimized C++/TS.
5. **GameMaker → Room Editor**: Collaborative Google Docs-style map editor with infinite procedural layers.
6. **RPG Maker → RPG Database**: MMO-ready relational database for Actors, Skills, Items, Weapons, Enemies, with map event pages.

## Technical Architecture

### Three-Platform Deterministic Core

| Platform | Language | Rendering | Audio | Networking |
|---|---|---|---|---|
| **Desktop (okgame)** | C++20 | SDL3 + Vulkan/OpenGL | libopenmpt + OpenAL | TCP/UDP P2P + WebSocket |
| **Desktop (Java)** | Java 21 | LibGDX | libopenmpt + OpenAL | Netty TCP |
| **Web (bobsgameweb)** | TypeScript 5+ | PixiJS v8 (WebGPU) | Web Audio API | Socket.io + WebRTC P2P |

Every RNG tick, piece rotation, physics step, and entity behavior must produce **identical results** across all three platforms. This enables cross-platform multiplayer, deterministic replays, and AI training.

### Web Engine Stack (187 Modules, 16 Subsystems)

```
src/renderer/engine/
├── ecs/ (47)          Entity-Component-System
├── rpg/ (40)          RPG Engine (events, GUI, saves, combat)
├── puzzle/ (17)       Puzzle Game Engine (the core game)
├── nd/ (12)           nD Mini-Game Console
├── map/ (12)          Map System (tiles, areas, doors, lights)
├── entity/ (11)       Entity System (sprites, characters, camera)
├── shared/ (11)       Utilities (math, color, cache, settings)
├── network/ (7)       Networking (Socket.io + WebRTC)
├── text/ (6)          Text Rendering (bitmap fonts, typewriter)
├── cinematics/ (5)    Cinematics (overlays, letterbox, glow)
├── audio/ (5)         Audio Engine (Web Audio API)
├── stadium/ (4)       Tournament System
├── state/ (3)         State Management
├── debug/ (3)         Debug Tools
├── input/ (2)         Input System
└── eventsheet/ (1)    Visual Scripting
```

## Deployment Architecture

```
bobsgame.com (Frontend)
├── nginx on Hetzner VPS (5.161.250.43)
├── Static files at /var/www/bobsgame.com/current
├── SSL via Let's Encrypt
└── Vite + TypeScript + PixiJS v8

ws.bobsgame.com (Backend)
├── nginx reverse proxy → localhost:6065
├── Node.js + Socket.io + Express
├── systemd service: bobsgameweb-server
├── /opt/bobsgameweb/server
└── Health check: /healthz
```

## The Ultimate Goal

**Every feature works. Every menu is populated. Every button does something. The game is fun, polished, and complete.** The MMO world is alive with players. The nD contains infinite games. The editors create anything imaginable. The tournaments are competitive and fair. The community thrives.

This is not a tech demo. This is not a prototype. This is **the finished product** — continuously improved, never regressing, always moving forward.

*"Don't stop the party."*
