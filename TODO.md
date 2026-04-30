# TODO List — bob's game Omni-Engine

**Last Updated**: 2026-04-29 | **Version**: 2.2.5

---

## 🔴 Critical — System Wiring

### Wire AudioManager throughout gameplay

- [x] ClientGameEngine syncs GlobalSettings audio to Howler AudioManager on init
- [x] SettingsScene has live audio sliders (master, music, SFX)
- [x] OptionsScene has live audio sliders with keyboard control
- [x] Placeholder SFX and music generated as WAV files
- [ ] Replace placeholder audio with actual game audio assets
- [ ] Music crossfading between scenes (menu → game → battle)

### Wire MapManager into rendering

- [x] MapLoader generates built-in procedural maps (town, overworld, interiors)
- [x] MapLoader loads maps from server API (GET/PUT /maps/:id)
- [x] Server has map CRUD endpoints
- [ ] DemoWorld renders MapManager tiles instead of its own procedural tiles
- [ ] GameMap renders tile layers using PixiJS sprites
- [ ] Cameraman follows player with smooth scrolling in MapManager context

### Wire BobsGame menu flow

- [x] Title screen with puzzle mode category selector
- [x] "Play Single Player" → difficulty select → controller select → start game
- [x] "Play Online" → network lobby → room select → start game
- [x] Game over → results screen → back to title

### Wire EventManager

- [x] EventManager has full flag/skill/dialogue/event system
- [ ] Event triggers fire when entering maps (OnMapEnter)
- [ ] Event triggers fire when stepping on tiles (OnTileStep)
- [ ] Event triggers fire when interacting with NPCs (OnInteract)
- [ ] Dialogue boxes appear from EventManager scripts
- [ ] Flags/skills persist across map changes via GameSave

## 🟡 High Priority — Missing Features

### Network login/auth flow

- [ ] Login screen (username + optional password → auth token → session)
- [ ] Session persistence (auto-login on return)
- [ ] Player profile API (GET/PUT /players/:id)
- [ ] Room creation with authentication
- [ ] P2P connections via WebRTC for low-latency gameplay

### Battle system

- [x] BattleScene with turn-based combat (attack, flee)
- [x] Damage popups with gravity animation
- [x] Screen shake on hit
- [x] Critical hit detection + heavy rumble
- [ ] Magic/special abilities
- [ ] Item usage in battle
- [ ] Party system (multiple party members)
- [ ] Enemy AI patterns (not just random attack)

### Puzzle features

- [x] Marathon, Sprint, Ultra modes
- [x] Seeded RNG for deterministic play
- [x] Ghost piece rendering
- [x] Hold piece functionality
- [ ] All 9 game types (Time Attack, Versus, etc.)
- [ ] Combo counter display
- [ ] T-spin detection
- [ ] Back-to-back bonus

### Map rendering

- [x] MapLoader with procedural generation
- [ ] Tile rendering using actual Tileset/Palette data
- [ ] Entity rendering on top of map layers
- [ ] Smooth camera follow with bounds clamping
- [ ] Map transition animations (fade, wipe)

## 🟢 Medium Priority — Polish & Features

### UI Polish

- [x] Animated transitions between scenes (fade via SceneTransition)
- [x] Particle effects on title screen
- [x] Toast notification system (ToastManager)
- [x] Touch controls for mobile
- [x] CRT post-processing filter
- [ ] Responsive layout for different screen sizes
- [ ] Gamepad navigation in all menus
- [ ] Tooltip system for menu items
- [ ] Notification system for online events

### RPG Features

- [x] DemoWorld with: NPCs, dialogue, shops, cafes, fishing, combat, inventory, quests
- [x] Day/night cycle (visual overlay + torch glow)
- [x] Weather system (rain, snow, storm)
- [x] Minimap with player trail
- [x] Building interiors with enter/exit
- [x] Floating damage/notification text
- [x] Buff timers (cafe drinks)
- [x] Achievement integration
- [ ] Turn-based battle system integration with WorldScene
- [ ] Skill leveling system
- [ ] Equipment system
- [ ] Quest log with real quest data

### Editor Features

- [x] Custom Game Editor with full piece/rotation/block editing
- [x] Map Editor (MapEditor.ts)
- [x] World Database Editor (WorldEditor.ts)
- [x] Template library with built-in presets
- [x] Share/import custom games via deep links
- [x] Preset save/load slots
- [ ] Sprite editor with pixel canvas
- [ ] Event sheet editor (visual scripting)
- [ ] Game sequence editor

## 🔵 Low Priority — Infrastructure

### Testing

- [ ] Unit tests for puzzle logic (Grid, GameLogic, Piece rotations)
- [ ] Unit tests for event system (EventScript parsing)
- [ ] Integration tests for networking
- [ ] E2E tests for game flow

### Performance

- [x] Lazy-load heavy subsystems (scene-level code splitting)
- [x] Vendor chunking (pixi, audio, compression)
- [x] Idle scene prefetching
- [ ] Object pooling for frequently created/destroyed objects
- [ ] Tile map batching for rendering
- [ ] WebSocket message batching

### DevOps

- [x] Deploy scripts for frontend (Hetzner) and backend (VPS)
- [x] Backend health check endpoints
- [x] Dockerfile for server
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Automated deployment on push to master
- [ ] Preview deployments for PRs
- [ ] Monitoring and alerting

## 🐛 Known Bugs

1. **NDDemoScene TypeScript errors** (2 errors) — NDPuzzleGame and LibretroGame don't properly extend MiniGameEngine. Pre-existing, not blocking build.
2. **okgame C++ build failures** — Compile/link errors need resolution, vcpkg modernization
3. **Git index.lock** — Another process continuously holds the git lock, blocking commits from this agent session.
4. **Audio 404s on first load** — Placeholder WAV files exist but Game.ts loads them before Vite serves them in dev mode. Production build is fine.

## 📝 Code Quality

- [x] AudioManager singleton pattern (Howler-based)
- [x] AudioUtils for procedural sound generation
- [x] MapLoader with clean JSON parsing
- [x] Version synced across 4 files
- [ ] Add JSDoc comments to all public methods
- [ ] Remove unused imports across all files
- [ ] Audit barrel exports for completeness
- [ ] Add input validation to public APIs
