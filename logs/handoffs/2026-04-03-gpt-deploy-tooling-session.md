# Archived Handoff — 2026-04-03 — GPT — DreamHost Deploy Attempt / Tooling Upgrade

## Delivered
- real DreamHost SSH attempt against provided host/user/password
- confirmed host reachability
- confirmed password-auth failure blocker
- upgraded bash deploy script with `scp` fallback + env controls
- added PowerShell deploy script
- rewrote deploy documentation with practical next steps
- version bump to `2.1.8`

## Validation
- `npm run build` ✅
- SSH host reachable ✅
- Password login ❌ (`Permission denied (publickey,password)`)

## Key Insight
At this point deployment is blocked more by remote auth state than by local tooling. The highest-leverage improvement is SSH key setup, not more shell scripting.
