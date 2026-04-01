# Omni-Workspace Roadmap: bob's game / OKGame

## Status: Active Development
**Current Version:** 2.0.0

## 1. Documentation & Standards (March 2026)
- [x] Establish root `UNIVERSAL_LLM_INSTRUCTIONS.md`.
- [x] Synchronize all sub-project instructions.
- [x] Create root `VISION.md`, `MEMORY.md`, and `DEPLOY.md`.
- [x] Maintain `SUBMODULE_DASHBOARD.md`.

## 2. Platform Parity (Ongoing)
- [x] **TS Serialization:** Bridge the gap in XML/GZip handling between Web and Desktop clients.
- [x] **Steam Polish:** Move C++ Steam integration from stubbed to fully functional.
- [x] **Tournament Mode:** Implemented automated server-side bracket generation (Java) and visual tree rendering (C++).
- [ ] **Build Validation Recovery:** Fresh `okgame` configure has been restored in `build_recheck_poco4`; finish the native `bobsgame` compile/link pass so recent C++ work is fully validated again.

## 3. Java Client Evolution
- [x] **Scene2D Modernization:** Established basic Scene2D dialog infrastructure and `GUIManager` integration.
- [ ] Refactor legacy core logic to modern Java 21 standards, starting with puzzle-engine feature parity against the C++ client.
- [ ] Refine the Undo/Redo system.

## 4. Future Goals
- **Mobile Deployment:** Established Capacitor foundation for Web; test actual iOS/Android builds.
- **Modding:** Advanced Lua hooks and creative tools beyond the current grid/piece/map bindings. Finalized per-frame update hook.
