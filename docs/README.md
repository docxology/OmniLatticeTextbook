# `OmniLatticeTextbook` Documentation

The **Infinite Octaves Omni-Lattice Textbook** — a filled fork of the modular
textbook scaffold. The book's structure is data-driven from a single
[`docs/manuscript/config.yaml`](../docs/manuscript/config.yaml); a tested
Python backbone under [`src/`](../src) scaffolds, validates, and illustrates
the manuscript; and thin orchestrator [`scripts/`](../scripts) wire everything
into the repository's reproducible pipeline.

The book is complete: 4 parts, 30 chapters, 30 labs, 30 question banks, 4
unit intros, and 7 appendices, with 31 corpus citation keys and 44 glossary
anchors.

If you are new here, read these in order.

## Guides

| Guide | Read it to learn |
| --- | --- |
| [`architecture.md`](architecture.md) | The two-layer + thin-orchestrator design as applied here: `config.yaml` as source of truth, the `src/textbook` engine, visualization + mermaid, render-time hydration, and the data flow into the rendered book. |
| [`manuscript_guide.md`](manuscript_guide.md) | How the manuscript is laid out (parts → chapters → labs → questions), the per-chapter required-element contract, and how auto-numbering and cross-references work. |
| [`authoring_guide.md`](authoring_guide.md) | How to grow the book from its filled state — add parts/chapters, scaffold, fill, and keep the contract green. |
| [`visualization_guide.md`](visualization_guide.md) | How figures and Mermaid diagrams are generated deterministically, the `<part_id>_<stem>.png` filename contract, render-time hydration, and how `mmdc`/`.puppeteer.json` get Chrome to the renderer. |
| [`testing_guide.md`](testing_guide.md) | The test suite, the no-mocks policy, the 90% coverage gate, the manuscript-integrity tests, and the `audit_textbook_quality.py` gates — with exact commands. |

## Source-of-truth files

These are the artifacts the guides keep pointing back to:

- [`docs/manuscript/config.yaml`](../docs/manuscript/config.yaml) — the book structure
  (parts, chapters, labs, question banks, appendices, layout, typography,
  render formats).
- [`src/textbook/`](../src/textbook) — the content engine
  (`constants`, `config`, `toc`, `content`, `models`, `contracts`, `audit`).
- [`src/visualization/`](../src/visualization) and
  [`src/mermaid/`](../src/mermaid) — deterministic figure and diagram generators.
- [`data/`](../data) — the claim ledger and numeric-facts registry (with
  `_evidence_*` chunk files) that anchor headline numbers.
- [`scripts/`](../scripts) — thin orchestrators
  (`generate_figures.py`, `generate_diagrams.py`, `analysis.py`,
  `scaffold_chapter.py`, `audit_textbook_quality.py`,
  `z_generate_manuscript_variables.py`).
- [`tests/`](../tests) — the full suite, including
  [`test_manuscript_integrity.py`](../tests/test_manuscript_integrity.py).

## Authoring contract in one screen

Every chapter carries a labelled H1 (`{#sec:<part>_<stem>}`), at least one
figure (`{#fig:...}`) with alt text, a metadata badge, a Study Blueprint,
Learning Objectives, a worked formalism (an equation `{#eq:...}` plus a
parameter table `{#tbl:...}`), an inline `` ```mermaid `` diagram, and
Summary / Key Terms / Further Reading / Practice sections. Cross-references use
pandoc-crossref syntax (`[@fig:..]`, `[@tbl:..]`, `[@eq:..]`, `[@sec:..]`) —
never hand-numbered. Citations `[@key]` must resolve in the closed 31-key
namespace of [`references.bib`](../docs/manuscript/references.bib); glossary
links `[**term**](#gl:<anchor>)` must resolve in the 44-anchor namespace of
[`glossary.md`](../docs/manuscript/glossary.md). The full contract and how to
extend it live in the [authoring guide](authoring_guide.md).

## Tooling

All commands use `uv` (never `pip`/`npm`). From inside this project directory,
tests run with `uv run --extra dev python -m pytest`; rendering and
validation run from the [docxology/template](https://github.com/docxology/template)
monorepo root (`uv run python scripts/pipeline/stage_03_render.py --project
working/OmniLatticeTextbook`, then `stage_04_validate.py` the same way), with
this repository placed at `projects/working/OmniLatticeTextbook`. Figures and
diagrams are produced by the scripts, never by hand. See each guide for exact
invocations.
