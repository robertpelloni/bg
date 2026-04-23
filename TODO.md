# TODO List — bob's game Omni-Engine

**Last Updated**: 2026-04-22 | **Version**: 2.1.79

---

## 🔴 Critical — Game Loop Integration

### Wire ClientGameEngine into the main game loop
- [x] `Game.ts` should create a `ClientGameEngine` instance
- [x] Main game loop should call `clientEngine.update(dt)` each frame
- [x] Main game loop should call `clientEngine.render()` and add result to stage
- [x] Keyboard events should be forwarded to ControlsManager
- [ ] Network events should be forwarded to NetworkManager

### Wire BobsGame menu flow
- [x] Title screen should use `BobsGame` menu system (not custom MainMenuScene)
- [ ] "Play Single Player" → difficulty select → controller select → start game
- [ ] "Play Online" → network lobby → room select → start game
- [ ] Game over → results screen → back to title

### Wire ND into gameplay
- [x] Pressing Enter in the RPG world should open the nD console
- [ ] nD should zoom in with parabolic bounce easing
- [x] nD should contain the puzzle game (BobsGame)
- [x] Closing nD should zoom out and return to RPG world

## 🟡 High Priority — System Wiring

### Map rendering
- [ ] `MapManager` should load actual map data from JSON
- [ ] `GameMap` should render tile layers using PixiJS sprites
- [ ] `Cameraman` should follow the player with smooth scrolling
- [ ] Entity rendering on top of map

### Event system
- [ ] `EventManager` should process event scripts when entering maps
- [ ] Event triggers (step on tile, interact with NPC, use item)
- [ ] Dialogue boxes should appear when NPCs talk
- [ ] Flags/skills should persist across map changes

### Audio
- [ ] Background music should play during gameplay
- [ ] SFX should play on actions (step, interact, puzzle move, line clear)
- [ ] Volume should respect GlobalSettings

### Networking
- [ ] Login flow (username/password → auth token → session)
- [ ] Room creation/joining in the lobby
- [ ] Real-time game state sync via Socket.io
- [ ] P2P connections via WebRTC for low-latency gameplay

## 🟢 Medium Priority — Polish & Features

### UI Polish
- [ ] Animated transitions between screens (fade, slide)
- [ ] Responsive layout for different screen sizes
- [ ] Gamepad navigation in all menus
- [ ] Tooltip system for menu items
- [ ] Notification system for online events

### Puzzle Features
- [ ] All 9 game types implemented (not just Marathon)
- [ ] Ghost piece rendering
- [ ] Hold piece functionality
- [ ] Combo counter display
- [ ] T-spin detection
- [ ] Back-to-back bonus

### RPG Features
- [ ] Inventory management (use/equip items)
- [ ] Turn-based battle system
- [ ] Skill leveling system
- [ ] Quest log
- [ ] Mini-map

### Editor Features
- [ ] Map editor with tile painting
- [ ] Sprite editor with pixel canvas
- [ ] Event sheet editor (visual scripting)
- [ ] Custom game type editor
- [ ] Game sequence editor

## 🔵 Low Priority — Infrastructure

### Testing
- [ ] Unit tests for puzzle logic (Grid, GameLogic, Piece rotations)
- [ ] Unit tests for event system (EventScript parsing)
- [ ] Integration tests for networking
- [ ] E2E tests for game flow

### Performance
- [ ] Lazy-load heavy subsystems
- [ ] Object pooling for frequently created/destroyed objects
- [ ] Tile map batching for rendering
- [ ] WebSocket message batching

### DevOps
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Automated deployment on push to master
- [ ] Preview deployments for PRs
- [ ] Monitoring and alerting

## 🐛 Known Bugs

1. **NDDemoScene TypeScript errors** (2 errors) — NDPuzzleGame and LibretroGame don't properly extend MiniGameEngine. Pre-existing, not blocking build.
2. **okgame C++ build failures** — Compile/link errors need resolution, vcpkg modernization
3. **Version in root VERSION.md is out of sync** (shows 2.1.15, actual is 2.1.73) — Need to sync
4. **Pre-existing LibretroGame/NDPuzzleGame** — These files exist but don't properly integrate with the new ND class

## 📝 Code Quality

- [ ] Add JSDoc comments to all public methods
- [ ] Remove unused imports across all files
- [ ] Ensure consistent error handling (try/catch with Logger)
- [ ] Review all `TODO` comments in code and resolve or create issues
- [ ] Audit barrel exports for completeness
- [ ] Add input validation to public APIs
