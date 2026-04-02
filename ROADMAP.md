# Omni-Workspace Roadmap: bob's game / OKGame

## Status: Active Development
**Current Version:** 2.0.1

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

## 3. Web Port Deployment Readiness (Current Phase)
- [x] **Audio Parity:** Integrated `chiptune3` (AudioWorklet) for tracker music support (MOD/XM).
- [x] **Networking Parity:** Implemented GZip/Base64 serialization and matched all packet constants.
- [x] **Tournament UI:** Implemented visual bracket rendering and specialized results screen.
- [x] **Puzzle Parity:** Achieved 100% logic parity for Piece rotation sets, RNG, and multiplayer garbage rules.
- [ ] **Editor Parity:** Port remaining `EditorMain.java` tile and entity placement logic to the web port.
- [ ] **Asset Pipeline:** Ensure web client can dynamically load assets from the S3 big data URL.

## 4. Mobile & Unified Deployment (Future)
- [ ] **Capacitor Build:** Perform final validation of iOS and Android builds from the `bobsgameweb` source.
- [ ] **bobsgame.com:** Deploy the 100% functional web port to the production domain.
- [ ] **Cross-Platform Tournament:** Conduct the first official tournament spanning Native, Web, and Java clients.
