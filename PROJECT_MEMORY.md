# PROJECT_MEMORY: bob's game Omni-Workspace

## 1. Core Architecture & Vision
The "bob's game" repository is a colossal monorepo representing an ambitious "Omni-Engine." It serves not only as a game engine for the titular puzzle game but also as an overarching meta-ecosystem (the "nD" virtual console concept) that allows for game emulation, massive multiplayer interaction, and an integrated development environment.
*   **The Vision:** To build an Omni-Engine that is a strict superset of 6 major game engines (Defold, LÖVE, Phaser, Construct, GameMaker, RPG Maker), capable of doing everything they do but natively intertwined.
*   **The Subsystems:**
    *   **okgame (C++):** A native SDL3 (previously SDL2) engine intended as the robust performance backend.
    *   **bobsgameonlinejava (Java):** A legacy LibGDX implementation primarily used as a logic reference for the newer ports.
    *   **bobsgameweb (TypeScript):** The current primary deployment target, utilizing PixiJS v8 and Vite to render the game natively in the browser via WebGL/WebGPU.

## 2. Technical Stack & Patterns
*   **Graphics (Web):** `PixiJS v8`. Important constraints: `strokeThickness` and `FillGradient` do not exist in Pixi v8 (unlike v7). Must use `stroke` and array-based color fills.
*   **Network:** `Socket.io` backend running on a Node.js server. `NetworkManager` coordinates messages for the lobby, room synchronization, and real-time multiplayer states.
*   **Audio:** `AudioManager` built atop standard web audio and WebAudio APIs. Handles spatial sound hooks based on positional map triggers.
*   **Engine Core:** 187+ modules structured around a classic `ClientGameEngine` loop (`update(dt)`, `render()`). The puzzle logic is deeply mapped with classes like `GameLogic`, `Grid`, `Piece`, and configuration singletons like `GameType`.

## 3. Deployment & DevOps
*   **Frontend Target:** `bobsgameweb` deploys to Hetzner (`5.161.250.43`). Deployment must utilize `BACKEND_FORCE_TAR=1` to bypass Windows/Cygwin rsync issues.
*   **Build Pipeline:** Requires `npx vite build` (NOT `npm run build`) locally to circumvent git memory/paging issues on Windows environments.
*   **Versioning:** Versioning is rigorously tracked across the monorepo via a root `VERSION.md`. Bumping a version requires synchronization in `package.json`, `index.js`, and `MainMenuScene.ts`.

## 4. Current State & Omni-Engine Assimilation (v2.1.98)
*   **Submodules:** Extensive focus has been placed on resolving and synchronizing a massive tree of Git submodules. Submodule integrity across `okgame`, `bobsgameweb`, and `bobsgameonlinejava` is a primary ongoing priority. We recently merged 34+ external sprite editor libraries (Aseprite, LibreSprite, etc.) as submodules to fulfill the Omni-Engine feature-parity goal.
*   **Generative AI Integration:** We scaffolded integrations for Diffusers, Stable Diffusion, and Shap-E. The Node.js server acts as a proxy (`/api/generate/sprite`) pointing to a local Python daemon, giving the `CustomGameEditor` the ability to generate assets dynamically.
*   **Editor Port Strategy:** `bgeditor` is being cross-ported to C++ (via `bobui` Qt6) and JavaFX. We drafted structural blueprints to inject these dependencies into `CMakeLists.txt` and `build.gradle` respectively.
*   **Web Parity:** Bridged the visual scripting gap between the C++ engine and the web port by implementing `SequenceEditorView.ts`, `GameSequenceNode.ts`, and `BlockBehaviorPanel.ts`.

## 5. Collaboration Model
The workspace relies on a strict multi-agent architecture outlined in `AGENTS.md` and `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`. Jules, Gemini, Claude, and GPT each hold distinct structural roles spanning massive file traversal, documentation integrity, unit testing, and immediate feature implementation.
