# MEMORY: Project Observations & Preferences

## 1. Codebase Patterns
- **C++:** Prefers `sp<T>` for `std::shared_ptr` and `ms<T>` for `std::make_shared`.
- **C++:** Thread-safe methods should have a `_S` suffix.
- **Java:** Uses LibGDX `Scene2D` for all UI components.
- **Unified Logic:** The `Puzzle` logic must be kept in sync across `okgame`, `bobsgameonlinejava`, and `bobsgameweb`.
- **ECS (Omni-Engine):** Standardized component types (Transform, Sprite, Behavior, Light) across 3 languages using string-based type registration for 1:1 serialization.
- **Visual Scripting:** Event Sheets use a nested JSON block structure (Conditions/Actions) interpreted by the `VisualScriptSystem`.
- **Multi-Threading:** Heavy logic (A* pathfinding, simulation) is offloaded to `GameWorker` (TS) or background threads (C++/Java) to maintain 60fps.

## 2. Environment Preferences
- **Java:** Standardized on Java 21 LTS. Gradle builds should use `--no-daemon`.
- **Versioning:** Single source of truth is the root `VERSION` file.
- **Commits:** Conventional commits are required, referencing version bumps.
- **Asset Resolution:** Use `BIG_DATA_URL` for absolute paths and the `manifest.json` for bulk asset queuing.

## 3. Recurring Issues & Fixes
- **Merge Conflicts:** Intelligently solve conflicts by prioritizing the most recent feature additions.
- **Detached HEAD:** Always ensure submodules are on a tracked branch (main/master).
- **Gradle/Java 25:** Incompatibility resolved by pinning to Java 21.
- **PIXI v8 API:** Standardized on options-object syntax for `Text`, `Graphics`, and `Filter`.

## 4. Current Work Context
- **April 2, 2026:** Final Session Wrap-up.
- **Omni-Engine:** Successfully transformed the puzzle game into a full-scale game creation engine with parity across Web, Java, and C++.
- **World State:** MMORPG world is functional with synced player movement, NPC AI, and interactive dialogue.
- **Editors:** Functional Custom Game Rule Editor and RPG World Database Editor implemented and synced to server.
- **Competitiveness:** Unified Elo rating system and tournament bracketing logic implemented in the backend.
- **Handoff:** Architectural phase complete. Ready for content generation and platform hardening.