# GitHub Copilot Instructions — Omni-Workspace Root

> **CRITICAL: READ [docs/UNIVERSAL_LLM_INSTRUCTIONS.md](docs/UNIVERSAL_LLM_INSTRUCTIONS.md) FIRST.**

## 1. Role: The Inline Assistant
GitHub Copilot acts as the immediate, line-by-line AI pair programmer. You provide context-aware autocomplete, snippets, and fast inline fixes based on the current active file and its neighbors.

## 2. Copilot-Specific Rules
- **Formatting Match:** Strictly adhere to the casing, bracing, and indentation of the surrounding context
- **Comments:** Add analytical comments explaining what code is doing, why it's there, side effects
- **Context Awareness:** Prioritize symbols and methods defined in the same file or imported headers
- **PixiJS v8:** Use options-object API (roundRect, fill, stroke) — not the legacy v7 API
- **TypeScript:** Use `export type { X }` for type-only exports when `isolatedModules` is enabled

## 3. Project Conventions
- **Barrel exports**: Every engine subsystem has `index.ts` with explicit named exports
- **Import paths**: Use `./SubPanel` (same directory), not `../SubPanel`
- **Naming**: PascalCase for classes/interfaces/enums, camelCase for methods/properties
- **Error handling**: Use try/catch with Logger for non-critical failures
- **Version**: Displayed in MainMenuScene bottom-right, single source of truth in VERSION.md
