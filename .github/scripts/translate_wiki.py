#!/usr/bin/env python3
"""Sync translations between the English and Chinese wiki repos (bidirectional).

Usage: translate_wiki.py <en_repo_dir> <zh_repo_dir>

Human edits on EITHER side are translated to the other:
  - English pages added/changed by human commits in yelab-wiki since the
    baseline recorded in <zh_repo_dir>/.translation-sync are translated into
    Chinese; pages humans deleted there are deleted on the Chinese side.
  - Chinese pages added/changed by human commits in yelab-wiki-zh since the
    baseline recorded in <en_repo_dir>/.translation-sync are back-translated
    into English; deletions are mirrored the same way.

Bot commits (author "wiki-translator[bot]") never trigger translation — that
is what keeps the two directions from chasing each other in an endless loop.
If the same path was human-edited on both sides, English wins. Static assets
(svg/png/jpg/jpeg/gif/webp/js/css) are copied verbatim, never translated.

Converges from a missing baseline (first run): pages present on only one
side are translated to the other, nothing is deleted without an explicit
human deletion on record, and the baseline marker is written and pushed so
later runs track modifications. A baseline marker whose recorded commit no
longer exists in the counterpart's history (history rewrite or corruption)
is a hard error: the run fails loudly instead of silently skipping
modifications to pages that exist on both sides.

Env:
  MOONSHOT_API_KEY   (required)
  MOONSHOT_BASE_URL  (default https://api.moonshot.cn/v1)
  MOONSHOT_MODEL     (default moonshot-v1-8k)
"""

import json
import os
import re
import subprocess
import sys
import time
import urllib.request

EN_DIR, ZH_DIR = sys.argv[1], sys.argv[2]
API_KEY = os.environ["MOONSHOT_API_KEY"]
BASE_URL = os.environ.get("MOONSHOT_BASE_URL", "https://api.moonshot.cn/v1")
MODEL = os.environ.get("MOONSHOT_MODEL", "moonshot-v1-8k")

BOT_AUTHOR = "wiki-translator"
MD_PATTERNS = ["*.md"]
ASSET_EXTS = ("svg", "png", "jpg", "jpeg", "gif", "webp", "js", "css")
ASSET_PATTERNS = [f"*.{e}" for e in ASSET_EXTS]

SYSTEM_PROMPTS = {
    ("en", "zh"): (
        "You are a professional translator for a neuroscience lab's internal wiki. "
        "Translate the given markdown document from English to Simplified Chinese. "
        "Preserve ALL markdown structure exactly: headings, lists, links, tables, "
        "code blocks, HTML tags such as <mark>...</mark>, and file paths in link "
        "targets (translate only the visible link text, never the .md path). "
        "Output ONLY the translated markdown, no commentary."
    ),
    ("zh", "en"): (
        "You are a professional translator for a neuroscience lab's internal wiki. "
        "Translate the given markdown document from Simplified Chinese to English. "
        "Preserve ALL markdown structure exactly: headings, lists, links, tables, "
        "code blocks, HTML tags such as <mark>...</mark>, and file paths in link "
        "targets (translate only the visible link text, never the .md path). "
        "Output ONLY the translated markdown, no commentary."
    ),
}


def git(repo, *args):
    return subprocess.run(["git", "-C", repo] + list(args),
                          capture_output=True, text=True, check=True).stdout.strip()


def md_files(root):
    out = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(dirpath, f), root))
    return sorted(out)


def asset_files(root):
    return {os.path.relpath(os.path.join(dp, f), root)
            for dp, dns, fns in os.walk(root) if ".git" not in dp.split(os.sep)
            for f in fns if f.rsplit(".", 1)[-1].lower() in ASSET_EXTS}


def patch_sidebar():
    """Append any .md page missing from sidebar.md under its folder section,
    reusing the README's link text as the title when available. Returns True
    if sidebar.md was modified (caller commits it)."""
    sb = os.path.join(EN_DIR, "sidebar.md")
    if not os.path.exists(sb):
        return False
    content = open(sb).read()
    linked = set(re.findall(r"\]\(([^)]+\.md)\)", content))
    missing = [p for p in md_files(EN_DIR) if p not in linked and p != "sidebar.md"]
    if not missing:
        return False
    readme_path = os.path.join(EN_DIR, "README.md")
    readme = open(readme_path).read() if os.path.exists(readme_path) else ""
    titles = {m.group(2): m.group(1)
              for m in re.finditer(r"\[([^\]]+)\]\(([^)]+\.md)\)", readme)}
    lines = content.rstrip().split("\n")
    for rel in missing:
        title = titles.get(rel) or os.path.basename(rel)[:-3].replace("-", " ").replace("_", " ")
        folder = os.path.dirname(rel)
        header = f"- **{folder}/**" if folder else None
        entry = f"  - [{title}]({rel})" if folder else f"- [{title}]({rel})"
        if header and header in lines:
            idx = lines.index(header)
            j = idx + 1
            while j < len(lines) and lines[j].startswith("  "):
                j += 1
            lines.insert(j, entry)
        else:
            lines += ([header, entry] if header else [entry])
        print(f"sidebar: added missing entry {rel}")
    open(sb, "w").write("\n".join(lines) + "\n")
    return True


