"""Small build hooks for public files that MkDocs would otherwise render.

Three generated files, all written after the build:
- /docs/changelog.md: the raw changelog, for installed app readers.
- <page>/index.md beside every page: the page's Markdown source, so an agent
  reads the text without parsing the rendered HTML. Relative links are
  rewritten to the twins they point at: a page's twin lives at the page's
  URL, which for `art-computer/play.md` is one directory deeper than the
  source (`/art-computer/play/index.md`), and `open-source.md` is served as
  `/open-source/index.md`. A redirected URL gets a twin that names the new
  page, so an agent holding an old link still lands.
- /llms.txt: what the site is and one line per page with its HTML and
  Markdown URLs (https://llmstxt.org).

Every rendered page also links its twin as rel="alternate", and its code
blocks keep spaces as plain text: Pygments wraps each run of whitespace in its
own span, and some HTML-to-text tools drop or add spaces around those spans
(an agent reads `npm i -g@feralfile/cli`).
"""

import re
from pathlib import Path
from shutil import copyfile

_PAGES = []


def on_files(files, config, **_kwargs):
    """Remember every documentation page; on_post_build writes their twins and llms.txt."""
    _PAGES[:] = list(files.documentation_pages())
    return files


_WHITESPACE_SPAN = re.compile(r'<span class="w">(\s*)</span>')


def on_post_page(output, page, config, **_kwargs):
    """Link the page's Markdown twin and unwrap whitespace spans in code blocks."""
    output = _WHITESPACE_SPAN.sub(r"\1", output)
    link = '<link rel="alternate" type="text/markdown" href="index.md">'
    return output.replace("</head>", f"{link}\n</head>", 1)


def _title(src):
    for line in src.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return src.stem


# A Markdown link or image target that is relative: no scheme, not a fragment,
# not site-absolute. Group 1 is the path, group 2 the optional fragment.
_RELATIVE_LINK = re.compile(r"\]\((?![a-z][a-z0-9+.\-]*:|#|/)([^)\s#]+)(#[^)]*)?\)")


def _twin_text(src, page):
    """The page's Markdown with relative links pointing at the served files."""
    source_is_index = src.name == "index.md"

    def served(match):
        path, fragment = match.group(1), match.group(2) or ""
        if path.startswith("./"):
            path = path[2:]
        if not source_is_index:
            path = "../" + path  # the twin sits one directory below its source
        if path.endswith(".md") and not (path == "index.md" or path.endswith("/index.md")):
            path = path[: -len(".md")] + "/index.md"
        return f"]({path}{fragment})"

    return _RELATIVE_LINK.sub(served, src.read_text(encoding="utf-8"))


def _twin_url(page_url):
    return "" if page_url in (".", "./") else page_url


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
    by_src_uri = {}
    for page in _PAGES:
        src = Path(page.abs_src_path)
        url = _twin_url(page.url)
        twin = site / url / "index.md"
        twin.parent.mkdir(parents=True, exist_ok=True)
        twin.write_text(_twin_text(src, page), encoding="utf-8")
        by_src_uri[page.src_uri] = (src, url)
        lines.append(f"- [{_title(src)}]({base}/{url}): Markdown at {base}/{url}index.md")
    (site / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # mkdocs-redirects writes an HTML page at each old URL; give it a Markdown
    # twin too, naming the page's new Markdown URL.
    redirects = config["plugins"].get("redirects")
    for old, new in (redirects.config["redirect_maps"] if redirects else {}).items():
        if new not in by_src_uri:
            continue
        src, url = by_src_uri[new]
        old_url = old[: -len("index.md")] if old.endswith("index.md") else old[: -len(".md")] + "/"
        twin = site / old_url / "index.md"
        twin.parent.mkdir(parents=True, exist_ok=True)
        twin.write_text(
            f"# {_title(src)}\n\nThis page moved. Read {base}/{url}index.md\n",
            encoding="utf-8",
        )
