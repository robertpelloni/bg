# TODO: Short-Term Tasks & Bug Fixes

## 1. Documentation & Standards
- [x] Create root `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `GPT.md`, `copilot-instructions.md`.
- [x] Create root `VISION.md`, `MEMORY.md`.
- [x] Create root `DEPLOY.md`.
- [ ] Create root `SUBMODULE_DASHBOARD.md`.
- [x] Sync all sub-project LLM instruction files to reference root `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`.
- [ ] Update all `CHANGELOG.md` files with recent accomplishments.

## 2. Infrastructure & Parity
- [ ] **TS Networking Parity:** Implement XML and GZip serialization in `bobsgameweb/src/shared/puzzle/GameType.ts`.
- [ ] **Steam SDK Polish:** Replace C++ SDK stubs with real Steamworks calls in `okgame/src/Utility/SteamManager.cpp`.
- [ ] **Steam UI Hooks:** Uncomment and wire up Steam features in `okgame/src/Puzzle/OKGameNetwork.cpp`.
- [ ] **Clean Legacy Code:** Remove legacy `SIGAR` and `JRE` references from C++ codebase.

## 3. Feature Polish (From Roadmaps)
- [ ] **Java Modernization:** Continue refactoring legacy Java code in `bobsgameonlinejava`.
- [ ] **UI Upgrade:** Upgrade Java UI components using TWL (as planned in Java roadmap).
- [ ] **Undo System:** Improve undo functionality in Java client.
- [ ] **Random Sprite Output:** Implement random sprite generation.
- [ ] **Map Movement:** Implement "Move map up/down" functionality.

## 4. Advanced Features
- [ ] **Lua Scripting:** Enhance Lua capabilities across platforms.
- [ ] **Tournament Mode:** Design and implement server-side tournament logic.
- [ ] **Mobile Prototyping:** Test Capacitor deployment for the Web fork.
