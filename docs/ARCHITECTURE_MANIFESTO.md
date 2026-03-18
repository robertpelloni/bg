# Omni-Workspace Architecture Manifesto: bob's game / OKGame

## Vision
To create a truly unified, cross-platform puzzle game ecosystem where C++, Java, and TypeScript clients share identical game logic, participate in synchronized multiplayer matches, and contribute to a global leaderboard system.

## 1. Core Architecture
The project is structured as an "Omni-Workspace" containing three distinct platform forks and a centralized server:

### A. The Puzzle Engine (Source of Truth)
- **Reference Implementation:** C++ (`okgame/src/Puzzle/`)
- **Parity Forks:**
  - Java (`bobsgameonlinejava/src/main/java/com/bobsgame/puzzle/`)
  - TypeScript (`bobsgameweb/src/shared/puzzle/`)
- **Key Principle:** 1:1 Behavioral Parity. All mechanics, from rotation systems to garbage timing, must be identical across all three languages to ensure deterministic multiplayer results.

### B. Subsystems
- **Audio:** Powered by `SDL3_mixer` in C++ and `LibGDX Audio` in Java. Specialized post-mix callbacks provide raw PCM data to visualizers.
- **Rendering:**
  - **C++:** SDL3 + Modern OpenGL Core Profile (3.3+).
  - **Java:** LibGDX 1.14.0 (OpenGL ES 2.0/3.0).
  - **Web:** WebGL via Vite/TypeScript.
- **UI:**
  - **C++:** Custom native `BobMenu` framework + legacy GWEN integration.
  - **Java:** Modern LibGDX `Scene2D` UI system.
  - **Web:** HTML5 Overlay + Canvas-based rendering.

## 2. Unified Networking (The Sync Protocol)
Multiplayer is facilitated by a centralized Node.js `socket.io` server (`bobsgameweb/server/`).

### A. Frame Synchronization
- **Frequency:** 12Hz (every 5 frames at 60FPS).
- **Format:** Unified JSON state snapshots via `getState()` and `applyState()`.
- **Payload:** Contains grid contents (compressed color IDs), active piece position/rotation, score, level, and player state.

### B. Matchmaking
- **Room Lifecycle:** Create -> List -> Join -> Sync -> Start.
- **Features:** Password protection, hidden private rooms, game mode selection (Marathon, Sprint, Ultra), and starting level synchronization.

## 3. Persistent Global Identity
- **Leaderboards:** Centralized `leaderboards.json` on the server, tracking Top 10 scores per mode across all platforms.
- **User Stats:** Reported via secure POST/WebSocket events upon game completion.
- **Steamworks:** Official SDK v1.64 integrated into the C++ client for achievements and (planned) Cloud Save synchronization.

## 4. Build Standards
- **C++:** CMake-based build with strictly linked submodules (Poco, SDL3, projectM, Steamworks).
- **Java:** Gradle-based build targeting Java 21 LTS with `--no-daemon` constraints for CI efficiency.
- **Web:** Vite + TypeScript for high-speed development and production bundling.

## 5. Development Philosophy
- **Autonomous Progress:** Leveraging AI agents to maintain parity across languages.
- **Zero-Regression Mandate:** Every milestone requires verified successful builds on all three platforms.
- **Code Portability:** Shared logic (like the Puzzle Engine) is designed to be easily translatable, avoiding language-specific features that hinder parity.

---
*Documented on March 18, 2026.*
