# Archived Handoff — 2026-04-03 — GPT — Bundle Optimization / Achievement Identity

## Delivered
- centralized achievement profile-name helper
- lazy-loaded secondary shell scenes
- cleaner Vite vendor chunking
- removal of large-chunk warning
- main renderer bundle reduced to ~169 kB
- version bump to `2.1.5`

## Validation
- `npx tsc --noEmit` ✅
- `npm run build` ✅

## Key Insight
The biggest bundle win came from honest lazy-loading of secondary scenes, not from forcing the core gameplay scene into dynamic imports where it was already statically rooted elsewhere.
