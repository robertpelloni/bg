# TODO List — bob's game Omni-Engine

**Last Updated**: 2026-04-29 | **Version**: 2.2.7

---

## 🔴 Critical — System Wiring

### Wire AudioManager throughout gameplay

- [x] ClientGameEngine syncs GlobalSettings audio to Howler AudioManager on init
- [x] SettingsScene has live audio sliders (master, music, SFX)
- [x] OptionsScene has live audio sliders with keyboard control
- [x] Placeholder SFX and music generated as WAV files
- [ ] Replace placeholder audio with actual game audio assets
- [x] Music crossfading between scenes (AudioManager.crossfadeMusic)

### Wire MapManager into rendering

- [x] MapLoader generates built-in procedural maps (town, overworld, interiors)
- [x] MapLoader loads maps from server API (GET/PUT /maps/:id)
- [x] Server has map CRUD endpoints
- [ ] DemoWorld renders MapManager tiles instead of its own procedural tiles
- [x] DemoWorld.loadFromMapData() bridges MapLoader tiles → DemoWorld Tile colors
- [x] ClientGameEngine loads town map into DemoWorld on init
- [ ] GameMap renders tile layers using PixiJS sprites
- [ ] Cameraman follows player with smooth scrolling in MapManager context

### Wire BobsGame menu flow

- [x] Title screen with puzzle mode category selector
- [x] "Play Single Player" → difficulty select → controller select → start game
- [x] "Play Online" → network lobby → room select → start game
- [x] Game over → results screen → back to title

### Wire EventManager

- [x] EventManager has full flag/skill/dialogue/event system
- [x] DefaultEvents registered on init (tutorial, NPC talk, area enter, bridge, explorer achievement)
- [x] Event triggers fire when entering maps (OnMapEnter)
- [x] Event triggers fire when stepping on tiles (OnTileStep)
- [x] Event triggers fire when interacting with NPCs (OnInteract)
- [x] Dialogue boxes appear from EventManager scripts
- [x] Flags/skills persist across map changes via GameSave

## 🟡 High Priority — Missing Features

### Network login/auth flow

- [ ] Login screen (username + optional password → auth token → session)
- [x] Session persistence (auto-login on return)
- [x] Player profile API (GET/PUT /players/:id)
- [ ] Room creation with authentication
- [ ] P2P connections via WebRTC for low-latency gameplay

### Battle system

- [x] BattleScene with turn-based combat (attack, flee)
- [x] Damage popups with gravity animation
- [x] Screen shake on hit
- [x] Critical hit detection + heavy rumble
- [x] Magic/special abilities (Fire/Ice/Lightning spells)
- [x] Item usage in battle (healing herbs)
- [ ] Party system (multiple party members)
- [x] Enemy AI patterns (normal/special/defend/desperate)

### Puzzle features

- [x] Marathon, Sprint, Ultra modes
- [x] Seeded RNG for deterministic play
- [x] Ghost piece rendering
- [x] Hold piece functionality
- [ ] All 9 game types (Time Attack, Versus, etc.)
- [ ] Combo counter display
- [x] T-spin detection (SRS 3-corner rule)
- [x] Back-to-back bonus

### Map rendering

- [x] MapLoader with procedural generation
- [x] Tile rendering using actual Tileset/Palette data (DefaultRPGTileset + TileRenderer)
- [ ] Entity rendering on top of map layers
- [x] Smooth camera follow with bounds clamping (lerp-based in DemoWorld)
- [x] Map transition animations (fade, iris, blinds, slide, door)

## 🟢 Medium Priority — Polish & Features

### UI Polish

- [x] Animated transitions between scenes (fade via SceneTransition)
- [x] Particle effects on title screen
- [x] Toast notification system (ToastManager)
- [x] Touch controls for mobile
- [x] CRT post-processing filter
- [x] Responsive layout for different screen sizes
- [ ] Gamepad navigation in all menus
- [x] Tooltip system for menu items
- [x] Notification system for online events

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
- [x] Skill leveling system (STR/VIT/AGI/LUK + auto-allocate)
- [x] Equipment system (Weapon/Armor/Accessory slots with bonuses)
- [x] Quest log with real quest data (7 quests with progress tracking)

### Editor Features

- [x] Custom Game Editor with full piece/rotation/block editing
- [x] Map Editor (MapEditor.ts)
- [x] World Database Editor (WorldEditor.ts)
- [x] Template library with built-in presets
- [x] Share/import custom games via deep links
- [x] Preset save/load slots
- [x] Sprite editor with pixel canvas (16x16, 32 colors, tools, export)
- [ ] Event sheet editor (visual scripting)
- [x] Game sequence editor

## 🔵 Low Priority — Infrastructure

### Testing

- [x] Unit tests for puzzle logic (60 tests: T-spin, B2B, scoring, level-up, combo, SRS kicks)
- [x] Unit tests for event system (42 tests passing)
- [ ] Integration tests for networking
- [ ] E2E tests for game flow

### Performance

- [x] Lazy-load heavy subsystems (scene-level code splitting)
- [x] Vendor chunking (pixi, audio, compression)
- [x] Idle scene prefetching
- [x] Object pooling (ObjectPool<T> generic class)
- [x] Tile map batching (TileBatcher class, color-grouped rendering)
- [x] WebSocket message batching (MessageBatcher class + server handler)

### DevOps

- [x] Deploy scripts for frontend (Hetzner) and backend (VPS)
- [x] Backend health check endpoints
- [x] Dockerfile for server
- [x] CI/CD pipeline (GitHub Actions — deploy.yml + quality.yml)
- [ ] Automated deployment on push to master
- [ ] Preview deployments for PRs
- [x] Monitoring and alerting (/stats endpoint with memory/connections/rooms)

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
