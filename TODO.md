# TODO List — bob's game Omni-Engine

**Last Updated**: 2026-11-13 | **Version**: 2.1.100

---

## 🔴 Open — found 2026-11-13 (dashboard / tray / runtime audit)

- [x] **BattleScene dashboard entry**: added "Demo Battle" (Play category) with fabricated player/enemy CombatComponents in the same field shape WorldScene passes for NPC battles — every scene is now reachable from the single dashboard page. Deployed to Hetzner prod 2026-11-13 (verified in the served bundle).
- [ ] **Local WS server cannot start**: `bobsgameweb/server/node_modules` was never installed; `npm install` fails here with `ERR_SSL_TLSV1_ALERT_PROTOCOL_VERSION` from registry.npmjs.org. Run `cd bobsgameweb/server; npm install` on an unrestricted network, then `node server/index.js` (port 6065).
- [ ] **Electron tray not yet run locally**: the Electron binary download hits the same npm TLS block. After a successful root `npm install`, run `npm run dev:electron` and verify the tray menu (Show/Hide, AI proxy 8080, Game Server 6065, Restart All, Quit Servers & Exit).
- [ ] **Test suite cannot run**: 34 files in `bobsgameweb/src/__tests__/` but no runner installed and no `test` script in `package.json`. Add vitest + a `test` script and wire it into the build.
- [x] **Production behind local**: ~~`ws.bobsgame.com/healthz` reported 3.0.10 vs local 3.0.34~~ — deployed to Hetzner 2026-11-13 (frontend + backend, remote backups `*_backup_20261113` kept on the VPS); `/healthz` now reports 3.0.34 and the served bundle contains the new dashboard entries.
- [ ] **okgame (C++) not present locally**: registered in `.gitmodules` but not cloned in this workspace; C++ build status unverified here.
- [x] **Duplicate settings surfaces**: consolidated 2026-11-14 — the dashboard now has a single "Settings & Options" entry (SettingsScene: audio + profile); the overlapping OptionsScene graphics/haptics controls are reached via its "Graphics & Haptics →" button, and Back returns. Verified live (System tab shows one settings entry; Settings page renders both sections + the link button).
- [x] **Shop crashed from every entry point** (found in live verification 2026-11-13): `ShopScene.shopConfig` was never assigned; fixed in the constructor + regression test `src/__tests__/shop-config.test.ts` (needs `tsx` to execute). Verified live: General Store renders from the dashboard.
- [x] **Player DEFEND missing in battle**: added (halves next hit, uses the previously dead `playerDefending` flag), verified live ("Blocked! Enemy deals only 1 damage!").
- [x] **Demo-battle defeat unreachable**: enemy retuned 2026-11-14 (HP 90, ATK 17 → ~11/hit unblocked, 5 blocked). Verified live: defend-spam run reached HP 0/100 and auto-exited to the dashboard; winning now needs magic, heals, or crits.
- [x] **World pause menu keyboard + Quit to Menu** (fixed and live-verified 2026-11-13): pause menu now has arrow+Enter navigation shared with the mouse handler; Enter is read before the consuming input pass; `Scene.onExit` removes the container before `destroy()`; `Camera.updateContainer` skips destroyed containers (the actual black-screen root cause). Verified on prod: Esc → ▼▼▼ → Enter → dashboard, zero page errors. Note: CDP-synthesized mouse clicks still never fired Pixi handlers in headless testing — real-mouse behavior of the pause buttons is inferred from the shared `activatePauseOption` handler, not independently confirmed.

---

## 🔴 Critical — Game Loop Integration

### Wire ClientGameEngine into the main game loop
- [x] `Game.ts` should create a `ClientGameEngine` instance
- [x] Main game loop should call `clientEngine.update(dt)` each frame
- [x] Main game loop should call `clientEngine.render()` and add result to stage
- [x] Keyboard events should be forwarded to ControlsManager
- [x] Network events should be forwarded to NetworkManager

### Wire BobsGame menu flow
- [x] Title screen should use `BobsGame` menu system (not custom MainMenuScene)
- [x] "Play Single Player" → difficulty select → controller select → start game
- [x] "Play Online" → network lobby → room select → start game
- [x] Game over → results screen → back to title

### Wire ND into gameplay
- [x] Pressing Enter in the RPG world should open the nD console
- [x] nD should zoom in with parabolic bounce easing
- [x] nD should contain the puzzle game (BobsGame)
- [x] Closing nD should zoom out and return to RPG world

## 🟡 High Priority — System Wiring

### Map rendering
- [x] `MapManager` should load actual map data from JSON
- [x] `GameMap` should render tile layers using PixiJS sprites
- [x] `Cameraman` should follow the player with smooth scrolling
- [x] Entity rendering on top of map

### Event system
- [x] `EventManager` should process event scripts when entering maps
- [x] Event triggers (step on tile, interact with NPC, use item)
- [x] Dialogue boxes should appear when NPCs talk
- [x] Flags/skills should persist across map changes

### Audio
- [x] Background music should play during gameplay
- [x] SFX should play on actions (step, interact, puzzle move, line clear)
- [x] Volume should respect GlobalSettings

### Networking
- [x] Login flow (username/password → auth token → session)
- [x] Room creation/joining in the lobby
- [x] Real-time game state sync via Socket.io
- [x] P2P connections via WebRTC for low-latency gameplay

## 🟢 Medium Priority — Polish & Features

### UI Polish
- [x] Animated transitions between screens (fade, slide)
- [x] Responsive layout for different screen sizes
- [x] Gamepad navigation in all menus
- [x] Tooltip system for menu items
- [x] Notification system for online events

### Puzzle Features
- [x] All 9 game types implemented (not just Marathon)
- [x] Ghost piece rendering
- [x] Hold piece functionality
- [x] Combo counter display
- [x] T-spin detection
- [x] Back-to-back bonus

### RPG Features
- [x] Inventory management (use/equip items)
- [x] Turn-based battle system
- [x] Skill leveling system
- [x] Quest log
- [x] Mini-map

### Editor Features
- [x] Map editor with tile painting
- [x] Sprite editor with pixel canvas
- [x] Event sheet editor (visual scripting)
- [x] Custom game type editor
- [x] Game sequence editor

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

1. ~~**NDDemoScene TypeScript errors** (2 errors) — NDPuzzleGame and LibretroGame don't properly extend MiniGameEngine. Pre-existing, not blocking build.~~ (Fixed in v2.1.86/v2.1.89 via TournamentDemoWrapper abstract sync)
2. **okgame C++ build failures** — Compile/link errors need resolution, vcpkg modernization
3. ~~**Version in root VERSION.md is out of sync** (shows 2.1.15, actual is 2.1.73) — Need to sync~~ (Fixed in v2.1.75+ version patch scripts)
4. ~~**Pre-existing LibretroGame/NDPuzzleGame** — These files exist but don't properly integrate with the new ND class~~ (No longer blocking; replaced by proper TS structure in v2.1.86+)

## 📝 Code Quality

- [x] Add JSDoc comments to all public methods
- [x] Remove unused imports across all files
- [x] Ensure consistent error handling (try/catch with Logger)
- [x] Review all `TODO` comments in code and resolve or create issues
- [x] Audit barrel exports for completeness
- [x] Add input validation to public APIs
