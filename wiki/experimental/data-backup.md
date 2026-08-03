# Data backup

## Policy in one line

**Code lives in git on Gitee. Data lives on the servers. Everything important exists in at least 3 copies, on 2 different media, with 1 off-site (the 3-2-1 rule).**

## Code

- All code is in git, pushed to the **yelab0** Gitee org — see [Git & Gitee policy](../code/git-gitee.md)
- Never keep the only copy of code on a server or laptop
- Large data, model weights, and results do **not** go in git

## Data

| What | Primary copy | Backup copy | Off-site copy | Frequency |
|---|---|---|---|---|
| Raw experimental data | {{SERVER_1}} | {{BACKUP_TARGET}} | {{OFFSITE}} | {{FREQUENCY}} |
| Derived data / results | {{PATH}} | {{BACKUP_TARGET}} | {{OFFSITE_OR_REBUILDABLE}} | {{FREQUENCY}} |

- Backup tooling: {{BACKUP_TOOL}} — e.g. rsync cron job, snapshots
- Restore is tested: {{RESTORE_TEST_POLICY}} — e.g. who checks, how often
- {{BACKUP_POLICY_NOTES}}
