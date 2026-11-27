# `src/mermaid/` — Agent Guide

Deterministic Mermaid diagram generation.

**Contents.** `diagram_specs.yaml` declares each diagram. `diagrams.py` builds
the specs, and `renderer.py` writes PNGs to `output/figures/mermaid/`. If it
cannot render a PNG, the standalone generator writes the `.mmd` source.
`_resolve_mmdc(start=None)` searches for `node_modules/.bin/mmdc` from `start`
or this module, then checks PATH.

**Contract.** Diagrams are generated to `output/figures/mermaid/` and tracked
as public release artifacts when they stay below the size ceiling; reproduce
them with `scripts/generate_diagrams.py`. The [pinned reader build](../../docs/rendering.md)
uses a separate inline Mermaid path and needs an available browser.

See the project [`AGENTS.md`](../../AGENTS.md) and [`docs/`](../../docs/) for the full map.
