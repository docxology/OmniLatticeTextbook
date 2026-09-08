# AGENTS.md — OmniLatticeTextbook

Agent-facing reference for working inside **The Infinite Octaves Omni-Lattice
Textbook**: a filled, contract-checked textbook fork. Read this before
editing anything. For the human-facing overview and quick-start commands, see
[`README.md`](README.md); for deposit/publication prep, see
[`STANDALONE.md`](STANDALONE.md).

## Invariants (do not violate)

1. **`docs/manuscript/config.yaml` is the single source of truth.** Book
   structure — parts, chapters, unit intros, labs, question banks, reference
   appendices, front matter, render formats, analysis-script order, page
   geometry and typography — lives there and nowhere else. Never
   hand-number chapters, figures, equations, or sections; the TOC and
   numbering are derived from this file by `src/textbook/toc.py`. Config
   paths must be relative, portable Markdown filenames; the validator
   rejects traversal, absolute paths, nested chapter filenames, and
   duplicate source paths before any scaffold or audit touches the
   filesystem.

2. **Cross-references use pandoc-crossref.** Refer with `[@fig:..]`,
   `[@tbl:..]`, `[@eq:..]`, `[@sec:..]`. The target definition
   (`{#fig:..}` etc.) must exist — a reference without its definition
   renders as a dangling `??`, and the integrity test requires the
   **definition**, not merely the reference.

3. **The citation and glossary namespaces are closed.** Every `[@key]` must
   match one of the **31 citation keys** listed in `CITATION_KEYS`
   (`src/textbook/constants.py`), all defined in
   [`docs/manuscript/references.bib`](docs/manuscript/references.bib) — the
   `mendez2026*` corpus of the SS Vibelandia engine papers. Every
   `[**term**](#gl:<anchor>)` link must use one of the **44 glossary
   anchors** in `GLOSSARY_ANCHORS`, all defined in
   [`docs/manuscript/glossary.md`](docs/manuscript/glossary.md). These are
   closed sets: to add a source, add the entry to `references.bib` **and**
   `CITATION_KEYS`; to add a term, add it to `glossary.md` **and**
   `GLOSSARY_ANCHORS`. The manuscript-integrity tests keep both sides in
   sync.

4. **The content contract.** Every chapter carries, in order: a labelled H1
   (`{#sec:<part>_<stem>}`), at least one figure (`{#fig:...}`) with alt
   text, a metadata badge (`<!-- chapter-metadata-badge -->`), a Study
   Blueprint (`<!-- curriculum-scaffold-start -->`), Learning Objectives, a
   worked formalism (equation `{#eq:...}` plus parameter table
   `{#tbl:...}`), an inline ```mermaid``` diagram, and Summary / Key Terms /
   Further Reading / Practice sections. Labs and question banks have their
   own required headings (`{#sec:lab_<part>_<stem>}`,
   `{#sec:q_<part>_<stem>}`). Stub markers are `<!-- STUB -->`, `TODO:`, and
   `TKTK`; **this filled book has zero of them**, and the gate below keeps
   it that way.

5. **Never retype mathematics.** Each worked equation is a tested function
   in `src/textbook/models.py` (23 public formalisms: `octave_term`,
   `catalog_size`, `prime_parity_partition`, `holographic_rhyme_field`,
   `metrological_overlap`, `net_zero_balance`, `goldilocks_band`,
   `unique_address`, `round_robin`, `densification`, `phi_dual`,
   `phi_powers`, `phi_fibonacci`, `transduction_brake`,
   `lattice_linear_profile`, `xd_yd_combine`, and the generic
   `logistic_growth` / `saturating_response` / `exponential_decay` /
   `half_life` / `linear_fit` / `descriptive_statistics` /
   `normalize_unit_interval`). Show the equation in prose, then call the
   function.

6. **The evidence-registry contract.** Headline numbers in prose must be
   machine-verifiable. The versioned inputs live in `data/`:
   `numeric_facts.yaml` (a few curated top-level facts) and
   `claim_ledger.yaml` (declared claims with expected values and provenance).
   Because the monorepo evidence-registry collector caps YAML/JSON list
   traversal at **256 items per list**
   (`infrastructure/validation/evidence_registry_collectors.py:
   _MAX_EVIDENCE_JSON_LIST_ITEMS = 256`), the long evidence lists are
   **chunked** into sibling files — `numeric_facts_evidence_b.yaml` (250
   facts) + `numeric_facts_evidence_c.yaml` (241 facts) and
   `claim_ledger_evidence_b.yaml` (157 claims) — each safely under the cap.
   When adding bulk facts/claims, keep every list ≤ 256 items and spill the
   remainder into the next `_evidence_*` chunk file with the same
   `schema_version`/top-level key. The monorepo pipeline compiles these into
   `output/reports/evidence_registry.json` during validation; a stale or
   unresolvable evidence path fails the registry.

7. **Render-time hydration.** Before the monorepo render stage consumes the
   manuscript, `scripts/z_generate_manuscript_variables.py` copies
   `docs/manuscript/` → `output/manuscript/` byte-for-byte (deterministic;
   no template variables in this book). The pipeline prefers the injected
   `output/manuscript/` tree, which keeps inline-Mermaid artifacts at
   `output/figures/mermaid_inline/` exactly like first-class pipeline
   projects. Editing `docs/manuscript/` and re-running hydration is the
   render path — never edit `output/manuscript/` directly (it is
   regenerated).

