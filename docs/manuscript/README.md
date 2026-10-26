# Manuscript Directory

This directory holds the **content** of the textbook — the Markdown the renderer
turns into a PDF. Everything here is driven by one file, [`config.yaml`](config.yaml),
which is the single source of truth for the book's structure.

## Layout

```
manuscript/
├── config.yaml          # THE single source of truth: parts, chapters, front
│                        #   matter, appendices, labs, question banks, layout,
│                        #   typography, numbering. Edit this to grow the book.
├── front_matter.md      # Title, "About This Book", edition/licence, navigation
├── preface.md           # Preface (purpose, audience, how to use the book)
├── preamble.md          # LaTeX preamble (packages, margins) — fenced ```latex
├── references.bib       # BibTeX database; every [@key] must resolve here
├── glossary.md          # Master glossary; anchors {#gl:...} for [**term**] links
├── part_0/              # Orientation and Methods        (5 chapters)
├── part_I/              # Foundations: Constants, Primes, and Rhyme (6 chapters)
├── part_II/             # Core Systems: The Physical Engine Shelf (8 chapters)
├── part_III/            # Implementations, Companions, and Frontiers (11 chapters)
├── labs/                # One guided lab per chapter, grouped by part
│   ├── part_0/  part_I/  part_II/  part_III/
├── questions/           # One question bank per chapter, grouped by part
│   ├── part_0/  part_I/  part_II/  part_III/
├── appendices/          # Appendices A–E and G: authoring guide, notation, math
│                        #   review, formalism table, format gallery, index
│                        #   (Appendix F, the master glossary, is glossary.md)
└── assets/              # Cover image and other static assets
```

Each chapter file lives under `part_<label>/<stem>.md`. Its companion lab is
`labs/<part>/lab_<stem>.md` and its companion question bank is
`questions/<part>/q_<stem>.md`. These names are not arbitrary — they are derived
from `config.yaml`, and `scripts/scaffold_chapter.py` will materialise any
missing file in exactly the right shape.

## How `config.yaml` Controls Everything

| You change in `config.yaml`… | …and this updates automatically |
| --- | --- |
| `units:` (add/remove a chapter) | Table of contents, chapter numbers, integrity tests |
| `appendices.labs` / `.questions` | Which labs and banks are included and titled |
| `front_matter.files` | Front-matter order and titles |
| `rendering.number_*` | Whether chapters/figures/equations/tables are numbered |
| `layout` / `typography` | Page geometry, fonts, link colour |

You never hand-number anything. Figures, tables, equations, sections, labs, and
question banks are referenced by **label** (e.g. `[@fig:part_0_orientation]`) and
numbered at render time by `pandoc-crossref`. See [`SYNTAX.md`](SYNTAX.md).

## Render Flow

The PDF is built, not typeset by hand. From the repository root:

```bash
# 1. Generate figures and diagrams (the analysis stage; deterministic)
uv run python scripts/pipeline/stage_02_analysis.py --project working/OmniLatticeTextbook

# 2. Render the manuscript to PDF (Pandoc + pandoc-crossref, multiple passes)
uv run python scripts/pipeline/stage_03_render.py --project working/OmniLatticeTextbook
```

The renderer reads
`config.yaml`, assembles the front matter, parts, chapters, appendices, labs, and
question banks in declared order, resolves cross-references and citations, and
writes the rendered PDF, HTML, EPUB, and DOCX under the project's `output/`
directory.

> **Tip:** a single render pass leaves cross-references and citations showing as
> `??`. The full pipeline runs the multiple LaTeX passes (plus BibTeX) needed to
> resolve them — prefer it for a final check.

## Validating as You Write

```bash
# Structural contract + stub accounting
uv run python scripts/audit_textbook_quality.py

# Manuscript-integrity tests (headings, labels, citations, glossary anchors)
uv run --extra dev python -m pytest tests/test_manuscript_integrity.py -v

# Full suite (engine, visuals, diagrams, structure)
uv run --extra dev python -m pytest tests/ -v
```

For the full editing contract see [`AGENTS.md`](AGENTS.md); for the authoring
walkthrough see [`appendices/appendix_authoring_guide.md`](appendices/appendix_authoring_guide.md).
