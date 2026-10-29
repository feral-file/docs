#!/usr/bin/env python3
"""Check the built Markdown twins: every relative link resolves to a built file.

mkdocs_hooks.py writes <page>/index.md beside every page and rewrites the
relative links so they point at the served twins. `mkdocs build --strict`
never looks at those files, so a wrong rewrite ships as a 404 that only an
agent reading the Markdown would hit. Run after the build:

    python3 scripts/check-twins.py site

Exit 1 lists each twin and the link that does not resolve.
"""

import re
import sys
from pathlib import Path

# Same shape as mkdocs_hooks._RELATIVE_LINK: a link or image target with no
# scheme, not a fragment, not site-absolute.
RELATIVE_LINK = re.compile(r"\]\((?![a-z][a-z0-9+.\-]*:|#|/)([^)\s#]+)(#[^)]*)?\)")


def main(site_dir):
    site = Path(site_dir)
    twins = sorted(p for p in site.rglob("index.md") if p.relative_to(site).parts[0] != "docs")
    if not twins:
        print(f"no Markdown twins under {site}", file=sys.stderr)
        return 1
    total = 0
    missing = []
    for twin in twins:
        for match in RELATIVE_LINK.finditer(twin.read_text(encoding="utf-8")):
            total += 1
            target = (twin.parent / match.group(1)).resolve()
            if not target.exists():
                missing.append((twin.relative_to(site), match.group(1)))
    for twin, link in missing:
        print(f"{twin}: {link} does not resolve", file=sys.stderr)
    print(f"{len(twins)} twins, {total} relative links, {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "site"))
