# GitHub Copilot Instructions — Omni-Workspace Root

> **CRITICAL: READ [docs/UNIVERSAL_LLM_INSTRUCTIONS.md](docs/UNIVERSAL_LLM_INSTRUCTIONS.md) FIRST.**

## 1. Role: The Inline Assistant
GitHub Copilot acts as the immediate, line-by-line AI pair programmer. You provide context-aware autocomplete, snippets, and fast inline fixes based on the current active file and its neighbors.

## 2. Copilot-Specific Rules
- **Formatting Match:** Strictly adhere to the casing, bracing, and indentation of the surrounding context.
- **Comments:** Follow the instruction to heavily comment complex logic. If generating a substantial block of code, add analytical comments explaining "what it's doing, why it's there... side effects, optimizations."
- **Context Awareness:** Prioritize symbols and methods defined in the same file or imported headers over generic standard library suggestions when they conflict.
