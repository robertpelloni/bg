# Session Handoff

## Date: 2026-04-01
## Agent: Gemini CLI (Architect & Analyst)

### Summary of Actions
1. **Global Documentation Overhaul:**
   - Evaluated the workspace against massive new user steering instructions.
   - Initialized and updated the Omni-Workspace documentation including `VERSION.md`, `CHANGELOG.md`, `TODO.md`, and created `SUBMODULE_DASHBOARD.md` to map the 30+ nested submodules and reference projects.
   - Rewrote all model-specific instructions (`GEMINI.md`, `CLAUDE.md`, `GPT.md`, `AGENTS.md`, `copilot-instructions.md`) to explicitly reference `docs/UNIVERSAL_LLM_INSTRUCTIONS.md` as the single source of truth.
   - Bumped root version to `2.0.1`.

2. **Web Port Parity (`bobsgameweb`):**
   - Conducted an investigation into the `bobsgameweb` port to determine what is missing for 100% functionality and parity with the Java server.
   - Identified that `BobNet.ts` was missing critical packet constants and `toBase64GZippedGSON` / `fromBase64GZippedGSON` serialization methods required to speak to the Java backend.
   - Installed `pako` and implemented the missing serialization methods in `BobNet.ts`.
   - Identified that `server/index.js` (the Node Socket.io server) is currently acting as the web multiplayer backend, bypassing the Java server.
   - Implemented "Tournament Bracket" visual tree rendering in `LobbyScene.ts` and added tournament room filtering support in `server/index.js`.
   - Confirmed `npm run build` succeeds and committed the new UI features.

### Unfinished Work / Next Steps (See `TODO.md` for full list)
- **Audio Engine (Tracker Music):** The `AudioManager.ts` currently uses `howler.js` which does not natively support MOD/XM/IT tracker files. A WebAssembly port of libopenmpt (like `chiptune2.js`) must be integrated to achieve audio parity with the original Java game.
- **Backend Architecture Decision:** A decision must be made whether to rewrite the `GameServerTCP.java` logic in the Node Socket.io server, OR to create a WebSocket-to-TCP proxy to allow the web client to connect directly to the existing robust Java server.
- **Puzzle Logic Audit:** A line-by-line parity check of `src/shared/puzzle` against the Java implementation is still pending.
- **Editor:** Port `EditorMain.java` capabilities to the web port.

### Advice for Next Model (Claude / GPT)
- **Claude:** Review the `TODO.md` and formulate a concrete plan for the Audio Engine tracker music integration. Consider whether we should use `libopenmpt` via WASM.
- **GPT:** Pick up the `Audio Engine` or `Puzzle Logic` task from `TODO.md`. Use `grep_search` and `codebase_investigator` heavily as the directory structure is deeply nested and spans multiple languages (Java, TypeScript, C++).

---
*End of Handoff.*
