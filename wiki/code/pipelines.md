# Pipelines

Data processing pipelines used in the lab.

| Pipeline | Input → output | Repo | Maintainer |
|---|---|---|---|
| {{PIPELINE_1}} | {{INPUT}} → {{OUTPUT}} | {{REPO_LINK}} | {{NAME}} |

## Requirements for any pipeline

- Config files, not magic constants in code
- Record the git commit hash with every result
- Experiment tracking: {{EXPERIMENT_TRACKING}} — e.g. wandb / mlflow / plain logs
- Raw data stays read-only; pipelines write derived data — see [data server](../experimental/data-server.md)
