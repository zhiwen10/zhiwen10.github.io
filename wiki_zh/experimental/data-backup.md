# 数据备份

## 一句话原则

**代码存放在 Gitee 上的 git 中。数据存放在服务器上。所有重要内容至少有 3 份副本，保存在 2 种不同的介质上，其中 1 份异地保存（3-2-1 原则）。**

## 代码

- 所有代码都在 git 中，推送到 **yelab0** Gitee 组织——见 [Git 与 Gitee 规范](../code/git-gitee.md)
- 永远不要把代码的唯一副本放在某台服务器或笔记本上
- 大型数据、模型权重和结果**不要**放进 git

## 数据

| 内容 | 主副本 | 备份副本 | 异地副本 | 频率 |
|---|---|---|---|---|
| 原始实验数据 | {{SERVER_1}} | {{BACKUP_TARGET}} | {{OFFSITE}} | {{FREQUENCY}} |
| 衍生数据 / 结果 | {{PATH}} | {{BACKUP_TARGET}} | {{OFFSITE_OR_REBUILDABLE}} | {{FREQUENCY}} |

- 备份工具：{{BACKUP_TOOL}}——例如 rsync 定时任务、快照
- 恢复已验证：{{RESTORE_TEST_POLICY}}——例如由谁检查、多久检查一次
- {{BACKUP_POLICY_NOTES}}
