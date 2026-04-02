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
| bobcoin | main (d869ca4) | `bobsgameonlinejava/bobcoin` |
| aseprite-file | master (d7d60c8) | `bobsgameonlinejava/libs/aseprite-file` |
| commons-lang | rel/commons-lang-3.20.0-318 (7176e6e) | `bobsgameonlinejava/libs/commons-lang` |
| jinput | 2.0.10-144 (0e81fb4) | `bobsgameonlinejava/libs/jinput` |
| lwjgl3 | 3.4.1-47 (20e17fa) | `bobsgameonlinejava/libs/lwjgl3` |
| lz4-java | 1.8.0-21 (e3c01b3) | `bobsgameonlinejava/libs/lz4-java` |
| micromod | master (953029e) | `bobsgameonlinejava/libs/micromod` |
| mysql-connector-j | 9.6.0-1 (3ab04e1) | `bobsgameonlinejava/libs/mysql-connector-j` |
| twl-lwjgl3 | master (de05f4e) | `bobsgameonlinejava/libs/twl-lwjgl3` |
| Cytopia | v0.2.1-1160 (7e03b16) | `bobsgameonlinejava/references/Cytopia` |
| LibreSprite | v1.2-29 (aa782ad) | `bobsgameonlinejava/references/LibreSprite` |
| OgmoEditor3-CE | 3.4.0-17 (f79af3c) | `bobsgameonlinejava/references/OgmoEditor3-CE` |
| Pixelorama | v1.1.8-59 (b996695) | `bobsgameonlinejava/references/Pixelorama` |
| PixiEditor | 2.0.1.18-482 (fc7f199) | `bobsgameonlinejava/references/PixiEditor` |
| Raylib-Examples | master (387800c) | `bobsgameonlinejava/references/Raylib-Examples` |
| aseprite | v1.3.17-5 (1afaead) | `bobsgameonlinejava/references/aseprite` |
| blockbench | v5.0.7-3 (b376486) | `bobsgameonlinejava/references/blockbench` |
| goxel | v0.15.1-59 (5881c5a) | `bobsgameonlinejava/references/goxel` |
| piskel | v0.1.0-1208 (998c9d7) | `bobsgameonlinejava/references/piskel` |
| tiled | v1.11.2-256 (8ea1b97) | `bobsgameonlinejava/references/tiled` |
| bobsgameweb | master (efc59cc) | `bobsgameweb` |
| okgame | 69431-200 (c11c423) | `okgame` |
| lib/CLove | master (42166e7) | `okgame/lib/CLove` |
| lib/FBNeo | v1.0.0.02-7727 (70b0586) | `okgame/lib/FBNeo` |
| lib/RetroArch | v1.2-45461 (78b3a43) | `okgame/lib/RetroArch` |
| lib/SDL | release-3.4.0-453 (a48dee5) | `okgame/lib/SDL` |
| lib/boost | boost-1.71.0.beta1-4703 (ee4d851) | `okgame/lib/boost` |
| lib/flac | 1.3.1-1106 (c674670) | `okgame/lib/flac` |
| lib/freetype | VER-2-14-3-10 (eebca3e) | `okgame/lib/freetype` |
| lib/glfw | 3.4-93 (fca9f5b) | `okgame/lib/glfw` |
| lib/libpng | v1.6.55-25 (9bb02bb) | `okgame/lib/libpng` |
| lib/lz4-java | 1.8.0-14 (d4969e4) | `okgame/lib/lz4-java` |
| lib/zlib | v1.3.2-1 (9b64db4) | `okgame/lib/zlib` |

*(Note: This is a summarized list of major submodules. See `git submodule status --recursive` for the full exhaustive list.)*
