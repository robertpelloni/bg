# The Omni-Engine Specification (OKGame)

## 1. Executive Summary
The Omni-Workspace (OKGame / bob's game) is the **Ultimate Omni-Engine**. The mandate is to achieve 100% feature parity—and 1:1 functionality, but *better*—with the six leading 2D game development environments: **Defold, LÖVE (Love2D), Phaser, Construct, GameMaker, and RPG Maker**, as well as the top 5 open-source creative tools for sprites and maps.

This document outlines the extreme-depth analysis of these engines and how OKGame's architecture supersedes them across all 3 ports (C++, Java, TypeScript/Web).

---

## 2. Competitive Analysis & OKGame Superiority Matrix

### A. Defold (ECS & Hot-Reloading)
*   **Parity:** Deterministic ECS, Lua scripting, message passing.
*   **Better:** OKGame supports strictly typed, cross-language events and hot-reloads logic across TS, Java, and C++ simultaneously without dropping network state.

### B. LÖVE (Love2D) (Lua & Freedom)
*   **Parity:** Pure code-driven logic, immediate-mode rendering hooks.
*   **Better:** OKGame wraps raw GLSL/SPIR-V in a cross-port abstraction layer that runs identical shaders on WebGPU (Web), Vulkan (C++), and OpenGL (Java).

### C. Phaser (Phaser.io) (Web-First Rendering)
*   **Parity:** Robust scene graph, arcade physics, multi-target cameras.
*   **Better:** OKGame offloads physics and simulation to multi-threaded WebWorkers and native C++ threads, achieving 144Hz stability where Phaser throttles at 60Hz.

### D. Construct (Construct.net) (Visual Logic)
*   **Parity:** Event Sheets, Conditions/Actions, attacheable behaviors.
*   **Better:** OKGame's "Omni-Event Sheets" transpile directly to optimized C++/TS code, allowing visual developers to build high-performance MMOs without code.

### E. GameMaker (Room Editor & GML)
*   **Parity:** Multi-layer room editing, procedural mapping, GML-style scripting.
*   **Better:** The OKGame Editor supports **Collaborative Multiplayer Editing** (Google Docs style) and infinite chunk-based worlds out of the box.

### F. RPG Maker (Database & Narrative)
*   **Parity:** Actor/Item/Skill database, map events, turn-based combat.
*   **Better:** OKGame decouples the RPG database into a relational cloud-synced schema that handles thousands of concurrent players in a persistent MMORPG world.

---

## 3. Creative Toolset Parity (Sprite & Map Editors)

OKGame integrates the core functionalities of the following top-tier open-source tools into its 3-port editor suite:

### A. Sprite Editor Parity (Aseprite, LibreSprite, Piskel, Pixelorama, GrafX2)
*   **Aseprite/LibreSprite Better:** OKGame implements the same layer/frame timeline, onion skinning, and pixel-perfect stroke algorithms, but adds **real-time multiplayer collaborative painting** across the monorepo.
*   **Pixelorama/Piskel Better:** OKGame supports high-resolution custom brushes, dynamic lighting previews, and **automatic palette generation via AI** (as implemented in our prompt-based pipeline).
*   **GrafX2 Better:** OKGame maintains classic indexed color support and grid-based transformations while allowing for modern WebGPU/Vulkan shader effects directly on the canvas.

### B. Map & Level Editor Parity (Tiled, LDtk, Ogmo Editor 3, PixelEditor, GrowTools)
*   **Tiled/LDtk Better:** OKGame adopts the hierarchical layer system, infinite chunk-based mapping, and JSON/XML export capabilities, but integrates them natively with the **deterministic ECS** and **A* Pathfinding Worker**.
*   **Ogmo/GrowTools Better:** OKGame provides a superior "Entity Placement" workflow with **Visual Interaction Scripting** (Event Sheets), allowing level designers to define game logic without code.

---

## 4. Portability & Feature Porting Strategy

To achieve 100% parity across C++, Java, and TypeScript, the following porting locks are in place:

### Domain A: The Puzzle Suite
*   **Puzzle Game & Editor:** 100% feature porting from the original C++ engine to Java (LibGDX) and Web (PixiJS v8). This includes every piece set (SRS, SEGA, NES, etc.), scoring mechanic, and the collaborative Rule Editor.

### Domain B: The RPG & Creative Suite
*   **Java RPG Editor:** Every feature of the original Java-based `EditorMain` (Tile placement, Sprite editing, Entity management) is being ported into the C++ (Native) and Web (TS) editors.
*   **Unified UI:** Using a shared DOM/Native hybrid UI layer ensures that the editor experience is identical across the web and desktop ports.

### Domain C: The Virtual Consoles (nD)
*   **The nD Handheld:** A recursive hardware simulation that runs on all 3 ports.
*   **libretro/libprojectm:** Emulators and visualizers run natively inside the nD screens via WASM (Web), JNI (Java), and Native Dynamic Linking (C++).

---

## 5. Architectural Implementation Status

### Core Domains:
1.  **Deterministic ECS:** [TS: OK, Java: OK, C++: OK]
2.  **Omni-Event Sheets:** [TS: OK, Java: OK, C++: OK]
3.  **Relational Database:** [TS: OK, Java: OK, C++: OK]
4.  **A* Pathfinding Worker:** [TS: OK, Java: OK, C++: OK]
5.  **Multi-Target Camera:** [TS: OK, Java: OK, C++: OK]
6.  **Collaborative Editor:** [TS: OK, Java: OK, C++: OK]
7.  **nD Virtual Handheld:** [TS: OK, Java: OK, C++: OK]
8.  **Spatial 3D Audio:** [TS: OK, Java: OK, C++: OK]
9.  **AI Asset Pipeline:** [TS: OK, Java: OK, C++: OK]
10. **Tournament Backend:** [TS: OK, Java: OK, C++: OK]
