#!/usr/bin/env python3
"""Validate the Markdown contract shared by app and store release notes."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


MOBILE_HEADING_PREFIX = "### Feral File Mobile App "
MOBILE_HEADING = re.compile(
    r"^### Feral File Mobile App "
    r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)"
    r"(?: (?:—|-) .+)?$"
)
DATE_HEADING = re.compile(r"^[A-Za-z]+ [0-9]{1,2},? [0-9]{4}$")
LEGACY_DATE_HEADING = re.compile(r"^[A-Za-z]+ [0-9]{1,2}$")
ENTRY_SEPARATOR = re.compile(r"^---[ \t]*$")
# 1.5.5 is the first release governed by this validator. Older yearless
# sections remain readable history, but every new entry must use a full date.
DATED_CHANGELOG_CONTRACT_VERSION = (1, 5, 5)


@dataclass(frozen=True)
class MobileEntry:
    """One canonical mobile changelog entry."""

    version: tuple[int, int, int]
    version_text: str
    line_number: int
    date_section: str | None
    body: str


def _entry_body(lines: list[str], heading_index: int) -> str:
    body: list[str] = []
    for line in lines[heading_index + 1 :]:
        if (
            line.startswith("## ")
            or line.startswith("### ")
            or ENTRY_SEPARATOR.fullmatch(line)
        ):
            break
        body.append(line)
    while body and not body[0].strip():
        body.pop(0)
    while body and not body[-1].strip():
        body.pop()
    return "\n".join(body)


def validate_mobile_changelog(markdown: str) -> list[str]:
    """Return every contract violation in a changelog document."""

    lines = markdown.splitlines()
    entries: list[MobileEntry] = []
    errors: list[str] = []
    date_section: str | None = None

    for index, line in enumerate(lines):
        if line.startswith("## ") and not line.startswith("### "):
            date_section = line.removeprefix("## ").strip() or None
            continue

        if not line.startswith(MOBILE_HEADING_PREFIX):
            continue

        match = MOBILE_HEADING.fullmatch(line)
        if match is None:
            errors.append(
                f"Line {index + 1}: invalid mobile heading; expected "
                "'### Feral File Mobile App X.Y.Z — Title'."
            )
            continue

        version = tuple(int(match.group(name)) for name in ("major", "minor", "patch"))
        version_text = ".".join(str(part) for part in version)
        entries.append(
            MobileEntry(
                version=version,
                version_text=version_text,
                line_number=index + 1,
                date_section=date_section,
                body=_entry_body(lines, index),
            )
        )

    if not entries:
        errors.append("No canonical Feral File Mobile App entries found.")
        return errors

    seen: set[tuple[int, int, int]] = set()
    previous: tuple[int, int, int] | None = None
    for entry in entries:
        if entry.date_section is None:
            errors.append(
                f"Line {entry.line_number}: mobile {entry.version_text} must be "
                "inside a '## <date>' date section."
            )
        elif not DATE_HEADING.fullmatch(entry.date_section) and not (
            entry.version < DATED_CHANGELOG_CONTRACT_VERSION
            and LEGACY_DATE_HEADING.fullmatch(entry.date_section)
        ):
            errors.append(
                f"Line {entry.line_number}: mobile {entry.version_text} must be "
                "inside a valid date section such as '## Aug 22 2026'."
            )
        if not entry.body:
            errors.append(
                f"Line {entry.line_number}: mobile {entry.version_text} body is empty."
            )
        if entry.version in seen:
            errors.append(f"Duplicate mobile version {entry.version_text}.")
        seen.add(entry.version)
        if previous is not None and entry.version >= previous:
            errors.append(
                "Canonical mobile versions must appear newest to oldest; "
                f"found {entry.version_text} after {'.'.join(map(str, previous))}."
            )
        previous = entry.version

    latest = entries[0]
    if len(latest.body) > 500:
        errors.append(
            f"Latest mobile entry {latest.version_text} is {len(latest.body)} "
            "characters; Google Play allows 500."
        )

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: validate_mobile_changelog.py CHANGELOG.md", file=sys.stderr)
        return 64

    changelog = Path(argv[1])
    errors = validate_mobile_changelog(changelog.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated mobile changelog contract: {changelog}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
