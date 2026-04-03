# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.1.1] - 2026-04-02
### Added
- **Global High Scores:** The `HighScoresScene` now fetches and displays real-time global leaderboards from the WebSocket server, gracefully merging with local scores if needed.
- **Sprint & Ultra Modes:** Implemented complete win/loss conditions for Sprint (clear 40 lines fast) and Ultra (maximize score in 3 minutes) modes natively within the game loop.
- **Visual Polish:** Implemented a new particle emission system (`spawnLineClearParticles`) that generates explosive physics-based particles on line clears.
- **Screen Shake:** Added a dynamic `shake()` effect to the `PuzzleRenderer` that triggers on Hard Drops and when receiving VS Garbage from opponents.
- **Lobby Enhancements:** The multiplayer Lobby now displays the actual names of players in a room (instead of just a count), shows real-time `[LOBBY]` vs `[PLAYING]` states, and features a "Connecting..." / "Disconnected" overlay status.
- **Audio Testing:** Added a "Test Sound" button to the `OptionsScene` so players can preview SFX volume changes.
- **Help Overlay:** Added a persistent F1 Help overlay that displays all keyboard bindings during a match.

### Fixed
- **Multiplayer Disconnection:** Fixed an issue where clicking "Quit to Menu" during a multiplayer match would leave the player's socket connected to the active room, causing ghost players.

## [2.1.0] - 2026-04-02
### Fixed
- **PixiJS v8 API Migration:** Fixed `LobbyScene.ts` and `SettingsScene.ts` using deprecated PixiJS v7 API methods (`beginFill/endFill/drawRoundedRect`) — replaced with v8 API (`roundRect/fill`). These scenes would crash at runtime on PixiJS 8.x.
- **Game Ticker Not Starting:** Fixed `Game.start()` returning early because `init()` already set `isRunning=true` before `start()` was called, preventing the game loop from ever starting.
- **Scene Manager Back-Reference:** Fixed `Scene.manager` property never being assigned — `StateManager.push()` now assigns the manager back-reference to Scene instances so `this.manager.pop()` and `this.manager.push()` work correctly for navigation.
- **NetworkManager Event Forwarding:** Added missing socket event forwarding for `roomCreated`, `joinedRoom`, `gameStart`, `error`, and `connected`/`disconnected` events. Without this, the LobbyScene could never receive responses from the server for room creation or game start.
- **Settings/Lobby Navigation:** Replaced fragile `this.manager.pop()` calls with `SceneTransition.popWithFade()` for safer navigation with transition effects.

### Added
- **Server Leaderboard Persistence:** The multiplayer server now persists leaderboard scores to `leaderboards.json`, handles `reportScore` events, and serves top scores via `getLeaderboard` events. Previously scores were never stored.
- **Dynamic Tournament Brackets:** Server now generates tournament brackets dynamically based on actual connected players instead of returning hardcoded dummy data.
- **Server Input Validation:** Added input sanitization for room names, player names, chat messages, and score reports to prevent injection and overflow.

### Changed
- **Server Architecture:** Complete rewrite of `server/index.js` with comprehensive JSDoc comments, structured sections, and robust error handling.
- Version bump to 2.1.0 across all version files.

## [2.0.3] - 2026-04-01
### Added
- **Map Editor v2.0:** Overhauled the web map editor with a professional UI, full 17-layer support, and real-time tile painting using PixiJS.
- **Tileset & Palette System:** Ported the core 8x8 RPG tile and palette management logic from Java to ensure cross-platform asset parity.
- **Production Asset Pipeline:** Configured `AudioManager` to dynamically fetch assets from the S3 big data URL in production environments.
- **Multiplayer Server Hardening:** Updated the Socket.io server with robust room management, player naming, and automated game starting.
- **Deployment Infrastructure:** Created a `Dockerfile` for the multiplayer server and a comprehensive `DEPLOY.md` guide for `bobsgame.com`.

### Changed
- **Production Readiness:** Fixed several TypeScript type-safety issues and syntax errors to ensure a clean production build.
- **Server Config:** Synchronized server and client addresses for the production domain.

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

---
*Historical milestones from sub-projects preserved in their respective CHANGELOG.md files.*
