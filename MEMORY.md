# MEMORY: Project Observations & Preferences

## 1. Codebase Patterns
- **C++:** Prefers `sp<T>` for `std::shared_ptr` and `ms<T>` for `std::make_shared`.
- **C++:** Thread-safe methods should have a `_S` suffix.
- **Java:** Uses LibGDX `Scene2D` for all UI components.
- **Unified Logic:** The `Puzzle` logic must be kept in sync across `okgame`, `bobsgameonlinejava`, and `bobsgameweb`.
- **ECS (Omni-Engine):** Standardized component types (Transform, Sprite, Behavior, Light, Combat, Pathfinding) across 3 languages using string-based type registration for 1:1 serialization.
- **Visual Scripting:** Event Sheets use a nested JSON block structure (Conditions/Actions) interpreted by the `VisualScriptSystem`.
- **Multi-Threading:** Heavy logic (A* pathfinding, simulation) is offloaded to `GameWorker` (TS) or background threads (C++/Java).
- **Sub-pixel Rendering:** Pieces and entities use `lerp` for smooth visual movement between deterministic grid ticks.

## 2. Environment Preferences
- **Java:** Standardized on Java 21 LTS. Gradle builds should use `--no-daemon`.
- **Versioning:** Single source of truth is the root `VERSION` file.
- **Commits:** Conventional commits are required, referencing version bumps.
- **Asset Resolution:** Use `BIG_DATA_URL` for absolute paths and the `manifest.json` for bulk asset queuing.
- **Mobile (Web):** Use Capacitor for iOS/Android bridging and `TouchControls` for the virtual input layer.

## 3. Recurring Issues & Fixes
- **Merge Conflicts:** Intelligently solve conflicts by prioritizing the most recent feature additions.
- **Detached HEAD:** Always ensure submodules are on a tracked branch (main/master).
- **Gradle/Java 25:** Incompatibility resolved by pinning to Java 21.
- **PIXI v8 API:** Standardized on options-object syntax for `Text`, `Graphics`, and `Filter`.
- **Worker Typing:** Use `(self as any).postMessage` for correct Transferable overload support in Vite.

## 4. Current Work Context
- **April 2, 2026:** Final Architectural Milestone complete.
- **Omni-Engine:** Successfully transformed the puzzle game into a massive multi-port creation engine.
- **MMORPG:** 100x100 world is functional with synced players, NPCs, AI, and combat.
- **Editors:** Map Editor, Game Rule Editor, and World Database Editor are 100% functional and synced.
- **Mobile:** Web port is mobile-ready with touch controls and automated Capacitor builds.
- **Backend:** Persistence, Elo, Matchmaking, and WebSocket gateways are established.
- **Released:** Version 2.1.5 is ready for content creation.
- **Achievements System:** Web port now includes a persistent local achievement/stat tracker plus toast notifications. Use whole-second batching for long-running meta stats like playtime instead of per-frame persistence.
- **Dialogue Metrics:** Only count NPC/player-initiated dialogue toward social/RPG interaction achievements; system prompts and console messages should not increment interaction stats.
- **Replay VOD Progression:** Leaderboard replay viewing is now a meaningful meta-loop and can feed spectator/social achievements.
- **Pause Access Pattern:** When adding metagame UX to active gameplay, prefer pause-menu entry points over modal hotkeys so controller users get consistent, discoverable access.
- **Editor Progression Pattern:** Hook achievement stats to explicit editor intents (save, share, first meaningful draw, actor creation, AI generation) rather than every low-level edit event to avoid noisy progression inflation.
- **Achievement Sync Strategy:** Merge server snapshots with local progress using numeric max + unlocked-id union. This is safe for cumulative stats and avoids deleting newer local progress when reconnecting from another device.
- **Achievement Identity Pattern:** Centralize player-name/profile derivation for achievement sync in one helper instead of sprinkling raw `localStorage` lookups across scenes.
- **Web Performance Pattern:** Prefer lazy scene imports for rarely used shells/tools and keep manual chunking limited to stable vendor groupings; over-eager source chunk rules can create circular-chunk warnings.