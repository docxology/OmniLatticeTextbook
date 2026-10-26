---
name: template-textbook
description: OmniLatticeTextbook manuscript engine — parts/chapters/labs/question banks from config.yaml, auto-numbering, deterministic figures, structural contract enforcement.
version: 0.1.2
author: Daniel Ari Friedman
license: Apache-2.0 AND CC-BY-4.0
tags: [textbook, manuscript, scaffold, contract]
---

# OmniLatticeTextbook

Project-scoped skill for **The Infinite Octaves Omni-Lattice Textbook** — this
repository, a filled fork of `docxology/template_textbook`. Load this when
working inside the project.

## When to Use

- Working inside this repository — running scripts, editing `src/`, editing
  chapters, or regenerating figures and diagrams.
- Filling or extending the manuscript structure declared in
  `docs/manuscript/config.yaml`.
- Validating that the repository's contracts (thin-orchestrator, layer
  boundaries, no-mocks testing) still hold after changes.

## Quick Reference

All commands run from **this repository's root**.

```bash
# Test suite with the 90% coverage gate
uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90

# Structural scaffold gate (reports stubs but allows them)
uv run python scripts/audit_textbook_quality.py

# Filled-manuscript gate (this book passes: zero stubs)
uv run python scripts/audit_textbook_quality.py --require-complete

# Regenerate deterministic figures and diagrams
uv run python scripts/generate_figures.py
uv run python scripts/generate_diagrams.py

# Materialise any missing chapter/lab/question stubs declared in config.yaml
uv run python scripts/scaffold_chapter.py
```

Rendering (PDF/HTML/EPUB/DOCX) is **not** part of this repository: it runs
through the host `docxology/template` monorepo pipeline with this repository
placed at `projects/working/OmniLatticeTextbook` — see
[`STANDALONE.md`](../../../STANDALONE.md).

## Pitfalls

- **Keep scripts thin.** Business logic belongs in `src/`, not in `scripts/`.
- **No mocks.** All tests must use real data, real files, and real
  computation.
- **`config.yaml` is the only source of truth** for parts, chapters, labs,
  question banks, and appendices. Never hand-number anything.
- **Keep the closed namespaces in lockstep.** `CITATION_KEYS` (31) and
  `GLOSSARY_ANCHORS` (44) in `src/textbook/constants.py` must match
  `docs/manuscript/references.bib` and `docs/manuscript/glossary.md`.
- **Keep `config.yaml.example` in lockstep with `config.yaml`** —
  `tests/test_contracts.py::test_live_and_example_config_shapes_are_lockstep`
  enforces matching shapes.
- **Outputs are disposable.** Never hand-edit `output/` — regenerate from
  source and config.
- **Choose the audit mode deliberately.** The default audit validates a
  fillable scaffold; `--require-complete` is the zero-stub gate this book
  passes.
- **On a slow external drive**, prefer `UV_PROJECT_ENVIRONMENT=/tmp/<name>-venv`
  and run the suite from a copy on the internal disk.

## Cross-refs

- Project contract: [`AGENTS.md`](../../../AGENTS.md)
- README: [`README.md`](../../../README.md)
- Provenance and deposit prep: [`STANDALONE.md`](../../../STANDALONE.md)
- Forward backlog: [`TODO.md`](../../../TODO.md)
