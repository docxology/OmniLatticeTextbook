# Manuscript Guide

How the book is laid out, what every chapter must contain, and how numbering and
cross-references are computed rather than typed.

## Layout

The structure is declared in
[`docs/manuscript/config.yaml`](../docs/manuscript/config.yaml) and mirrored on disk:

```
manuscript/
  config.yaml        # the structure (parts → chapters → labs → questions)
  references.bib     # bibliography; every [@key] must resolve here
  glossary.md        # every [**term**](#gl:anchor) must resolve here (Appendix F)
  front_matter.md    # front matter + preface (ordering declared in config)
  preface.md
  part_0/            # Orientation and Methods
  part_I/            # Foundations: Constants, Primes, and Rhyme
  part_II/           # Core Systems: The Physical Engine Shelf
  part_III/          # Implementations, Companions, and Frontiers
  labs/<part_id>/    # lab_<stem>.md, one per chapter
  questions/<part_id>/ # q_<stem>.md, one per chapter
  appendices/        # reference appendices A–E and G
  assets/            # deterministic cover image, etc.
```

The book's parts and chapters are declared in `docs/manuscript/config.yaml` (the single
source of truth); the filled book is organised as:

| Part | Title | Chapters |
| --- | --- | --- |
| 0 | Orientation and Methods | orientation, living-pem, tensor-decoupling, master-synthesis, octave-map |
| I | Foundations: Constants, Primes, and Rhyme | fractal-constant, prime-parity, holographic-rhyme, multidimensional-rhyme, topology-void, higgs-awareness |
| II | Core Systems: The Physical Engine Shelf | proton-theater, viscosity-light, eddy-current-mirror, crystalline-field, metrological-overlap, metamorphic-octaves, planetary-core, singularity-crystal |
| III | Implementations, Companions, and Frontiers | cmos-protonic, protein-folding, volumetric-storage, kinematic-recycling, moving-up-stack, reality-bridge, y-chromosome, pdvsa-gateway, macro-protein, invisible-frontier, frontiers |

30 chapters in all, each with a matching lab (`labs/<part_id>/lab_<stem>.md`)
and question bank (`questions/<part_id>/q_<stem>.md`), plus one
`unit_intro.md` per part. Lab and question display titles are derived
from the parent chapter title by [`src/textbook/toc.py`](../src/textbook/toc.py)
— the config lists only file names.

Config path safety is part of the contract: `units:` takes precedence over the
legacy `parts:` alias, and declared part directories plus chapter/intro files
must be relative, portable, single-level paths ending in `.md`. Traversal,
absolute paths, malformed mappings, and duplicate source paths are rejected by
`textbook.config.validate_config` before scaffolding or auditing begins.

## The per-chapter contract

Every chapter must carry the elements below. They are enforced by
[`textbook.content.validate_chapter`](../src/textbook/content.py) against the
literal tokens and headings in
[`src/textbook/constants.py`](../src/textbook/constants.py), so this list is the
contract, not a summary of it.

- **Labelled H1** — `# <Title> {#sec:<part_id>_<stem>}`.
- **At least one figure** — `{#fig:...}` with descriptive alt text (an `<!-- alt: ... -->`
  comment alongside the `![]()` image).
- **Metadata badge** — `<!-- chapter-metadata-badge -->` followed by a level /
  read-time / lecture-time / prerequisites line.
- **Study Blueprint** — opened by `<!-- curriculum-scaffold-start -->`
  (big idea, core concepts, quantitative lens, data skill, misconception,
  primary lab, question bank, bridge to computation).
- **Learning Objectives** section.
- **A worked formalism** — at least one equation `{#eq:...}` *and* one parameter
  table `{#tbl:...}`, pointing to the tested function in `textbook.models`.
- **An inline diagram** — a `` ```mermaid `` fenced block.
- **Closing sections** — `Summary`, `Key Terms`, `Further Reading`, `Practice`
  (the `REQUIRED_SECTION_HEADINGS`).

`STUB_MARKERS` (`<!-- STUB`, `TODO:`, `TKTK`) mark unwritten content. The
filled book contains **zero** of them; `scripts/audit_textbook_quality.py
--require-complete` enforces that, and any newly scaffolded chapter must be
filled before the gate goes green again.

## Numbering and cross-references

Numbering is **computed**, never hand-typed:

- Chapters number sequentially across the whole book; the order comes from the
  `units` list in `config.yaml` and is resolved by
  [`textbook.toc.chapter_number`](../src/textbook/toc.py).
- Within the rendered document, **pandoc-crossref** assigns figure, table,
  equation, and section numbers from the `{#fig:...}`, `{#tbl:...}`,
  `{#eq:...}`, `{#sec:...}` labels.

Always reference, never number, in prose:

| To refer to a… | Write | Not |
| --- | --- | --- |
| Section / chapter | `[@sec:part_0_octave-map]` | "Chapter 5" |
| Figure | `[@fig:part_0_octave-map]` | "Figure 5.1" |
| Table | `[@tbl:...]` | "Table 2" |
| Equation | `[@eq:...]` | "Equation 3" |

If you hand-number, the rendered book will show dangling `??` once numbers
shift; the cross-ref keeps prose correct as the book grows.

## Citations and glossary

- Citations use `[@key]` and must resolve in
  [`references.bib`](../docs/manuscript/references.bib). The contract keys are the
  31 in `CITATION_KEYS` — the `mendez2026*` corpus of the SS Vibelandia engine
  papers (ship blog, catalog, Living PEM, the 99-octave digit map, prime-parity,
  holographic rhyme, the physical engine shelf, and the engineering companions).
  There are no placeholder keys. To add a source, add the entry to
  `references.bib` and `CITATION_KEYS` together.
- Glossary links use `[**term**](#gl:<anchor>)` and must resolve in
  [`glossary.md`](../docs/manuscript/glossary.md). The contract anchors are the
  44 `GLOSSARY_ANCHORS` (omni-lattice, octave band, digit drawer, prime parity,
  holographic rhyme, and the rest of the book's vocabulary). New terms go in
  `glossary.md` **and** `GLOSSARY_ANCHORS`.

The manuscript-integrity tests fail if a chapter cites a key or links an anchor
that is not defined — see the [testing guide](testing_guide.md).

## Rendering

Rendering is handled by the monorepo's generic `infrastructure/` rendering stage
(pandoc + pandoc-crossref → PDF/HTML/EPUB/DOCX), driven by the same `config.yaml`
for layout, typography, and front-matter ordering. From the
[docxology/template](https://github.com/docxology/template) monorepo root, with
this repository at `projects/working/OmniLatticeTextbook`:

```bash
uv run python scripts/pipeline/stage_03_render.py --project working/OmniLatticeTextbook
uv run python scripts/pipeline/stage_04_validate.py --project working/OmniLatticeTextbook
```

Before rendering, `scripts/z_generate_manuscript_variables.py` hydrates the
render-time tree (`docs/manuscript/` → `output/manuscript/`) so the stage
consumes the injected manuscript like a first-class pipeline project.
Figures must already exist under `output/figures/` (run `generate_figures.py`
first) so the chapters'
`![...](../../output/figures/<part_id>_<stem>.png)` paths resolve. The numbering
settings live under `rendering:` in `config.yaml` (`number_chapters`,
`number_figures`, `number_equations`, `number_tables`, `toc_depth`); the output
formats under `render.formats` (PDF, HTML, EPUB, DOCX; slides off by default).
