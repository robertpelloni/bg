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
- [x] **Engine Bindings:** Expose `getScore`, `getLevel`, and `sendGarbage` to Lua scripting.

## 3. Feature Polish (From Roadmaps)
- [x] **Lobby View System:** Implemented state-based lobby views (Rooms, Stats, Leaderboard) with CANCEL/Back navigation.
- [x] **Tournament Results:** Implemented specialized "TOURNAMENT RESULTS" screen in `showResultsRanking`.
- [x] **Steam Friends:** Implemented "Add friends from Steam" with persona name synchronization.
- [ ] **Java Modernization:** Continue refactoring legacy Java code in `bobsgameonlinejava`.
- [ ] **UI Upgrade:** Upgrade Java UI components using TWL (as planned in Java roadmap).
- [x] **Map Editor:** Added "Shift Map Up/Down/Left/Right" functionality with full Undo/Redo.
- [x] **Sprite Editor:** Added "Random PNGs" export button to the UI.

## 4. Advanced Features
- [ ] **Lua Deep Bindings:** Expose `Grid`, `Piece`, and `Map` data to Lua.
- [ ] **Tournament Brackets:** Implement server-side automated tournament orchestration.
- [ ] **Mobile Prototyping:** Test Capacitor deployment for the Web fork.
