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
- **March 25, 2026:** Lua deep bindings were extended in `okgame`, including richer grid, piece, hold/next queue, and map data for Lua scripts.
- **March 25, 2026:** `okgame` native build recovery is now focused on local CMake/vendor resilience: optional `projectM`, a restored `lib/CTPL` include path, disabled AVIF in `SDL_image`, and module-mode ZLIB lookup for fresh build directories.
- **March 25, 2026:** `okgame`'s newer websocket multiplayer path now reports finished match scores through `NetworkManager::reportScore()` using the shared `{ mode, name, score, lines, time }` contract already used by the web and Java clients.
- **March 25, 2026:** The websocket `opponentFrame` payload can arrive as either a JSON string or JSON object; both `NetworkManager.cpp` and `BobsGame.cpp` now treat those shapes as valid.
- **March 25, 2026:** The latest fresh `okgame/build_recheck` configure no longer fails in the earlier SDL codec/vendor traps; the next blockers are project-level issues like missing `src/Engine/rpg/Avatar.cpp` and unresolved `Poco::Foundation` target linkage.
- **March 26, 2026:** After removing the stale `Avatar.cpp` source entry and enabling a minimal vendored Poco build, the next configure blocker became a vendored alias collision (`Poco` trying to redefine `ZLIB::ZLIB` and `PNG::PNG` after SDL_image had already created them).
- **March 26, 2026:** Guarding Poco's bundled `zlib` and `png` alias creation lets the fresh `okgame` configure move past the old Poco failure point and back into deeper `SDL_mixer` dependency configuration.
- **March 26, 2026:** The fresh `okgame/build_recheck_poco4` configure now completes successfully; the active validation frontier has moved from CMake configure failures to the first real native `bobsgame` compile/link errors.
- **March 26, 2026:** The newer websocket lobby path in `okgame` lives in `src/Engine/rpg/gui/LobbyMenuPanel.cpp`, not the legacy `Puzzle/OKGameNetwork.cpp` UDP lobby, and it now has in-flight parity work for `roomCreated`, `joinedRoom`, `gameStart`, `gameMode`, and `startLevel`.
