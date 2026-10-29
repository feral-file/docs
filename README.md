# Feral File Docs

Authoritative documentation for Feral File’s open technology stack.

* Live site: **https://docs.feralfile.com**
* Private companion repo: `feral-file/docs-private`
* Art Computer docs: `docs/art-computer/`.

## Quick start

```bash
git clone https://github.com/feral-file/docs.git
cd docs
python -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve
```

## Weekly product updates

`docs/changelog.md` is the public, authored weekly summary. Write one entry
for a week with meaningful changes, grouped by what people can now do. Lead
with the news, then use three to five changes when there is enough to say.
Skip quiet weeks; an urgent action can be announced immediately.

Use `## Week of Sep 21 2026` (the Monday starting that week), newest first.
End the entry with the versions it covers and any iOS/Android availability
differences. Check the public stores or promotion record: a merged PR,
GitHub release, TestFlight build, or internal Play upload is not evidence of
public availability. Correct a factual mistake in place.

Write the entry when you promote the build, then label the PR
`awaiting-stores` and leave it. The `store-availability` workflow runs
hourly: it reads the version from the closing line ("available in X.Y.Z on
iOS and Android"), checks the App Store lookup API and the Play store page,
and merges the PR once both serve that version. If one store has served it
for 48 hours and the other has not, the workflow comments once; rewrite the
closing line as an availability difference and merge by hand. Run it locally
with `python3 .github/scripts/store_availability.py --dry-run`.

The first trial groups mobile versions 1.8.10–1.8.11. Earlier per-release
entries remain as history, including the records used to ground that trial.
Judge it by whether a reader can understand what changed and which version
they need in under a minute.

GitHub keeps automatically generated per-version details. The mobile store
workflows generate a short link to this page; they do not parse this Markdown.
There is no 500-character limit on the weekly entry and no second set of
release copy to author. The mobile workflow change is in `feral-file/ff-app`;
its Release Notes browser handoff is PR #967. The raw `/docs/changelog.md`
endpoint remains available to already-installed versions with the old reader.

Validate before opening a PR:

```bash
mkdocs build --strict
cmp docs/changelog.md site/docs/changelog.md
python3 scripts/check-twins.py site
```

## After a Material upgrade

The brand layer (`docs/stylesheets/extra.css`, `overrides/main.html`) restates three Material assumptions that break on a `mkdocs-material` bump: the search float collapses the adjacent nav link, the results panel is revealed by a toggle outside the header, and the rail width is pinned by a padding rule. `scripts/brand-check.js` reads all three in a built page and returns them as JSON. Build the site at the old and the new version, run the check on each, and compare the readings; a pixel diff of screenshots at 1280 and 390 wide is the second check.

```bash
# build each version to its own directory, then, with ff3's shot script (needs Chromium on PATH):
DIST=<site dir> SHOT_PORT=4411 node ~/Work/ff3/scripts/shot.mjs /art-computer/ 1280x800 - old.png "$(cat scripts/brand-check.js)"
DIST=<site dir> SHOT_PORT=4412 node ~/Work/ff3/scripts/shot.mjs /art-computer/ 390x844 - old-phone.png "$(cat scripts/brand-check.js)"
```

## License

The documentation is CC BY 4.0 (see [LICENSE](LICENSE)); the faceplate files under `docs/art-computer/faceplates/` carry their own CC BY-SA 4.0 license.
