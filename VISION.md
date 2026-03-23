# VISION: bob's game / OKGame (Omni-Workspace)

## 1. The Ultimate Goal
The vision for **bob's game / OKGame** is to create the most robust, cross-platform, and technologically advanced puzzle game ecosystem in existence. This involves a unified logic core implemented across C++, Java, and TypeScript, enabling seamless multiplayer and global persistence across all devices (Desktop, Web, and Mobile).

## 2. Core Pillars

### A. Unified Logic (The Deterministic Core)
- 1:1 behavioral parity across all programming languages.
- Identical mechanics (rotation systems, garbage timing, scoring) to ensure deterministic outcomes in cross-platform play.
- Unified JSON state snapshots for frame-perfect synchronization.

### B. Technological Excellence
- **Modern Standards:** SDL3, Java 21, LibGDX 1.14.0, Vite, TypeScript, and Modern OpenGL (Core Profile).
- **High Performance:** Optimized rendering loops, low-latency networking (socket.io), and efficient memory management (shared pointers).
- **Visual Sophistication:** Full integration of `projectM` and `MilkDrop` visualizers with modernized shaders.

### C. Seamless Multiplayer & Persistence
- A centralized server facilitating real-time matchmaking, high-frequency state sync, and global leaderboards.
- Cross-platform identity and stats tracking.
- Steam Integration (Achievements, Cloud Saves, Multiplayer) for the C++ client.

## 3. The Future Roadmap
- **Mobile Expansion:** Deployment to iOS and Android via Java (LibGDX) or Web (Capacitor).
- **Advanced Scripting:** Enhanced Lua scripting capabilities for game logic and mods.
- **Tournament Orchestration:** Automated bracket systems and server-side tournament management.
- **Creative Tools:** Integrated editors for maps, sprites, and visualizer presets.

## 4. Development Philosophy
- **Autonomy:** Leveraging specialized AI agents (Gemini, Claude, GPT) for continuous development and maintenance.
- **Self-Healing:** A robust CI/CD and self-documenting infrastructure.
- **Zero-Regression:** Mandated build validation across all platforms for every milestone.
