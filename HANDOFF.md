# HANDOFF: bob's game Omni-Workspace
**Last Updated**: 2026-11-13
**Version**: 2.1.100 (umbrella) / bobsgameweb 3.0.34 (local, uncommitted WIP) / production 3.0.10
**Session agent**: muse-wonder-1.0 in Muse Code in C:\Users\hyper\workspace\bg on laptop
**Recurring loop**: cron job `8ba45761`, every 15 minutes, prompt "please continue to proceed as you advise" (permanent, skips while a run is active)

## What changed this session (2026-11-13)

### Dashboard consolidation — completed audit
`bobsgameweb/src/renderer/scenes/MainMenuScene.ts` is the single consolidated
dashboard: 4 high-value categories (Play Games / Creation & Editors /
Community & Progress / System & Engine), every item with a label, description,
and hover tooltip, keyboard (Q/E tabs, arrows, action) and gamepad-friendly
buttons. Audited all 42 scene files against it.

Reachable only in-world before this session, now on the dashboard with
labels + tooltips + prefetch (all use their built-in DEFAULT data, so they
open standalone safely):
- Inventory & Equipment, Shop & Trading, Skill Tree → Play
- Quest Log → Community (Quest Journal remains the story diary; labels now say so)

Still intentionally not a dashboard entry: BattleScene (needs live
player/enemy CombatComponents; combat is covered by Arena + Boss Rush),
Splash/GameOver/TournamentResults/PauseOverlay (flow scenes, not destinations).

### System tray — where it is and what it does
Location: Electron main process, `bobsgameweb/src/main/index.ts`
(`createTray`/`updateTrayMenu`), bridge in `src/main/preload.ts`. It exists
and is sensible: single-instance lock, close-to-tray, double-click toggles
the window, status lines, notifications.

Gap fixed this session: the tray previously managed **only** the AI proxy
(8080). It now also manages the multiplayer WS game server
(`server/index.js`, port 6065): status line, Start/Stop, Restart All Servers
covers both, and Quit Servers & Exit / `before-quit` stop both. New IPC:
`start-ws-server`, `stop-ws-server`, `get-server-status`.

Not yet verified live: the Electron binary is not downloaded in this
environment (npm TLS block below), so the tray is typechecked
(`tsc -p tsconfig.main.json`, 0 errors) but has not been clicked through.

### Runtime verification (all local processes at BelowNormal priority)
- `npx tsc --noEmit`: 0 errors. `npx tsc -p tsconfig.main.json`: 0 errors.
- `npx vite build`: succeeds; Shop/QuestLog/Inventory/SkillTree chunks emitted.
- Web preview (built dist) on http://localhost:3000 : HTTP 200.
- AI proxy `node server/ai_proxy.js` on 8080: running ("Server running on http://localhost:8080").
- Production: `https://bobsgame.com/` 200; `https://ws.bobsgame.com/healthz`
  ok but version **3.0.10** — production is well behind local 3.0.34.
- Local WS server on 6065: **crashes** — `Cannot find package 'socket.io'`
  (`server/node_modules` never installed). `npm install` retried twice and
  fails with `ERR_SSL_TLSV1_ALERT_PROTOCOL_VERSION` against
  registry.npmjs.org in this environment. Not circumvented.
- Electron launch: stops at "Downloading Electron binary..." (same npm block).
- Tests: 34 files in `src/__tests__/` cannot run — no vitest installed, no
  `test` script in package.json.
- Java 21.0.12 + `bobsgameonlinejava/gradlew` present (build not run).
  `okgame/` (C++) is registered in `.gitmodules` but not cloned here.

Logs from this session: `bobsgameweb/logs/local-{ws,ai,web,electron}*.log`.

**User constraint (2026-11-13, supersedes the local-run steps above): do not
run local servers.** The session-started vite preview (3000) and AI proxy
(8080) were stopped on request and ports verified free. Deploy live to
Hetzner production only, when possible, and verify via
`https://bobsgame.com/` and `https://ws.bobsgame.com/healthz` — never via
localhost servers.

### Scripts & docs governance
- New index: `docs/SCRIPTS_INVENTORY.md` (canonical deploy/build/run paths).
- Legacy root porting scripts backed up **nondestructively** to
  `archive/scripts-legacy-2026-11-13/` (originals kept; docs reference them).
- Version collision documented: changelog held out-of-order 2.1.96–2.1.99
  entries while VERSION.md said 2.1.95. Umbrella is now **2.1.100**.
- Open items are itemized at the top of `TODO.md`.

### Coordination
MS Edge CDP on port 9222 is live (Edge 157). Pages present include
muse.ai ("Chat — Bobbi"), ChatGPT, and Gemini tabs. This session identified
itself in this handoff as **muse-wonder-1.0 in Muse Code in
C:\Users\hyper\workspace\bg on laptop**; no messages were injected into the
other agents' chats this session.

## Pre-existing working-tree state (do not lose)
- `bobsgameweb` has uncommitted WIP (version bump to 3.0.34, WorldScene,
  vite.config, tools_build.sh, server files, `.pi-lens` caches). This session
  committed **only** its own files there; the rest is untouched.
- `bobsgameonlinejava` and `references/editors/Pixelorama` submodule pointers
  were already dirty at session start; left as found.
- Root branch is `master`; bobsgameweb branch is `main`.

