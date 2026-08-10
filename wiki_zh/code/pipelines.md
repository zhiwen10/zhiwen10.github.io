# 流水线

实验室使用的数据处理流水线。

| 流水线 | 输入 → 输出 | 仓库 | 维护者 |
|---|---|---|---|
| {{PIPELINE_1}} | {{INPUT}} → {{OUTPUT}} | {{REPO_LINK}} | {{NAME}} |

## 对所有流水线的要求

- 使用配置文件，不要在代码中写魔法常量
- 每次产生结果时记录对应的 git commit 哈希
- 实验跟踪：{{EXPERIMENT_TRACKING}} —— 例如 wandb / mlflow / 普通日志
- 原始数据保持只读；流水线写入派生数据 —— 参见[数据服务器](../experimental/data-server.md)
