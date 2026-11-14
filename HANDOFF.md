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

## Next steps (priority order)
1. Restore npm registry access (or run on an unrestricted machine):
   `cd bobsgameweb/server; npm install`, then verify WS server on 6065 and
   the Electron tray end-to-end.
2. Add vitest + `test` script; make the 34 test files runnable in CI.
3. Deploy bobsgameweb 3.0.34+ to Hetzner (production still on 3.0.10).
4. Optional: demo-battle dashboard entry; merge Options/Settings scenes.
5. Clone/build `okgame` (C++) separately; run the Java gradle build.
