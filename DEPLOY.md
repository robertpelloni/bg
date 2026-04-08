# DEPLOY: Deployment Instructions (v2.1.73)

## Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    Hetzner VPS (5.161.250.43)                │
│                                                              │
│  bobsgame.com          ws.bobsgame.com                       │
│  ├─ nginx (SSL)        ├─ nginx (SSL, reverse proxy)         │
│  ├─ /var/www/          ├─ proxy_pass localhost:6065          │
│  │  bobsgame.com/      ├─ /opt/bobsgameweb/server/           │
│  │  current/           │  ├─ index.js (Socket.io + Express)  │
│  │  ├─ index.html      │  └─ systemd: bobsgameweb-server     │
│  │  └─ assets/         │                                     │
│  └─ Let's Encrypt SSL  └─ Let's Encrypt SSL                  │
└──────────────────────────────────────────────────────────────┘
```

## Prerequisites

1. SSH access to Hetzner VPS (`root@5.161.250.43`)
2. SSH access to backend host (`root@ws.bobsgame.com`)
3. `sshpass` installed (or SSH key configured)
4. Node.js 18+ on the VPS for the backend
5. nginx and certbot installed on the VPS

## Quick Deploy (One Command Each)

### Frontend Deploy
```bash
cd bobsgameweb
# Bump version first!
FRONTEND_HOST=5.161.250.43 FRONTEND_USER=root bash scripts/deploy-frontend-hetzner.sh
```

### Backend Deploy
```bash
cd bobsgameweb
BACKEND_HOST=ws.bobsgame.com BACKEND_FORCE_TAR=1 BACKEND_RESTART=1 bash scripts/deploy-backend-vps.sh
```

**IMPORTANT**: Always use `BACKEND_FORCE_TAR=1` — rsync fails on Windows/Cygwin.

## Step-by-Step Deployment Process

### 1. Build
```bash
cd bobsgameweb
npx vite build    # DO NOT use "npm run build" — git paging file error on Windows
```

### 2. Bump Version
Update version in these 4 files:
- `VERSION.md` — just the version string
- `package.json` — `"version"` field
- `src/renderer/scenes/MainMenuScene.ts` — displayed in main menu
- `server/index.js` — reported by `/healthz`

### 3. Verify Build
```bash
npx tsc --noEmit   # Should show 0 errors (2 pre-existing NDDemoScene errors are ok)
ls dist/renderer/  # Should have index.html + assets/
```

### 4. Deploy Frontend
```bash
FRONTEND_HOST=5.161.250.43 FRONTEND_USER=root bash scripts/deploy-frontend-hetzner.sh
```
This uploads `dist/` contents to `/var/www/bobsgame.com/current/` via scp.

### 5. Deploy Backend
```bash
BACKEND_HOST=ws.bobsgame.com BACKEND_FORCE_TAR=1 BACKEND_RESTART=1 bash scripts/deploy-backend-vps.sh
```
This uploads `server/` via tar-over-SSH and restarts the systemd service.

### 6. Verify Deployment
```bash
# Backend health check
curl -s https://ws.bobsgame.com/healthz
# Expected: {"ok":true,"service":"bobsgameweb-socket-server","version":"2.1.XX",...}

# Frontend check
curl -sI https://bobsgame.com/ | head -1
# Expected: HTTP/1.1 200 OK

# Socket.io check
curl -s "https://ws.bobsgame.com/socket.io/?EIO=4&transport=polling"
# Expected: 0{"upgrades":["websocket"],...}
```

### 7. Commit & Push
```bash
cd bobsgameweb
git add -A
git commit -m "v2.1.XX: description of changes"
git push origin master
```

## Version Numbering Convention

- Format: `MAJOR.MINOR.PATCH` (e.g., `2.1.73`)
- Bump PATCH for each deploy during a session
- Bump MINOR for new features/subsystems
- Bump MAJOR for breaking changes
- Always reference the version in the commit message

## Backend Service Management (on VPS)

```bash
# Check status
systemctl status bobsgameweb-server

# View logs
journalctl -u bobsgameweb-server -f

# Restart
systemctl restart bobsgameweb-server

# Stop/Start
systemctl stop bobsgameweb-server
systemctl start bobsgameweb-server
```

## nginx Configuration

Frontend: `/etc/nginx/sites-available/bobsgame.com`
- Serves static files from `/var/www/bobsgame.com/current`
- SPA fallback (try_files $uri /index.html)
- SSL via Let's Encrypt

Backend: `/etc/nginx/sites-available/ws.bobsgame.com`
- Reverse proxy to `localhost:6065`
- WebSocket upgrade headers for Socket.io
- SSL via Let's Encrypt

## Troubleshooting

### "paging file too small" git error
→ Use `npx vite build` instead of `npm run build`

### rsync fails on Windows
→ Use `BACKEND_FORCE_TAR=1` environment variable

### Backend not responding
→ Check systemd status: `systemctl status bobsgameweb-server`
→ Check nginx: `nginx -t`
→ Check logs: `journalctl -u bobsgameweb-server -n 50`

### Frontend 404
→ Check files exist: `ls /var/www/bobsgame.com/current/`
→ Check nginx config: `nginx -t`

### Git index.lock exists
→ Remove stale lock: `rm -f .git/index.lock`
→ DO NOT remove while git operations are running

## Cross-Platform Builds (Future)

### C++ (okgame)
```bash
cd okgame/build
cmake .. && make
```

### Java (bobsgameonlinejava)
```bash
cd bobsgameonlinejava
./gradlew desktop:dist --no-daemon
```
