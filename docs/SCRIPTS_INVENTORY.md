# Scripts inventory (2026-11-13)

Single index for every script in the umbrella workspace, so nothing is
hunted for again. Canonical entry points are listed first.

## Canonical (use these)

| Script | What it does |
|---|---|
| `bobsgameweb/scripts/deploy-frontend-hetzner.sh` | Deploy built frontend to Hetzner VPS |
| `bobsgameweb/scripts/deploy-backend-vps.sh` | Deploy backend (`BACKEND_FORCE_TAR=1` on Windows) |
| `bobsgameweb/scripts/deploy-with-rollback.sh` | Deploy with rollback (`npm run deploy:hetzner`) |
| `bobsgameweb/scripts/verify-production-stack.sh` | Post-deploy production verification |
| `bobsgameweb/scripts/check-production-frontend.sh` / `check-production-runtime-chunks.sh` / `check-production-editor.sh` | Production frontend checks |
| `bobsgameweb/scripts/check-backend-host.sh`, `collect-backend-diagnostics.sh`, `tail-backend-logs.sh` | Backend diagnostics |
| `scripts/generate-distro.cjs` (root) | Distro generation helper |

## Build & run (local)

```powershell
cd bobsgameweb
npx vite build            # NOT "npm run build" (Windows git paging error)
npx vite preview --port 3000
node server/index.js      # WS game server, port 6065 (needs server/npm install first)
node server/ai_proxy.js   # AI proxy, port 8080
```

All heavy local processes should run at BelowNormal priority:
`(Get-Process -Id $PID).PriorityClass = 'BelowNormal'` in the launching shell.

## Legacy root scripts

`port_*.py`, `consolidate_*.py`, `restore_and_consolidate.py`, plus small
helpers (`check_braces.py`, `remove_bom.py`, `remove_duplicates.py`) are
one-off porting/consolidation tools from the engine-port era. Backed up to
`archive/scripts-legacy-2026-11-13/` (see its `MANIFEST.md`); originals stay
in place because docs reference them. Do not extend them — new automation
belongs in `bobsgameweb/scripts/`.

## Known gap

`bobsgameweb/src/__tests__/` holds 34 test files but no test runner is
installed and `package.json` has no `test` script, so the suite cannot run
until vitest (or equivalent) is added. Tracked in `TODO.md`.
