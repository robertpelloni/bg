# TODO List - Omni-Workspace

## Highest Priority: Web Port (`bobsgameweb`) Parity for Deployment

### 1. Networking (`BobNet.ts` vs Java `BobNet.java`)
- [ ] Audit `BobNet.ts` against the Java server communication protocol.
- [ ] Ensure 100% protocol parity for multiplayer and online features (Tournament bracket packets, Chat, Stats, Leaderboard, Room Lists).
- [ ] Handle GZip/Base64 JSON serialization edge cases if any remain.

### 2. Audio Engine
- [ ] Audit `bobsgameweb/src/renderer/audio/`.
- [ ] Implement or integrate Web Audio API support for tracker music formats (MOD/S3M/XM/IT) present in the original Java version (which used `micromod` and `ibxm`).

### 3. Game Logic
- [ ] Line-by-line audit of `src/shared/puzzle` in the web port against the Java `puzzle` package to ensure identical physics, RNG, and frame timing.
- [ ] Implement any missing game modes or piece types.

### 4. UI / Menus
- [ ] Ensure all settings, modes, and screens from the original game are present in the web UI.
- [ ] Implement the "TOURNAMENT RESULTS" screen and tournament room filtering.
- [ ] Implement the visual tournament bracket tree rendering (like the C++ version).

### 5. Editor Functionality
- [ ] Port the massive `EditorMain.java` functionality to the web version's `src/renderer/editor/`.
- [ ] Implement "Shift Map" features, Undo/Redo buffers, and "Random PNGs" export.

## Ongoing Maintenance
- [ ] Continuously merge AI feature branches into `main`.
- [ ] Keep `SUBMODULE_DASHBOARD.md` updated with every submodule version change.
- [ ] Resolve any conflicts intelligently without losing feature progress.