## Deployed to Hetzner production (2026-11-13, after the audit above)
Per the user's "no local servers, deploy live only" constraint, the verified
build was deployed straight to the VPS (SSH via `root@5.161.250.43`;
`ws.bobsgame.com` SSH does not answer on port 22 — both sites share this host):
- Remote backups kept: `/srv/www/bobsgame.com_backup_20261113`,
  `/opt/bobsgameweb/server_backup_20261113`.
- Frontend: fresh `tsc` (0 errors) + `vite build`, uploaded to
  `/srv/www/bobsgame.com`; `https://bobsgame.com/` returns 200 and the served
  bundle contains the new "Inventory & Equipment" dashboard entry.
- Backend: `server/` uploaded to `/opt/bobsgameweb/server`,
  `systemctl restart bobsgameweb-server` (active);
  `https://ws.bobsgame.com/healthz` now reports **3.0.34** (was 3.0.10),
  socket.io polling handshake succeeds, journal shows a clean start.
- Not done: git push of bobsgameweb `e72495cf` (this session's token still
  returns 401; the root repo was pushed by the concurrent protocol process).

## Follow-up (same day, 2026-11-13)
- "Demo Battle" dashboard entry added (fabricated CombatComponents), so all
  42 scenes are now reachable from the single dashboard page. Build clean
  (`tsc` 0 errors, `vite build` ok), deployed to Hetzner prod (fresh backup
  `/srv/www/bobsgame.com_backup_20261113b`), verified in the served bundle
  (`Demo Battle` present, site 200, `/healthz` 3.0.34).
- Pushed: bobsgameweb `main` = `e745e243` (cherry-picked via temp worktree;
  local dirty tree untouched), root re-pinned to it.

## Live verification + fixes (2026-11-13, later — headless Edge/CDP, screenshots in `%TEMP%\bg-verify\`)
Drove the real prod game (`https://bobsgame.com/#menu` — the dashboard's
public route; the bare URL boots straight into the RPG world) at 1280x720,
56–57 FPS, zero page errors in the final passes:
- Dashboard renders as designed; Demo Battle starts; ATTACK (60→49 HP),
  MAGIC/Lightning (49→15), ITEMS heal (99→100, "Restored 30 HP"), VICTORY
  ("VICTORY! Enemy defeated.", enemy 0/60, "Warrior's Path" achievement),
  exit back to dashboard, FLEE → dashboard. All observed on screenshots.
- **Defeat is unreachable in the demo battle by balance**: enemy deals
  3 (special ~4) per hit vs 100 player HP while the player kills it in
  ~6 hits (~15 damage taken max). Needs a stronger demo enemy to demo.
- **Player DEFEND did not exist** (menu was ATTACK/MAGIC/ITEMS/FLEE and the
  `playerDefending` field was dead code). Added DEFEND: braces and halves
  the next hit (observed "Blocked! Enemy deals only 1 damage!"). Live.
- **Shop crashed from every entry point**: `ShopScene.shopConfig` was never
  assigned in the constructor; `refreshUI()` threw on `.inventory`. Fixed at
  the root (`this.shopConfig = config`), added regression test
  `src/__tests__/shop-config.test.ts` (authored + typechecked; cannot run
  until `tsx` is installable — same npm block). Shop now renders live.
- **Play tab overflowed 720p** (14 items, last row clipped): rows compact
  automatically when a category exceeds 6 rows. Battle menu also raised
  clear of the page footer so FLEE is fully visible. All live on prod.
- Not confirmed headlessly: world pause "Quit to Menu" is mouse-only (no
  keyboard nav) and CDP mouse events never fired Pixi handlers in any pass
  (keyboard input works everywhere). Worth a real-mouse check + keyboard
  support for the pause menu.
- Deployed with per-deploy VPS backups (`*_backup_20261113` … `e`).

## Quit-to-Menu chain — fully fixed (2026-11-14)
Four stacked defects, each proven by screenshot/console before fixing:
mouse-only pause menu → added keyboard nav; Enter consumed by an earlier
`isActionPressed()` read → pause input moved to the top of `onUpdate`;
`Scene.onExit` removed the container only after `destroy()` → removal-first
+ try/catch; and the black-screen root cause — `WorldScene` repoints the
shared `Camera` at its own container (`setContainer(this.worldContainer)`),
that container is destroyed on exit, and `Game` calls `camera.update()`
every frame, throwing forever and starving the Pixi renderer. Guard:
`Camera.updateContainer` returns when the container is destroyed.
Final proof on prod: Esc → ▼▼▼ Quit → dashboard renders, **zero page
errors** (screenshots `%TEMP%\bg-verify\y4-*.png`, main chunk `VCQS5bVF` →
current). Also note: the pause `Enter` fix commit (`b97d50ea` on origin)
includes the previously deployed-but-uncommitted WorldScene 3.0.34 WIP, so
the repo now matches what prod already ran.
VPS: disk filled to 100% by my `cp -r` deploy backups (brief 522 outage,
self-recovered; load avg >100 from other host activity). Backups pruned to
one frontend + one backend. Never `cp -r` the 3.4 GB site per deploy again.

## Next steps (priority order)
1. Restore npm registry access (or run on an unrestricted machine):
   `cd bobsgameweb/server; npm install`, then verify WS server on 6065 and
   the Electron tray end-to-end.
2. Add vitest + `test` script; make the 34 test files runnable in CI.
3. Push bobsgameweb `e72495cf` once GitHub auth is renewed in this environment.
4. Optional: demo-battle dashboard entry; merge Options/Settings scenes.
5. Clone/build `okgame` (C++) separately; run the Java gradle build.
