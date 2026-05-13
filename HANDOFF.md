# HANDOFF: bob's game Omni-Engine
**Last Updated**: 2026-05-12 22:50:37
**Version**: 2.1.95

## AI Agent Hand-off Document

This document tracks the ongoing development of the bob's game engine across multiple AI agent sessions.

---

## 🟢 Current State (v2.1.95)


### Recent Accomplishments (Jules)
- **Omni-Engine Generative Tools**: Cloned and added 34 new sprite-editing related submodules to `references/editors/` and 5 massive Generative AI toolsets (Diffusers, Stable Diffusion, ControlNet, Shap-E) to `references/ai/`.
- **Feature Gap Analysis**: Wrote `docs/analysis/editor_parity_analysis.md` comparing the web editor against the C++ `CustomGameEditor` logic.
- **bgeditor Port Strategy**: Drafted `docs/analysis/bgeditor_port_strategy.md` outlining the integration of `bobui` (Qt6) into the C++ `okgame` framework, as well as the transition to JavaFX for `bobsgameonlinejava`.
- **Version Management**: Bumped workspace version to `2.1.95` to seal the massive repository submodule sync.

### Previous Accomplishments (Jules)
- **Phase 4 (Puzzle Game Types) Complete**: Fleshed out `GameType.ts` configuration logic and enumerated constants representing all 9 planned game types (Marathon, Sprint, Ultra, Survival, Dig, Combo, Master, Zen, Classic), defining respective gravity and behavior parameters natively inside the class logic.
- **Phase 3 (RPG World Demo & Map rendering) Complete**: Validated MapManager functionality and proper parsing of dynamic tilemaps through Pixi. RPG World features functioning NPCs.
- **Phase 3 (Tournament Demo) Complete**: Hooked up the `TournamentManager` to interactive components. Added a placeholder demo representation within the `NDOS` menu structure. Validated the `LobbyScene` properly initializes tournaments and correctly instantiates the `showTournamentBracket()` UI view while navigating cleanup conditions to prevent orphaned DOM overlays.
- **Phase 3 (ECS Demo) Complete**: Evaluated the ECS structure (`bobsgameweb/src/renderer/engine/ecs`) and successfully wired it into `DemoWorld.ts`.
  - Linked ECS `TransformComponent` positional data to the legacy renderer array, preserving PIXI map rendering.
- **Phase 2 (Audio & Network Wiring) Complete**:
  - Wired `AudioManager` into `DemoWorld.ts` and `PuzzleScene.ts`.
  - Added spatial `menu_select` sounds upon dialogue interactions and `piece_move` step sounds to map movement.
  - Validated that `NetworkManager` is instantiated and connected to the socket backend within `ClientGameEngine`.
- **System Synchronization**: Completely pulled, merged, and stabilized all Git Submodules (`okgame`, `bobsgameonlinejava`, `bobsgameweb`) linking them to the master remote. Tracked newly acquired UI ref engine submodules (`love2d`, `defold`, `phaser`) in `SUBMODULE_DASHBOARD.md`.
- **Documentation**: Incremented version from `2.1.92` to `2.1.93`, logged to `CHANGELOG.md`, updated `ROADMAP.md` ticking off Map Rendering, RPG Demo, and Editor Demos. Provided the user with extensive `[PROJECT_MEMORY]` responses detailing architectural paradigms.
- **Build Checks**: Run `npm run build` to ensure Vite pipeline compiles correctly. Synced all submodules across the tree.

### 🟡 Outstanding Tasks & Next Steps (Handing Over)

**1. Polish & Refine (Phase 4):**
- UI elements and interactions within the Editor Demos need fine-tuning to reach full parity.
- Implement detailed scoring mechanics specific to T-spins, B2B bonuses, and Combo multipliers inside `GameLogic.ts`.

**2. Known Architecture Quirks to Observe:**
- *Do not* use dynamic imports in the `update(dt)` loop. It will flicker.
- *Do not* mutate UI state outside of getters/setters in `BobMenu`.
- PIXI v8 dropped `strokeThickness` and `FillGradient`.

## 🤖 Instructions for Next Agent
1. Read `AGENTS.md`, `ROADMAP.md`, `TODO.md`, `MEMORY.md`, and this `HANDOFF.md`.
2. Choose the next highest priority item in `TODO.md` (e.g., implementing combo displays or T-spins).
3. Bump the version number across all related files and document heavily when committing.
