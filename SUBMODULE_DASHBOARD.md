# Submodule Dashboard & Architecture Tree

**Last Updated:** 2026-04-29

## Overview
This document tracks all external submodules, library dependencies, and integrated porting tools referenced within the *bob's game Omni-Engine* monorepo. It serves as a unified reference map for where C++, Java, and Web logic originate, intersect, or diverge.

---

## 🏗️ Core Codebases

| Submodule | Description | Location | Sync Status | Target Platform |
|-----------|-------------|----------|-------------|-----------------|
| **`okgame`** | Native C++20 engine utilizing SDL3, OpenGL, and raw deterministic loops. Needs vcpkg refactor. | `/okgame` | Active | Win/Mac/Linux |
| **`bobsgameonlinejava`** | Legacy Java 21 engine utilizing LibGDX. Serves as the primary reference map for logic parity. | `/bobsgameonlinejava` | Active | Desktop |
| **`bobsgameweb`** | TypeScript/PixiJS v8 port. Serves as the primary deployment for `bobsgame.com`. | `/bobsgameweb` | Active | Web (HTML5) |

---

## 📚 Integrated Libraries & Reference Submodules

The following tools and libraries are tracked either directly via Git Submodule or through architectural assimilation to ensure the Omni-Engine maintains robust tooling parity.

### 🎨 Sprite & Pixel Art Editors
*To be implemented in `/src/renderer/editor/`*

- [Aseprite](https://github.com/aseprite/aseprite) - Reference for frame sequence logic and color manipulation.
- [Pixelorama](https://github.com/Orama-Interactive/Pixelorama) - Reference for Web-native sprite canvas editing.
- [LibreSprite](https://github.com/LibreSprite/LibreSprite) - Reference for open-source feature parity.
- [PixiEditor](https://github.com/PixiEditor/PixiEditor) - Layer logic and raster generation.
- [Piskel](https://github.com/piskelapp/piskel) - Reference for browser-based real-time animation playback.
- [Tile-Studio](https://github.com/Wiering/Tile-Studio) / [tilemap-studio](https://github.com/Rangi42/tilemap-studio) - Reference for Tile palette rendering and Map arrays.

### 🕹️ Emulation & Compatibility
- **Libretro / JNI** - Java JNI bindings for legacy game ROM compatibility are stored in `/bobsgameonlinejava`. To be ported to WebAssembly for `bobsgameweb`.
- **ProjectM** - Native bindings tracked inside `okgame/lib/projectm`.

### 🔊 Audio & Synthesis
- **Howler.js** - Driving Web Audio API. See `/src/renderer/audio/AudioManager.ts`.
- **Chiptune3.js** - Tracker music fallback for `.mod` and `.xm` files.

### 🌐 Networking
- **Socket.io** - Realtime lobby and meta-state syncing. Node backend located at `bobsgameweb/server/index.js`.
- **WebRTC DataChannels** - High frequency deterministic loop updates across peers. Handled via `PeerConnection.ts`.

---

## 🛠️ Project Structure

```text
/ (Root Monorepo)
├── AGENTS.md                   # AI tooling conventions & rules
├── ROADMAP.md                  # High-level goals & Milestones
├── TODO.md                     # Granular task lists
├── CHANGELOG.md                # Version history
├── VERSION.md                  # Current deployment string
├── SUBMODULE_DASHBOARD.md      # This file
│
├── bobsgameweb/                # Web engine port (Primary Dev Branch)
│   ├── src/renderer/           # TS + PixiJS logic
│   │   ├── engine/             # Core ported systems (ECS, Network, Input)
│   │   ├── scenes/             # Menu states & Views
│   │   └── puzzle/             # BobsGame engine logic
│   └── server/                 # Node.js + Socket.io Lobby backend
│
├── okgame/                     # C++ Native Port
│   ├── src/                    # C++ Logic matching bobsgameweb
│   └── lib/                    # C++ specific libs (ProjectM, SDL3)
│
└── bobsgameonlinejava/         # Java Legacy Port
    ├── src/com/bobsgame/       # Original Java logic
    └── libs/                   # Java specific jars
```

### 🤖 Generative AI Tools
*To be evaluated for integration into generative asset workflows.*

- [Diffusers](https://github.com/huggingface/diffusers) - Stable Diffusion orchestration.
- [Shap-E](https://github.com/openai/shap-e) - Text/image to 3D.
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion) - Text-to-image base model.
- [ControlNet](https://github.com/lllyasviel/ControlNet) - Granular control over diffusion models.