def translate(text, src_lang, dst_lang):
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPTS[(src_lang, dst_lang)]},
            {"role": "user", "content": text},
        ],
    }).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions", data=body,
        headers={"Authorization": f"Bearer {API_KEY}",
                 "Content-Type": "application/json"}, method="POST")
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=360) as r:
                return json.load(r)["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:500]
            if attempt == 3:
                raise RuntimeError(f"HTTP {e.code}: {detail}") from e
            print(f"  retry after error: HTTP {e.code}: {detail}", file=sys.stderr)
            time.sleep(30 * (attempt + 1))
        except Exception as e:
            if attempt == 3:
                raise
            print(f"  retry after error: {e}", file=sys.stderr)
            time.sleep(30 * (attempt + 1))


def read_baseline(marker_path, repo, marker_repo, counterpart_repo):
    """The counterpart commit hash this repo's content was last synced to.

    Missing/empty marker -> '' (initial full sync; this run then writes and
    pushes the marker so later runs can track modifications). A marker whose
    commit no longer exists in the counterpart's history means the history
    was rewritten or the file was corrupted: fail loudly, because running on
    would silently skip modifications to pages that exist on both sides."""
    if not os.path.exists(marker_path):
        return ""
    base = open(marker_path).read().strip()
    if not base:
        return ""
    try:
        git(repo, "rev-parse", "--verify", f"{base}^{{commit}}")
        return base
    except subprocess.CalledProcessError:
        sys.exit(
            f"ERROR: {marker_repo}/.translation-sync records {base[:12]}, which\n"
            f"is not a commit in {counterpart_repo}'s history (history rewritten or\n"
            f"marker corrupted?). Stopping instead of silently skipping edits.\n"
            f"Fix: set {marker_repo}/.translation-sync to a {counterpart_repo} commit\n"
            f"from before the divergence (e.g. `git rev-list -1 --before=<date> main`),\n"
            f"commit it, then rerun this workflow."
        )


def human_changes(repo, baseline, patterns):
    """Map path -> status (A/M/D) for files touched by human (non-bot) commits
    in baseline..HEAD. Bot translation commits are ignored so machine
    translations never trigger re-translation back the other way."""
    if not baseline:
        return {}
    out = {}
    log = git(repo, "log", "--reverse", "--no-merges", "--format=%H%x09%an",
              f"{baseline}..HEAD")
    for line in log.splitlines():
        sha, _, author = line.partition("\t")
        if BOT_AUTHOR in author:
            continue
        for ns in git(repo, "diff-tree", "--root", "--no-commit-id", "-r",
                      "--name-status", sha, "--", *patterns).splitlines():
            parts = ns.split("\t")
            if len(parts) >= 2:
                status = parts[0][0]
                out[parts[-1]] = "M" if status == "R" else status
    return out


def main():
    sidebar_changed = patch_sidebar()
    if sidebar_changed:
        git(EN_DIR, "config", "user.name", "wiki-translator[bot]")
        git(EN_DIR, "config", "user.email", "translator@yelab.local")
        git(EN_DIR, "add", "sidebar.md")
        git(EN_DIR, "commit", "-q", "-m", "sidebar: add missing page entries")

    en_head = git(EN_DIR, "rev-parse", "HEAD")
    zh_head = git(ZH_DIR, "rev-parse", "HEAD")
    en_base = read_baseline(os.path.join(ZH_DIR, ".translation-sync"), EN_DIR,
                            "yelab-wiki-zh", "yelab-wiki")
    zh_base = read_baseline(os.path.join(EN_DIR, ".translation-sync"), ZH_DIR,
                            "yelab-wiki", "yelab-wiki-zh")
    print(f"baselines: en={en_base[:12] or '(none — full sync)'} "
          f"zh={zh_base[:12] or '(none — full sync)'}")

    en_md = human_changes(EN_DIR, en_base, MD_PATTERNS)
    zh_md = human_changes(ZH_DIR, zh_base, MD_PATTERNS)
    en_assets = human_changes(EN_DIR, en_base, ASSET_PATTERNS)
    zh_assets = human_changes(ZH_DIR, zh_base, ASSET_PATTERNS)
    # the sidebar patch is a bot commit, so force its (re)translation
    if sidebar_changed:
        en_md["sidebar.md"] = "M"

    # same path human-edited on both sides: English wins
    for p in sorted(set(en_md) & set(zh_md)):
        print(f"conflict: {p} edited on both sides — English wins")
        del zh_md[p]
    for p in sorted(set(en_assets) & set(zh_assets)):
        print(f"conflict: {p} edited on both sides — English wins")
        del zh_assets[p]

    en_pages, zh_pages = set(md_files(EN_DIR)), set(md_files(ZH_DIR))
    en_asset_set, zh_asset_set = asset_files(EN_DIR), asset_files(ZH_DIR)

    ez_delete = {p for p, s in en_md.items() if s == "D"}
    ez_translate = ({p for p, s in en_md.items() if s in ("A", "M")}
                    | (en_pages - zh_pages)) - ez_delete
    ze_delete = {p for p, s in zh_md.items() if s == "D"}
    ze_translate = ({p for p, s in zh_md.items() if s in ("A", "M")}
                    | (zh_pages - en_pages)) - ze_delete - ez_delete

    ez_del_assets = {p for p, s in en_assets.items() if s == "D"}
    ez_copy = ({p for p, s in en_assets.items() if s in ("A", "M")}
               | (en_asset_set - zh_asset_set)) - ez_del_assets
    ze_del_assets = {p for p, s in zh_assets.items() if s == "D"}
    ze_copy = ({p for p, s in zh_assets.items() if s in ("A", "M")}
               | (zh_asset_set - en_asset_set)) - ze_del_assets - ez_del_assets

    stats = {d: {"translated": [], "copied": [], "deleted": [], "failed": []}
             for d in ("ez", "ze")}

    def apply(direction, src_dir, dst_dir, to_translate, to_copy, to_delete,
              src_lang, dst_lang):
        st = stats[direction]
        for rel in sorted(to_copy):
            src = os.path.join(src_dir, rel)
            if not os.path.exists(src):
                continue
            dst = os.path.join(dst_dir, rel)
            os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
            subprocess.run(["cp", src, dst], check=True)
            st["copied"].append(rel)
            print(f"copied asset {src_lang}->{dst_lang} {rel}")
        for rel in sorted(to_translate):
            src_path = os.path.join(src_dir, rel)
            if not os.path.exists(src_path):
                continue
            text = open(src_path).read()
            print(f"translating {src_lang}->{dst_lang} {rel} ({len(text)} chars)")
            try:
                out = translate(text, src_lang, dst_lang)
            except Exception as e:
                print(f"  FAILED {rel}: {e}", file=sys.stderr)
                st["failed"].append(rel)
                continue
            dst = os.path.join(dst_dir, rel)
            os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
            open(dst, "w").write(out if out.endswith("\n") else out + "\n")
            st["translated"].append(rel)
        for rel in sorted(to_delete):
            p = os.path.join(dst_dir, rel)
            if os.path.exists(p):
                os.remove(p)
                st["deleted"].append(rel)
                print(f"deleted {dst_lang} {rel}")

    apply("ez", EN_DIR, ZH_DIR, ez_translate, ez_copy, ez_delete | ez_del_assets,
          "en", "zh")
    apply("ze", ZH_DIR, EN_DIR, ze_translate, ze_copy, ze_delete | ze_del_assets,
          "zh", "en")

    ez_active = any(stats["ez"][k] for k in ("translated", "copied", "deleted"))
    ze_active = any(stats["ze"][k] for k in ("translated", "copied", "deleted"))

    # Each side's marker records the counterpart HEAD its content now reflects.
    # Bot commits are filtered out of future diffs, so the markers only need to
    # anchor the window of human commits already processed. A marker written
    # here must be pushed even when nothing else changed (otherwise a missing
    # baseline would never be established), so it counts towards "changed".
    markers_updated = False
    if not stats["ez"]["failed"] and (ez_active or not en_base):
        open(os.path.join(ZH_DIR, ".translation-sync"), "w").write(en_head + "\n")
        markers_updated = True
    if not stats["ze"]["failed"] and (ze_active or not zh_base):
        open(os.path.join(EN_DIR, ".translation-sync"), "w").write(zh_head + "\n")
        markers_updated = True

    print(f"\n== summary: en->zh {len(stats['ez']['translated'])} translated, "
          f"{len(stats['ez']['copied'])} copied, {len(stats['ez']['deleted'])} deleted, "
          f"{len(stats['ez']['failed'])} failed | zh->en "
          f"{len(stats['ze']['translated'])} translated, "
          f"{len(stats['ze']['copied'])} copied, {len(stats['ze']['deleted'])} deleted, "
          f"{len(stats['ze']['failed'])} failed ==")
    for rel in stats["ez"]["translated"] + stats["ez"]["copied"]:
        print(f"  en->zh + {rel}")
    for rel in stats["ze"]["translated"] + stats["ze"]["copied"]:
        print(f"  zh->en + {rel}")
    if stats["ez"]["failed"] or stats["ze"]["failed"]:
        sys.exit(1)
    if not ez_active and not ze_active and not sidebar_changed \
            and not markers_updated:
        print("nothing to do")


if __name__ == "__main__":
    main()
