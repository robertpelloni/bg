# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.2.5] - 2026-04-29

### Added

- **AudioManager Wiring**: ClientGameEngine now syncs GlobalSettings audio volume (master, music, SFX) to the Howler-based AudioManager singleton at engine init time. Added `syncAudioSettings()` method for runtime sync.
- **MapLoader**: New `src/renderer/engine/map/MapLoader.ts` — complete map data pipeline with:
  - Server API loading (`GET /maps/:id`)
  - Static JSON asset loading
  - Manifest-based batch loading
  - Built-in procedural map generation (town with buildings/paths/water, 80x80 overworld, building interiors)
  - Dual JSON format support (flat tiles + layered ground/objects)
  - Server map saving (`PUT /maps/:id`)
- **Map Server API**: Added HTTP endpoints to server:
  - `GET /maps/:id` — Load map from server storage
  - `PUT /maps/:id` — Save map to server (with validation)
  - `GET /maps` — List all available maps (manifest)
- **SettingsScene Enhancement**: Complete rewrite with:
  - Master/Music/SFX volume sliders with real-time drag interaction
  - Mute toggle button
  - Test Sound button
  - Profile name editing
  - ESC key navigation
  - Hover effects on buttons
- **Placeholder Audio Assets**: Generated 11 SFX WAV files (menu_move, menu_select, pause, piece_move, piece_rotate, piece_drop, piece_lock, line_clear, tetris, level_up, game_over) and 2 music WAV files (menu, game) using procedural synthesis.
- **ClientGameEngine Map System**: Integrated MapManager + MapLoader into ClientGameEngine with automatic built-in map generation on startup + non-blocking server map loading.

### Changed

- Game.ts music asset paths updated from `.mp3` to `.wav` to match generated files.
- Version bumped to 2.2.5 across all version files.

### Verified

- `npx vite build` succeeds (291 TypeScript files, 885 modules, no errors)

## [2.2.4] - 2026-04-29

### Added

- **Network Manager integration**: Wired NetworkManager into BobsGame.ts with NETWORK_MULTIPLAYER_LOBBY state mapping.
- **Live Socket.io connections**: Clicking 'Connect to Server' creates live websocket connections to ws.bobsgame.com.
- **Room list rendering**: BobMenu UI displays server connection state and room list data from Socket.io.

## [2.1.81] - 2026-04-23

### Added

- **Puzzle Game Demo**: Fully wired up the `BobsGame` menu flow directly into playable `GameLogic` matches with PIXI rendering integration.

## [2.1.80] - 2026-04-22

### Added

- **Submodule Updates**: Fetched and merged upstream changes across submodules.
- **Documentation Updates**: Synchronized roadmap and todo files for Phase 3.

## [2.1.79] - 2026-04-22

### Added

- **Game Loop Integration**: Wired ClientGameEngine as primary engine in Game.ts.
- **ND Integration**: ND console fully wired up and displays on boot.
- **Render Pipeline**: BGClientEngine render pipeline wired into main loop.
- **Menu Flow**: BobsGame title menu flow handles inputs.
- **Managers**: MapManager, EventManager, NetworkManager, TournamentManager instantiated in ClientGameEngine.

---

_For full historical changelog, see bobsgameweb/CHANGELOG.md_
