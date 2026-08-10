# How this website works

The wiki lives in two repos that are kept in sync automatically: the English [yelab-wiki](https://gitee.com/ye-lab/yelab-wiki) and the Chinese [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh). You may edit **either** one — changes are translated to the other side by a bot. The public website is generated from both repos.

![wiki pipeline](pipeline.svg)

**Sites**

- English: **https://www.yezhiwen.com/wiki/**
- 中文: **https://www.yezhiwen.com/wiki_zh/** — lives at [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh)
- Both are excluded from search engines (`robots.txt` + `noindex` meta).

**Viewing note (browser caching)**

The wiki viewer is a single-page app that caches pages aggressively in your browser. If a page looks stale right after an update, hard-refresh: Safari **⌥⌘R** (or Develop → Empty Caches), Chrome **⌘⇧R**. If it is still stale, close and reopen the tab.

**Editing**

- Edit pages in whichever language you prefer and push to `main` of that repo. Your edits are machine-translated to the other repo within ~20 minutes (see **Translation** below). The English site updates within ~15 minutes.
- To add a page: create the `.md` file and add a matching entry to `sidebar.md`, keeping the same order as this README. A page added on one side appears on the other side once it is translated.
- Avoid editing the same page in both repos at the same time: if a page was changed on both sides since the last sync, the **English version wins** and the Chinese edit is overwritten.
- Never edit `wiki/` or `wiki_zh/` in the website repo by hand — the sync overwrites them.

**Publishing** (`.github/workflows/sync-wiki.yml` in [zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io))

Every 15 minutes a GitHub Action clones the English repo into the site's `wiki/` folder and the Chinese repo into `wiki_zh/`, commits any changes, and triggers the Jekyll rebuild that publishes to GitHub Pages.

**Translation** (`.github/workflows/translate-wiki.yml`)

Every 15 minutes a second Action checks **both** repos for human edits since the last sync (recorded in `.translation-sync` on each side). New and changed pages are translated to the other repo with the Kimi API (`kimi-k2.6`) — English→Chinese for edits here, Chinese→English for edits in [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh) — deletions are mirrored, and the publishing sync is triggered immediately (no second cron wait). The translator's own commits never trigger re-translation, so the two directions cannot loop. End to end, an edit on either side typically reaches the opposite site within ~20 minutes. The workflow can also be run manually from the website repo's Actions tab.

Translations are machine-generated: skim the `Auto-translate` commit diffs when convenient. Note that a manual fix on one side is treated as an edit and will be translated back over the other side's version — so fix the source wording, not just the translation.
