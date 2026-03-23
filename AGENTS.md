# AGENTS Instructions — Omni-Workspace Root

> **CRITICAL: READ [docs/UNIVERSAL_LLM_INSTRUCTIONS.md](docs/UNIVERSAL_LLM_INSTRUCTIONS.md) FIRST.**

## 1. Agent Overview
This workspace is a multi-agent orchestration environment. Agents must follow the protocols defined in the universal instructions.

## 2. Multi-Agent Collaboration
- **Gemini CLI:** Performance, large context operations, and workspace-wide synchronization.
- **Claude:** Architecture, planning, and documentation.
- **GPT:** Specific implementation details, unit tests, and algorithms.
- **Google Jules:** Continuous development and branch maintenance.

## 3. Key Protocols
- **Atomic Commits:** Every build results in a version bump and a commit.
- **Handoff:** Every session ends with a detailed `HANDOFF.md`.
- **Single Source of Truth:** `VERSION` and `docs/UNIVERSAL_LLM_INSTRUCTIONS.md`.

## 4. Model-Specific Files
- [GEMINI.md](GEMINI.md)
- [CLAUDE.md](CLAUDE.md)
- [GPT.md](GPT.md)
- [copilot-instructions.md](copilot-instructions.md)
