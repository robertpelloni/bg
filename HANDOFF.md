# Handoff — 2026-04-22 — Version 2.1.81

## Agent
Jules

## Session Focus
Phase 3: Interactive Demos - Puzzle Game Demo

## What Was Accomplished

### Puzzle Game Demo
- Successfully connected `BobsGame.ts` native UI menus (`BobMenu`) to execute matches using the actual `GameLogic` engine ported from C++/Java.
- Handled logic instantiation and rendered the grid utilizing `PuzzleRenderer` on the ND canvas.
- Overrode the `update()` loop on `BobsGame` to dynamically fetch user inputs via `InputManager` and assign them directly to `PuzzlePlayer` variables (`UP_HELD`, `ROTATECW_HELD`, etc.).
- Added fallback controls parsing to make sure Esc/X correctly exit or trigger appropriate actions.

## Current State

### What Works ✅
- Compiles cleanly and chunk optimization errors have been resolved for dynamic imports of the puzzle engine properties.
- Opening the game renders the ND, from there you can navigate to Single Player, start a match on any difficulty, and the puzzle board generates dynamically. You can then drop blocks and pause/exit the game back to the menu.

### What Doesn't Work Yet / Next Steps ❌
- **RPG World Demo**: This is the next target for Phase 3. The `ClientGameEngine` is mapped and displays `DemoWorld`, but currently has no actual Map data parsing connected and loaded via `MapManager`.
- **Tournament Demo**: Needs full tournament bracket simulation wiring.
- **ND Console Demo**: Playable mini-games alongside `BobsGame` (Ping, Ramio) remain to be mapped back correctly inside the `NDDemoScene` replacement.

## Constraints & Warnings
- **DO NOT** kill any processes
- **DO NOT** use `npm run build` — use `npx vite build`
- **DO NOT** deploy without `BACKEND_FORCE_TAR=1`
- **DO** bump version in 4 files on every deploy
- **DO** commit and push between features
- **DO** keep going autonomously
