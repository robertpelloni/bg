# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.1.10] - 2026-04-04
### Added
- **Backend Smoke-Test Endpoints:** Added plain HTTP responses for `/` and `/healthz` in the Socket.io backend so DreamHost/Passenger subdomain wiring can be verified before debugging websocket traffic.
- **DreamHost Backend Checklist:** Added `WS_BACKEND_SETUP.md` with a focused `ws.bobsgame.com` configuration and validation sequence.

### Changed
- **Deployment Guidance:** `DEPLOY.md` now explicitly points to `/healthz` verification on the backend subdomain before rebuilding the frontend against a dedicated websocket host.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.10`, including replay version metadata, achievement snapshot metadata, manifest version, package version, menu display, and config version string.

### Verified
- **Build:** `npm run build` passes in `bobsgameweb` after backend smoke-test additions.
- **Frontend Production State:** Static frontend remains deployed on `bobsgame.com` while backend-subdomain preparation continues.

## [2.1.9] - 2026-04-03
### Added
- **Passenger-Friendly Server Entrypoint:** Added `bobsgameweb/server/app.js` so the Socket.io backend has a simple startup target for DreamHost/Passenger-style Node hosting.
- **Production Env Example:** Added `.env.production.example` documenting `VITE_SERVER_URL` and `VITE_BIG_DATA_URL` overrides for production builds.

### Changed
- **Config Flexibility:** `src/shared/Config.ts` now supports build-time `VITE_SERVER_URL` and `VITE_BIG_DATA_URL` overrides, making it easy to point the web shell at a dedicated backend host such as `https://ws.bobsgame.com`.
- **Version Drift Fix:** Corrected `APP_VERSION` drift in `Config.ts` so the configuration layer no longer reported the stale `2.1.0` string.
- **Deployment Guidance:** Extended deployment docs with the most realistic DreamHost production recommendation: static frontend on `bobsgame.com`, Node/Socket.io backend on a dedicated Passenger-backed subdomain.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.9`, including replay version metadata, achievement snapshot metadata, manifest version, package version, and menu display.

### Verified
- **Build:** `npm run build` passes in `bobsgameweb` after the configuration and deployment-prep changes.
- **Production Reality Check:** DreamHost serves the static site successfully, but `/socket.io` on `bobsgame.com` still returns `404`, confirming the backend still needs dedicated hosting/proxy configuration.

## [2.1.8] - 2026-04-03
### Added
- **Windows Deployment Script:** Added `scripts/deploy.ps1` for PowerShell-based deployment workflows on Windows machines.
- **SCP Fallback Deployment:** Upgraded `scripts/deploy.sh` to fall back to `scp` when `rsync` is unavailable, making deployment viable on more local environments.
- **Env-Driven Deploy Controls:** Added support for `DEPLOY_PASSWORD`, `DEPLOY_INSTALL_SERVER`, `DEPLOY_RESTART_SERVER`, and related deploy environment variables.

### Changed
- **Deployment Documentation:** Rewrote `DEPLOY.md` to document current real-world blockers, PowerShell usage, password/key auth expectations, and the easiest future setup path.
- **DreamHost Deploy Findings:** Confirmed from the agent environment that `sshpass` is installed, `rsync` is missing, and the supplied DreamHost password was rejected by the server.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.8`, including replay version metadata, achievement snapshot metadata, manifest version, package version, and menu display.

### Verified
- **Build:** `npm run build` passes in `bobsgameweb` before deploy attempts.
- **Connectivity Attempt:** SSH connection to `pdx1-shared-a1-33.dreamhost.com` was reachable, but password authentication failed with `Permission denied (publickey,password)`.

## [2.1.7] - 2026-04-03
### Added
- **Shared Persistence Identity:** Extended the stable local profile identity model into character saves and emulator save-state persistence so those systems can begin migrating away from mutable display-name keys.
- **Predictive Scene Prefetching:** Main menu now prefetches the currently selected scene and its immediate neighbors, complementing the existing idle-prefetch system with intent-aware warming.

### Changed
- **Server Persistence Compatibility:** Character, emulator, and achievement persistence endpoints now accept structured identity payloads with backward-compatible fallback to legacy name-based lookups.
- **Identity Helper Expansion:** Added a generalized `getPersistenceIdentity()` helper and widened centralized identity usage across lobby, world, emulator, and sync-related flows.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.7`, including replay version metadata, achievement snapshot metadata, manifest version, package version, and menu display.

### Verified
- **TypeScript + Build:** `npx tsc --noEmit && npm run build` passes in `bobsgameweb`.
- **Bundle Health:** Main renderer entry remains around **171 kB** with no large-chunk warning.

## [2.1.6] - 2026-04-03
### Added
- **Stable Achievement Profile IDs:** Added a shared identity layer that now creates and persists a stable local `profileId` for achievement snapshot sync, alongside the existing player display name.
- **Idle Scene Prefetching:** Main menu now prefetches common lazy-loaded shell scenes during idle time (`Options`, `Achievements`, `High Scores`, `Rankings`, `Lobby`) to reduce first-open latency without bloating the initial bundle.
- **Settings Identity Visibility:** Settings now surfaces the local profile ID so the current identity model is visible and easier to reason about during testing and future account migration.

### Changed
- **Achievement Sync Payloads:** Snapshot save/load calls now pass a structured identity object (`profileId` + `name`) instead of raw display-name strings, while the server keeps backward-compatible fallback behavior.
- **Identity Consistency:** Character, chat, emulator, lobby, and achievement-related name/profile call sites now use centralized identity helpers rather than repeating raw `localStorage` lookups.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.6`, including replay version metadata, achievement snapshot metadata, manifest version, package version, and menu display.

