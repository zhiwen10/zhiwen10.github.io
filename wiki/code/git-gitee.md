# Git & Gitee policy

## Platform strategy

- **Gitee is the lab's primary platform** (GitHub is unreachable from some lab networks)
- Lab org: https://gitee.com/yelab0
- Selected lab-owned repos are push-mirrored to GitHub for international visibility
- Default visibility: **private**. Making a repo public on Gitee requires manual platform review — only do it deliberately

## Install git

Gitee is just a hosting server — all interaction happens through the `git` command, so install it first. Check with `git --version`; if you get a version number, you're done.

**macOS**

```bash
xcode-select --install
```

This installs Apple's Command Line Tools, which include git. (Or `brew install git` if you already use Homebrew.)

**Windows**

Download Git for Windows from https://git-scm.com. If the download is slow from China, use the npmmirror mirror instead: https://registry.npmmirror.com/binary.html?path=git-for-windows/ — pick the latest `Git-*-64-bit.exe`. Default installer options are fine.

## Connecting git to Gitee

You talk to Gitee with the regular `git` command — Gitee is just the server that hosts the repos. When you `git clone` / `pull` / `push`, git has to prove your identity. Two ways:

**HTTPS + personal access token (recommended)**

1. Clone using the repo's HTTPS URL, e.g. `git clone https://gitee.com/yelab0/yelab-wiki.git`
2. When git asks for a password, paste a **personal access token**, not your login password — create one at https://gitee.com/profile/personal_access_tokens (the `projects` scope is enough)
3. On macOS the Keychain remembers the token, so you only do this once

**SSH keys (optional)**

Same result, different mechanism — no token to manage, but the setup is fiddlier. Skip unless you prefer it.

```bash
# generate a key (skip if you already have one)
ssh-keygen -t ed25519 -C "your-gitee-email@example.com"

# print the public key and add it at https://gitee.com/profile/sshkeys
cat ~/.ssh/id_ed25519.pub

# test
ssh -T git@gitee.com
```

## Repo conventions

- Naming: `lowercase-with-dashes`, e.g. `spike-sorting-pipeline`
- Every repo gets a README with: what it is, how to install, how to run, who maintains it
- Default branch: `main`. Use feature branches + pull requests for shared projects
- Large data, model weights, and results do **not** go in git — see [computers/storage](../the-lab/computers.md#storage)

## Third-party (upstream) repos

For repos we don't own but need local access to:

1. **Private mirror, read-only** — import from GitHub (`+` → 从 GitHub 导入仓库) or push a `--mirror` clone
2. Name it `mirror-<owner>-<repo>` and note the upstream URL + sync date in the description
3. Keep LICENSE and full git history intact; check the license before mirroring
4. **Never commit directly to a mirror** — to modify upstream code, create a separate lab repo forked from the mirror
5. Keep mirrors fresh via Gitee's pull-mirror feature (repo settings → 仓库镜像管理 → Pull) or a scheduled `git fetch && git push --mirror`

## Contributing back to GitHub projects

Do it on GitHub (fork + PR there). Gitee is just our local access layer; contributing from a Gitee copy to a GitHub upstream is nonstandard and painful.