8. **Mermaid rendering needs a Chrome binary.** `mmdc` (via the monorepo
   render stage) renders inline ```` ```mermaid ```` blocks and the
   spec-driven diagrams to PNG. The repo-local, git-ignored
   [`.puppeteer.json`](.puppeteer.json) points Puppeteer at a
   machine-specific Chrome path:
   `{"executablePath": "/Applications/Google Chrome.app/.../Google Chrome",
   "args": ["--no-sandbox", "--disable-setuid-sandbox"]}`. Adjust it per
   machine, or set `PUPPETEER_EXECUTABLE_PATH`. Without a reachable browser,
   diagrams degrade to fenced code blocks / `.mmd` sources — the build never
   hard-fails.

9. **No mocks.** Tests use real data and real computation — never
   `MagicMock`, `mocker.patch`, or any mocking framework. Use real temp
   files, real numbers, real PDFs. Determinism via fixed RNG seeds.

10. **Coverage floor is 90%** for project `src/` (enforced in
    `pyproject.toml`). Exit code 0 is not proof: confirm tests collected
    > 0 and coverage met the floor.

11. **Tooling is `uv`** (never `pip`/`npm`). Markdown only for content (no
    raw HTML except `<details>`). Figures and diagrams come from the
    scripts, never hand-drawn.

12. **Thin orchestrators.** All business logic lives in `src/textbook/`,
    `src/visualization/`, or `src/mermaid/`. Scripts under `scripts/` only
    import tested methods, handle I/O and visualization, and orchestrate.
    They never implement algorithms.

## Frozen vs. fillable

**Frozen — do not modify** (the engine and the structural contract):

- All `.py` under `src/` and `scripts/` — the content engine, the 23 tested
  formalisms, visualization, Mermaid spec rendering, and the thin
  orchestrators (including the hydration script).
- `docs/manuscript/config.yaml` — structure is changed by adding entries,
  but the schema and existing keys are stable; treat it as the contract
  (`tests/test_contracts.py` keeps `config.yaml.example` in lockstep).
- `docs/manuscript/references.bib` and `docs/manuscript/glossary.md` — the
  closed 31-key / 44-anchor namespaces every chapter depends on.
- `data/` — the claim ledger and numeric-facts registry (inputs, not
  outputs); edit only per the chunking rule above.
- `tests/` — especially `test_manuscript_integrity.py`, which encodes the
  contract.

**Fillable — author here:**

- Chapter prose under `docs/manuscript/part_*/`, labs under
  `docs/manuscript/labs/`, and question banks under
  `docs/manuscript/questions/` — keep the labelled headings and
  cross-references; keep the zero-stub invariant.
- New parts/chapters: add them to `config.yaml`, then scaffold and fill.

## Layout of `docs/manuscript/`

```
docs/manuscript/
  config.yaml         # the structure (parts → chapters → labs → questions)
  references.bib      # the 31 Mendez-corpus citation keys
  glossary.md         # the 44 glossary anchors (rendered as Appendix F)
  front_matter.md, preface.md, preamble.md
  part_0/…part_III/   # chapter .md files + unit_intro.md per part
  labs/<part_id>/     # lab_<stem>.md, one per chapter
  questions/<part_id>/# q_<stem>.md, one per chapter
  appendices/         # A authoring guide, B notation, C math review,
                      # D formalisms, E format gallery, G index
  assets/cover/       # deterministic cover (omnilattice_cover.png)
```

## Worked exemplars

Three chapters are the finished-prose references — copy their shape when
adding or revising chapters:

- `docs/manuscript/part_0/octave-map.md` — data-driven map chapter
  (convention disambiguation behind `textbook.models.octave_term`).
- `docs/manuscript/part_I/fractal-constant.md` — model-derivation chapter
  (golden-ratio formalism with worked numbers).
- `docs/manuscript/part_III/frontiers.md` — source-backed synthesis chapter
  (integrates and cites the papers it maps).

## Gate battery

Run from this project root unless noted:

```bash
# Structural + contract integrity (no-mocks suite)
uv run --extra dev python -m pytest tests/test_manuscript_integrity.py

# Full suite with the coverage gate
uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90

# Filled-manuscript gate (zero stubs; strict by default)
uv run python scripts/audit_textbook_quality.py --require-complete

# Deterministic figure + diagram regeneration
uv run python scripts/generate_figures.py
uv run python scripts/generate_diagrams.py

# Render + validate (from the docxology/template monorepo root, with this
# repository at projects/working/OmniLatticeTextbook)
uv run python scripts/pipeline/stage_03_render.py --project working/OmniLatticeTextbook
uv run python scripts/pipeline/stage_04_validate.py --project working/OmniLatticeTextbook
```

For monorepo-wide pipeline semantics and the two-layer architecture, see the
monorepo root [`AGENTS.md`](https://github.com/docxology/template/blob/main/AGENTS.md)
(a sibling `docxology/template` checkout in the local workspace).
