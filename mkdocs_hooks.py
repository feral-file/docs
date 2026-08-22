"""Small build hooks for public files that MkDocs would otherwise render."""

from pathlib import Path
from shutil import copyfile


def on_post_build(config, **_kwargs):
    """Expose the authored changelog unchanged for app and release clients."""
    source = Path(config["docs_dir"]) / "changelog.md"
    destination = Path(config["site_dir"]) / "docs" / "changelog.md"
    destination.parent.mkdir(parents=True, exist_ok=True)
    copyfile(source, destination)
