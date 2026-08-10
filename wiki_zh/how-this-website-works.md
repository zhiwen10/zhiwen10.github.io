# 本网站的工作原理

本 wiki 存放在两个自动同步的仓库中：英文版 [yelab-wiki](https://gitee.com/ye-lab/yelab-wiki) 和中文版 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)。您可以编辑**任意一个**——修改会由机器人翻译并同步到另一侧。公开网站由这两个仓库共同生成。

![wiki pipeline](pipeline.svg)

**网站地址**

- 英文站：**https://www.yezhiwen.com/wiki/**
- 中文站：**https://www.yezhiwen.com/wiki_zh/** — 对应仓库为 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)
- 两个站点均已被排除在搜索引擎之外（通过 `robots.txt` + `noindex` meta）。

**查看注意事项（浏览器缓存）**

本 wiki 的查看器是一个单页应用，会在您的浏览器中积极缓存页面。如果更新后页面看起来仍是旧版，请强制刷新：Safari 使用 **⌥⌘R**（或“开发”→“清空缓存”），Chrome 使用 **⌘⇧R**。如果仍然显示旧版，请关闭并重新打开标签页。

**编辑**

- 用您偏好的语言编辑页面，并推送到对应仓库的 `main` 分支。您的修改将在约 20 分钟内被机器翻译到另一个仓库（详见下方的**翻译**部分）。英文站约在 15 分钟内更新。
- 添加页面：创建 `.md` 文件，并在 `sidebar.md` 中添加对应的条目，顺序与本 README 保持一致。在一侧添加的页面会在翻译完成后出现在另一侧。
- 避免同时在两个仓库中编辑同一页面：如果自上次同步以来，两侧都对同一页面做了修改，**以英文版为准**，中文侧的修改将被覆盖。
- 切勿手动编辑网站仓库中的 `wiki/` 或 `wiki_zh/` 目录——同步操作会覆盖它们。

**发布**（[zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io) 中的 `.github/workflows/sync-wiki.yml`）

每隔 15 分钟，一个 GitHub Action 会将英文仓库克隆到网站的 `wiki/` 目录，将中文仓库克隆到 `wiki_zh/` 目录，提交任何变更，并触发 Jekyll 重新构建，随后发布到 GitHub Pages。

**翻译**（`.github/workflows/translate-wiki.yml`）

每隔 15 分钟，第二个 Action 会检查**两个**仓库中自上次同步以来的人工编辑（记录在各自仓库的 `.translation-sync` 文件中）。新增和修改的页面会通过 Kimi API（`kimi-k2.6`）翻译到另一个仓库——在此仓库中的编辑由英文翻译为中文，在 [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh) 中的编辑由中文翻译为英文——删除操作也会同步镜像，并立即触发发布同步（无需等待第二轮定时任务）。翻译机器人自身的提交不会触发重新翻译，因此两个方向不会形成循环。端到端来看，任一侧的编辑通常会在约 20 分钟内到达对侧站点。该工作流也可以从网站仓库的 Actions 标签页手动运行。

翻译内容由机器生成：请在方便时浏览 `Auto-translate` 提交的差异。请注意，在一侧进行的手动修正会被视为一次编辑，并会被翻译回去覆盖另一侧的版本——因此请修正源文本的措辞，而不是只修改翻译。
