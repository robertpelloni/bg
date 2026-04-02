# VISION: bob's game / OKGame (Omni-Workspace)

## 1. The Ultimate Goal
The vision for **bob's game / OKGame** is to create the most robust, cross-platform, and technologically advanced puzzle game ecosystem in existence. This involves a unified logic core implemented across C++, Java, and TypeScript, enabling seamless multiplayer and global persistence across all devices (Desktop, Web, and Mobile). 

The Omni-Workspace acts as a "Single Source of Truth" where development in one language informs and synchronizes with the others, maintaining 100% behavioral parity.

## 2. Core Pillars

### A. Omni-Logic (The Deterministic Core)
- **1:1 Behavioral Parity:** Every rotation (SRS, NES, GB, SEGA, DTET), every garbage calculation, and every RNG tick must produce identical results across C++, Java, and TypeScript.
- **Deterministic Simulation:** The game engine is designed as a pure-state machine. Given the same seed and input stream, any client on any platform will render an identical frame.
- **Unified Serialization:** Utilizing GZip/Base64 GSON/JSON for state snapshots, allowing a Java server to process a TypeScript client's frame and broadcast it to a C++ client seamlessly.

### B. Technological Excellence & Modernization
- **Modern Standards:**
    - **C++:** SDL3, C++20, and Modern OpenGL (Core Profile).
    - **Java:** Java 21 LTS, LibGDX 1.14.0, and Netty for high-performance TCP.
    - **Web:** Vite, TypeScript 5+, PixiJS v8, and Socket.io.
- **Visual Sophistication:** Deep integration of `projectM` and `MilkDrop` visualizers. Native C++ logic is bridged into Java via Project Panama (Foreign Function API) to ensure zero-compromise performance.
- **Audio Fidelity:** A hybrid audio engine supporting both high-quality PCM (Howler.js) and authentic tracker music (MOD/XM/S3M/IT) via libopenmpt WASM.

### C. Universal Identity & Global Persistence
- **Single Sign-On:** Integrated Facebook and custom account management across all platforms.
- **Cross-Platform Play:** A centralized Java server facilitating real-time matchmaking, high-frequency state sync, and global leaderboards.
- **Steam Integration:** Full utilization of Steamworks (Achievements, Stats, Cloud Saves, Multiplayer) for the native desktop experience.

## 3. Structural Design & Submodules
The monorepo is composed of specialized sub-projects:
- `bobsgameonlinejava/`: The high-performance Java backend and legacy desktop powerhouse.
- `bobsgameweb/`: The modern, zero-install web port (okgame v2.0) designed for bobsgame.com.
- `okgame/`: The original C++ engine, optimized for low-latency native execution.
- `references/`: Over 20+ reference implementations of editors (Aseprite, Tiled, Pixelorama) to inspire our creative toolset.

## 4. Development Philosophy
- **AI-First Orchestration:** Leveraging specialized AI agents (Gemini, Claude, GPT) for continuous development. Gemini handles large-scale analysis, Claude handles architecture/docs, and GPT handles rapid implementation.
- **Self-Documenting:** All logic must be heavily commented, and all project metadata (Roadmap, Todo, Dashboard) must be updated autonomously.
- **Zero-Stop Development:** The project is in a state of "continuous party"—development never stops, regressions are never accepted, and every build is better than the last.
