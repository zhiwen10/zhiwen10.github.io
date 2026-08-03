# YeLab Wiki

欢迎来到 YeLab wiki —— 实验室的中央知识库。

> 托管于 Gitee:https://gitee.com/yelab0/yelab-wiki

## 实验室概况

- [使命宣言](the-lab/mission-statement.md)—— 实验室的宗旨
- [期望](the-lab/expectations.md)—— 实验室对你的期望，以及你可以对实验室抱有的期望
- [成员与联系方式](the-lab/people.md)—— 我们是谁
- [实验室计算机](the-lab/computers.md)—— 服务器、GPU、存储

## 组织事务

- [实验室例会](organizational/meetings.md)—— 日程安排与会议纪要存档 
- [新成员入职](organizational/onboarding.md)—— 新成员清单、账号、git 访问配置 
- [日历](organizational/calendar.md)—— 实验室共享日历
- [休假](organizational/vacations.md)—— 休假政策 <mark>[to-do]</mark>
- [采购](organizational/ordering.md)—— 如何购买物品 <mark>[to-do]</mark>
- [学术会议](organizational/conferences.md)—— 差旅与会议事务 <mark>[to-do]</mark>
- [安全](organizational/safety.md)—— 实验室安全联系人与规程 <mark>[to-do]</mark>

## 科研

- [各领域咨询对象](science/expert-list.md)—— 专家名单
- [邮件列表](science/mailing-lists.md)—— 值得加入的邮件列表
- [学术活动日历](science/events-calendars.md)—— 报告与研讨会 <mark>[to-do]</mark>
- [阅读清单](science/reading-list.md)—— 入门论文推荐 <mark>[to-do]</mark>

## 实验

- [通用规程](experimental/general.md)—— 适用于所有实验的规则 <mark>[to-do]</mark>
- [实验方案](experimental/protocols.md)—— 实验方案页面索引 <mark>[to-do]</mark>
- [数据服务器](experimental/data-server.md)—— 数据存放位置及组织方式 <mark>[to-do]</mark>
- [数据备份](experimental/data-backup.md)—— 备份策略(3-2-1) <mark>[to-do]</mark>

## 实验动物

- [实验动物](animals/README.md)—— 动物工作枢纽(**如不适用请删除本节**)
  - [伦理审批](animals/protocol.md)—— 伦理 / IACUC 审批 <mark>[to-do]</mark>
  - [动物订购](animals/ordering.md) <mark>[to-do]</mark>
  - [动物饲养](animals/husbandry.md) <mark>[to-do]</mark>

## 安全与培训

- [必修培训](safety-and-training/README.md)—— 谁需要哪些培训，以及如何完成 <mark>[to-do]</mark>

## 代码

- [Git 与 Gitee 规范](code/git-gitee.md)—— git 安装与 Gitee 配置、平台策略、仓库约定
- [Python](code/python.md)—— 学习 Python 及实验室开发环境 <mark>[to-do]</mark>
- [共享仓库](code/shared-repos.md)—— yelab0 组织下的内容 <mark>[to-do]</mark>
- [数据处理流程](code/pipelines.md)—— 数据处理 pipeline <mark>[to-do]</mark>

## 硬件

- [设备](hardware/README.md)—— 实验室硬件清单 <mark>[to-do]</mark>

## 职业发展

- [职业发展](career/README.md)—— 研究生申请、如何读好博士、论文发表 <mark>[to-do]</mark>

## 经费

- [奖学金与基金](funding/README.md)—— 经费申请机会 <mark>[to-do]</mark>

---

## 同步说明（重要）

本仓库是英文版 [yelab-wiki](https://gitee.com/yelab0/yelab-wiki) 的中文翻译版。**英文版是唯一权威来源**——所有内容修改应首先在英文版进行，本仓库仅作翻译同步。

- 本仓库根目录的 `.translation-sync` 文件记录了当前翻译对应的英文版 commit hash；英文版仓库根目录的同名文件则记录了它最近同步对应的中文版 commit hash。
- 同步流程（由 Kimi Code CLI 执行）：对英文版做 `git diff <hash>..HEAD`，仅重新翻译有改动的页面，推送后更新 `.translation-sync`。
- 如果直接在本仓库做了修改，请告知维护者，这些修改会被翻译回英文版（不推荐，尽量先改英文版）。
- 发起同步只需对 Kimi 说：**"sync the wikis"**。
