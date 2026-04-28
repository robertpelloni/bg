# MEMORY: Project Architecture, Patterns, and Decisions

## 1. Project Overview & Ultimate Vision
- **The "Omni-Engine" Goal:** The ultimate vision is to create a massive, streamlined "ultra-project" 2D game engine, integrating and exceeding the feature parity of Defold, Love2D, Phaser, Construct, GameMaker, and RPGMaker.
- **Core Capabilities:** Built for deterministic cross-platform multiplayer (up to 30 players), leaderboards, in-game editing, integrated sprite editors (referencing ~30+ specific submodules like Aseprite, Pixelorama, LibreSprite, etc.), and generative AI tools (text-to-sprite, image-to-3d, etc.).
- **Current Paradigms:** The game currently supports multiple embedded experiences, including a Puzzle Game Demo, RPG World Demo, Network Demo, and an OS-level launcher menu (nD Console) transitioning between `BobsGame`, `Ping`, and `Ramio`.

## 2. Repository & Monorepo Structure
- **Root Workspace:** Serves as the global synchronization point (`C:/Users/hyper/workspace/bg/` or `/home/jules/workspace/bg/`). Contains overarching documentation (AGENTS.md, ROADMAP.md, VISION.md, TODO.md, etc.).
- **bobsgameweb:** The web port utilizing Vite, TypeScript, and PixiJS v8.
- **okgame:** Native C++20 and SDL3 engine port (currently needs vcpkg/Conan modernization).
- **bobsgameonlinejava:** Legacy/Reference Java 21 and LibGDX engine.
- *Decision:* Codebases are treated as submodules. Any universal logic ported to TypeScript must closely parallel its C++/Java counterparts structurally, adapting where browser paradigms dictate.

## 3. Deployment & DevOps Protocol
- **Infrastructure:** Hetzner VPS (`5.161.250.43`).
- **Frontend:** Served by Nginx from `/var/www/bobsgame.com/current`.
- **Backend:** Node.js Socket.io server running at `ws.bobsgame.com` (`/opt/bobsgameweb/server`), managed via systemd (`bobsgameweb-server`). SSL provided by Let's Encrypt.
- **Deployment Quirks:** 
  - Must use `BACKEND_FORCE_TAR=1` for backend deployments due to Windows/Cygwin rsync failures (tar-over-SSH works).
  - Web builds must use `npx vite build` directly. `npm run build` is known to cause a "paging file too small" Git error on Windows.
- **Health Checks:** Evaluated against `curl -s https://ws.bobsgame.com/healthz`.

## 4. Version Management
- **Single Source of Truth:** `VERSION.md` in the root dictates the current string (e.g., `2.1.84`).
- **Synchronization:** Any version bump requires parallel updates in `VERSION.md`, `package.json`, `src/renderer/scenes/MainMenuScene.ts` (for UI display), and `server/index.js`.
- Every deployment requires a version bump, which must be clearly documented in `CHANGELOG.md` and referenced in Git commit messages.

## 5. Architectural Patterns & Refactoring Discoveries
- **ECS (Entity Component System):** The game is migrating toward a formal ECS architecture. Decoupling game loops from legacy scene wrappers allows distinct `Entities` (with `Transform` and `Behavior` components) to be processed cleanly by an `ECSManager` (or `World.ts` which has a rollback-ready architecture saving up to 60 ticks of state).
- **Static vs. Dynamic Imports:** **Crucial Discovery:** Dynamic imports (e.g., `import('../../input/InputManager')`) inside hot `update(dt)` loops cause severe PIXI rendering flickers and Vite chunking warnings. *Decision:* Always use static imports for singletons like `InputManager` to ensure frame stability.
- **Barrel Export Pattern:** Every subsystem maintains an `index.ts` with explicit named exports. Internal imports use `./SubPanel` instead of `../SubPanel`.
- **Type-Only Exports:** Under Vite's `isolatedModules` flag, interfaces and types must strictly use `export type { X }`.

## 6. TypeScript / PixiJS v8 Specific Constraints
- **Styling:** `strokeThickness` is deprecated/removed in PIXI v8; use the `stroke` property. `FillGradient` serializes to garbage; utilize array-based colors `fill: [0xffffff, 0x00ffff]`.
- **ImageData:** The constructor demands `new Uint8ClampedArray()` to correctly fulfill the ArrayBuffer type.
- **Encapsulation:** 
  - `MiniGameEngine.container` is `protected` (accessed by subclasses). `MiniGameEngine.render()` returns `void`, not `Container`.
  - `BobMenu` options and cursor positions are rigidly encapsulated (`getCursorPosition()`, `getCurrentOption()`, etc.). Properties should not be mutated directly.
- **Instantiation Patterns:** `BGClientEngine` and `GUIManager` strictly require `(container, width, height)` upon construction.

## 7. C++/Java to TypeScript Porting Map
- C++ `private` → TS `protected` (when subclassing demands access).
- C++ UDP Sockets → WebRTC DataChannels (`PeerConnection.ts`).
- C++ OpenAL → Web Audio API (`AudioUtils.ts`).
- Java `synchronized` methods → Handled natively (no-ops) due to JavaScript's single-threaded event loop.
- Java `ArrayList` / `HashMap` → TS `Array` / `Map` or `Record`.
- C++ `shared_ptr` → Relies on standard TS garbage collection.

## 8. Workflow & Documentation Directives
- **Documentation:** Strict maintenance of `ROADMAP.md`, `TODO.md`, `CHANGELOG.md`, `HANDOFF.md`, and AI-specific instruction files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, etc.).
- **Code Comments:** Explanatory depth is expected—document *why* decisions were made, *what* side effects exist, and alternative approaches. Self-explanatory code remains bare.
- **Execution Style:** Autonomous, aggressive momentum. Implement features completely, commit/push incrementally (tagging versions), and immediately proceed to the next feature without stalling.

*End of [PROJECT_MEMORY]*