# The Infinite Octaves Omni-Lattice Textbook

**The Infinite Octaves Omni-Lattice Textbook** — *A Modular Synthesis of the
SynthOBS Engine Papers*, by **Daniel Ari Friedman** (FractiAI). The book
synthesises the Infinite Octaves Omni-Lattice engine papers of the SS
Vibelandia ship blog — authored by **Prudencio Mendez** (FractiAI · SS
Vibelandia · SynthOBS Autonomous Agent Program; catalogued at
<https://www.ssvibelandiaquestfest24x365.com/papers>) — into a modular,
data-driven manuscript: 4 parts → 30 chapters → 30 labs → 30 question banks,
a tested computational backbone under `src/` (23 tested formalisms in
`textbook.models`), deterministic figure and diagram generators, and a
content scaffold/validation engine that keeps the whole book pinned to one
structural contract.

Forked from
[docxology/template_textbook](https://github.com/docxology/template_textbook),
it inherits the modular-textbook shape: everything downstream — the table of
contents, chapter auto-numbering, figure generation, lab/question wiring, and
the manuscript-integrity tests — reads a single source of truth:
[`docs/manuscript/config.yaml`](docs/manuscript/config.yaml).

The book is **complete**: every declared chapter, lab, and question bank is
filled (zero stubs — verified by
`scripts/audit_textbook_quality.py --require-complete`), the six reference
appendices plus the master glossary are in place, and the render pipeline
produces PDF, HTML, DOCX, and EPUB from the same sources.

## The book at a glance

| Part | Title | Chapters |
| --- | --- | --- |
| 0 | Orientation and Methods | 5 |
| I | Foundations: Constants, Primes, and Rhyme | 6 |
| II | Core Systems: The Physical Engine Shelf | 8 |
| III | Implementations, Companions, and Frontiers | 11 |

30 chapters in all, each with a matching lab (`docs/manuscript/labs/`) and
question bank (`docs/manuscript/questions/`), plus a unit intro per part.
The bibliography ([`docs/manuscript/references.bib`](docs/manuscript/references.bib))
defines the 31 citation keys of the Mendez engine-paper corpus — no
placeholder references remain. Three chapters are worked in particular depth
and serve as finished-prose references:

- [`part_0/octave-map.md`](docs/manuscript/part_0/octave-map.md) — *Nine
  Digits, Ninety-Nine Octaves*: the 99-octave digit map, with both
  conventions of the octave term implemented and tested behind
  `textbook.models.octave_term`.
- [`part_I/fractal-constant.md`](docs/manuscript/part_I/fractal-constant.md)
  — *El Gran Sol's Fractal Constant*: a model-derivation chapter around the
  golden-ratio formalism (`phi_powers`, `phi_fibonacci`, `phi_dual`).
- [`part_III/frontiers.md`](docs/manuscript/part_III/frontiers.md) —
  *Frontiers and the Research Program*: a source-backed synthesis chapter
  that maps the corpus's open questions and cites the papers it integrates.

## Publication status

**Not yet deposited.** No DOI has been minted for this fork: the
`publication:` section of `config.yaml` has empty `doi`/`version_doi` fields
and no `published_artifacts`, and the citation sidecars at the project root
([`CITATION.cff`](CITATION.cff), [`.zenodo.json`](.zenodo.json),
[`codemeta.json`](codemeta.json)) carry intentionally blank DOI fields. They
are otherwise filled in (title, author, ORCID, license, repository
`docxology/OmniLatticeTextbook`) so a first Zenodo/GitHub deposit can drop
its identifiers straight into `config.yaml` — see [`STANDALONE.md`](STANDALONE.md)
for the deposit checklist. Do not cite this project by DOI until one exists.

## Rendering

The canonical renderer is the shared pipeline of the
[docxology/template](https://github.com/docxology/template) monorepo. Place
(or clone) this repository at `projects/working/OmniLatticeTextbook` in a
monorepo checkout, then from the **monorepo root**:

```bash
uv sync
uv run python scripts/pipeline/stage_03_render.py --project working/OmniLatticeTextbook
uv run python scripts/pipeline/stage_04_validate.py --project working/OmniLatticeTextbook
```

This renders **PDF, HTML, EPUB, and DOCX** (`render.formats` in
`config.yaml`) and writes the validation report plus the evidence registry
under the project's `output/`. Rendered artifacts are tracked under
[`output/`](output/). Inline Mermaid diagrams embed as images when a Chrome
binary is reachable by `mmdc` (see
[`docs/visualization_guide.md`](docs/visualization_guide.md)).

Standalone checks (run from **this** project root, no monorepo needed):

```bash
uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90
uv run python scripts/scaffold_chapter.py
uv run python scripts/generate_figures.py
uv run python scripts/generate_diagrams.py
uv run python scripts/audit_textbook_quality.py --require-complete
```

`audit_textbook_quality.py` without `--require-complete` reports the same
structure while allowing stub markers; `--require-complete` is the
filled-manuscript gate this book passes (zero stubs in every audited
section). Exit code 0 alone is not proof: confirm the suite collected more
than zero tests and that coverage met the floor.

## What this book is

- **Modular.** Structure is declared in YAML, not hand-numbered. Add a part
  or a chapter in `config.yaml` and the numbering, TOC labels, lab, and
  question bank all follow.
- **Tested.** Every worked equation in the book is a tested function in
  `src/textbook/models.py` — the octave term (both conventions), catalog
  size, prime-parity partition, holographic rhyme field, metrological
  overlap, net-zero balance, and their generic ancestors. The backbone and
  the structural contract are enforced by a no-mocks test suite at ≥90%
  coverage.
- **Evidence-anchored.** Headline numbers in prose are bound to a
  machine-verifiable evidence registry built from `data/numeric_facts.yaml`
  and `data/claim_ledger.yaml` (with their `_evidence_*` chunk files) — see
  [`AGENTS.md`](AGENTS.md).
- **Reproducible.** Figures and diagrams come from deterministic Python
  (fixed seeds, headless matplotlib, spec-driven Mermaid). The same inputs
  always produce the same outputs.

## Directory map

```
OmniLatticeTextbook/
├── docs/
│   ├── manuscript/            # THE BOOK
│   │   ├── config.yaml        # SINGLE SOURCE OF TRUTH (parts → chapters)
│   │   ├── references.bib     # the 31 Mendez-corpus citation keys
│   │   ├── glossary.md        # glossary anchors ([**term**](#gl:anchor))
│   │   ├── part_0/ … part_III/# one .md per chapter + unit_intro.md per part
│   │   ├── labs/<part>/       # one lab per chapter (lab_<stem>.md)
│   │   ├── questions/<part>/  # one question bank per chapter (q_<stem>.md)
│   │   ├── appendices/        # reference appendices A–G
│   │   └── assets/            # deterministic cover and static assets
│   ├── architecture.md        # engine architecture guide
│   ├── authoring_guide.md     # how to extend the book
│   ├── manuscript_guide.md    # layout + per-chapter contract
│   ├── visualization_guide.md # figures, diagrams, hydration, mmdc
│   └── testing_guide.md       # suite, coverage gate, audits
├── src/
│   ├── textbook/              # config, toc, content engine, contracts, models
│   ├── visualization/         # deterministic matplotlib figures
│   └── mermaid/               # Mermaid specs (PNG or .mmd fallback)
├── scripts/                   # thin orchestrators (figures, diagrams, analysis, scaffold, audit, hydration)
├── data/                      # versioned inputs: claim ledger + numeric facts (+ evidence chunks)
├── tests/                     # no-mocks suite incl. test_manuscript_integrity.py
├── output/                    # tracked rendered artifacts (PDF/HTML/EPUB/DOCX, figures, reports)
└── pyproject.toml             # project config (90% coverage gate)
```

## Quick start

All commands assume `uv` (never `pip`/`npm`). Standalone commands run from
this project root; rendering runs from the monorepo root as shown above.

```bash
# 1. Install dependencies
uv sync

# 2. Materialise any missing stub files declared in config.yaml
#    (no-op for this filled book; used when you grow the structure)
uv run python scripts/scaffold_chapter.py

# 3. Regenerate the deterministic figures and diagrams
uv run python scripts/generate_figures.py
uv run python scripts/generate_diagrams.py

# 4. Run the test suite with coverage (must collect >0 tests, ≥90% coverage)
uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90

# 5. Filled-manuscript gate (zero stubs in audited sections)
uv run python scripts/audit_textbook_quality.py --require-complete
```

## How to grow the book

The workflow is always **edit config, then scaffold**:

1. Open [`docs/manuscript/config.yaml`](docs/manuscript/config.yaml) and add a chapter under
   the relevant part (a `file:` + `title:` entry), or add a whole new part with
   its `id`, `title`, `label`, `directory`, and `chapters`.
2. Run `scripts/scaffold_chapter.py`. It reads the config and writes any missing
   chapter, lab, and question-bank stub in the contract-compliant shape. Existing
   files are left untouched.
3. Fill the prose between the stub markers (`<!-- STUB -->`, `TODO:`, `TKTK`).
   Keep the labelled headings, the figure/equation/table cross-references, and
   the curriculum scaffold intact. New worked equations belong in
   `src/textbook/models.py` behind a test; new sources go into
   `references.bib` and `CITATION_KEYS`; new glossary terms into
   `glossary.md` and `GLOSSARY_ANCHORS`.
4. Regenerate figures/diagrams if you added new ones, then run the tests and
   the filled-manuscript audit (`--require-complete`); it reports each
   section's stub count and fails until the total reaches zero.

Because structure is declared once in YAML, the book can grow past its
current 30 chapters without renumbering anything by hand. The detailed
workflow is in [`docs/authoring_guide.md`](docs/authoring_guide.md).

## The design in one paragraph

`config.yaml` declares the structure. `src/textbook/` turns that declaration
into numbering (`toc.py`), validation and scaffolding (`content.py`), the
structural contract (`constants.py`), source-bound drift checks
(`contracts.py`), and the worked formalisms (`models.py`). `scripts/` are
**thin orchestrators**: they import tested methods from `src/`, handle I/O
and visualization, and never implement business logic themselves. `tests/`
enforce both the math and the manuscript contract with real data and no
mocks.

## Documentation map

| Document | Read it for |
| --- | --- |
| **This file (`README.md`)** | Overview, publication status, render commands, quick start, how to grow the book |
| [`AGENTS.md`](AGENTS.md) | Agent-facing reference: invariants, evidence-registry contract, editing checklist, frozen vs. fillable files |
| [`STANDALONE.md`](STANDALONE.md) | Provenance and publication-prep guide: what a first deposit does, validation commands |
| [`TODO.md`](TODO.md) | Forward backlog (deposit, CI, lab test translation) |
| [`docs/`](docs/README.md) | Deeper guides: architecture, manuscript/authoring/visualization/testing (`docs/README.md` is the index) |
| [`docs/manuscript/config.yaml`](docs/manuscript/config.yaml) | The single source of truth for book structure |
| Monorepo [`README.md`](https://github.com/docxology/template/blob/main/README.md) / [`AGENTS.md`](https://github.com/docxology/template/blob/main/AGENTS.md) | Pipeline semantics, CI parity, two-layer architecture |

## Output formats

The book renders to **PDF, HTML, EPUB, and DOCX** (`render.formats` in
`config.yaml`). The 31 inline Mermaid diagrams in the chapters (plus the
format-gallery appendix) embed as images when a Chrome binary is reachable
by `mmdc` — on this machine a local, git-ignored
[`.puppeteer.json`](.puppeteer.json) points Puppeteer at Chrome — and degrade
gracefully to fenced code blocks otherwise. See
[`docs/visualization_guide.md`](docs/visualization_guide.md).

## License

Dual-licensed: **code** (`src/`, `scripts/`, `tests/`) under **Apache-2.0**
([`LICENSE`](LICENSE)); **manuscript content** (`docs/manuscript/`) under
**CC BY 4.0** ([`LICENSE-CONTENT.md`](LICENSE-CONTENT.md)). See also
[`CHANGELOG.md`](CHANGELOG.md).

## Repository integrity

- Forward backlog: [`TODO.md`](TODO.md).
- Structural example config: [`docs/manuscript/config.yaml.example`](docs/manuscript/config.yaml.example),
  kept in lockstep with the live config by
  `tests/test_contracts.py::test_live_and_example_config_shapes_are_lockstep`.

<!-- foam-orphan-nav:start (hand-maintained: links sub-docs so they are reachable; no generator refreshes or validates this block) -->

## Directory & sub-document map

Navigation links to in-tree documents (keeps them discoverable):

- [src/ — agent notes](src/AGENTS.md)

<!-- foam-orphan-nav:end -->
