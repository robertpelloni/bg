# TODO List - Omni-Workspace

## Highest Priority: Web Port (`bobsgameweb`) Polish for Deployment

### 1. Game Flow (Critical Path)
- [x] **Wire GameOverScene:** When `GameLogic` emits `gameOver`, transition to `GameOverScene` with actual stats.
- [x] **Version Display:** Read `VERSION.md` (or embed at build time) and display the version string in the main menu.
- [x] **Options Menu Item:** Add "Options" back to the main menu items list.
- [x] **Configurable Server URL:** Extracted `http://localhost:6065` to `Config.ts`.

### 2. Networking (`BobNet.ts` / `NetworkManager.ts`)
- [x] Audit `BobNet.ts` against the Java server communication protocol.
- [x] Ensure 100% protocol parity for multiplayer and online features.
- [x] Handle GZip/Base64 JSON serialization edge cases using `pako`.
- [x] Fix socket-to-EventEmitter event forwarding for `roomCreated`, `joinedRoom`, `gameStart`, `error`.
- [x] Implement reconnection logic — if the socket disconnects, auto-reconnect with exponential backoff.
- [x] Implement spectator mode support (watch matches without playing).

### 3. Audio Engine
- [x] Implement Web Audio API support for tracker music formats (MOD/S3M/XM/IT) using `chiptune3` and AudioWorklet.
- [x] Create placeholder audio files in `data/audio/` so dev mode doesn't spam console with 404 warnings.
- [x] Add a "Test Sound" button in Options to verify audio is working.

### 4. Game Logic
- [x] Achieved parity for `Piece` rotation sets (SRS, SEGA, NES, GB, DTET) and `DifficultyType`.
- [x] Complete deep audit and port of `GameLogic.ts` core physics, Seeded RNG, and multiplayer garbage routing.
- [x] Implement "Sprint" mode win condition (clear 40 lines as fast as possible).
- [x] Implement "Ultra" mode timer (3-minute time limit, maximize score).
- [x] Score saving: persist high scores to server via `reportScore` and fetch with `getLeaderboard`.

### 5. UI / Menus
- [x] Implement the visual tournament bracket tree rendering.
- [x] Implement tournament room filtering in the Lobby.
- [x] Implement the "TOURNAMENT RESULTS" screen with bracket visualization and session stats.
- [x] Fix PixiJS v8 API in LobbyScene and SettingsScene.
- [x] Show player list in lobby room (currently only shows count).
- [x] Add room state display (LOBBY vs PLAYING) in room list.
- [x] Implement "Quit to Menu" button during multiplayer games with proper disconnect.
- [x] Add a "Connecting..." overlay when waiting for server connection.
- [x] Add keyboard shortcut help overlay (F1 or ?).
- [x] Full Gamepad/Controller Support (UI Navigation and Haptic Feedback/Rumble).
- [x] Add a persistent Achievement/Trophy system with an Achievements menu and unlock pop-up notifications.
- [x] Wire editor activity and pause-menu access into the achievement metagame layer.

### 6. Editor Functionality
- [x] Port core RPG data structures (`AssetData`, `MapData`, `MapStateData`, `EventData`, `DoorData`).
- [x] Implement `Palette` and `Tileset` logic for 8x8 RPG tiles.
- [x] Overhaul `MapEditor.ts` with full layer selection (17 layers) and real-time tile painting.
- [x] Port the massive `EditorMain.java` functionality (Flood fill, Rect tool, Entity placement).
- [x] Implement "Shift Map" features, Undo/Redo buffers, and "Random PNGs" export.
- [x] Wire `CustomGameEditor.ts` to allow creating and saving custom game types/rules.

### 7. Visual Polish & Extras
- [x] Add particle effects for line clears (explosion/sparkle).
- [x] Add screen shake on hard drop and garbage receive.
- [x] Implement smooth piece drop animation (interpolated movement).
- [x] Add combo counter popup text (DOUBLE!, TRIPLE!, TETRIS!, etc.).
- [x] Animate the stats panel (score counter rolling up effect).
- [x] Implement Base64 compressed Deep Links for Custom Games and Replays (Shareable Links).
- [x] Advanced RPG Combat: Floating damage numbers, screen shake, hit flashes.

## Ongoing Maintenance
- [x] Synchronize all submodules and merge feature branches across the monorepo.
- [x] Keep `SUBMODULE_DASHBOARD.md` updated with every submodule version change.
- [x] Resolve any conflicts intelligently without losing feature progress.
- [x] Update `SUBMODULE_DASHBOARD.md` with current commit hashes.
- [x] Merge any upstream changes for all forked submodules.
