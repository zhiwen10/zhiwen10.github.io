# 本网站工作原理

本仓库是实验室 wiki 的**权威来源**。其他所有内容——公开网站和中文翻译——均从此处自动生成。

![wiki pipeline](pipeline.svg)

**站点**

- 英文: **https://www.yezhiwen.com/wiki/**
- 中文: **https://www.yezhiwen.com/wiki_zh/** — 翻译自本仓库，托管于 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)
- 两者均被排除在搜索引擎之外（`robots.txt` + `noindex` meta）。

**查看说明（浏览器缓存）**

Wiki 查看器是一个单页应用，会在您的浏览器中强力缓存页面。如果更新后页面看起来仍是旧的，请强制刷新：Safari **⌥⌘R**（或 开发 → 清空缓存），Chrome **⌘⇧R**。如果仍然陈旧，请关闭并重新打开标签页。

**编辑**

- 所有内容编辑请在此处用英文完成，并推送到 `main`。英文站点约在 15 分钟内更新。
- 添加页面：创建 `.md` 文件，并在 `sidebar.md` 中添加对应的条目，顺序与本 README 保持一致。
- 切勿手动编辑网站仓库中的 `wiki/` 或 `wiki_zh/` —— 同步会覆盖它们。

**发布**（`.github/workflows/sync-wiki.yml`，位于 [zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io)）

每 15 分钟，一次 GitHub Action 将此仓库克隆到网站的 `wiki/` 文件夹，将中文仓库克隆到 `wiki_zh/`，提交任何更改，并触发 Jekyll 重新构建，发布到 GitHub Pages。

**翻译**（`.github/workflows/translate-wiki.yml`）

每 15 分钟，第二个 Action 将此仓库与上次同步的提交（记录在两侧的 `.translation-sync` 中）进行比对，使用 Kimi API（`kimi-k2.6`）将新增和更改的页面翻译成中文，同步删除操作，推送到 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)，并立即触发发布同步（无需等待第二次定时任务）。端到端来看，一次英文编辑通常在约 20 分钟内到达中文站点。两个工作流也可以从网站仓库的 Actions 标签页手动运行。

翻译由机器生成：请在方便时浏览 `Auto-translate` 提交的 diff，并直接在 zh 仓库中修正错误（修正会一直保留，直到对应的英文页面再次更改）。
