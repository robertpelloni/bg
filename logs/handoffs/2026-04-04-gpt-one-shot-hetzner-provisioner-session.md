# Archived Handoff — 2026-04-04 — GPT — One-Shot Hetzner Provisioner

## Delivered
- `scripts/provision-hetzner-backend.sh`
- docs updated to incorporate the one-shot provisioning path
- version bump to `2.1.14` in web repo changes

## Validation
- `bash -n scripts/provision-hetzner-backend.sh` ✅
- `npm run build` ✅

## Key Insight
The backend rollout path is now layered correctly: smoke-test endpoints, provider-neutral runtime, Hetzner ops assets, low-level scripts, and finally a one-shot provisioner. The remaining challenge is infrastructure execution and root-workspace lock contention, not design uncertainty.
