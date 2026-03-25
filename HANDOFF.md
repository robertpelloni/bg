# HANDOFF: bob's game / OKGame (Omni-Workspace) - March 22, 2026

## 1. Summary of Changes
- **Root Documentation:** Established a unified documentation framework (`UNIVERSAL_LLM_INSTRUCTIONS.md`, `VISION.md`, `MEMORY.md`, `DEPLOY.md`, `ROADMAP.md`, `TODO.md`, `SUBMODULE_DASHBOARD.md`).
- **Agent Protocols:** Created model-specific instructions (`GEMINI.md`, `CLAUDE.md`, `GPT.md`, `copilot-instructions.md`) that all reference the master instructions.
- **Version Sync:** Synchronized all project versions to **2.0.0**.
- **TS Serialization:** Implemented `toBase64GZippedJSON` and `fromBase64GZippedJSON` in `bobsgameweb/src/shared/puzzle/GameType.ts` using native `CompressionStream` APIs to match C++/Java logic.
- **Sub-project Documentation:** Created `IDEAS.md` for both Java and C++ clients and synchronized their `LLM_INSTRUCTIONS.md`.

## 2. Current Status
- **Root:** Ready for 2.0.0 deployment.
- **Java Client:** In progress - modernization and UI (Scene2D/TWL) tasks pending.
- **C++ Client:** In progress - Steam Integration is currently stubbed and needs real SDK binaries.
- **Web Client:** Stable with new parity serialization logic.

## 3. Blockers & Roadblocks
- **Git Push:** Failed due to interactive authentication requirements. Changes are committed locally but not pushed to origin.
- **Submodule Sync:** `lib/brotli` in `okgame` and `bobcoin` recursive updates are failing due to missing refs or URLs. Manual synchronization is required for deep-nested dependencies.

## 4. Next Steps
1.  **Steam Integration:** Focus on `okgame/src/Utility/SteamManager.cpp`. Replace stubs with real Steamworks SDK v1.64 logic.
2.  **Java Modernization:** Continue refactoring `bobsgameonlinejava` core logic to Java 21 standards.
3.  **UI Polish:** Wire up the commented-out Steam UI features in the C++ lobby.
4.  **Submodule Cleanup:** Systematically fix the broken submodule mappings identified in this session.

## 5. Deployment Notes
Refer to `DEPLOY.md` for the current multi-platform strategy. Ensure Java 21 is used for the Java build.
