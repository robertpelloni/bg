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
- [ ] **Build Validation Recovery:** Fresh `okgame` configure has been restored in `build_recheck_poco4`; finish the native `bobsgame` compile/link pass so recent C++ work is fully validated again.
- [ ] **Network Convergence:** Standardize low-level networking where platform constraints allow.
- [ ] **Websocket Lobby Parity:** Bring the native websocket lobby flow closer to the web client by exposing room options (`name`, `privacy`, `gameMode`, `startLevel`) and ensuring room creation/join/start events drive the native puzzle scene cleanly.

## 3. Java Client Evolution
- [ ] Refactor legacy core logic to modern Java 21 standards, starting with puzzle-engine feature parity against the C++ client.
- [ ] Implement TWL-based UI components for enhanced desktop experience.
- [ ] Refine the Undo/Redo system.

## 4. Future Goals
- **Tournament Mode:** Automated server-side brackets.
- **Mobile Deployment:** iOS/Android via LibGDX or Capacitor.
- **Modding:** Advanced Lua hooks and creative tools beyond the current grid/piece/map bindings.
