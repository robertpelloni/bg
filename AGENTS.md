# AGENTS Instructions — Omni-Workspace Root

> **CRITICAL: READ [docs/UNIVERSAL_LLM_INSTRUCTIONS.md](docs/UNIVERSAL_LLM_INSTRUCTIONS.md) FIRST.**

## 1. Agent Overview
This workspace is a multi-agent orchestration environment. All agents (Gemini, Claude, GPT, Copilot, Jules) must follow the core protocols defined in the universal instructions.

## 2. Multi-Agent Collaboration & Handoff
- **Gemini CLI:** Performance, large context operations, workspace-wide synchronization, and deep codebase analysis.
- **Claude:** Architecture, planning, system-wide design, and maintaining extreme-detail global documentation.
- **GPT:** Specific implementation details, unit tests, fast coding, and autonomous algorithmic execution.
- **Google Jules:** Continuous development, branch maintenance, and periodic sweeping updates.

## 3. Model-Specific Overrides
Do not duplicate instructions. Refer to the model-specific files for unique capabilities and rules:
- [GEMINI.md](GEMINI.md)
- [CLAUDE.md](CLAUDE.md)
- [GPT.md](GPT.md)
- [copilot-instructions.md](copilot-instructions.md)

## 4. Version Management Protocol
- **Single source of truth**: `VERSION.md` contains only the version string (e.g., `2.1.73`)
- **Bump on every deploy**: Update `VERSION.md`, `package.json`, `MainMenuScene.ts`, `server/index.js`
- **Commit message**: Must reference version number (e.g., `v2.1.73: description`)
- **Changelog**: Every version bump gets an entry in `CHANGELOG.md`
- **Display**: Version is shown in the main menu UI (bottom-right corner)

## 5. Documentation Protocol
- **Session start**: Read AGENTS.md, VISION.md, MEMORY.md, ROADMAP.md, TODO.md, HANDOFF.md
- **During**: Update docs when making significant changes
- **Session end**: Update HANDOFF.md, MEMORY.md, ROADMAP.md, TODO.md, CHANGELOG.md
- **Quality**: Documentation must be in "FULL extreme detail" — comprehensive, thorough, actionable

## 6. Deployment Protocol
- See [DEPLOY.md](DEPLOY.md) for complete deployment instructions
- Always use `BACKEND_FORCE_TAR=1` for backend deploys
- Use `npx vite build` (not `npm run build`) to avoid Windows git errors
- Verify deployment with health checks before proceeding

## 7. Safety Rules
- **DO NOT** `taskkill` any processes — this kills active sessions
- **DO NOT** force push or overwrite working code
- **DO** merge intelligently, preserving all features
- **DO** commit and push regularly between features
- **DO** keep going autonomously without pausing for confirmation
