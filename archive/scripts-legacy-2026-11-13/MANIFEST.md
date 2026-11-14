# Legacy root scripts — backup manifest (2026-11-13)

Nondestructive backup only. Originals remain in the workspace root because
[README.md](/README.md) and the porting plans reference them by name.
Nothing here was deleted or moved.

| File | Purpose | Status |
|---|---|---|
| `port_all.py` | Java→C++/TS porting driver | Legacy one-off, kept |
| `port_cpp.py`, `port_cpp_2.py` | C++ port iterations | Legacy, superseded by web engine |
| `port_grid.py` | Grid/puzzle port helper | Legacy one-off, kept |
| `consolidate_src.py`, `consolidate_v2.py`, `consolidate_v3.py` | Source consolidation iterations | Legacy, v3 is latest |
| `restore_and_consolidate.py` | Restore + consolidate helper | Legacy one-off, kept |

Canonical automation now lives in `bobsgameweb/scripts/` (deploy, health
checks, Hetzner provisioning) — see `docs/SCRIPTS_INVENTORY.md`.
