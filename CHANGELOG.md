# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.0.0] - 2026-03-22
### Added
- **Root Documentation:** Established `UNIVERSAL_LLM_INSTRUCTIONS.md`, `VISION.md`, `MEMORY.md`, and `DEPLOY.md`.
- **Agent Protocols:** Created root `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, and `GPT.md` to standardize multi-agent orchestration.
- **Project Structure:** Standardized `VERSION` and `ROADMAP.md` across the entire workspace.
- **Steam Integration:** Initialized Steamworks with AppID 480 and enabled stats/achievements synchronization in `okgame`.
- **Steam UI:** Re-enabled Steam-related menu items in the C++ lobby.
- **Map Editor (Java):** Implemented "Shift Map Up/Down/Left/Right" functionality with full `UndoableEdit` support and Shift+Arrow key shortcuts.
- **Sprite Editor (Java):** Added "Random PNGs" export button to the UI for batch exporting procedurally generated sprites.
- **Lua API (C++):** Integrated Lua 5.1 engine into `okgame` and established `LuaManager` with core logging bindings for modding.

### Changed
- **TypeScript Parity:** Implemented GZip/Base64 JSON serialization in `GameType.ts` to match C++ and Java logic.
- **Instruction Sync:** Updated all sub-project `LLM_INSTRUCTIONS.md` files to reference the root master instructions.
- **Build System:** Fixed Steam library linking in `okgame/CMakeLists.txt`.

### Fixed
- **Serialization Gaps:** Resolved the misnamed and unimplemented `toBase64GZippedXML` stub in the TypeScript client.
- **Legacy Cleanup:** Purged obsolete `SIGAR` and `JRE` references from the C++ codebase for full modernization.

---
*Historical milestones from sub-projects preserved in their respective CHANGELOG.md files.*
