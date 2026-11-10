# HANDOFF: bob's game Omni-Workspace
**Last Updated**: 2026-07-08
**Version**: 2.1.96

## Session Overview & Structural Shifts
- **Omni-Engine Dashboard Consolidation**:
  - `MainMenuScene.ts` in `bobsgameweb` had several functional RPG and progression scenes unreferenced in its navigation grid.
  - Wired `ShopScene` (Item Shop & Merchant), `InventoryScene` (Equipment & Inventory), `QuestLogScene` (Quest Log & Trackers), and `SkillTreeScene` (Skill Tree & Abilities) into the unified menu system.
  - Added rich tooltips, action dispatches, and prefetching for all new entries.
- **Asset Cleanups & Vite Build Warnings**:
  - Eliminated Vite public folder warning during `LegacyMapLoader` dynamic doors import by copying `data/doors.json` to `bobsgameweb/src/data/doors.json` and cleanly importing it.
- **Workflow & Server Script Consolidation**:
  - Created `scripts/run-servers.sh` supporting `start`, `stop`, `restart`, and `status` for background dev services (Vite server on port 3000, AI Proxy on port 8080).
  - Created `scripts/build-all.sh` to handle dependencies, asset verification, and web building.
  - Archived one-off conversion scripts into `archive/scripts/` and `archive/bobsgameweb/` nondestructively.
- **Automated Verification**:
  - Created Python test runner tool `/home/jules/self_created_tools/test_runner.py` verifying all 35 test suites (100% pass rate).
  - Verified frontend UI visual output with Playwright across all 4 dashboard categories.

## Multi-Repo Synchronization — Complete

### Repositories Synced

| Repo | Status | Notes |
|---|---|---|
| **bg** (parent) | v2.1.95 ✅ | Submodule pointers updated |
| **bobsgameweb** | v3.0.26 ✅ | main branch synced, collision fixes, Wasm/WebGPU/AI merged |
| **bobsgameweb/submodules/bobui** | main ✅ | Merged feature/audio-graph-native-linking-test (Go oscilloscope) |
| **bobsgameonlinejava** | main ✅ | Submodule refs synced, upstream pulled |
| **bobsgameonlinejava/bobcoin** | main ✅ | All feature branches already merged (0 unique commits) |

### Feature Branches Processed

| Branch | Action |
|---|---|
| `bobsgameweb/jules-3-0-10-sanitization-and-editor-updates` | Already merged (0 unique vs main) |
| `bobsgameweb/jules-3-0-9-engine-sync` | Already merged (0 unique vs main) |
| `bobsgameweb/jules-port-legacy-engines` | Already merged (0 unique vs main) |
| `bobui/feature/audio-graph-native-linking-test` | **Merged into main** ✅ |
| `bobui/bqt-renaming-and-audio-graph` | Already merged (0 unique vs main) |
| `bobcoin/jules-11361461399368937485` | Already merged (0 unique vs main) |
| `bobcoin/jules-7611463505171352863` | Already merged (0 unique vs main) |
| `bobcoin/dependabot/go_modules` | Already merged (0 unique vs main) |

### Production Fix
- **bobsgame.com SSL certificate expired** — Renewed via certbot, webroot path corrected from `/var/www/bobsgame.com/current` → `/srv/www/bobsgame.com`, cert valid until **Oct 6 2026**

### Next Steps
1. Deploy bobsgameweb v3.0.26 build to Hetzner production
2. Set up auto-renewal monitoring for Let's Encrypt certs
3. Resolve nested submodule clone issues (juce, ultimatepp are large upstream repos)
