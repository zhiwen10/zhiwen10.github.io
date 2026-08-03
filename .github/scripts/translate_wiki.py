#!/usr/bin/env python3
"""Translate changed English wiki pages to Chinese via the Moonshot (Kimi) API.

Usage: translate_wiki.py <en_repo_dir> <zh_repo_dir>

Reads the English commit hash recorded in <zh_repo_dir>/.translation-sync as
the baseline, translates every added/modified markdown file since then into
the corresponding path in the Chinese repo, mirrors deletions, and refreshes
.translation-sync on the Chinese side. Converges even if the baseline is
missing/stale: English files absent from the Chinese repo are translated,
Chinese files absent from the English repo are deleted.

Env:
  MOONSHOT_API_KEY   (required)
  MOONSHOT_BASE_URL  (default https://api.moonshot.cn/v1)
  MOONSHOT_MODEL     (default moonshot-v1-8k)
"""

import json
import os
import subprocess
import sys
import time
import urllib.request

EN_DIR, ZH_DIR = sys.argv[1], sys.argv[2]
API_KEY = os.environ["MOONSHOT_API_KEY"]
BASE_URL = os.environ.get("MOONSHOT_BASE_URL", "https://api.moonshot.cn/v1")
MODEL = os.environ.get("MOONSHOT_MODEL", "moonshot-v1-8k")

SYSTEM_PROMPT = (
    "You are a professional translator for a neuroscience lab's internal wiki. "
    "Translate the given markdown document from English to Simplified Chinese. "
    "Preserve ALL markdown structure exactly: headings, lists, links, tables, "
    "code blocks, HTML tags such as <mark>...</mark>, and file paths in link "
    "targets (translate only the visible link text, never the .md path). "
    "Output ONLY the translated markdown, no commentary."
)


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


def translate(text):
    body = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
    }).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions", data=body,
        headers={"Authorization": f"Bearer {API_KEY}",
                 "Content-Type": "application/json"}, method="POST")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            detail = e.read().decode(errors="replace")[:500]
            if attempt == 2:
                raise RuntimeError(f"HTTP {e.code}: {detail}") from e
            print(f"  retry after error: HTTP {e.code}: {detail}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))


def main():
    head = git(EN_DIR, "rev-parse", "HEAD")
    sync_file = os.path.join(ZH_DIR, ".translation-sync")
    baseline = open(sync_file).read().strip() if os.path.exists(sync_file) else ""
    try:
        git(EN_DIR, "rev-parse", "--verify", f"{baseline}^{{commit}}")
    except subprocess.CalledProcessError:
        baseline = ""
    print(f"baseline: {baseline or '(none — full sync)'}")

    if baseline:
        changed = git(EN_DIR, "diff", "--name-status", f"{baseline}..HEAD",
                      "--", "*.md").splitlines()
        todo = {(s[0], s[1]) for line in changed if (s := line.split("\t"))}
    else:
        todo = set()

    en_files = set(md_files(EN_DIR))
    zh_files = set(md_files(ZH_DIR))

    to_translate = {p for st, p in todo if st in ("A", "M")} | (en_files - zh_files)
    to_delete = {p for st, p in todo if st == "D"} | (zh_files - en_files)

    translated, failed = [], []
    for rel in sorted(to_translate):
        src = open(os.path.join(EN_DIR, rel)).read()
        print(f"translating {rel} ({len(src)} chars)")
        try:
            out = translate(src)
        except Exception as e:
            print(f"  FAILED {rel}: {e}", file=sys.stderr)
            failed.append(rel)
            continue
        dst = os.path.join(ZH_DIR, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w").write(out if out.endswith("\n") else out + "\n")
        translated.append(rel)

    for rel in sorted(to_delete):
        p = os.path.join(ZH_DIR, rel)
        if os.path.exists(p):
            os.remove(p)
            print(f"deleted {rel}")

    if translated or to_delete or not baseline:
        open(sync_file, "w").write(head + "\n")

    print(f"\n== summary: {len(translated)} translated, "
          f"{len(to_delete)} deleted, {len(failed)} failed ==")
    for rel in translated:
        print(f"  + {rel}")
    if failed:
        sys.exit(1)
    if not translated and not to_delete:
        print("nothing to do")


if __name__ == "__main__":
    main()
