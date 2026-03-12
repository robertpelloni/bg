# Omni-Workspace Refactoring & Porting Plan

## 1. Project Analysis & Current State

### `bobsgameonlinejava` (Java)
*   **Origin:** The original RPG engine with basic puzzle elements.
*   **Current State:** Successfully ported the core "engine" of the puzzle game (dropping blocks, matching, clearing, basic garbage). However, the "meta-game" features are severely lacking. For instance, the `CustomGameEditor` in Java is a mere skeleton (17KB) compared to the C++ version (220KB).
*   **Deficiencies:** Missing deep menu logic, game sequence editors, and advanced special block behaviors (BOMB, WEIGHT, FLASHING CLEAR, etc.).
*   **Tech Stack:** Uses older LWJGL. Needs modernization to the latest LWJGL and libGDX.

### `okgame` (C++)
*   **Origin:** Translated from Java, significantly expanding the puzzle game into its own robust ecosystem.
*   **Current State:** The RPG engine side suffers from broken memory management. However, the puzzle logic is highly modular, advanced, and feature-rich (e.g., `GameLogicChains.cpp`, `GameLogicGarbage.cpp`, `GameSequenceEditor.cpp`).
*   **Tech Stack:** Currently on SDL2. Needs upgrading to SDL3.

## 2. Strategic Goals

1.  **Deep Parity (C++ to Java):** Port the `okgame` C++ puzzle game back to the `bobsgameonlinejava` engine IN FULL, missing zero features or details.
2.  **Modernization (C++):** Upgrade `okgame` to use SDL3.
3.  **Modernization (Java):** Upgrade `bobsgameonlinejava` to use the latest LWJGL and libGDX.
4.  **TypeScript Port:** Port the entire unified engine to TypeScript.
5.  **Library Unification:** Ensure that C++, Java, and TypeScript versions share the exact same libraries, abstractions, and capabilities.

## 3. Step-by-Step Execution Plan

### Phase 1: Puzzle Engine Parity (C++ to Java Port)
*   **1.1 Structure Alignment:** Refactor the monolithic `GameLogic.java` in the client to match the modular C++ structure (`GameLogicChains`, `GameLogicGarbage`, `GameLogicRender`, `GameLogicNetwork`).
*   **1.2 Feature Porting - Editors:** Translate the massive `CustomGameEditor.cpp` and `GameSequenceEditor.cpp` into Java.
*   **1.3 Feature Porting - Mechanics:** Ensure all special pieces (BOMB, WEIGHT, SUBTRACTOR, ADDER, SCANLINE CLEAR) behave identically to C++'s `removeFlashedChainBlocks`.
*   **1.4 Menus and UI:** Port the deep menu structures from `BobsGameMenus.cpp` and `OKGameMenus.cpp`.

### Phase 2: Engine Modernization
*   **2.1 Java Upgrade:** Update `bobsgameonlinejava` build files (Gradle) to pull the latest LWJGL 3.x and libGDX. Rewrite the rendering and input polling loops to use the new APIs.
*   **2.2 C++ Upgrade:** Update `okgame`'s CMake configuration to link SDL3 instead of SDL2. Refactor window creation, event polling, and rendering to SDL3 standards.

### Phase 3: TypeScript Port
*   **3.1 Project Scaffolding:** Set up a clean Vite/TypeScript environment (building upon the existing `.ts` files in `okgame/src/main` if applicable).
*   **3.2 Core Logic Translation:** Translate the unified Java/C++ puzzle logic directly into strict TypeScript classes.
*   **3.3 Render/Audio Layer:** Implement an HTML5 Canvas / WebGL rendering layer and Web Audio API layer that mimics the SDL3 / LibGDX abstractions.

### Phase 4: Library & Capability Unification
*   **4.1 Abstract Interfaces:** Create standard interfaces for `Renderer`, `Audio`, `Input`, and `Network` across all three languages.
*   **4.2 Dependency Sync:** Ensure any third-party libraries (like tweening, pathfinding, or JSON parsing) have identical implementations or wrappers in all three languages.
*   **4.3 Verification:** Create cross-platform test suites (or data-driven tests) to prove that the same input yields the exact same game state frame-by-frame.