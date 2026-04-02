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
