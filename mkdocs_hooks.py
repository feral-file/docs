"""Small build hooks for public files that MkDocs would otherwise render.

Three generated files, all written after the build:
- /docs/changelog.md: the raw changelog, for installed app readers.
- <page>/index.md beside every page: the page's Markdown source as written,
  so an agent reads the text without parsing the rendered HTML.
- /llms.txt: what the site is and one line per page with its HTML and
  Markdown URLs (https://llmstxt.org).
"""

from pathlib import Path
from shutil import copyfile

_PAGES = []


def on_files(files, config, **_kwargs):
    """Remember every documentation page; on_post_build writes their twins and llms.txt."""
    _PAGES[:] = list(files.documentation_pages())
    return files


def _title(src):
    for line in src.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return src.stem


def on_post_build(config, **_kwargs):
    site = Path(config["site_dir"])
    docs = Path(config["docs_dir"])
    base = config["site_url"].rstrip("/")

    destination = site / "docs" / "changelog.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    copyfile(docs / "changelog.md", destination)

    lines = [
        f"# {config['site_name']}",
        "",
        "> Developer documentation for Feral File: the Art Computer, ff-cli, the hosted DP-1 feed, and how agents work with them.",
        "> Every page has a Markdown twin at its URL plus index.md.",
        "",
        "## Pages",
        "",
    ]
    for page in _PAGES:
        src = Path(page.abs_src_path)
        url = "" if page.url in (".", "./") else page.url
        twin = site / url / "index.md"
        twin.parent.mkdir(parents=True, exist_ok=True)
        copyfile(src, twin)
        lines.append(f"- [{_title(src)}]({base}/{url}): Markdown at {base}/{url}index.md")
    (site / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
