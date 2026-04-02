# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.0.2] - 2026-04-01
### Added
- **Tournament Results Scene:** Implemented a new `TournamentResultsScene` in the web port with bracket visualization and tournament session statistics.
- **Seeded RNG:** Implemented a custom seeded random number generator in `GameLogic.ts` to ensure 100% deterministic parity with the Java/C++ versions and multiplayer synchronization.
- **Advanced Chain Logic:** Ported robust chain-checking algorithms (Horizontal, Vertical, Diagonal, Recursive) from Java to the web port.
- **Special Piece Logic:** Ported support for BOMB, WEIGHT, SUBTRACTOR, and ADDER pieces to `GameLogic.ts`.
- **VS Garbage Scaling:** Implemented difficulty-based garbage scaling and negation logic in the web port.
- **Detailed Documentation:** Massively expanded `VISION.md` into an architectural manifesto and updated `ROADMAP.md` to reflect Phase 3 progress.

### Changed
- **GameLogic Audit:** Completed a line-by-line parity audit of `GameLogic.ts` against `GameLogic.java`, fixing several subtle physics and timing discrepancies.
- **Multiplayer Routing:** Synchronized multiplayer garbage distribution rules (ALL, RANDOM, LEAST_BLOCKS) with the server-side implementation.

## [2.0.1] - 2026-04-01
### Added
- **Global Documentation Overhaul:** Initiated massive update to all root-level project documentation per new comprehensive steering instructions.
- **Submodule Dashboard:** Created `SUBMODULE_DASHBOARD.md` to track all repository components, versions, and locations.
- **LLM Instructions Alignment:** Rewrote `GEMINI.md`, `CLAUDE.md`, `GPT.md`, `AGENTS.md`, and `copilot-instructions.md` to cleanly reference `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`.
- **Audio Parity:** Integrated `chiptune3` (AudioWorklet) for tracker music support (MOD/XM) in `bobsgameweb`.
- **Editor Foundation:** Ported core RPG data structures and established `MapEditor.ts` foundation in the web port.

## [2.0.0] - 2026-03-22
### Added
- **Root Documentation:** Established `UNIVERSAL_LLM_INSTRUCTIONS.md`, `VISION.md`, `MEMORY.md`, and `DEPLOY.md`.
- **Agent Protocols:** Created root `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, and `GPT.md` to standardize multi-agent orchestration.
- **Project Structure:** Standardized `VERSION` and `ROADMAP.md` across the entire workspace.
- **Steam Integration:** Initialized Steamworks with AppID 480 and enabled stats/achievements synchronization in `okgame`.
- **Map Editor (Java):** Implemented "Shift Map Up/Down/Left/Right" functionality with full `UndoableEdit` support and Shift+Arrow key shortcuts.
- **Java Server Implementation:** Implemented major core stubs in `GameServerTCP.java`, including Room List requests, Friend Management, Game Stats storage, Leaderboard querying, Activity Stream, and global Chat broadcasting.
- **Lua API & Modding (C++):** Integrated Lua 5.1 engine into `okgame`, established `LuaManager` with deep engine bindings, per-frame `onUpdate` hook, and provided `docs/LUA_API.md` documentation.
- **Tournament Orchestration (Java):** Created `TournamentManager` on the server with recursive single-elimination bracket generation and protocol strings in `BobNet`.

---
*Historical milestones from sub-projects preserved in their respective CHANGELOG.md files.*
