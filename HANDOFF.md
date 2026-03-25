# HANDOFF: bob's game / OKGame (Omni-Workspace) - March 22, 2026

## 1. Summary of Changes
- **Root Documentation:** Established a unified documentation framework (`UNIVERSAL_LLM_INSTRUCTIONS.md`, `VISION.md`, `MEMORY.md`, `DEPLOY.md`, `ROADMAP.md`, `TODO.md`, `SUBMODULE_DASHBOARD.md`, `LUA_API.md`).
- **Agent Protocols:** Created model-specific instructions (`GEMINI.md`, `CLAUDE.md`, `GPT.md`, `copilot-instructions.md`) that all reference the master instructions.
- **Version Sync:** Synchronized all project versions to **2.0.0**.
- **TS Serialization:** Implemented `toBase64GZippedJSON` and `fromBase64GZippedJSON` in `bobsgameweb/src/shared/puzzle/GameType.ts` using native `CompressionStream` APIs to match C++/Java logic.
- **Steam Integration:**
    - Initialized Steamworks with AppID 480 in `okgame/src/Utility/SteamManager.cpp`.
    - Fixed Steam library linking in `okgame/CMakeLists.txt`.
    - Created `okgame/steam_appid.txt` for local development.
    - Re-enabled Steam-related menu items in `okgame/src/Puzzle/OKGameNetwork.cpp`.
    - **Steam Friends:** Implemented `SteamManager::getFriends()` and integrated "Add friends from Steam" into the lobby with persona name synchronization.
- **Lua API & Modding (C++):**
    - Integrated Lua 5.1 engine into `okgame` by adding sources from `CLove` submodule to `CMakeLists.txt`.
    - Created `LuaManager.h` and `LuaManager.cpp` in `okgame/src/Utility/`.
    - **Deep Bindings:** Provided extensive engine bindings for Lua scripts:
        - `log(msg)`, `logError(msg)`
        - `getScore()`, `getLevel()`
        - `sendGarbage(amt)`, `receiveGarbage(amt)`
        - `getGridWidth()`, `getGridHeight()`
        - `getTile(x, y)`, `setTile(x, y, typeName)`
        - `shakeScreen()`, `wiggleScreen()`
        - `getPieceInfo()` (returns table with x, y, rotation, type)
    - **Modding Framework:** Created `okgame/data/scripts/init.lua` framework and comprehensive `docs/LUA_API.md` documentation.
    - **Frame Hook:** Integrated `LuaManager::update()` into `BobsGame::update()`, enabling per-frame Lua logic via the global `onUpdate()` Lua function.
    - **Advanced Sample:** Provided a sample `init.lua` demonstrating real-time score monitoring and dynamic screen effects.
- **Lobby & Tournament Improvements (C++):**
    - **Lobby State Machine:** Implemented state-based views (Rooms, Stats, Leaderboard) with `CANCEL`/`Back` navigation and dynamic menu repopulation.
    - **Tournament Mode:** Implemented specialized "TOURNAMENT RESULTS" screen in `showResultsRanking` and enabled tournament room filtering in the lobby.
- **Java Editor Improvements:**
    - **Map Editor:** Added "Shift Map Up/Down/Left/Right" functionality with full Undo/Redo (`MapShiftEdit.java`) and Shift+Arrow key shortcuts in `EditorMain.java`.
    - **Sprite Editor:** Added "Random PNGs" export button to the UI in `SpriteEditor.java` to trigger batch PNG output of procedural sprites.
- **Legacy Cleanup:** Purged obsolete `SIGAR` and `JRE` references from the C++ codebase (`System.h`, `System.cpp`, and entire `src/` directory).

## 2. Current Status
- **Root:** Ready for 2.0.0 deployment.
- **Java Client:** Modernized UI and enhanced editor tools. Logic modernization ongoing.
- **C++ Client:** Steam, Lua, and Lobby View systems fully functional and integrated with real-time scripting capabilities.
- **Web Client:** Stable with new parity serialization logic.

## 3. Blockers & Roadblocks
- **Git Push:** Failed due to interactive authentication requirements. All changes are committed locally to `master` (root) and respective submodule branches.
- **Submodule Sync:** Some deep-nested submodules (e.g., `lib/brotli`) have missing refs on origin. Manual cleanup was performed but recursion remains fragile.

## 4. Next Steps
1.  **Tournament Brackets:** Focus on server-side automated tournament orchestration and C++ bracket UI.
2.  **Java UI Upgrade:** Continue transition to LibGDX Scene2D for all remaining legacy dialogs.
3.  **Mobile Prototyping:** Test Capacitor deployment for the Web fork.
4.  **Lua Expansion:** Add bindings for audio control and sprite manipulation.

## 5. Deployment Notes
Refer to `DEPLOY.md` for the current multi-platform strategy. Ensure Java 21 is used for the Java build.
