#!/usr/bin/env python3
"""Merge a weekly changelog PR once both public stores serve its version.

A PR labelled `awaiting-stores` adds an entry to docs/changelog.md that ends
"These changes are available in X.Y.Z on iOS and Android." That line is only
true once the App Store and Google Play both serve X.Y.Z, so the PR waits
for the stores rather than for a person to remember. Each run:

- reads the version from the PR's added lines,
- asks the App Store lookup API and the Play store page what they serve,
- merges the PR when both serve the version,
- comments once when the stores have disagreed for more than STALE_HOURS,
  so a human can rewrite the closing line as an availability difference.

Standard library only. Needs `gh` on PATH with a token that can read PRs,
comment, and merge. `--dry-run` reports without merging or commenting.
"""

import json
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

REPO = "feral-file/docs"
LABEL = "awaiting-stores"
BUNDLE_ID = "com.feralfile.app"
STALE_HOURS = 48
STALE_MARKER = "<!-- store-availability: stale -->"
VERSION_LINE = re.compile(
    r"^\+.*available in (\d+\.\d+\.\d+) on iOS and Android\.?\s*$", re.M
)
USER_AGENT = "Mozilla/5.0 (feral-file/docs store-availability check)"


def gh(*args, parse=True):
    out = subprocess.run(
        ["gh", *args], check=True, capture_output=True, text=True
    ).stdout
    return json.loads(out) if parse and out.strip() else out


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "replace")


def app_store_version():
    data = json.loads(fetch(f"https://itunes.apple.com/lookup?bundleId={BUNDLE_ID}"))
    results = data.get("results") or []
    return results[0].get("version") if results else None


def play_serves(version):
    html = fetch(
        f"https://play.google.com/store/apps/details?id={BUNDLE_ID}&hl=en"
    )
    # The page embeds the current version as [[["1.8.11"]] in its data blob.
    return f'[[["{version}"]]' in html


def pr_version(number):
    diff = gh("pr", "diff", str(number), "-R", REPO, parse=False)
    versions = sorted(set(VERSION_LINE.findall(diff)))
    return versions[0] if len(versions) == 1 else None


def hours_open(pr):
    created = datetime.fromisoformat(pr["createdAt"].replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - created).total_seconds() / 3600


def already_flagged(number):
    comments = gh("pr", "view", str(number), "-R", REPO, "--json", "comments")
    return any(STALE_MARKER in c["body"] for c in comments.get("comments", []))


def checks_green(number):
    checks = gh("pr", "checks", str(number), "-R", REPO, "--json", "bucket")
    return bool(checks) and all(c["bucket"] == "pass" for c in checks)


def main(dry_run):
    prs = gh(
        "pr", "list", "-R", REPO, "--state", "open", "--label", LABEL,
        "--json", "number,title,createdAt",
    )
    if not prs:
        print("no open PRs labelled", LABEL)
        return

    ios = app_store_version()
    print(f"App Store serves {ios}")

    for pr in prs:
        n = pr["number"]
        version = pr_version(n)
        if not version:
            print(f"#{n}: no single 'available in X.Y.Z on iOS and Android' line added; skipping")
            continue
        ios_ok = ios == version
        play_ok = play_serves(version)
        print(f"#{n}: wants {version}; App Store {'yes' if ios_ok else 'no'}, Play {'yes' if play_ok else 'no'}")

        if ios_ok and play_ok:
            if not checks_green(n):
                print(f"#{n}: stores agree but checks are not all green; leaving for a human")
                continue
            if dry_run:
                print(f"#{n}: would merge")
                continue
            gh("pr", "merge", str(n), "-R", REPO, "--squash", "--delete-branch", parse=False)
            print(f"#{n}: merged")
            continue

        if (ios_ok or play_ok) and hours_open(pr) >= STALE_HOURS and not already_flagged(n):
            body = (
                f"{STALE_MARKER}\n"
                f"{version} has been live on {'the App Store' if ios_ok else 'Google Play'} "
                f"but not {'Google Play' if ios_ok else 'the App Store'} for over {STALE_HOURS} hours. "
                "Either wait, or rewrite the closing line as an availability difference and merge by hand."
            )
            if dry_run:
                print(f"#{n}: would comment: {body.splitlines()[1]}")
                continue
            gh("pr", "comment", str(n), "-R", REPO, "--body", body, parse=False)
            print(f"#{n}: commented")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv[1:])
