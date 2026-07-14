# HANDOFF: bob's game Omni-Workspace
**Last Updated**: 2026-07-08
**Version**: 2.1.95

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
