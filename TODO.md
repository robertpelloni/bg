# TODO: Short-Term Tasks & Bug Fixes

## 1. Documentation & Standards
- [x] Create root `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `GPT.md`, `copilot-instructions.md`.
- [x] Create root `VISION.md`, `MEMORY.md`.
- [x] Create root `DEPLOY.md`.
- [x] Create root `SUBMODULE_DASHBOARD.md`.
- [x] Sync all sub-project LLM instruction files to reference root `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`.
- [ ] Update all `CHANGELOG.md` files with recent accomplishments.

## 2. Infrastructure & Parity
- [x] **TS Networking Parity:** Implement GZip/JSON serialization in `bobsgameweb/src/shared/puzzle/GameType.ts`.
- [x] **Steam SDK Polish:** Replace C++ SDK stubs with real Steamworks calls in `okgame/src/Utility/SteamManager.cpp`.
- [x] **Steam UI Hooks:** Uncomment and wire up Steam features in `okgame/src/Puzzle/OKGameNetwork.cpp`.
- [x] **Clean Legacy Code:** Remove legacy `SIGAR` and `JRE` references from C++ codebase.
- [x] **Lua API:** Integrate Lua 5.1 engine into `okgame` and establish `LuaManager` with basic logging bindings.

## 3. Feature Polish (From Roadmaps)
- [ ] **Java Modernization:** Continue refactoring legacy Java code in `bobsgameonlinejava`.
- [ ] **UI Upgrade:** Upgrade Java UI components using TWL (as planned in Java roadmap).
- [x] **Map Editor:** Added "Shift Map Up/Down/Left/Right" functionality with full Undo/Redo.
- [x] **Sprite Editor:** Added "Random PNGs" export button to the UI.
- [ ] **Undo System:** Improve undo functionality in Java client (prevent wrapping, skip redundant states).

## 4. Advanced Features
- [ ] **Lua Bindings:** Expose more `okgame` and `bobsgameonlinejava` internals to the Lua scripting layer.
- [ ] **Tournament Mode:** Design and implement server-side tournament logic.
- [ ] **Mobile Prototyping:** Test Capacitor deployment for the Web fork.
