# YeLab Wiki

欢迎来到 YeLab wiki — 实验室的中央知识库。

> 托管于 Gitee：https://gitee.com/ye-lab/yelab-wiki

## 实验室

- [使命宣言](the-lab/mission-statement.md) — 实验室的宗旨
- [期望](the-lab/expectations.md) — 实验室对你的期望，以及你对实验室的期望
- [人员与联系方式](the-lab/people.md) — 我们是谁
- [实验室电脑](the-lab/computers.md) — 服务器、GPU、存储

## 组织架构

- [组会](organizational/meetings.md) — 日程与纪要存档
- [入职引导](organizational/onboarding.md) — 新成员清单、账户、git 权限
- [日历](organizational/calendar.md) — 共享实验室日历
- [休假](organizational/vacations.md) — 休假政策 <mark>[待办]</mark>
- [采购](organizational/ordering.md) — 如何购买物品 <mark>[待办]</mark>
- [会议](organizational/conferences.md) — 差旅与会议后勤 <mark>[待办]</mark>
- [安全](organizational/safety.md) — 实验室安全联系人与流程 <mark>[待办]</mark>

## 科研

- [该向谁请教什么](science/expert-list.md) — 专家名单
- [邮件列表](science/mailing-lists.md) — 值得加入的列表
- [活动日历](science/events-calendars.md) — 报告与研讨会 <mark>[待办]</mark>
- [阅读清单](science/reading-list.md) — 入门论文 <mark>[待办]</mark>

## 实验

- [通用流程](experimental/general.md) — 适用于所有实验的规则 <mark>[待办]</mark>
- [实验方案](experimental/protocols.md) — 实验方案页面索引 <mark>[待办]</mark>
- [数据服务器](experimental/data-server.md) — 数据存储位置与组织方式 <mark>[待办]</mark>
- [数据备份](experimental/data-backup.md) — 备份政策 (3-2-1) <mark>[待办]</mark>

## 动物

- [动物](animals/README.md) — 动物实验中心（**如不适用请删除此节**）
  - [方案](animals/protocol.md) — 伦理 / IACUC 审批 <mark>[待办]</mark>
  - [订购动物](animals/ordering.md) <mark>[待办]</mark>
  - [饲养管理](animals/husbandry.md) <mark>[待办]</mark>

## 安全与培训

- [必修培训](safety-and-training/README.md) — 谁需要完成什么，以及如何完成 <mark>[待办]</mark>

## 代码

- [Git 与 Gitee 政策](code/git-gitee.md) — git 安装与 Gitee 配置、平台策略、仓库规范
- [Python](code/python.md) — Python 学习与实验室开发环境 <mark>[待办]</mark>
- [共享仓库](code/shared-repos.md) — yelab0 组织下的内容 <mark>[待办]</mark>
- [流程管道](code/pipelines.md) — 数据处理流程 <mark>[待办]</mark>

## 硬件

- [设备](hardware/README.md) — 实验室硬件清单 <mark>[待办]</mark>

## 职业发展

- [职业](career/README.md) — 研究生院申请、博士生涯的成功之道、论文发表 <mark>[待办]</mark>

## 经费

- [奖学金与基金](funding/README.md) — 资助机会 <mark>[待办]</mark>

---

## 本网站运作方式

本仓库是实验室 wiki 的**权威来源**。其他所有内容——公开网站和中文翻译——均由此处自动生成。

**站点**

- 英文：**https://www.yezhiwen.com/wiki/**
- 中文：**https://www.yezhiwen.com/wiki_zh/** — 由本仓库翻译而来，存放于 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)
- 二者均对搜索引擎不可见（`robots.txt` + `noindex` meta）。

**编辑**

- 所有内容编辑均在此处以英文进行，并推送到 `main` 分支。英文站点约在 15 分钟内更新。
- 要添加页面：创建 `.md` 文件，并在 `sidebar.md` 中添加对应条目，保持与本 README 相同的顺序。
- 切勿手动编辑网站仓库中的 `wiki/` 或 `wiki_zh/` —— 同步操作会覆盖它们。

**发布**（位于 [zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io) 的 `.github/workflows/sync-wiki.yml`）

每 15 分钟，一次 GitHub Action 会将本仓库克隆到站点的 `wiki/` 文件夹，将中文仓库克隆到 `wiki_zh/`，提交任何更改，并触发 Jekyll 重建以发布到 GitHub Pages。

**翻译**（`.github/workflows/translate-wiki.yml`）

每 30 分钟，第二个 Action 会将本仓库与上次同步的提交（记录在两侧的 `.translation-sync` 中）进行比对，使用 Kimi API (`kimi-k2.6`) 将新增和修改的页面翻译成中文，同步删除操作，并推送到 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh) —— 随后发布流程会将其同步到 `/wiki_zh/`。端到端来看，一次英文编辑大约在 45 分钟内到达中文站点。两个工作流均可从网站仓库的 Actions 标签页手动触发。

翻译为机器生成：请在方便时浏览 `Auto-translate` 提交的差异，并直接在中文仓库中修正错误（修正会持续有效，直到对应的英文页面再次更改）。