### Verified
- **TypeScript + Build:** `npx tsc --noEmit && npm run build` passes in `bobsgameweb`.
- **Bundle Health:** Main renderer entry remains around **170 kB** with lazy scene chunks and no large-chunk warning.

## [2.1.5] - 2026-04-03
### Added
- **Achievement Identity Helper:** Added a shared `getAchievementProfileName()` helper so achievement snapshot save/load flows stop duplicating ad hoc `localStorage` identity lookups across scenes and editors.
- **Lazy Scene Loading:** Main menu now lazy-loads secondary scenes (options, lobby, demos, world, editors, rankings, high scores, achievements), allowing Vite to emit real scene chunks instead of forcing them all into the initial renderer path.

### Changed
- **Web Bundle Architecture:** Added explicit vendor chunking in `vite.config.ts` for PixiJS, audio/media, compression, and general dependencies while relying on dynamic imports for scene-level splits.
- **Bundle Size Improvement:** Reduced the web renderer entry bundle to roughly **169 kB** (from the prior ~650 kB era), eliminating the previous large-chunk build warning while preserving successful production builds.
- **Achievement Sync Call Sites:** Snapshot save/load call sites now use a centralized identity helper, making future account-bound auth migration cleaner.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.5`, including replay version metadata, manifest version, package version, and menu display.

### Verified
- **TypeScript + Build:** `npx tsc --noEmit && npm run build` passes in `bobsgameweb` with no large-chunk warning.

## [2.1.4] - 2026-04-03
### Added
- **Achievement Snapshot Sync Scaffolding:** Added `saveAchievementData` / `loadAchievementData` support to the Socket.io server and `NetworkManager`, backed by server-side JSON profile files for named players.
- **World Editor Progression Hooks:** Wired `WorldEditor.ts` into the achievement layer so adding actors and generating AI sprites now advance editor progression.
- **Editor Toast Feedback:** Added `ToastManager`-based feedback for custom-game saves/shares, map saves/loads, and world-database operations so editor flows no longer rely solely on blocking browser alerts.
- **New Editor Achievements:** Added new editor achievements for creating a world actor and generating an AI sprite.

### Changed
- **Achievement Manager Sync API:** Added snapshot export/merge plumbing so client-local progress can be merged with server profiles without rewriting scene logic.
- **Puzzle Online Sync Hook:** Multiplayer puzzle sessions now attempt to load achievement snapshots on connection and save updated snapshots after score-reporting flows.
- **Version Metadata:** Bumped workspace and web metadata to `2.1.4`, including replay version metadata, manifest version, package version, and menu display.

### Verified
- **TypeScript + Build:** `npx tsc --noEmit && npm run build` passes in `bobsgameweb`.

## [2.1.3] - 2026-04-03
### Added
- **Pause-Menu Achievement Access:** Added an `Achievements` action to the puzzle pause overlay so the trophy cabinet is now reachable during active play sessions instead of only from the main menu.
- **Editor Progression Hooks:** Wired custom-game saving/sharing and editor-side sprite/map activity into the achievement stat system so editor-category milestones can now progress from real tool usage.
- **Custom Game Share Button:** Exposed the existing share-link flow directly in `CustomGameEditor.ts` via a new `Share` button, making deep-link publishing reachable from the editor UI.

### Changed
- **Version Metadata:** Bumped workspace and web metadata to `2.1.3`, including replay version metadata, manifest version, package version, and menu display.
- **Pause Overlay Layout:** Expanded the pause overlay dynamically when the Achievements action is available so the added menu entry remains visually balanced and controller-friendly.
- **Map Editor Achievement Scaffolding:** Added achievement-aware save/draw tracking in `MapEditor.ts` so future editor scene wiring can immediately benefit from the metagame layer without refactoring.

### Verified
- **TypeScript + Build:** `npx tsc --noEmit && npm run build` passes in `bobsgameweb`.

## [2.1.2] - 2026-04-03
### Added
- **Achievements / Trophy Cabinet:** Added a new persistent `AchievementManager` to the web port with cross-mode stat tracking for puzzle, RPG, social, editor, and meta milestones.
- **Achievement UI Scene:** Added `AchievementsScene.ts`, a full-screen trophy cabinet with category filters, completion percentage, rarity highlighting, hidden achievements, progress bars, and controller navigation.
- **Toast Notifications:** Added `ToastManager.ts` for animated unlock toasts with slide-in presentation, rarity accents, countdown bars, and controller rumble feedback.
- **Main Menu Entry:** Added an `Achievements` option to the main menu so the metagame layer is accessible without developer tooling.

### Changed
- **Replay / Version Metadata:** Bumped workspace and web version metadata to `2.1.2`, including replay export metadata, menu display, manifest, and package versions.
- **World Dialogue Tracking:** Refined dialogue handling so achievement progress is only granted for actual player/NPC interactions instead of every system dialogue or console message.
- **Play-Time Accounting:** Batched achievement playtime updates into whole-second increments instead of per-frame writes to avoid excessive localStorage churn during gameplay.
- **Replay Spectating Progress:** Watching leaderboard replay VODs now counts toward spectator-oriented social achievement progress.

### Verified
- **TypeScript:** `npx tsc --noEmit` passes in `bobsgameweb`.
- **Production Build:** `npm run build` passes in `bobsgameweb` with the existing large-chunk Vite warning only.

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
