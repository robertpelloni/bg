# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.0.0] - 2026-03-22
### Added
- **Root Documentation:** Established `UNIVERSAL_LLM_INSTRUCTIONS.md`, `VISION.md`, `MEMORY.md`, and `DEPLOY.md`.
- **Agent Protocols:** Created root `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, and `GPT.md` to standardize multi-agent orchestration.
- **Project Structure:** Standardized `VERSION` and `ROADMAP.md` across the entire workspace.

### Changed
- **TypeScript Parity:** Implemented GZip/Base64 JSON serialization in `GameType.ts` to match C++ and Java logic.
- **Instruction Sync:** Updated all sub-project `LLM_INSTRUCTIONS.md` files to reference the root master instructions.

### Fixed
- **Serialization Gaps:** Resolved the misnamed and unimplemented `toBase64GZippedXML` stub in the TypeScript client.

---
*Historical milestones from sub-projects preserved in their respective CHANGELOG.md files.*
