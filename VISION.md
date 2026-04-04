# VISION: The Omni-Engine (bob's game / OKGame)

## 1. The Ultimate Goal
The vision for **bob's game / OKGame** has transcended a cross-platform puzzle game. It is the **Omni-Engine**—a massively multiplayer game creation ecosystem designed to achieve 100% feature parity, and 1:1 functionality (but *better*), with the six leading 2D engines: **Defold, LÖVE, Phaser, Construct, GameMaker, and RPG Maker**.

This involves a unified deterministic core implemented flawlessly across C++, Java, and TypeScript, enabling seamless MMO-scale multiplayer, global persistence, and hot-reloading across Desktop, Web, and Mobile.

The Omni-Workspace acts as a "Single Source of Truth" where an RPG Maker-style database, Construct-style event sheets, Defold-style ECS, and GameMaker-style room editors all compile down into a universal, deterministic, multiplayer-native format.

## 2. Core Pillars

### A. Omni-Logic (The Deterministic Core & ECS)
- **1:1 Behavioral Parity:** Every entity behavior (Platformer, 8-Direction, Bullet), every RPG event condition, every piece rotation (SRS, NES), and every RNG tick must produce identical results across C++, Java, and TypeScript.
- **Deterministic ECS:** The game engine is designed as a strict Entity-Component-System state machine, allowing rollback netcode and absolute sync across the globe.
- **Universal Serialization:** Utilizing GZip/Base64 GSON/JSON to serialize the entire GameMaker/RPG Maker style database (Maps, Actors, Items, Event Sheets) so it can be streamed from the Java Server to any C++ or Web client instantly.

### B. The Superset Feature Matrix
- **Defold (Better):** A heavily typed, network-synced message-passing architecture that hot-reloads instantly across languages.
- **LÖVE (Better):** Complete raw immediate-mode access to the GPU and Audio graph (WebGPU/Vulkan/OpenGL) wrapped in safe bindings, scriptable in Lua, TS, or C++.
- **Phaser (Better):** Multi-threaded architecture leveraging WebWorkers and native compiled backends instead of single-threaded JS, with fractionally zoomed multi-target cameras.
- **Construct (Better):** An **Omni-Event Sheet System** that compiles visual node blocks directly into highly optimized C++/TS code, supporting deeply nested conditions and actions.
- **GameMaker (Better):** A collaborative, multiplayer map editor (Google Docs style) that surpasses the Room Editor, featuring infinite procedural layers and raw GML-equivalent script editing.
- **RPG Maker (Better):** A fully decoupled, MMO-ready relational database (Actors, Classes, Items, Weapons, Armor, Enemies) with classic map event pages and conditions, executing asynchronously.

### C. Technological Excellence & Modernization
- **Modern Standards:**
    - **C++:** SDL3, C++20, Modern Vulkan/OpenGL, EnTT (ECS).
    - **Java:** Java 21 LTS, LibGDX 1.14.0, Netty TCP.
    - **Web:** Vite, TypeScript 5+, PixiJS v8 (WebGPU), WebWorkers, WebRTC.
- **Visual Sophistication & The nD:** Deep integration of `libprojectM` (audio visualizers) and `libretro` (native emulators). These run natively inside virtual screens (the "nD" handheld) seamlessly across Web (WASM), Java (JNI), and C++.
- **Audio Fidelity:** A hybrid audio engine supporting both high-quality PCM and authentic tracker music (MOD/XM/S3M/IT) via libopenmpt across all ports.
- **Console-Quality Metagame:** The engine should not stop at runtime parity; it must also provide a platform-level metagame layer including achievements, replay VODs, rankings, haptics, progression feedback, polished notification UX, in-session access paths, eventually cloud-synced progression, and a frontend architecture fast enough that this shell feels native across every target.

## 3. Structural Design & Submodules
The monorepo is composed of specialized sub-projects:
- `bobsgameonlinejava/`: The high-performance Java backend and legacy desktop powerhouse.
- `bobsgameweb/`: The modern, zero-install web port (okgame v2.0) designed for bobsgame.com.
- `okgame/`: The original C++ engine, optimized for low-latency native execution.
- `references/`: Over 20+ reference implementations of editors (Aseprite, Tiled, Pixelorama) to inspire our creative toolset.

## 4. Development Philosophy
- **AI-First Orchestration:** Leveraging specialized AI agents (Gemini, Claude, GPT) for continuous development. Gemini handles large-scale analysis, Claude handles architecture/docs, and GPT handles rapid implementation.
- **Self-Documenting:** All logic must be heavily commented, and all project metadata (Roadmap, Todo, Dashboard) must be updated autonomously.
- **Zero-Stop Development:** The project is in a state of "continuous party"—development never stops, regressions are never accepted, and every build is better than the last.
