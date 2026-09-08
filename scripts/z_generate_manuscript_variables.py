"""Hydrate the render-time manuscript (output/manuscript) from docs/manuscript.

The shared rendering pipeline prefers an injected manuscript at
``output/manuscript/`` when present (see
``infrastructure.rendering._manuscript_source.resolve_manuscript_dir``).
Materialising that tree here keeps the Omni-Lattice fork on the same
render-time layout as first-class pipeline projects, which places the
inline-Mermaid artifact directory at ``output/figures/mermaid_inline/``.

The copy is deterministic: file contents are transferred byte-for-byte with no
timestamp or template-variable substitution (this manuscript carries no
``{{variable}}`` placeholders). Existing files are overwritten; extraneous
files from earlier runs are left in place so partial renders stay inspectable.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SOURCE = PROJECT / "docs" / "manuscript"
DEST = PROJECT / "output" / "manuscript"

_SKIP_DIRS = frozenset({"__pycache__", ".pytest_cache"})


def _copy_tree() -> int:
    if not SOURCE.is_dir():
        print(f"source manuscript missing: {SOURCE}", file=sys.stderr)
        return 1
    DEST.mkdir(parents=True, exist_ok=True)
    copied = 0
    for src in sorted(SOURCE.rglob("*")):
        if src.is_dir():
            continue
        if any(part in _SKIP_DIRS for part in src.relative_to(SOURCE).parts):
            continue
        dst = DEST / src.relative_to(SOURCE)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied += 1
    print(f"hydrated {copied} file(s) into {DEST}")
    return 0


def main() -> int:
    """Materialise the injected manuscript tree."""
    return _copy_tree()


if __name__ == "__main__":
    sys.exit(main())
