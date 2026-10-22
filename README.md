# bg — the bob's game umbrella workspace

`bg` is the master workspace repository for **bob's game**: it ties together every engine implementation of the game plus the porting/consolidation tooling being used to modernize them. Version **2.1.95** (see `VERSION.md`). Default branch: `master`.

> **Alpha workspace.** This is a working developer tree, not a clean distributable repo — it contains logs, local databases, an SDK zip, and bot-session artifacts alongside the code and plans.

## What's in here

**The engines, as git submodules:**

| Submodule | What it is |
|---|---|
| `bobsgameonlinejava/` | The original Java client+server — the 2D MMORPG engine and world |
| `bobsgameweb/` | The TypeScript/PixiJS engine ("okgame") — the current web/desktop build |
| `okgame/` | The C++ engine tree |
| `references/` | Third-party editor/tool repos pinned for reference only (`update = none` — skipped by recursive clones) |

**The porting effort, as scripts and plans:** `port_all.py`, `port_cpp.py`, `port_cpp_2.py`, `port_grid.py` (Java→C++/TS porting), `consolidate_src.py` / `consolidate_v2.py` / `consolidate_v3.py` / `restore_and_consolidate.py` (source consolidation), `c_engine_files.txt` / `java_engine_files.txt` (engine file inventories), and the planning docs `PLAN_PORTING_MODERNIZATION.md` and `PLAN_REFACTORING.md`.

**Project docs:** `VISION.md`, `ROADMAP.md`, `TODO.md`, `SUBMODULE_INVENTORY.md`, `SUBMODULE_DASHBOARD.md`, plus per-assistant instruction files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `GPT.md`) from the bot-assisted development process.

## Getting it

```bash
git clone https://github.com/robertpelloni/bg.git
cd bg
git submodule update --init bobsgameonlinejava bobsgameweb okgame
```

Don't clone `--recursive` blindly: the `references/` submodules are intentionally marked `update = none` and are not needed for development. To work on the game itself, go into the relevant engine submodule (most active: `bobsgameweb/`).

## Status

Active, messy, single-developer + AI-bot workspace. The game itself is Robert Pelloni's long-running project ("bob's game", aka "ok"); this repo is where its codebases are being consolidated and ported, not a release artifact.
