# Epic: Porting and Modernization

## Overview
This document outlines the master plan for the "bobsgameonline" modernization and cross-platform porting epic.

## Phases

### Phase 1: Port C++ Puzzle Enhancements Back to Java
- **Goal:** The C++ version of the puzzle game (`okgame/legacy-src/src/Puzzle`) was expanded significantly beyond the original Java version (`bobsgameonlinejava/shared/src/main/java/com/bobsgame/puzzle`). We need to backport all features, details, and logic improvements from the C++ `okgame` puzzle code into the Java engine.
- **Tasks:**
  - Analyze differences between `okgame/legacy-src/src/Puzzle` and `bobsgameonlinejava/shared/src/main/java/com/bobsgame/puzzle`.
  - Port `Block`, `Piece`, `Grid`, `GameLogic`, `GameType`, etc., back to Java, ensuring 1:1 feature parity.
  - Test and verify the Java puzzle engine works with the backported changes.

### Phase 2: Upgrade `okgame` to SDL3
- **Goal:** Update the C++ `okgame` engine to use SDL3 instead of SDL2.
- **Tasks:**
  - Update `CMakeLists.txt` and dependency scripts to fetch/link SDL3.
  - Refactor `Engine` code (`okgame/legacy-src/src/Engine`) replacing SDL2 API calls with SDL3 equivalents.
  - Test compiling and running the game in C++.

### Phase 3: Upgrade `bobsgameonlinejava` to latest LWJGL and libGDX
- **Goal:** Modernize the Java engine by updating to the latest LWJGL and libGDX versions.
- **Tasks:**
  - Update `build.gradle` dependencies.
  - Resolve any deprecations or breaking changes in the API usage (e.g., rendering, input, audio).
  - Verify full functionality.

### Phase 4: Port Engine to TypeScript
- **Goal:** Port the engine to TypeScript (which seems to have started in `okgame/src` as an Electron/web app).
- **Tasks:**
  - Port the unified Puzzle engine to TypeScript.
  - Port the RPG engine components to TypeScript.
  - Set up build/bundling (Vite, Electron, etc.).

### Phase 5: Unify Libraries Across C++ and Java
- **Goal:** Ensure both the C++ and Java versions share the exact same capabilities and underlying libraries (where applicable/wrapper-based).
- **Tasks:**
  - Audit dependencies.
  - Standardize formats (e.g., networking protocols, serialization).
  - Ensure features are parallel in both projects.

### Phase 6: Unify Libraries for TypeScript
- **Goal:** Bring the TypeScript port up to identical capability and library usage as the C++/Java versions.
- **Tasks:**
  - Map unified libraries to TS equivalents or WebAssembly ports.
  - Test for feature parity.

## Current Progress
- **Status:** Initializing Phase 1 (Analyzing differences between C++ and Java puzzle implementations).
