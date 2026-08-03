# YeLab Wiki

Welcome to the YeLab wiki — the lab's central knowledge base.

> Hosted on Gitee: https://edu.gitee.com/ye-lab/yelab-wiki

## The Lab

- [Mission statement](the-lab/mission-statement.md) — what the lab is for
- [Expectations](the-lab/expectations.md) — what the lab expects of you, and what you can expect of it
- [People and contact info](the-lab/people.md) — who we are
- [Lab computers](the-lab/computers.md) — servers, GPUs, storage

## Organizational

- [Lab meetings](organizational/meetings.md) — schedule and notes archive 
- [Onboarding](organizational/onboarding.md) — new member checklist, accounts, git access 
- [Calendar](organizational/calendar.md) — the shared lab calendar
- [Vacations](organizational/vacations.md) — time-off policy <mark>[to-do]</mark>
- [Ordering](organizational/ordering.md) — how to buy things <mark>[to-do]</mark>
- [Conferences](organizational/conferences.md) — travel and conference logistics <mark>[to-do]</mark>
- [Safety](organizational/safety.md) — lab safety contacts and procedures <mark>[to-do]</mark>

## Science

- [Who to ask about what](science/expert-list.md) — the expert list
- [Mailing lists](science/mailing-lists.md) — lists worth joining
- [Events calendars](science/events-calendars.md) — talks and seminars <mark>[to-do]</mark>
- [Reading list](science/reading-list.md) — papers to start with <mark>[to-do]</mark>

## Experimental

- [General procedures](experimental/general.md) — rules applying to all experiments <mark>[to-do]</mark>
- [Protocols](experimental/protocols.md) — index of experimental protocol pages <mark>[to-do]</mark>
- [Data server](experimental/data-server.md) — where data lives and how it's organized <mark>[to-do]</mark>
- [Data backup](experimental/data-backup.md) — backup policy (3-2-1) <mark>[to-do]</mark>

## Animals

- [Animals](animals/README.md) — animal work hub (**delete this section if not applicable**)
  - [Protocol](animals/protocol.md) — ethics / IACUC approval <mark>[to-do]</mark>
  - [Ordering animals](animals/ordering.md) <mark>[to-do]</mark>
  - [Husbandry](animals/husbandry.md) <mark>[to-do]</mark>

## Safety and training

- [Required trainings](safety-and-training/README.md) — who needs what, and how to complete it <mark>[to-do]</mark>

## Code

- [Git & Gitee policy](code/git-gitee.md) — git install & Gitee setup, platform strategy, repo conventions
- [Python](code/python.md) — learning python and the lab dev environment <mark>[to-do]</mark>
- [Shared repos](code/shared-repos.md) — what lives in the yelab0 org <mark>[to-do]</mark>
- [Pipelines](code/pipelines.md) — data processing pipelines <mark>[to-do]</mark>

## Hardware

- [Equipment](hardware/README.md) — lab hardware inventory <mark>[to-do]</mark>

## Career development

- [Career](career/README.md) — grad school applications, succeeding in a PhD, publishing <mark>[to-do]</mark>

## Funding

- [Fellowships & grants](funding/README.md) — funding opportunities <mark>[to-do]</mark>

---

## How this website works

This repo is the **authoritative source** of the lab wiki. Everything else — the public website and the Chinese translation — is generated from here automatically.

**Sites**

- English: **https://www.yezhiwen.com/wiki/**
- 中文: **https://www.yezhiwen.com/wiki_zh/** — translated from this repo, lives at [yelab-wiki-zh](https://edu.gitee.com/ye-lab/yelab-wiki-zh)
- Both are excluded from search engines (`robots.txt` + `noindex` meta).

**Editing**

- Make all content edits here, in English, and push to `main`. The English site updates within ~15 minutes.
- To add a page: create the `.md` file and add a matching entry to `sidebar.md`, keeping the same order as this README.
- Never edit `wiki/` or `wiki_zh/` in the website repo by hand — the sync overwrites them.

**Publishing** (`.github/workflows/sync-wiki.yml` in [zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io))

Every 15 minutes a GitHub Action clones this repo into the site's `wiki/` folder and the Chinese repo into `wiki_zh/`, commits any changes, and triggers the Jekyll rebuild that publishes to GitHub Pages.

**Translation** (`.github/workflows/translate-wiki.yml`)

Every 30 minutes a second Action diffs this repo against the last-synced commit (recorded in `.translation-sync` on both sides), translates new and changed pages into Chinese with the Kimi API (`kimi-k2.6`), mirrors deletions, and pushes to [yelab-wiki-zh](https://edu.gitee.com/ye-lab/yelab-wiki-zh) — the publishing pipeline then carries it to `/wiki_zh/`. End to end, an English edit reaches the Chinese site within ~45 minutes. Both workflows can also be run manually from the website repo's Actions tab.

Translations are machine-generated: skim the `Auto-translate` commit diffs when convenient and fix mistakes directly in the zh repo (a fix persists until that English page changes again).
