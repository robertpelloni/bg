# Omni-Workspace Roadmap: bob's game / OKGame

## Status: Active Development
**Current Version:** 2.1.1

## 1. Documentation & Multi-Agent Alignment (COMPLETED)
- [x] Establish root `UNIVERSAL_LLM_INSTRUCTIONS.md`.
- [x] Synchronize and rewrite all sub-project agent instructions (`GEMINI.md`, `CLAUDE.md`, `GPT.md`).
- [x] Create root `VISION.md`, `MEMORY.md`, and `DEPLOY.md`.
- [x] Maintain `SUBMODULE_DASHBOARD.md` mapping 30+ components.

## 2. Java Backend & Native Polish (March 2026 - COMPLETED)
- [x] **Map Editor Shift:** Implemented "Shift Map" features with Undo/Redo support.
- [x] **Scene2D Modernization:** Implemented modern, animated dialogs (`Scene2DNumberDialog`, etc.).
- [x] **Server Orchestration:** Implemented `TournamentManager` for automated recursive bracket generation.
- [x] **Steam Integration:** Finalized C++ Steam integration for stats and persona sync.

## 3. Web Port Core Functionality (COMPLETED)
- [x] **Audio Parity:** Integrated `chiptune3` (AudioWorklet) for tracker music support (MOD/XM).
- [x] **Networking Parity:** Implemented GZip/Base64 serialization and matched all packet constants.
- [x] **Tournament UI:** Implemented visual bracket rendering and specialized results screen.
- [x] **Puzzle Parity:** Achieved 100% logic parity for Piece rotation sets, RNG, and multiplayer garbage rules.
- [x] **PixiJS v8 Migration:** Fixed all scenes to use the PixiJS v8 Graphics API (roundRect/fill/stroke).
- [x] **Networking Event Forwarding:** Fixed socket-to-EventEmitter event bridging for lobby/room events.
- [x] **Game Loop Fix:** Fixed ticker not starting due to premature `isRunning` flag.
- [x] **Leaderboard Persistence:** Server now persists and serves leaderboard scores.

## 4. Web Port Deployment Readiness (Current Phase)
- [x] **Custom Game Editor UI:** Fully wired the rule customization interface to the internal logic.
- [ ] **Editor Parity:** Port remaining `EditorMain.java` tile and entity placement logic to the web port.
- [x] **Asset Pipeline:** Hardened the `AssetLoader` with dynamic path resolution and dummy asset generation.
- [x] **Version Display:** Show version number prominently in the main menu UI.
- [x] **Game Over Screen Integration:** Wired GameOver flow to show stats and handle replay/exit logic.
- [x] **Options Menu:** Functional volume sliders and "Test Sound" system.
- [x] **Production Server URL:** Abstracted server configuration to `Config.ts`.
- [x] **Responsive Layout:** Workspace-wide resize handling across all scenes and the virtual handheld.

## 5. The Omni-Engine Expansion (RPG Engine Parity Phase)
- [x] **Defold Parity (ECS):** Created a deterministic Entity-Component-System with state history and network rollback.
- [x] **Logic Hot-Reloading:** Implemented a `ScriptSystem` that allows behavior injection at runtime.
- [x] **Phaser Parity (Rendering):** Robust multi-target camera system and WebWorker logic offloading.
- [x] **LÖVE Parity (Scripting):** Immediate-mode shader and raw drawing hooks for custom entity behavior.
- [x] **Construct Parity (Behaviors):** Attachable ECS behaviors (Platformer, 8-Direction) with visual script support.
- [x] **GameMaker Parity (Persistence):** Collaborative map editor with real-time sync and server-side JSON storage.
- [x] **RPG Maker Parity (Database):** Globally synced Relational Database for Actors, Skills, and Items.
- [x] **The nD (Virtual Console):** Functional dual-screen virtual handheld running emulators and puzzles.
- [x] **Spatial Audio:** 3D audio engine with dynamic listener tracking in the MMO world.
- [x] **Developer Console:** In-game live command line for real-time world manipulation (~ key).
- [x] **AI Asset Generation:** Prompt-based AI pipeline for generating NPC sprites and tiles.
- [x] **Cross-Platform Tournament:** Competitive matchmaking and bracket orchestration in the backend.
- [x] **Java Backend Modernization:** Scaffolded the `WebSocketGateway` in the Netty backend to support modern Socket.io events and high-performance WebSocket scaling.
- [ ] **Libretro Integration (Native/Java):** Complete JNI and Native pipelines for emulator cores.
- [ ] **ProjectM Integration (Native/Java):** Complete native bindings for audio visualizations.

## 6. Native C++ Port (`okgame`) Modernization (In Progress)
- [ ] **Build Recovery:** Resolve remaining compile/link errors.
- [ ] **Vcpkg/Conan Conversion:** Modernize the C++ dependency management system.
- [x] **WebSocket Lobby Parity:** C++ client now supports v2.1.1 spectator and tournament fields.
- [x] **ECS Parity:** Ported core ECS systems and behaviors to C++.

## 7. Mobile & Unified Deployment (Future)
- [ ] **Capacitor Build:** Perform final validation of iOS and Android builds.
- [x] **bobsgame.com:** Initial web port deployment successful.
- [ ] **Unified MMR:** Deploy the unified cross-platform player rating system.
