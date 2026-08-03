# Shared repos

All lab code lives in the **yelab0** Gitee org: https://gitee.com/yelab0. Platform strategy, git access setup, and mirroring rules: see [Git & Gitee policy](git-gitee.md).

## Lab-owned repos

| Repo | What it is | Maintainer |
|---|---|---|
| [yelab-wiki](https://gitee.com/yelab0/yelab-wiki) | This wiki | {{NAME}} |
| {{REPO_1}} | {{DESCRIPTION}} | {{NAME}} |

## Third-party mirrors

- Mirrors of repos we don't own are named `mirror-<owner>-<repo>`, private, read-only — details in [Git & Gitee policy](git-gitee.md#third-party-upstream-repos)

## What a lab repo looks like

- Naming: `lowercase-with-dashes`
- Default branch `main`; feature branches + pull requests for shared projects
- Every repo gets a README: what it is, how to install, how to run, who maintains it
- Layout: `src/` library code, `scripts/` entry points, `notebooks/` exploration, `configs/` experiment configs, `tests/`
- Code style: {{STYLE}} — e.g. black/ruff for Python, pre-commit hooks

## Working on shared code

- When changing a shared file, ping whoever changed it recently for an informal review
- Commit and push often — don't let uncommitted changes pile up on a server
- Large data, weights, and results never go in git — see [data server](../experimental/data-server.md)
