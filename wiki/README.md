# YeLab Wiki

Welcome to the YeLab wiki — the lab's central knowledge base.

> Hosted on Gitee: https://gitee.com/yelab0/yelab-wiki

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

## Translation sync

This repo is the **authoritative source**. A Chinese translation lives at [yelab-wiki-zh](https://gitee.com/ye-lab/yelab-wiki-zh) — make content edits here first; they will be synced over. 

`.translation-sync` (repo root) records the yelab-wiki-zh commit this repo was last synced against, and vice versa.

## How this website works

This wiki is edited on Gitee at [ye-lab/yelab-wiki](https://gitee.com/ye-lab/yelab-wiki) and published automatically to **https://www.yezhiwen.com/wiki/**.

- Push to `main` on Gitee — the website updates itself within ~15 minutes.
- A scheduled GitHub Action in the website repo ([zhiwen10.github.io](https://github.com/zhiwen10/zhiwen10.github.io), `.github/workflows/sync-wiki.yml`) clones this repo every 15 min, syncs it into the site's `wiki/` folder, and triggers the site rebuild. The Chinese translation is synced the same way into `wiki/zh/`.
- To add a page: create the `.md` file and add a matching entry to `sidebar.md`.
- Do not edit `wiki/` in the website repo by hand — the sync overwrites it.
