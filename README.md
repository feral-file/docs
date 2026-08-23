# Feral File Docs

Authoritative documentation for Feral File’s open technology stack.

* Live site: **https://docs.feralfile.com**
* Private companion repo: `feral-file/docs-private`
* Device‑specific docs (FF1): see submodule `docs/devices/ff1`.

## Quick start

```bash
git clone https://github.com/feral-file/docs.git
cd docs
git submodule update --init   # pulls in ff1-docs
python -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt

mkdocs serve
```

## Mobile app changelog contract

`docs/changelog.md` is the one authored source for the in-app screen, GitHub
releases, Google Play, and TestFlight. Prepend each mobile release in this
shape:

```markdown
## Aug 22 2026

### Feral File Mobile App 1.5.5 — Short title

Release-note body, no more than 500 characters.

---
```

The full date heading is required, with exactly one space after `##`: the app
groups entries by that section, and the store publisher accepts the same
month/day/year shape. Historical yearless headings before version 1.5.5 are
explicitly grandfathered. Versions
must be unique and ordered newest to oldest. Keep the body non-empty and do not
put another `##`, `###`, or `---` inside it because those markers end the
store-note excerpt. The 500-character limit includes Markdown whitespace.
Once a version is published, treat its entry as an immutable release record; a
code or notes correction gets a new patch version.

Validate before opening a PR:

```bash
python -m unittest tests/test_validate_mobile_changelog.py
python scripts/validate_mobile_changelog.py docs/changelog.md
mkdocs build --strict
```
