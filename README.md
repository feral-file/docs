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
```
