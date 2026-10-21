#!/usr/bin/env python3
"""Check meeting structure and inline Markdown file links without network access.

Intentionally handles the repository's simple inline-link convention, not the full
Markdown grammar. Anchors, reference links, HTML, and external URLs are not checked.
"""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MEETING = re.compile(r"([0-9]{2})-[a-z0-9]+(?:-[a-z0-9]+)*")
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+\"[^\"\n]*\")?\s*\)")
IGNORED = {".git", ".venv", "__pycache__", "node_modules"}


def links(path):
    """Yield line numbers and destinations, excluding fenced and inline code."""
    fence = None
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, tail = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence is None:
            line = re.sub(r"(`+).*?\1", "", line)
            for match in LINK.finditer(line):
                yield number, match.group(1).strip("<>")


def check(root):
    errors = []
    catalogue = root / "README.md"
    if not catalogue.is_file():
        return ["README.md: missing root catalogue"]
    indexed = {urlsplit(url).path for _, url in links(catalogue)}
    ids = set()
    for folder in sorted(root.iterdir()):
        if not folder.is_dir() or not folder.name[:1].isdigit():
            continue
        match = MEETING.fullmatch(folder.name)
        if not match or match[1] == "00":
            errors.append(f"{folder.name}: expected NN-topic with a decimal ID 01-99")
            continue
        meeting_id = match[1]
        if meeting_id in ids:
            errors.append(f"{folder.name}: duplicate meeting ID {meeting_id}")
        ids.add(meeting_id)
        readme = folder / "README.md"
        if not readme.is_file():
            errors.append(f"{folder.name}: missing README.md")
        elif not re.match(
            rf"\A# Meeting {meeting_id}: \S", readme.read_text(encoding="utf-8")
        ):
            errors.append(f"{folder.name}/README.md: expected '# Meeting {meeting_id}: Topic'")
        if f"{folder.name}/README.md" not in indexed:
            errors.append(f"README.md: missing catalogue link to {folder.name}/README.md")

    for path in sorted(root.rglob("*.md")):
        if any(part in IGNORED for part in path.relative_to(root).parts):
            continue
        for number, destination in links(path):
            url = urlsplit(destination)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (root if url.path.startswith("/") else path.parent) / unquote(
                url.path.lstrip("/")
            )
            target = target.resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f"{path.relative_to(root)}:{number}: link leaves repository: {destination}")
            elif not target.exists():
                errors.append(f"{path.relative_to(root)}:{number}: missing local target: {destination}")
    return errors


if __name__ == "__main__":
    problems = check(ROOT)
    if problems:
        print("\n".join(problems), file=sys.stderr)
        sys.exit(1)
    print("Repository structure and inline Markdown file links passed.")
