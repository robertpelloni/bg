# Submodule Dashboard

This document tracks all submodules across the Omni-Workspace, their versions, and locations.

## Project Directory Structure

- `bobsgameonlinejava/`: The Java backend and legacy desktop client for bob's game online.
- `bobsgameweb/`: The modern web port (okgame) built with Vite, TypeScript, and PixiJS.
- `okgame/`: The original C++ client/engine.
- `docs/`: Workspace-level documentation and universal instructions.
- `submodules/`: (If present) Additional shared libraries.

## Submodule Status (Last Updated: 2026-04-01)

| Submodule | Branch/Commit | Location |
| :--- | :--- | :--- |
| bobsgameonlinejava | main (7719d49) | `bobsgameonlinejava` |
| bobcoin | main (98bed79) | `bobsgameonlinejava/bobcoin` |
| aseprite-file | master (06b6189) | `bobsgameonlinejava/libs/aseprite-file` |
| commons-lang | rel/commons-lang-3.20.0-317 (acb1436) | `bobsgameonlinejava/libs/commons-lang` |
| jinput | 2.0.10-140 (208c0fc) | `bobsgameonlinejava/libs/jinput` |
| lwjgl3 | 3.4.1-53 (2ce2b31) | `bobsgameonlinejava/libs/lwjgl3` |
| lz4-java | 1.8.0-13 (be9ce57) | `bobsgameonlinejava/libs/lz4-java` |
| micromod | master (287d8fa) | `bobsgameonlinejava/libs/micromod` |
| mysql-connector-j | 9.6.0 (fdef61f) | `bobsgameonlinejava/libs/mysql-connector-j` |
| twl-lwjgl3 | master (647ec34) | `bobsgameonlinejava/libs/twl-lwjgl3` |
| xpp3 | xpp3-1.1.4c.0-9 (68498e7) | `bobsgameonlinejava/libs/xpp3` |
| xz-java | v1.12-2 (492b6ea) | `bobsgameonlinejava/libs/xz-java` |
| Cytopia | v0.2.1-1158 (b67e255) | `bobsgameonlinejava/references/Cytopia` |
| DTile | master (22a977f) | `bobsgameonlinejava/references/DTile` |
| GrowTools | master (fe146b8) | `bobsgameonlinejava/references/GrowTools` |
| LibreSprite | v1.2-26 (9edb7a6) | `bobsgameonlinejava/references/LibreSprite` |
| OgmoEditor3-CE | 3.4.0-15 (b2a5215) | `bobsgameonlinejava/references/OgmoEditor3-CE` |
| Pixelorama | v1.1.8-99 (07c9925) | `bobsgameonlinejava/references/Pixelorama` |
| PixiEditor | 2.0.1.18-496 (a14776a) | `bobsgameonlinejava/references/PixiEditor` |
| blockbench | v5.1.1 (fc3760d) | `bobsgameonlinejava/references/blockbench` |
| tiled | v1.12.1-11 (b81cec5) | `bobsgameonlinejava/references/tiled` |
| bobsgameweb | master (4967b50) | `bobsgameweb` |
| okgame | 69431-200 (c11c423) | `okgame` |

*(Note: This is a summarized list of major submodules. See `git submodule status --recursive` for the full exhaustive list.)*
