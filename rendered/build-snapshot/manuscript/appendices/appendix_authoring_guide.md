# Appendix A — Authoring Guide: How This Book Was Built {#sec:appendix_authoring_guide}

<!-- chapter-metadata-badge -->
> Reference appendix · For readers, reviewers, and contributors.

This appendix records how *The Infinite Octaves Omni-Lattice Textbook* was
produced. The book is not typeset by hand: it is **generated from a single
source of truth**, its mathematics is **tested code**, and its figures are
**deterministic output**. Readers can trust the numbers because they can
re-derive them; contributors can extend the book without breaking it, because
the structure is declared, not hand-maintained.

## The Big Idea: One Source of Truth

The book is **data-driven from
[`config.yaml`](../../../docs/manuscript/config.yaml)**. The list of parts,
chapters, labs, question banks, and reference appendices lives there and
nowhere else. The Python engine in `src/textbook/` reads that file; the
scaffolding scripts in `scripts/` materialise the matching markdown files.
Nobody hand-numbers a chapter, figure, equation, or section —
pandoc-crossref resolves every `{#fig:...}`, `{#eq:...}`, `{#tbl:...}`, and
`{#sec:...}` label at render time.

The stem of each config entry drives every downstream name:

- chapter file → `manuscript/<part>/<stem>.md`, label `{#sec:<part>_<stem>} `
- lab file → `manuscript/labs/<part>/lab_<stem>.md`
- question bank → `manuscript/questions/<part>/q_<stem>.md`
- figure → `output/figures/<part>_<stem>.png`

Adding a chapter means adding a config entry and re-running
`scripts/scaffold_chapter.py`; the table of contents, numbering, lab and
question wiring, and figure paths all extend automatically
(`src/textbook/toc.py`).

## The Provenance Pipeline

Every chapter is built from a **faithful source digest** under
`research/sources/`, one per paper of the SS Vibelandia corpus
[@mendez2026ship; @mendez2026catalog]. Each digest records:

- the page's fixed copy, extracted verbatim;
- **formalism IDs** `F-<slug>-<n>` for every symbolic statement;
- **claim IDs** `C-<slug>-<n>` for every substantive claim, with the
  paper's own honesty clause preserved;
- the vocabulary the paper introduces.

Chapter authors cover 100% of their digest's substantive content and cite the
source paper wherever a digest claim is restated. The corpus's **honesty
first** disclaimers travel with the claims: when this book says "the paper
files $c$ as a transduction line", the sentence carries both the citation
[@mendez2026eddyMirror] and the paper's own scope note (catalog architecture,
not relativity retirement).

## The Tested Computational Backbone

Every worked formalism in the book is a function in
[`src/textbook/models.py`](../../../src/textbook/models.py), covered by the
test suite under `tests/`. Chapter prose names the function that backs each
equation — for example, the octave recursion of [@mendez2026primeParity] is
backed by `octave_term` (which implements **both** printed readings of
"Ωn = Φn · Ω0"), the holographic catalog size of [@mendez2026digitsMaster] by
`catalog_size` (99 × 81 = 8,019), and the eddy-brake damping of
[@mendez2026eddyMirror] by `transduction_brake`. Key functions include:

| Function | Formalism it backs |
| --- | --- |
| `phi_powers`, `phi_fibonacci` | golden-ratio powers and Fibonacci ratios |
| `octave_term` | octave recursion $\Omega_n$ under both conventions |
| `catalog_size` | $99 \times 81 = 8{,}019$ master register |
| `prime_parity_partition` | sole-even 2 / odd irreducible sets |
| `holographic_rhyme_field`, `xd_yd_combine` | four-pillar and xD±yD fields |
| `transduction_brake` | eddy-brake damping $v_0 e^{-kt}$ |
| `metrological_overlap` | min-normalized set overlap |
| `net_zero_balance` | inflow/outflow residual |
| `unique_address` | injective prime encoding $\prod p_i^{e_i}$ |
| `round_robin` | kinematic set-recycling |
| `densification` | logarithmic metamorphic densification |
| `lattice_linear_profile` | EGS gateway linear ramp |
| `goldilocks_band` | planetary-core band mask |
| `phi_dual` | the $\Phi$ duality pair $(x\Phi,\, x/\Phi)$ |

: The tested backbone and the corpus formalisms it backs. {#tbl:appendix_authoring_guide_backbone}

Worked numbers are pinned in the book's configuration and regression-checked:
$\Phi \approx 1.6180339887$, $\varphi_{\mathrm{fib}}(5) = 1.6$,
$\varphi_{\mathrm{fib}}(10) \approx 1.618182$, $v(1) \approx 0.367879$,
$v(2) \approx 0.135335$, $\mathrm{overlap}(\{a,b\},\{b,c\}) = 0.5$,
`unique_address([2,3],[2,1]) = 12`, and $1 + \ln 5 \approx 2.609438$. If a
prose number disagrees with `textbook.models`, the prose is wrong.

## Deterministic Figures

Figures are matplotlib output from `src/visualization/plots.py`, regenerated
by `scripts/generate_figures.py` into `output/figures/<part>_<stem>.png`.
Because every figure is drawn from the tested models with fixed seeds and
pinned parameters, rebuilding the book reproduces byte-identical images.
Chapter captions are written against the canonical figure plan, so a caption
describes exactly what the generator draws. Diagrams come from
`src/mermaid/diagram_specs.yaml` via `scripts/generate_diagrams.py`.

## The Closed Namespaces

Two vocabularies are contracts, not conventions:

1. **Citations** — `[@key]` keys must resolve in
   [`references.bib`](../../../docs/manuscript/references.bib); the corpus's
   31 papers form the closed key set tracked in
   `src/textbook/constants.py:CITATION_KEYS`.
2. **Glossary anchors** — `[**term**](#gl:<anchor>)` links must point at the
   44 anchors defined in [`glossary.md`](../../../docs/manuscript/glossary.md)
   and tracked in `GLOSSARY_ANCHORS`.

Integrity tests fail the build on an undefined citation, a missing anchor, a
dropped required section, or any leftover scaffolding placeholder of the kind
the scaffolder emits — so the contract is enforced, not aspirational.


From the repository root:

```bash
uv run python scripts/generate_figures.py      # deterministic figures
uv run python scripts/generate_diagrams.py     # mermaid diagrams
uv run python scripts/pipeline/stage_03_render.py   # PDF / HTML / EPUB / DOCX
uv run --extra dev python -m pytest tests/test_manuscript_integrity.py
uv run python scripts/audit_textbook_quality.py     # stub + word counts
```

The audit reports per-file word and stub counts, and the render stage reads
only `config.yaml` — there is no per-chapter build logic to re-plumb when the
book grows.

## Extending the Book

To add a chapter end-to-end:

1. add its `stem`/`title` under the right part in `config.yaml`;
2. add matching lab and question-bank entries;
3. run `scripts/scaffold_chapter.py` (it creates only missing files);
4. write the chapter from a faithful source digest, citing the corpus keys
   and linking glossary anchors;
5. add or extend the backing model functions and figure generator in `src/`,
   with tests;
6. run the integrity tests and audit until green.

Because structure, numbering, references, and figure paths are all derived
from the one config, a 1,000-page book obeys exactly the same rules as this
one — contributors only ever add content, never re-number the book.

See also: [Appendix B — Notation](appendix_notation.md),
[Appendix C — Mathematical Review](appendix_math_review.md), and the
developer-facing [`docs/authoring_guide.md`](../../../docs/authoring_guide.md).
