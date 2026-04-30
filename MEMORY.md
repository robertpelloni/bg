# MEMORY: Project Observations, Patterns & Preferences

## Repository Structure

- **Root workspace**: `C:/Users/hyper/workspace/bg/`
- **bobsgameweb**: `C:/Users/hyper/workspace/bg/bobsgameweb/` (Vite + TS + PixiJS v8 web port) — tracked directly in parent repo (NOT a submodule despite .gitmodules entry)
- **okgame**: `C:/Users/hyper/workspace/bg/okgame/` (C++20 + SDL3 native engine) — submodule
- **bobsgameonlinejava**: `C:/Users/hyper/workspace/bg/bobsgameonlinejava/` (Java 21 + LibGDX) — submodule

## Session v2.2.5 Notes

- **Git index.lock**: Persistently held by external process (another agent/IDE). Could not commit any changes this session. All work is uncommitted.
- **295 TypeScript files** (up from 291), 893 modules, builds in ~25s
- **Two audio systems coexist**: Howler AudioManager (singleton, high-level) + Web Audio AudioUtils (engine-level procedural). Both work independently.
- **EventManager** is now wired into ClientGameEngine.update() loop
- **LoginScene** connects to Socket.io server and sets player identity
- **GameSequenceEditor** is a full visual campaign editor

## Deployment Knowledge

- **Frontend**: Hetzner VPS `5.161.250.43`, nginx `/var/www/bobsgame.com/current`
- **Backend**: `ws.bobsgame.com`, Node.js Socket.io `/opt/bobsgameweb/server`, systemd `bobsgameweb-server`
- **Must use `BACKEND_FORCE_TAR=1`** — rsync fails on Windows
- **Build**: `npx vite build` only — `npm run build` fails
- **Health check**: `curl -s https://ws.bobsgame.com/healthz`
- **Map API**: Server now has GET/PUT /maps/:id, GET /maps

## Version Management (v2.2.5+)

- Bump in 4 files: `VERSION.md`, `package.json`, `MainMenuScene.ts`, `server/index.js`
- Displayed bottom-right of main menu
- Every deploy = new version

## PixiJS v8 Constraints

- No strokeThickness → use `stroke` property
- No FillGradient in TextStyle → use `fill: [color1, color2]`
- Use options-object API (roundRect, fill, stroke) — not legacy v7

## Audio System

- **Howler AudioManager** (src/renderer/audio/AudioManager.ts): Singleton. Used by Game.ts, scenes. Supports Howl loading, tracker music, spatial audio, fade, analyzer.
- **Web Audio AudioUtils** (src/renderer/engine/audio/AudioUtils.ts): Used by DemoWorld for procedural SFX. Channel pooling, tone generation.
- **Sync**: ClientGameEngine.syncAudioSettings() on init

## Map System

- **MapManager**: Stores registered maps, handles transitions, door/warp tracking
- **MapLoader**: Loads from server/static/procedural. Generates: town (40×40), overworld (80×80), interiors
- **Server API**: GET/PUT /maps/:id, GET /maps
- **Map JSON**: `{ id, name, width, height, tileWidth, tileHeight, tiles: number[][], areas, doors, warps, lights, isOutside }`

## Event System

- **EventManager**: Manages flags, skills, dialogues, events, conditions
- Wired into ClientGameEngine.update() each frame
- Full serialization (loadFromSave/getSaveData) for persistence
- Event triggers: registerEvent(), triggerEvents(trigger), evaluateCondition(command)

## Key API Patterns

- GameClock: exported as `GameClock` from `./Clock`
- Wallet: uses `.money` property
- GameSave: static `loadFromLocal(slotIndex)` / `saveToLocal(slot)`
- BobMenu: private cursorPosition/options — use getter methods
- BGClientEngine: constructor requires `(container, width, height)`
- GUIManager: constructor requires `(container, width, height)`
- Player/Character: x/y are public properties
