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
- [ ] Line-by-line audit of `src/shared/puzzle` in the web port against the Java `puzzle` package to ensure identical physics, RNG, and frame timing.
- [ ] Implement any missing game modes or piece types.

### 4. UI / Menus
- [x] Implement the visual tournament bracket tree rendering.
- [x] Implement tournament room filtering in the Lobby.
- [ ] Ensure all settings, modes, and screens from the original game are present in the web UI.
- [ ] Implement the "TOURNAMENT RESULTS" screen.

### 5. Editor Functionality
- [x] Port core RPG data structures (`AssetData`, `MapData`, `MapStateData`, `EventData`, `DoorData`) to the web port `shared` folder.
- [x] Established `MapEditor.ts` foundation with PixiJS viewport and HTML UI panels.
- [ ] Port the massive `EditorMain.java` functionality (Tile painting, Entity placement, Layer management).
- [ ] Implement "Shift Map" features, Undo/Redo buffers, and "Random PNGs" export.

## Ongoing Maintenance
- [x] Synchronize all submodules and merge feature branches across the monorepo.
- [x] Keep `SUBMODULE_DASHBOARD.md` updated with every submodule version change.
- [x] Resolve any conflicts intelligently without losing feature progress.
