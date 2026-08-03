# 本网站如何运作

本仓库是实验室 wiki 的**权威来源**。其他所有内容——公开网站和中文翻译——都是从此处自动生成的。

![wiki 流程图](pipeline.svg)

**站点**

- 英文：**https://www.yezhiwen.com/wiki/**
- 中文：**https://www.yezhiwen.com/wiki_zh/** — 翻译自本仓库，位于 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)
- 两者均对搜索引擎隐藏（`robots.txt` + `noindex` 元标签）。

**编辑**

- 所有内容编辑均在此处以英文进行，并推送到 `main` 分支。英文站点会在约 15 分钟内更新。
- 添加页面：创建 `.md` 文件，并在 `sidebar.md` 中添加对应的条目，顺序与 README 保持一致。
- 切勿手动编辑网站仓库中的 `wiki/` 或 `wiki_zh/` —— 同步操作会覆盖它们。

**发布**（`.github/workflows/sync-wiki.yml`，位于 [zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io)）

每 15 分钟，GitHub Action 会将本仓库克隆到站点的 `wiki/` 文件夹，并将中文仓库克隆到 `wiki_zh/`，提交任何更改，并触发 Jekyll 重新构建以发布到 GitHub Pages。

**翻译**（`.github/workflows/translate-wiki.yml`）

每 30 分钟，第二个 Action 会将本仓库与上次同步的提交（记录在双方的 `.translation-sync` 中）进行比对，使用 Kimi API（`kimi-k2.6`）将新增和修改的页面翻译成中文，同步删除操作，并推送到 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh) —— 随后发布流水线会将其部署到 `/wiki_zh/`。端到端来看，英文编辑会在约 45 分钟内到达中文站点。两个工作流也都可以从网站仓库的 Actions 标签页手动运行。

翻译内容由机器生成：请在方便时快速浏览 `Auto-translate` 提交的差异，并直接在中文仓库中修正错误（修正会持续到对应的英文页面再次更改为止）。
