# SUBMODULE DASHBOARD: Omni-Workspace

## 1. Project Structure Overview
The Omni-Workspace consists of three core repositories facilitating cross-platform parity:

| Repository | Path | Role | Version |
| --- | --- | --- | --- |
| **bobsgameonlinejava** | `bobsgameonlinejava/` | Java (LibGDX) Client & Editor | 2.0.0 |
| **okgame** | `okgame/` | C++ (SDL3) Reference Implementation | 2.0.0 |
| **bobsgameweb** | `bobsgameweb/` | TypeScript (Vite/PixiJS) Web Client | 2.0.0 |

## 2. Core Dependencies & Submodules (Recursive)

### A. C++ Logic & Visualizers (`okgame/lib/`)
- `lib/projectm`: Core visualizer engine.
- `lib/MilkDrop3`: MilkDrop3 implementation.
- `lib/SDL3`: (Linked dependency) Core engine framework.
- `lib/Poco`: (Linked dependency) Networking stack.

### B. Java Libraries (`bobsgameonlinejava/libs/`)
- `libs/lwjgl3`: Lightweight Java Game Library.
- `libs/twl-lwjgl3`: UI framework for LWJGL.
- `libs/mysql-connector-j`: Database connectivity.

### C. Reference Assets & Tools (`bobsgameonlinejava/references/`)
- `references/aseprite`: Pixel art tool reference.
- `references/blockbench`: 3D modeling reference.
- `references/tiled`: Tilemap editor reference.

## 3. Maintenance Protocols
Run the following to ensure all submodules are synchronized:
```powershell
# Recursive update and sync
git submodule update --init --recursive
python scripts/update_repos_v5.py
```

---
*Dashboard generated on March 22, 2026.*
