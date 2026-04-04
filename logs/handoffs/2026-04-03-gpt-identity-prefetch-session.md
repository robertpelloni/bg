# Archived Handoff — 2026-04-03 — GPT — Stable Profile IDs / Idle Prefetch

## Delivered
- stable local `profileId` generation for achievement sync
- structured identity payloads for achievement save/load
- server compatibility for profile-keyed snapshot storage with fallback loading
- centralized display-name helpers
- settings visibility for profile ID
- idle prefetching for common lazy-loaded scenes
- version bump to `2.1.6`

## Validation
- `npx tsc --noEmit` ✅
- `npm run build` ✅

## Key Insight
The right long-term split is: **profile ID for persistence**, **display name for presentation**. Once that separation exists, account/auth integration becomes an additive step instead of a rewrite.
