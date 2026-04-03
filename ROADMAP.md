# Omni-Workspace Roadmap: bob's game / OKGame

## Status: Active Development
**Current Version:** 2.1.0

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
- [ ] **Custom Game Editor UI:** Wire up `CustomGameEditor.ts` with full rule customization UI.
- [ ] **Editor Parity:** Port remaining `EditorMain.java` tile and entity placement logic to the web port.
- [ ] **Asset Pipeline:** Ensure web client can dynamically load assets from the S3 big data URL. Create a `data/` directory with placeholder assets for dev mode.
- [x] **Version Display:** Show version number prominently in the main menu UI.
- [x] **Game Over Screen Integration:** Wire GameOver flow to actually show `GameOverScene` with stats after game over.
- [x] **Options Menu:** Add `Options` menu item to main menu.
- [x] **Production Server URL:** Make the server URL configurable.
- [x] **Responsive Layout:** Implemented workspace-wide resize handling across all scenes and the virtual nD console.
- [x] **Asset Pipeline:** Hardened the `AssetLoader` to dynamically resolve paths using the central `BIG_DATA_URL` for cloud/local switching.

## 5. The Omni-Engine Expansion (RPG Engine Parity Phase)
- [x] **Defold Parity (ECS):** Created a deterministic Entity-Component-System with state history, network rollback scaffolding, and cross-language hot-reloading.
- [x] **Logic Hot-Reloading:** Implemented a `ScriptSystem` that allows swapping entity behavior at runtime via dynamic code injection.
- [x] **Phaser Parity (Rendering):** Established a robust multi-target camera system with interpolation, viewport bounds, and native screen shake.
- [x] **WebWorker Multi-Threading:** Scaffolded the `GameWorker` architecture for offloading heavy deterministic logic from the main thread.
- [x] **LÖVE Parity (Scripting):** Provide raw, immediate-mode shader (SPIR-V/GLSL) and draw hooks bound securely to Lua/TS scripts. (Initial ECS scaffolding complete).
- [x] **Construct Parity (Behaviors):** Implemented attachable "Behaviors" (Platformer, 8-Direction) as ECS components with a dedicated logic system.
- [x] **GameMaker Parity (Room Editor):** Upgraded the `MapEditor` with infinite procedural mapping, real-time concurrent multiplayer editing, and server-side JSON persistence.
- [x] **Spatial Audio:** Implemented a 3D audio engine in `AudioManager` with dynamic listener tracking for the MMORPG world.
- [x] **The nD (Virtual Console):** Implemented the dual-screen virtual handheld system natively in C++ (`okgame`), Java (`bobsgameonlinejava`), and Web (`bobsgameweb`).
- [x] **Virtual nD Puzzle Game:** Successfully instantiated the puzzle engine inside the `nD` container across all 3 platforms (`NDPuzzleGame`).
- [x] **Libretro Integration (Web):** Scaffolded the WASM-based Libretro frontend with WebWorker support and dual-screen nD core selection UI.
- [ ] **Libretro Integration (Native/Java):** Complete JNI (Java) and Native (C++) pipelines to run actual retro emulator cores securely inside the `nD`.
- [x] **ProjectM Integration (Web):** Successfully integrated `butterchurn` (Web) bindings to power immersive audio visualizations.
- [ ] **ProjectM Integration (Native/Java):** Complete JNI (Java) and `libprojectM` (C++) bindings synced to the global sound mixer.

## 6. Native C++ Port (`okgame`) Modernization (In Progress)
- [ ] **Build Recovery:** Resolve remaining compile/link errors after CMake configure succeeds.
- [ ] **Vcpkg/Conan Conversion:** Shift away from massively bundled submodules to a formal C++ package manager.
- [x] **WebSocket Lobby Parity:** Updated C++ `NetworkManager` to support `isTournament`, `state`, and `spectator` room fields, ensuring compatibility with the v2.1.1 Node.js server.
- [ ] **Lua Bindings:** Continue extending Lua deep bindings for grid, piece, and map data.

## 7. Mobile & Unified Deployment (Future)
- [ ] **Capacitor Build:** Perform final validation of iOS and Android builds from the `bobsgameweb` source.
- [ ] **bobsgame.com:** Deploy the 100% functional web port to the production domain.
- [ ] **Cross-Platform Tournament:** Conduct the first official tournament spanning Native, Web, and Java clients.
