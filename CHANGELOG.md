# CHANGELOG: bob's game / OKGame (Omni-Workspace)

## [2.0.3] - 2026-04-01
### Added
- **Map Editor v2.0:** Overhauled the web map editor with a professional UI, full 17-layer support, and real-time tile painting using PixiJS.
- **Tileset & Palette System:** Ported the core 8x8 RPG tile and palette management logic from Java to ensure cross-platform asset parity.
- **Production Asset Pipeline:** Configured `AudioManager` to dynamically fetch assets from the S3 big data URL in production environments.
- **Multiplayer Server Hardening:** Updated the Socket.io server with robust room management, player naming, and automated game starting.
- **Deployment Infrastructure:** Created a `Dockerfile` for the multiplayer server and a comprehensive `DEPLOY.md` guide for `bobsgame.com`.

### Changed
- **Production Readiness:** Fixed several TypeScript type-safety issues and syntax errors to ensure a clean production build.
- **Server Config:** Synchronized server and client addresses for the production domain.

## [2.0.2] - 2026-04-01
### Added
- **Tournament Results Scene:** Implemented a new `TournamentResultsScene` in the web port with bracket visualization and tournament session statistics.
- **Seeded RNG:** Implemented a custom seeded random number generator in `GameLogic.ts` to ensure 100% deterministic parity with the Java/C++ versions and multiplayer synchronization.
- **Advanced Chain Logic:** Ported robust chain-checking algorithms (Horizontal, Vertical, Diagonal, Recursive) from Java to the web port.
- **Special Piece Logic:** Ported support for BOMB, WEIGHT, SUBTRACTOR, and ADDER pieces to `GameLogic.ts`.
- **VS Garbage Scaling:** Implemented difficulty-based garbage scaling and negation logic in the web port.
- **Detailed Documentation:** Massively expanded `VISION.md` into an architectural manifesto and updated `ROADMAP.md` to reflect Phase 3 progress.

### Changed
- **GameLogic Audit:** Completed a line-by-line parity audit of `GameLogic.ts` against `GameLogic.java`, fixing several subtle physics and timing discrepancies.
- **Multiplayer Routing:** Synchronized multiplayer garbage distribution rules (ALL, RANDOM, LEAST_BLOCKS) with the server-side implementation.

---
*Historical milestones from sub-projects preserved in their respective CHANGELOG.md files.*
