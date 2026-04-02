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
- [ ] Implement reconnection logic — if the socket disconnects, auto-reconnect with exponential backoff.
- [ ] Implement spectator mode support (watch matches without playing).

### 3. Audio Engine
- [x] Implement Web Audio API support for tracker music formats (MOD/S3M/XM/IT) using `chiptune3` and AudioWorklet.
- [ ] Create placeholder audio files in `data/audio/` so dev mode doesn't spam console with 404 warnings.
- [ ] Add a "Test Sound" button in Options to verify audio is working.

### 4. Game Logic
- [x] Achieved parity for `Piece` rotation sets (SRS, SEGA, NES, GB, DTET) and `DifficultyType`.
- [x] Complete deep audit and port of `GameLogic.ts` core physics, Seeded RNG, and multiplayer garbage routing.
- [ ] Implement "Sprint" mode win condition (clear 40 lines as fast as possible).
- [ ] Implement "Ultra" mode timer (3-minute time limit, maximize score).
- [ ] Score saving: persist high scores to server via `reportScore` in addition to `localforage`.

### 5. UI / Menus
- [x] Implement the visual tournament bracket tree rendering.
- [x] Implement tournament room filtering in the Lobby.
- [x] Implement the "TOURNAMENT RESULTS" screen with bracket visualization and session stats.
- [x] Fix PixiJS v8 API in LobbyScene and SettingsScene.
- [ ] Add a "Connecting..." overlay when waiting for server connection.
- [ ] Show player list in lobby room (currently only shows count).
- [ ] Add room state display (LOBBY vs PLAYING) in room list.
- [ ] Implement "Quit to Menu" button during multiplayer games.
- [ ] Add keyboard shortcut help overlay (F1 or ?).

### 6. Editor Functionality
- [x] Port core RPG data structures (`AssetData`, `MapData`, `MapStateData`, `EventData`, `DoorData`).
- [x] Implement `Palette` and `Tileset` logic for 8x8 RPG tiles.
- [x] Overhaul `MapEditor.ts` with full layer selection (17 layers) and real-time tile painting.
- [ ] Port the massive `EditorMain.java` functionality (Flood fill, Rect tool, Entity placement).
- [ ] Implement "Shift Map" features, Undo/Redo buffers, and "Random PNGs" export.
- [ ] Wire `CustomGameEditor.ts` to allow creating and saving custom game types/rules.

### 7. Visual Polish
- [ ] Add particle effects for line clears (explosion/sparkle).
- [ ] Add screen shake on hard drop and garbage receive.
- [ ] Implement smooth piece drop animation (interpolated movement).
- [ ] Add combo counter popup text (DOUBLE!, TRIPLE!, TETRIS!, etc.).
- [ ] Animate the stats panel (score counter rolling up effect).

## Ongoing Maintenance
- [x] Synchronize all submodules and merge feature branches across the monorepo.
- [x] Keep `SUBMODULE_DASHBOARD.md` updated with every submodule version change.
- [x] Resolve any conflicts intelligently without losing feature progress.
- [ ] Update `SUBMODULE_DASHBOARD.md` with current commit hashes.
- [ ] Merge any upstream changes for all forked submodules.
