# ROADMAP: bob's game — The Ultimate Omni-Engine

## Current Version: 2.2.5 | Status: Active Development

---

## Phase 1: Engine Porting ✅ COMPLETE (v2.1.58 – v2.1.75)

**Goal**: Port all C++/Java engine systems to TypeScript web engine

- [x] 291 TypeScript modules across 16 subsystems
- [x] Complete puzzle game engine (OKGame, BobsGame, Grid, GameLogic, Piece, Block)
- [x] Complete RPG engine (EventManager, EventScript, GUI, Wallet, Clock, Player)
- [x] Complete ECS (47 modules — behaviors, components, systems)
- [x] Complete audio engine (AudioManager, AudioUtils, WaveData, OggDecoder)
- [x] Complete networking (Socket.io, WebRTC P2P, ServerConnection)
- [x] Complete map system (GameMap, MapManager, MapLoader, AutoTiler, AsepriteParser)
- [x] Complete entity system (Sprites, Characters, Camera, PathFinder)
- [x] Complete text system (BitmapFont, TextManager, DialogueBox, CaptionManager)
- [x] nD mini-game console (ND, Wheel, NDMenu, Ping, Ramio)
- [x] Tournament system (Stadium, TournamentManager)
- [x] State management (StateManager, GameFlowStates)
- [x] Client game engine (ClientGameEngine, BGClientEngine)
- [x] Settings & persistence (GlobalSettings, GameSave, NetworkGameSave)
- [x] Utilities (FileUtils, ManifestLoader, OKMath, OKColor, Cache, BobMenu)
- [x] Procedural audio SFX generation (AudioUtils.generateTone)

## Phase 2: Game Loop Integration ✅ COMPLETE (v2.1.79 – v2.2.5)

**Goal**: Wire up all systems into the actual running game

- [x] **Wire ClientGameEngine as the running game engine** in the main game loop
- [x] **Wire BGClientEngine render pipeline** to actually render maps, entities, and GUI
- [x] **Wire ND into the game** — pressing Enter should open the nD with the puzzle game
- [x] **Wire BobsGame menu flow** — title screen → game type selection → difficulty → play
- [x] **Wire MapManager** to load and render actual map data
- [x] **Wire EventManager** to process event scripts on map triggers
- [x] **Wire AudioManager** to play music and SFX during gameplay (v2.2.5: synced GlobalSettings → Howler AudioManager)
- [x] **Wire NetworkManager** for real multiplayer connections
- [x] **Wire TournamentManager** for bracket-style tournaments
- [x] **MapLoader** with procedural map generation (town, overworld, interiors)
- [x] **Map Server API** (GET/PUT /maps/:id, GET /maps manifest)
- [x] **Placeholder audio assets** — 11 SFX + 2 music tracks (procedurally generated WAV)
- [x] **SettingsScene** enhanced with live audio volume sliders + mute toggle

## Phase 3: Interactive Demos 🔄 IN PROGRESS

**Goal**: Create playable demo scenes for each major subsystem

- [x] Puzzle Game Demo — fully playable puzzle with BobsGame menu flow
- [x] RPG World Demo — DemoWorld with NPCs, dialogue, shops, cafes, fishing, combat, inventory, quests, day/night cycle, weather, minimap
- [x] nD Console Demo — open nD, play mini-games, browse game library
- [x] ECS Demo — EngineDemoScene with entities, behaviors, pathfinding, events, cinematics
- [ ] Tournament Demo — create/join tournament, play bracket matches
- [ ] Editor Demo — map editor, sprite editor, event sheet editor
- [x] Network Demo — connect to server, join room, play online
- [x] Battle System Demo — turn-based combat with animations, damage popups, screen shake
- [x] Shop System Demo — buy/sell items with gold in building interiors
- [x] Achievement System Demo — trophy cabinet with categories, progress bars, toast notifications

## Phase 4: Content & Polish 📋 PLANNED

**Goal**: Fill the game with content and polish the experience

- [x] Procedural map data (town, overworld, building interiors via MapLoader)
- [ ] Create actual sprite data (player characters, NPCs, enemies, items)
- [ ] Create event scripts (story events, NPC dialogue, puzzle triggers)
- [x] Create procedural music tracks and sound effects (v2.2.5)
- [ ] Implement all 9 puzzle game types in PuzzleTypes
- [x] Complete the Custom Game Editor UI (v2.1.35 — full editor with presets, templates, share, history)
- [ ] Complete the Game Sequence Editor UI
- [x] Add achievement system integration (v2.1.2)
- [x] Add replay recording and VOD playback (v2.1.0)
- [x] Add deep linking for sharing custom games and replays (v2.1.0)

## Phase 5: Native Engine Modernization 📋 PLANNED

**Goal**: Modernize C++ and Java engines

- [ ] **okgame C++**: Resolve compile/link errors, vcpkg/Conan modernization
- [ ] **okgame C++**: Port latest web features back to native (tournament, replay)
- [ ] **Java**: Complete Libretro JNI integration
- [ ] **Java**: Complete libprojectM native bindings
- [ ] **Java**: Ensure MMO server parity with Node.js backend

## Phase 6: Mobile & Launch 📋 FUTURE

**Goal**: Mobile apps and public launch

- [ ] Capacitor iOS build validation
- [ ] Capacitor Android build validation
- [ ] Performance optimization (lazy loading, code splitting)
- [ ] SEO and meta tags
- [ ] Analytics and crash reporting
- [ ] Community features (forums, chat, user profiles)
- [ ] Monetization (if applicable)

## Phase 7: Omni-Engine Integration 📋 FUTURE

**Goal**: Integrate all 2D game engines into the ultimate omni-engine

- [ ] Research and feature-parity with Defold (ECS, rollback netcode)
- [ ] Research and feature-parity with LÖVE (shader programming, raw GPU)
- [ ] Research and feature-parity with Phaser (WebWorkers, WebGPU)
- [ ] Research and feature-parity with Construct (visual scripting, event sheets)
- [ ] Research and feature-parity with GameMaker (room editor, collaborative)
- [ ] Research and feature-parity with RPG Maker (RPG database, MMO-ready)

## Phase 8: Sprite Editor Suite 📋 FUTURE

**Goal**: Integrate all sprite/tile editors as submodules and build an internal tool

- [ ] Add aseprite, LibreSprite, Pixelorama, PixiEditor as submodules for reference
- [ ] Add Tiled, Ogmo Editor, Tilemap Studio as submodules for tilemap reference
- [ ] Build internal sprite editor with: universal brushes, layers, onion skins, animation
- [ ] Build internal tilemap editor with: multi-layer, auto-tiling, collision
- [ ] Generative AI tools: sprite from description, from image, from 3D model
