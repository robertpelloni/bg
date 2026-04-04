# Archived Handoff — 2026-04-04 — GPT — DreamHost Backend Host Preparation

## Delivered
- verified static frontend is live on `bobsgame.com`
- verified `/socket.io` on main domain still returns `404`
- added `VITE_SERVER_URL` / `VITE_BIG_DATA_URL` build-time override support
- added Passenger-friendly `server/app.js`
- added `.env.production.example`
- documented dedicated-backend-subdomain deployment recommendation
- version bump to `2.1.9`

## Validation
- `npm run build` ✅
- `https://bobsgame.com` ✅
- `https://bobsgame.com/socket.io/...` ❌ (`404`, expected under current setup)

## Key Insight
The frontend deployment problem is solved. The remaining production gap is specifically backend hosting topology, not static publishing.
