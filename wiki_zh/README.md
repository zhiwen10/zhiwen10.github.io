# YeLab 知识库

欢迎来到 YeLab 知识库 — 本实验室的中央知识库。

> 托管于 Gitee：https://edu.gitee.com/ye-lab/yelab-wiki

## 实验室

- [使命宣言](the-lab/mission-statement.md) — 实验室的宗旨
- [期望](the-lab/expectations.md) — 实验室对你的期望，以及你对实验室的期望
- [人员与联系方式](the-lab/people.md) — 我们是谁
- [实验室计算机](the-lab/computers.md) — 服务器、GPU、存储

## 组织管理

- [组会](organizational/meetings.md) — 日程与纪要存档
- [入职指南](organizational/onboarding.md) — 新成员清单、账户、Git 访问权限
- [日历](organizational/calendar.md) — 共享实验室日历
- [休假](organizational/vacations.md) — 休假政策 <mark>[待办]</mark>
- [采购](organizational/ordering.md) — 如何购买物品 <mark>[待办]</mark>
- [会议](organizational/conferences.md) — 差旅与会议后勤 <mark>[待办]</mark>
- [安全](organizational/safety.md) — 实验室安全联系人及流程 <mark>[待办]</mark>

## 科研

- [遇到问题该问谁](science/expert-list.md) — 专家列表
- [邮件列表](science/mailing-lists.md) — 值得加入的列表
- [活动日历](science/events-calendars.md) — 讲座与研讨会 <mark>[待办]</mark>
- [阅读清单](science/reading-list.md) — 入门论文 <mark>[待办]</mark>

## 实验

- [通用流程](experimental/general.md) — 适用于所有实验的规则 <mark>[待办]</mark>
- [实验方案](experimental/protocols.md) — 实验方案页面索引 <mark>[待办]</mark>
- [数据服务器](experimental/data-server.md) — 数据存放位置及组织方式 <mark>[待办]</mark>
- [数据备份](experimental/data-backup.md) — 备份策略（3-2-1） <mark>[待办]</mark>

## 动物实验

- [动物](animals/README.md) — 动物实验主页（**如不适用请删除本节**）
  - [方案](animals/protocol.md) — 伦理 / IACUC 审批 <mark>[待办]</mark>
  - [订购动物](animals/ordering.md) <mark>[待办]</mark>
  - [饲养管理](animals/husbandry.md) <mark>[待办]</mark>

## 安全与培训

- [必修培训](safety-and-training/README.md) — 谁需要什么，以及如何完成 <mark>[待办]</mark>

## 代码

- [Git 与 Gitee 规范](code/git-gitee.md) — Git 安装与 Gitee 配置、平台策略、仓库规范
- [Python](code/python.md) — 学习 Python 及实验室开发环境 <mark>[待办]</mark>
- [共享仓库](code/shared-repos.md) — yelab0 组织中的内容 <mark>[待办]</mark>
- [流程管道](code/pipelines.md) — 数据处理流程 <mark>[待办]</mark>

## 硬件

- [设备](hardware/README.md) — 实验室硬件清单 <mark>[待办]</mark>

## 职业发展

- [职业](career/README.md) — 研究生院申请、攻读博士、论文发表 <mark>[待办]</mark>

## 经费

- [奖学金与资助](funding/README.md) — 资助机会 <mark>[待办]</mark>

---

## 翻译同步

本仓库是**权威源**。中文翻译位于 [yelab-wiki-zh](https://edu.gitee.com/ye-lab/yelab-wiki-zh) — 请优先在此编辑内容；它们将被同步过去。

`.translation-sync`（仓库根目录）记录了本仓库上次与 yelab-wiki-zh 同步的提交，反之亦然。

## 本网站工作原理

本知识库在 Gitee 的 [ye-lab/yelab-wiki](https://edu.gitee.com/ye-lab/yelab-wiki) 上编辑，并自动发布至 **https://www.yezhiwen.com/wiki/**。

- 推送到 Gitee 的 `main` 分支 — 网站将在约 15 分钟内自动更新。
- 网站仓库 ([zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io), `.github/workflows/sync-wiki.yml`) 中的定时 GitHub Action 每 15 分钟克隆本仓库，将其同步到网站的 `wiki/` 文件夹，并触发站点重建。中文翻译以相同方式同步到 `wiki_zh/`。
- 添加页面：创建 `.md` 文件，并在 `sidebar.md` 中添加对应条目。
- 请勿手动编辑网站仓库中的 `wiki/` — 同步会覆盖它。
