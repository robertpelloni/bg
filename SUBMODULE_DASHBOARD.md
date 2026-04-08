# Submodule Dashboard

**Last Updated**: 2026-04-08 | **Workspace Version**: 2.1.73

## Project Directory Structure

```
bg/                              (Root workspace — git monorepo)
├── AGENTS.md                    Multi-agent orchestration instructions
├── CLAUDE.md                    Claude-specific instructions
├── GEMINI.md                    Gemini-specific instructions
├── GPT.md                       GPT-specific instructions
├── copilot-instructions.md      GitHub Copilot instructions
├── VISION.md                    Project vision and goals
├── MEMORY.md                    Ongoing observations and patterns
├── DEPLOY.md                    Deployment instructions
├── ROADMAP.md                   Long-term feature roadmap
├── TODO.md                      Short-term task list
├── VERSION.md                   Single source of truth for version (2.1.73)
├── CHANGELOG.md                 Version history
├── HANDOFF.md                   Inter-model session handoff notes
├── SUBMODULE_DASHBOARD.md       This file
│
├── bobsgameweb/                 Web port (Vite + TypeScript + PixiJS v8)
│   ├── src/renderer/engine/     187 TypeScript modules, 16 subsystems
│   ├── server/                  Node.js Socket.io backend
│   ├── scripts/                 Deploy scripts
│   ├── dist/                    Build output
│   ├── VERSION.md               2.1.73
│   ├── package.json             Dependencies and scripts
│   └── vite.config.ts           Vite configuration
│
├── okgame/                      C++ native engine (SDL3 + C++20)
│   ├── src/Engine/              Core engine (ECS, RPG, entity, map, etc.)
│   ├── src/Puzzle/              Puzzle game engine
│   ├── src/Utility/             Utilities (math, color, controls, etc.)
│   └── build/                   CMake build output
│
├── bobsgameonlinejava/          Java engine (LibGDX + Java 21)
│   ├── src/main/java/com/bobsgame/  Java source
│   ├── libs/                    Native libraries
│   └── references/              Editor references (Aseprite, Tiled, etc.)
│
├── docs/                        Workspace-level documentation
│   ├── UNIVERSAL_LLM_INSTRUCTIONS.md
│   ├── ARCHITECTURE_MANIFESTO.md
│   ├── FINAL_PROJECT_SUMMARY.md
│   └── ai/                      AI phase documentation
│
├── scripts/                     Automation scripts
├── data/                        Shared data files
├── logs/                        Operation logs
└── steamworks_sdk_164/          Steam SDK (C++ integration)
```

## Submodule Status

| Submodule | Repository | Branch | Version | Status |
|---|---|---|---|---|
| **bobsgameweb** | robertpelloni/bobsgameweb | master | 2.1.73 | ✅ Deployed live at bobsgame.com + ws.bobsgame.com |
| **okgame** | robertpelloni/okgame | main | - | ⚠️ Build needs modernization |
| **bobsgameonlinejava** | robertpelloni/bobsgameonlinejava | main | - | ✅ Reference source for porting |

## Web Engine Subsystem Breakdown (bobsgameweb)

| Subsystem | Modules | Key Components |
|---|---|---|
| ecs | 47 | Entity, World, behaviors, components, systems |
| rpg | 40 | ClientGameEngine, BGClientEngine, events, GUI, saves |
| puzzle | 17 | OKGame, BobsGame, Grid, GameLogic, Piece, Block |
| nd | 12 | ND, Wheel, NDMenu, WheelItem, MiniGameEngine, Ping, Ramio |
| map | 12 | GameMap, MapManager, AutoTiler, AsepriteParser, MapStateData |
| entity | 11 | BobSprite, Character, Cameraman, PathFinder, Sprite |
| shared | 11 | GlobalSettings, FileUtils, Cache, BobMenu, OKMath, OKColor |
| network | 7 | NetworkManager, OKNet, ServerConnection, PeerConnection, BobsGameRoom |
| text | 6 | TextManager, BitmapFont, DialogueBox, CaptionManager |
| cinematics | 5 | CinematicsManager, ScreenOverlay, Letterbox, GlowTileBackground |
| audio | 5 | AudioManager, AudioUtils, WaveData, OggDecoder |
| stadium | 4 | OKGameStadium, TournamentManager |
| state | 3 | StateManager, GameFlowStates |
| debug | 3 | DebugConsole, Logger |
| input | 2 | ControlsManager |
| eventsheet | 1 | EventSheet |

## Live Endpoints

| Endpoint | URL | Purpose |
|---|---|---|
| Frontend | https://bobsgame.com | Static web app (PixiJS v8) |
| Backend | https://ws.bobsgame.com | Socket.io server |
| Health | https://ws.bobsgame.com/healthz | Service health check |
| Socket.io | wss://ws.bobsgame.com/socket.io | WebSocket game connection |
| GitHub | https://github.com/robertpelloni/bobsgameweb | Source repository |
