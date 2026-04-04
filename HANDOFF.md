# Handoff — 2026-04-04 — Version 2.1.9

## Agent
GPT

## Session Focus
Proceed from the successful static DreamHost deploy toward the most realistic production backend plan: verify the current hosting constraints, then prepare the codebase for a dedicated production websocket/backend host.

## What I Verified
### Static Frontend Deployment
Confirmed live on DreamHost:
- `https://bobsgame.com` serves the deployed `index.html`
- built JS assets are accessible from the public domain

### Backend Reality Check
Confirmed:
- `/socket.io` on `https://bobsgame.com` returns `404`
- `node` exists on the DreamHost shell (`v12.22.9` observed)
- `passenger-config` and `passenger-status` binaries exist
- Passenger does not appear to be actively running for this current site/app context

Conclusion:
- the static frontend is deployed
- the multiplayer/backend side still needs dedicated hosting/proxy configuration
- the cleanest likely shape is a dedicated subdomain such as `ws.bobsgame.com`

## What I Implemented

### 1. Production Backend Host Override Support
Updated:
- `bobsgameweb/src/shared/Config.ts`

Implemented:
- support for `VITE_SERVER_URL`
- support for `VITE_BIG_DATA_URL`
- fixed stale `APP_VERSION` drift

Result:
- the web build can now be pointed at a dedicated backend host without code edits
- example target: `VITE_SERVER_URL=https://ws.bobsgame.com`

### 2. Passenger-Friendly Server Entrypoint
Added:
- `bobsgameweb/server/app.js`

Purpose:
- provides a simple startup target for DreamHost/Passenger-style Node hosting
- boots the existing Socket.io server via `import './index.js'`

### 3. Production Env Example
Added:
- `bobsgameweb/.env.production.example`

Purpose:
- documents production override values for backend host and asset host
- makes the dedicated-subdomain deployment path much easier to reproduce

### 4. Deployment Documentation Upgrade
Updated:
- `bobsgameweb/DEPLOY.md`

Added:
- explicit recommendation for a dedicated backend subdomain
- DreamHost-specific notes based on the live probe
- concrete production build example using `VITE_SERVER_URL`

## Validation Performed
- `npm run build` in `bobsgameweb` ✅
- live HTTP check against `https://bobsgame.com` ✅
- live Socket.io path check against `https://bobsgame.com/socket.io/...` ❌ (returns `404`, as expected under current hosting shape)

## Recommended Next Steps
1. Create/configure a dedicated backend subdomain such as `ws.bobsgame.com` in DreamHost.
2. Point that subdomain at `~/bobsgame.com/server` as a Node/Passenger app if supported.
3. Build/deploy the frontend with:
   ```bash
   VITE_SERVER_URL=https://ws.bobsgame.com npm run build
   ```
4. Re-deploy static files after that build.
5. Verify Socket.io connectivity on the new host, then retest multiplayer from the web client.

## Constraints Respected
- No processes were killed.
- Static deployment was verified externally.
- Pre-existing dirty submodule working trees in `bobsgameonlinejava` and `okgame` were left untouched.
