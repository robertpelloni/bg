# ROADMAP: bob's game — The Ultimate Omni-Engine

## Current Version: 2.1.100 | Status: Active Development

---

## Phase 1: Engine Porting ✅ COMPLETE (v2.1.100 – v2.1.100)
**Goal**: Port all C++/Java engine systems to TypeScript web engine

- [x] 187 TypeScript modules across 16 subsystems
- [x] Complete puzzle game engine (OKGame, BobsGame, Grid, GameLogic, Piece, Block)
- [x] Complete RPG engine (EventManager, EventScript, GUI, Wallet, Clock, Player)
- [x] Complete ECS (47 modules — behaviors, components, systems)
- [x] Complete audio engine (AudioManager, AudioUtils, WaveData, OggDecoder)
- [x] Complete networking (Socket.io, WebRTC P2P, ServerConnection)
- [x] Complete map system (GameMap, MapManager, AutoTiler, AsepriteParser)
- [x] Complete entity system (Sprites, Characters, Camera, PathFinder)
- [x] Complete text system (BitmapFont, TextManager, DialogueBox, CaptionManager)
- [x] nD mini-game console (ND, Wheel, NDMenu, Ping, Ramio)
- [x] Tournament system (Stadium, TournamentManager)
- [x] State management (StateManager, GameFlowStates)
- [x] Client game engine (ClientGameEngine, BGClientEngine)
- [x] Settings & persistence (GlobalSettings, GameSave, NetworkGameSave)
- [x] Utilities (FileUtils, ManifestLoader, OKMath, OKColor, Cache, BobMenu)

## Phase 2: Game Loop Integration 🔄 IN PROGRESS
**Goal**: Wire up all systems into the actual running game

- [x] **Wire ClientGameEngine as the running game engine** in the main game loop
  - The Game.ts main loop should instantiate and run ClientGameEngine
  - All subsystems (Player, GUI, Clock, Friends, Map, Events) should update each frame
- [x] **Wire BGClientEngine render pipeline** to actually render maps, entities, and GUI
- [x] **Wire ND into the game** — pressing Enter should open the nD with the puzzle game
- [x] **Wire BobsGame menu flow** — title screen → game type selection → difficulty → play
- [x] **Wire MapManager** to load and render actual map data
- [x] **Wire EventManager** to process event scripts on map triggers
- [x] **Wire AudioManager** to play music and SFX during gameplay
- [x] **Wire NetworkManager** for real multiplayer connections
- [x] **Wire TournamentManager** for bracket-style tournaments

## Phase 3: Interactive Demos 📋 PLANNED
**Goal**: Create playable demo scenes for each major subsystem

- [x] Puzzle Game Demo — fully playable puzzle with BobsGame menu flow
- [x] RPG World Demo — walkable map with NPCs, dialogue, items
- [x] nD Console Demo — open nD, play mini-games, browse game library
- [ ] Tournament Demo — create/join tournament, play bracket matches
- [x] ECS Demo — spawn entities with behaviors, watch them interact
- [x] Editor Demo — map editor, sprite editor, event sheet editor
- [x] Network Demo — connect to server, join room, play online

## Phase 4: Content & Polish 📋 PLANNED
**Goal**: Fill the game with content and polish the experience

- [ ] Create actual map data (town, buildings, interiors, overworld)
- [ ] Create sprite data (player characters, NPCs, enemies, items)
- [ ] Create event scripts (story events, NPC dialogue, puzzle triggers)
- [ ] Create music tracks and sound effects
- [ ] Implement all 9 puzzle game types in PuzzleTypes
- [ ] Complete the Custom Game Editor UI
- [ ] Complete the Game Sequence Editor UI
- [ ] Add achievement system integration
- [ ] Add replay recording and VOD playback
- [ ] Add deep linking for sharing custom games and replays

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

## Phase 5: Omni-Engine Assimilation (In Progress)
**Goal**: Integrate features from 34+ sprite/tilemap editors and provide Generative AI toolsets within the Omni-Engine (`bgeditor`).

- [ ] Port `bgeditor` to C++ using Qt6 (`bobui`)
- [ ] Port `bgeditor` to JavaFX
- [ ] Implement Unified Sprite Canvas mimicking Aseprite & Pixelorama
- [ ] Integrate text-to-sprite using local stable-diffusion pipelines
- [ ] Integrate image-to-3d mesh via Shap-E
