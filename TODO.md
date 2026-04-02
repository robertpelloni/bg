# TODO List - Omni-Workspace

## Highest Priority: Web Port (`bobsgameweb`) Parity for Deployment

### 1. Networking (`BobNet.ts` vs Java `BobNet.java`)
- [x] Audit `BobNet.ts` against the Java server communication protocol.
- [x] Ensure 100% protocol parity for multiplayer and online features (Tournament bracket packets, Chat, Stats, Leaderboard, Room Lists).
- [x] Handle GZip/Base64 JSON serialization edge cases using `pako`.

### 2. Audio Engine
- [x] Audit `bobsgameweb/src/renderer/audio/`.
- [x] Implement Web Audio API support for tracker music formats (MOD/S3M/XM/IT) using `chiptune3` and AudioWorklet.

### 3. Game Logic
- [x] Achieved parity for `Piece` rotation sets (SRS, SEGA, NES, GB, DTET) and `DifficultyType`.
- [x] Complete deep audit and port of `GameLogic.ts` core physics, Seeded RNG, and multiplayer garbage routing for 100% parity.

### 4. UI / Menus
- [x] Implement the visual tournament bracket tree rendering.
- [x] Implement tournament room filtering in the Lobby.
- [x] Implement the "TOURNAMENT RESULTS" screen with bracket visualization and session stats.
- [ ] Ensure all settings, modes, and screens from the original game are present in the web UI.

### 5. Editor Functionality
- [x] Port core RPG data structures (`AssetData`, `MapData`, `MapStateData`, `EventData`, `DoorData`).
- [x] Implement `Palette` and `Tileset` logic for 8x8 RPG tiles.
- [x] Overhaul `MapEditor.ts` with full layer selection (17 layers) and real-time tile painting.
- [ ] Port the massive `EditorMain.java` functionality (Flood fill, Rect tool, Entity placement).
- [ ] Implement "Shift Map" features, Undo/Redo buffers, and "Random PNGs" export.

## Ongoing Maintenance
- [x] Synchronize all submodules and merge feature branches across the monorepo.
- [x] Keep `SUBMODULE_DASHBOARD.md` updated with every submodule version change.
- [x] Resolve any conflicts intelligently without losing feature progress.
