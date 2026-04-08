# MEMORY: Project Observations, Patterns & Preferences

## Repository Structure
- **Root workspace**: `C:/Users/hyper/workspace/bg/`
- **bobsgameweb**: `C:/Users/hyper/workspace/bg/bobsgameweb/` (Vite + TS + PixiJS v8 web port)
- **okgame**: `C:/Users/hyper/workspace/bg/okgame/` (C++20 + SDL3 native engine)
- **bobsgameonlinejava**: `C:/Users/hyper/workspace/bg/bobsgameonlinejava/` (Java 21 + LibGDX)
- All three are git submodules under `robertpelloni` on GitHub
- Feature branches in bobsgameonlinejava (`fix-build-and-backport-gametype-*`, `modernize-codebase-final-final`) are 0 commits ahead of main — already merged, safe to ignore

## Deployment Knowledge
- **Frontend**: Hetzner VPS at `5.161.250.43`, nginx serves static files from `/var/www/bobsgame.com/current`
- **Backend**: `ws.bobsgame.com`, Node.js Socket.io server at `/opt/bobsgameweb/server`, managed by systemd `bobsgameweb-server`
- **Deploy scripts**: `scripts/deploy-frontend-hetzner.sh` and `scripts/deploy-backend-vps.sh`
- **Must use `BACKEND_FORCE_TAR=1`** — rsync fails on Windows/Cygwin; tar-over-SSH works
- **Build command**: `npx vite build` directly — `npm run build` fails with "paging file too small" git error on Windows
- **SSL**: Let's Encrypt via certbot on the VPS
- **Health check**: `curl -s https://ws.bobsgame.com/healthz`

## Version Management
- Root `VERSION.md` contains just the version string (e.g., `2.1.73`)
- Version must be bumped in: `VERSION.md`, `package.json`, `src/renderer/scenes/MainMenuScene.ts`, `server/index.js`
- Version displayed in bottom-right of main menu
- Every deploy gets a new version number
- Commit message references version bump

## TypeScript / PixiJS v8 Constraints
- **No `strokeThickness`** on TextStyle — use `stroke` property instead
- **No `FillGradient`** in TextStyle — it serializes to garbage; use `fill: [0xffffff, 0x00ffff]` color arrays
- **`ImageData`** constructor needs `new Uint8ClampedArray()` for proper ArrayBuffer type
- **`isolatedModules`** requires `export type { X }` for type-only re-exports
- **MiniGameEngine.render()** returns void, not Container
- **MiniGameEngine.container** is protected, accessible in subclasses
- **BobMenu.cursorPosition** and **BobMenu.options** are private — use `getCursorPosition()`, `getOptionAt()`, `getCurrentOption()`, `getOptions()`, `setCursorPosition()`

## API Patterns
- **GameClock**: exported as `GameClock` from `./Clock`
- **Wallet**: uses `.money` property (not getters/setters)
- **GameSave**: static methods `loadFromLocal(slotIndex)` / `saveToLocal(slot)`
- **Skill**: uses `getValue()`
- **FriendCharacter.isOnline()**: is a method, not a property
- **SpriteData**: `widthPixels`/`heightPixels` (not `getImageWidth`), `animationList` (not `getAnimationList`), `getAnimation()` (not `getAnimationByName()`), sequences have `name` not `frameSequenceName`
- **BGClientEngine**: constructor requires `(container, width, height)`
- **GUIManager**: constructor requires `(container, width, height)`, has `isAnyMenuOpen()` (not `isAnyPanelOpen()`)
- **StatusBar**: constructor requires `StatusBarConfig { width, height? }`
- **Player/Character**: x/y are public properties (no setPosition method)
- **StateManager**: constructor requires a Container

## Barrel Export Pattern
- Every subsystem has `index.ts` with explicit named exports
- Import from `./SubPanel` (same directory), not `../SubPanel`
- Use `export type { X }` for type-only exports when `isolatedModules` is enabled

## C++/Java → TypeScript Port Map
- C++ `private` → TypeScript `protected` when subclass needs access
- C++ UDP sockets → WebRTC DataChannels (`PeerConnection.ts`)
- C++ OpenAL → Web Audio API (`AudioUtils.ts`)
- Java `synchronized` methods → no-op in single-threaded JS
- Java `ArrayList` → TypeScript `Array`
- Java `HashMap` → TypeScript `Map` or `Record`
- C++ `shared_ptr` → TypeScript direct references (GC handles memory)

## Code Style
- **Comments**: Explain what, why, and any non-obvious decisions. Don't comment self-explanatory code.
- **Naming**: PascalCase for classes/interfaces/enums, camelCase for methods/properties/variables
- **Imports**: Use barrel exports from subsystem index files
- **Error handling**: Use try/catch with console.warn for non-critical failures
- **No TODO blocks**: Either implement or create an issue in TODO.md

## Session Protocol
- **Start**: Read AGENTS.md, VISION.md, MEMORY.md, ROADMAP.md, TODO.md, HANDOFF.md
- **During**: Update VERSION.md for each deploy, commit with version in message, push regularly
- **End**: Update HANDOFF.md, MEMORY.md, ROADMAP.md, TODO.md with session progress

## Known Issues (as of v2.1.73)
- **NDDemoScene**: 2 pre-existing TypeScript errors (NDPuzzleGame and LibretroGame don't properly extend MiniGameEngine)
- **okgame build**: C++ build has compile/link errors (needs vcpkg/Conan modernization)
- **BobGameOnlineJava feature branches**: Local branches exist but are 0 ahead of main — already merged

## Recurring Observations
- The project uses a **monorepo with submodules** structure
- Each submodule is independently deployable
- Documentation must be updated in BOTH the submodule AND the root workspace
- The `scripts/` directory contains deployment automation
- The `docs/ai/` directory contains phase documentation (requirements, design, planning, implementation, testing)
- The engine is designed for **deterministic cross-platform multiplayer**
