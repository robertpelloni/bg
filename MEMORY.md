# MEMORY: Project Observations & Preferences

## 1. Codebase Patterns
- **C++:** Prefers `sp<T>` for `std::shared_ptr` and `ms<T>` for `std::make_shared`.
- **C++:** Thread-safe methods should have a `_S` suffix.
- **Java:** Uses LibGDX `Scene2D` for all UI components.
- **Unified Logic:** The `Puzzle` logic must be kept in sync across `okgame`, `bobsgameonlinejava`, and `bobsgameweb`.

## 2. Environment Preferences
- **Java:** Standardized on Java 21 LTS. Gradle builds should use `--no-daemon`.
- **Versioning:** Single source of truth is the root `VERSION` file.
- **Commits:** Conventional commits are required, referencing version bumps.

## 3. Recurring Issues & Fixes
- **Merge Conflicts:** Intelligently solve conflicts by prioritizing the most recent feature additions.
- **Detached HEAD:** Always ensure submodules are on a tracked branch (main/master).
- **Gradle/Java 25:** Incompatibility resolved by pinning to Java 21.

## 4. Current Work Context
- **March 22, 2026:** Gemini CLI session started.
- **Standardizing Instructions:** Consolidating model-specific instruction files to reference the universal instructions.
- **Feature Gap Analysis:** Identifying unimplemented features from roadmaps and conversation history.
