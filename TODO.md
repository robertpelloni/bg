# TODO: Short-Term Tasks & Bug Fixes

## 1. Documentation & Standards
- [x] Create root `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `GPT.md`, `copilot-instructions.md`.
- [x] Create root `VISION.md`, `MEMORY.md`.
- [x] Create root `DEPLOY.md`.
- [x] Create root `SUBMODULE_DASHBOARD.md`.
- [x] Sync all sub-project LLM instruction files to reference root `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`.
- [x] Update all `CHANGELOG.md` files with recent accomplishments.

## 2. Infrastructure & Parity
- [x] **TS Networking Parity:** Implement GZip/JSON serialization in `bobsgameweb/src/shared/puzzle/GameType.ts`.
- [x] **Steam SDK Polish:** Replace C++ SDK stubs with real Steamworks calls in `okgame/src/Utility/SteamManager.cpp`.
- [x] **Steam UI Hooks:** Uncomment and wire up Steam features in `okgame/src/Puzzle/OKGameNetwork.cpp`.
- [x] **Clean Legacy Code:** Remove legacy `SIGAR` and `JRE` references from C++ codebase.
- [x] **Lua API:** Integrate Lua 5.1 engine into `okgame` and establish `LuaManager` with basic logging bindings.
- [x] **Engine Bindings:** Expose `getScore`, `getLevel`, `sendGarbage`, `getTile`, `setTile`, and screen effects to Lua.
- [x] **Java Server Implementation:** Implemented major stubs in `GameServerTCP.java`.
- [x] **Tournament Orchestration:** Implemented `TournamentManager` with recursive bracket generation and protocol strings in `BobNet`.

## 3. Feature Polish (From Roadmaps)
- [x] **Lobby View System:** Implemented state-based lobby views (Rooms, Stats, Leaderboard) with CANCEL/Back navigation.
- [x] **Tournament Results:** Implemented specialized "TOURNAMENT RESULTS" screen in `showResultsRanking`.
- [x] **Tournament Brackets:** Added "Tournament Bracket" UI methods and rendering hooks in C++ client.
- [x] **Steam Friends:** Implemented "Add friends from Steam" with persona name synchronization.
- [x] **Lua Framework:** Established `data/scripts/init.lua` loading and per-frame `onUpdate` hook.
- [x] **Map Editor:** Added "Shift Map Up/Down/Left/Right" functionality with full Undo/Redo.
- [x] **Sprite Editor:** Added "Random PNGs" export button to the UI.

## 4. Advanced Features
- [x] **Bracket UI Implementation:** Finalized the C++ bracket tree rendering logic and network parsing.
- [x] **Lua Expansion:** Added bindings for audio control, sprite manipulation, and per-frame update hook.
- [x] **Java UI Upgrade:** Implemented `Scene2DStringDialog` and `Scene2DYesNoDialog` with `GUIManager` integration.
- [ ] **Java UI Modernization:** Replace remaining legacy AWT/Swing dialogs with Scene2D equivalents.
- [x] **Mobile Prototyping:** Established Capacitor foundation in the Web fork with `capacitor.config.ts` and platform dependencies.
- [ ] **Mobile Deployment:** Test actual Android/iOS builds via Capacitor.
