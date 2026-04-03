# The Omni-Engine Specification (OKGame)

## 1. Executive Summary
The Omni-Workspace (OKGame / bob's game) is no longer just a cross-platform puzzle game; it is an **Omni-Engine**. The mandate is to achieve 100% feature parity—and 1:1 functionality, but *better*—with the six leading 2D game development environments: **Defold, LÖVE (Love2D), Phaser, Construct, GameMaker, and RPG Maker**.

This document outlines the extreme-depth analysis of these engines and how OKGame's architecture supersedes them across all 3 ports (C++, Java, TypeScript/Web).

---

## 2. Competitive Analysis & OKGame Superiority Matrix

### A. Defold
*   **Core Philosophy:** Message-passing Entity-Component-System (ECS), zero-setup cross-platform builds, Lua scripting, hot-reloading.
*   **Key Features:**
    *   Collections (Scenes) and Game Objects.
    *   Asynchronous message passing (`msg.post()`).
    *   Spine animation support, Particle FX.
    *   Box2D (2D) and Bullet (3D) physics.
*   **OKGame's Superior Implementation:**
    *   *Defold Better:* OKGame implements a strictly deterministic, network-synced ECS (`EnginePart` / `Entity`). Instead of loosely typed string messages, OKGame uses a strictly typed, multi-language event bus (`EventEmitter3` in TS, `EventBus` in Java/C++) that supports cross-network RPC natively.
    *   *Hot-reloading:* OKGame will hot-reload *across languages*. A Lua script edit in the editor instantly reloads the Web (WASM/JS), Java (JNI), and C++ native clients simultaneously without dropping the TCP multiplayer connection.

### B. LÖVE (Love2D)
*   **Core Philosophy:** Framework over engine. Pure Lua scripting. "Do it yourself" immediate-mode rendering freedom.
*   **Key Features:**
    *   Massive flexibility, no enforced GUI or editor.
    *   Low-level access to audio, physics (love.physics), and custom GLSL shaders (love.graphics).
*   **OKGame's Superior Implementation:**
    *   *LÖVE Better:* OKGame provides the same low-level `NDGameEngine.ts` and `BobsGame.cpp` immediate-mode rendering hooks, but wraps them in a highly optimized abstraction layer (`PixiJS v8 WebGPU` / `SDL3 + Vulkan` / `LibGDX`).
    *   *Scripting:* Instead of being restricted to Lua, OKGame allows logic to be written in TypeScript, Java, C++, or Lua (via Sol3 bindings), all compiling down to or interoperating with a universal deterministic core.

### C. Phaser (Phaser.io)
*   **Core Philosophy:** HTML5 web-first game framework. Scene management, Sprite atlases, and Tweening.
*   **Key Features:**
    *   Arcade Physics (AABB) and Matter.js (Rigid body).
    *   Scene graph (`Phaser.Scene`).
    *   Robust input handling (Pointers, Keyboards, Gamepads).
    *   Scale Manager and Camera pipelines.
*   **OKGame's Superior Implementation:**
    *   *Phaser Better:* Phaser is inherently single-threaded JS. OKGame's web port leverages WebWorkers for heavy logic, WebGL/WebGPU for rendering (via PixiJS), and provides *native* C++ and Java clients. A Phaser game runs in the browser; an OKGame runs identically on a native 144Hz desktop client, a Java backend server, and the browser, with perfectly synced state.
    *   *Camera:* OKGame's camera system handles multi-target tracking, fractional zooming, and post-processing (CRT shaders, Bloom) natively across all ports.

### D. Construct (Construct.net)
*   **Core Philosophy:** No-code/low-code visual scripting. Event Sheets (Conditions -> Actions).
*   **Key Features:**
    *   Event Sheets (Condition / Action / Sub-events / Local variables).
    *   Behaviors (Platformer, 8-Direction, Bullet, Sine, Turret).
    *   Effect shaders and layer blending.
    *   Offline PWA support.
*   **OKGame's Superior Implementation:**
    *   *Construct Better:* Construct's event sheets are heavily tied to its proprietary JSON format. OKGame introduces an **Omni-Event Sheet System**—a visual node/block editor that compiles directly into highly optimized Lua/TypeScript/C++ code.
    *   *Behaviors:* OKGame's ECS natively supports "Behaviors" as attachable Components. Unlike Construct, you can drop down into the raw C++ or TS code of a Behavior, modify it, and hot-reload it into the Visual Editor.

### E. GameMaker (GameMaker.io)
*   **Core Philosophy:** Room editor, Object-Oriented event system (Create, Step, Draw), GameMaker Language (GML).
*   **Key Features:**
    *   Room Editor (Layers, Instances, Tiles, Paths).
    *   Sequences (Animation timelines).
    *   Texture Group management.
    *   Audio grouping and 3D audio.
*   **OKGame's Superior Implementation:**
    *   *GameMaker Better:* GameMaker's GML is quirky and historically slow (though YYC improves this). OKGame uses industry-standard languages (TS, C++, Java, Lua).
    *   *Room Editor:* The OKGame `MapEditor` supersedes GM's Room Editor by integrating "Shift Map" topology, infinite procedural generation layers, and multi-user concurrent editing (Google Docs style, powered by the Java Server).

### F. RPG Maker
*   **Core Philosophy:** Database-driven RPG creation. Tile-based mapping, eventing, turn-based battle systems.
*   **Key Features:**
    *   The Database: Actors, Classes, Skills, Items, Weapons, Armor, Enemies, Troops, States, Animations, Tilesets, Common Events.
    *   Map Events (Pages, Conditions, Movement Routes).
    *   Auto-tiling algorithms.
    *   Message/Dialogue systems with face graphics.
*   **OKGame's Superior Implementation:**
    *   *RPG Maker Better:* RPG Maker is historically limited to its rigid grid and single-threaded Ruby/JS engines. OKGame decouples the RPG Database into a universal relational schema (`JSON/SQLite`) synced via the Java Server.
    *   *Eventing:* OKGame implements the exact same "Event Page / Condition / Action Route" logic but executes it asynchronously and supports full network sync (MMORPG out of the box).
    *   *Grid:* OKGame supports classic 16x16 / 32x32 grids, but also seamless pixel-perfect movement, isometric planes, and hex grids, switchable per map.

---

## 3. The Omni-Engine Architectural Blueprint

To achieve 100% feature parity across C++, Java, and TypeScript, OKGame is structured into universally mirrored domains:

### Domain 1: The Unified Database (RPG Maker + GameMaker)
*   **Data Structures:** A central registry of `AssetData`, `EntityData`, `SkillData`, `ItemData`, `MapData`.
*   **Implementation:** Stored in SQLite (Native/Java) and IndexedDB (Web), serialized over GZip/Base64 JSON via the TCP/WebSocket server.

### Domain 2: The Visual Logic Core (Construct + GameMaker)
*   **Event Sheets:** A visual JSON structure representing Conditions and Actions.
*   **Transpiler:** The engine reads Event Sheets and executes them via an interpreter, or transpiles them into native code for release builds.

### Domain 3: The Deterministic ECS (Defold + Phaser)
*   **Entities:** Everything is an Entity (Player, Bullet, Map Event).
*   **Components:** Attach `SpriteComponent`, `PlatformerBehavior`, `EightDirectionBehavior`, `PhysicsComponent`.
*   **Systems:** `PhysicsSystem`, `RenderSystem`, `EventSystem` update all components in strict deterministic order to ensure network rollback capability.

### Domain 4: The Immediate-Mode Hooks (LÖVE)
*   **Custom Shaders:** The engine provides a universal Shader API that translates GLSL (Web/Java) into SPIR-V/Vulkan/WebGPU.
*   **Raw Draw:** `Renderer.drawRect`, `Renderer.drawTexture` available in scripts for complete custom rendering bypass.

### Domain 5: The Virtual Consoles (Libretro + ProjectM)
*   **The nD (Virtual Handheld):** The engine natively supports embedding virtual screens (like the Nintendo DS layout) anywhere in the game world.
*   **Libretro:** Emulators (NES, SNES, Genesis) run inside these virtual screens using WASM in the browser, JNI in Java, and native dynamic libraries in C++.
*   **ProjectM:** Audio visualizers run in the background (butterchurn on Web, native libprojectM on C++) synced to the global audio track.

## 4. Execution Plan (Next Steps)
1. **Web Port ECS Scaffold:** Implement the base Entity-Component-System mirroring Construct's Behaviors.
2. **Event Sheet Interpreter:** Build a visual-script JSON runner in TypeScript/Java/C++ that perfectly mimics RPG Maker Map Events and Construct Event Sheets.
3. **Database Schema Expansion:** Expand `MapData` and `AssetData` to encompass the entire RPG Maker Database spec (Actors, Items, Enemies).
4. **Libretro/ProjectM Submodules:** Secure the WASM, JNI, and Native pipelines for the virtual consoles.
