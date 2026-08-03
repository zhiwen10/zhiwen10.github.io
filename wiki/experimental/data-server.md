# Data server

Experimental data lives on the lab servers, not in git and not (only) on local machines.

## Servers

| Server | Mount / path | Purpose |
|---|---|---|
| {{SERVER_1}} | {{DATA_PATH}} | Raw + derived data |
| {{SERVER_2}} | {{PATH}} | {{PURPOSE}} |

Server hardware and access: see [lab computers](../the-lab/computers.md).

## Layout and conventions

- Raw data is **read-only**. Processing writes derived data to a separate location
- Every dataset directory gets a short `README.md`: source, date, format, who generated it
- Naming: {{DATA_NAMING}} — conventions for experiments/runs
- Data lives in {{DATA_PATH}}, never in git — Gitee repos have size limits

Backups: see [data backup](data-backup.md).
