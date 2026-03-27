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
- **Java Server Implementation:**
    - Implemented major core stubs in `GameServerTCP.java`:
        - `incomingBobsGameRoomListRequest`: Sends encoded room list to clients.
        - `incomingAddFriendByUserNameRequest`: Adds friends via DB lookup.
        - `incomingBobsGameGameStats`: Stores game results in Amazon RDS.
        - `incomingBobsGameGetHighScoresAndLeaderboardsRequest`: Queries and sends leaderboards.
        - `incomingBobsGameActivityStreamRequest`: Returns recent server activity.
        - `incomingChatMessage`: Broadcasts chat messages to all clients.
- **Lua API & Modding (C++):**
    - Integrated Lua 5.1 engine into `okgame`.
    - Created `LuaManager.h` and `LuaManager.cpp` in `okgame/src/Utility/`.
    - **Deep Bindings:** Provided extensive engine bindings (`log`, `getScore`, `getGridWidth`, `setTile`, `shakeScreen`, etc.).
    - **Frame Hook:** Integrated `LuaManager::update()` into `BobsGame::update()`, enabling per-frame Lua logic via `onUpdate()`.
    - **Modding Framework:** Created `okgame/data/scripts/init.lua` framework and comprehensive `docs/LUA_API.md`.
- **Lobby & Tournament Improvements (C++):**
    - **Lobby State Machine:** Implemented state-based views (Rooms, Stats, Leaderboard) with `CANCEL`/`Back` navigation.
    - **Tournament Mode:** Implemented specialized "TOURNAMENT RESULTS" screen in `showResultsRanking`.
- **Java Editor Improvements:**
    - **Map Editor:** Added "Shift Map Up/Down/Left/Right" functionality with full Undo/Redo (`MapShiftEdit.java`).
    - **Sprite Editor:** Added "Random PNGs" export button to the UI.
- **Legacy Cleanup:** Purged obsolete `SIGAR` and `JRE` references from the C++ codebase.

## 2. Current Status
- **Root:** Ready for 2.0.0 deployment.
- **Java Server:** Highly functional with Room, Friend, Stat, and Chat logic implemented.
- **C++ Client:** Steam, Lua, and Lobby View systems fully functional and integrated with real-time scripting.
- **Web Client:** Stable with new parity serialization logic.

## 3. Blockers & Roadblocks
- **Git Push:** Failed due to interactive authentication requirements. All changes are committed locally to `master`.
- **Submodule Sync:** Some deep-nested submodules have missing refs on origin. Recursion remains fragile.

## 4. Next Steps
1.  **Tournament Brackets:** Implement server-side automated tournament orchestration and C++ bracket UI.
2.  **Java UI Upgrade:** Continue transition to LibGDX Scene2D for all remaining legacy dialogs.
3.  **Mobile Prototyping:** Test Capacitor deployment for the Web fork.
4.  **Lua Expansion:** Add bindings for audio control and sprite manipulation.

## 5. Deployment Notes
Refer to `DEPLOY.md` for the current multi-platform strategy. Ensure Java 21 is used for the Java build.
