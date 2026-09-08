# Authoring Guide

This is the developer-facing companion to the in-book authoring appendix
([`appendix_authoring_guide.md`](../docs/manuscript/appendices/appendix_authoring_guide.md)).
It shows how to grow the book from its current filled state — 30 chapters
across 4 parts, all zero-stub — to hundreds or thousands of pages while
keeping the contract green.

The mental model: **`config.yaml` declares the book; the engine scaffolds and
checks it; you fill the new stubs; the tests and audit keep you honest.** You
never hand-build structure, numbering, or figure paths.

## 1. Scaffold (or grow) the structure

The current book is fully scaffolded and filled. To add a chapter or a whole
part, edit
[`docs/manuscript/config.yaml`](../docs/manuscript/config.yaml):

```yaml
units:
  - id: part_I
    title: "Foundations: Constants, Primes, and Rhyme"
    label: "I"
    directory: part_I
    intro_file: unit_intro.md
    chapters:
      - file: fractal-constant.md
        title: "El Gran Sol's Fractal Constant"
      - file: my_new_chapter.md        # add an entry…
        title: "My New Chapter"
```

Then materialise any missing stub files in the correct shape:

```bash
uv run python scripts/scaffold_chapter.py            # all missing files
uv run python scripts/scaffold_chapter.py --part part_I
uv run python scripts/scaffold_chapter.py --force    # overwrite (destructive)
```

[`scaffold_chapter.py`](../scripts/scaffold_chapter.py) writes the chapter under
`manuscript/<part>/`, plus its `labs/<part_id>/lab_<stem>.md` and
`questions/<part_id>/q_<stem>.md`, each contract-complete but stub-heavy.
Existing files are never touched without `--force`. To skip a chapter without
deleting it, add `enabled: false` to its config entry.

Generate the matching figure placeholder so the chapter's image path resolves:

```bash
uv run python scripts/generate_figures.py            # → output/figures/<part_id>_<stem>.png
```

## 2. Fill the stubs

A scaffolded chapter contains the full required-element skeleton (labelled H1,
figure + alt text, metadata badge, Study Blueprint, Learning Objectives, a
worked formalism with `{#eq:...}` and `{#tbl:...}`, an inline `` ```mermaid ``
block, and Summary / Key Terms / Further Reading / Practice). Unwritten spots are
flagged with `STUB_MARKERS`: `<!-- STUB ... -->`, `TODO:`, and `TKTK`.

Replace each marker with real content while obeying the contract (see the
[manuscript guide](manuscript_guide.md)):

- **Write objectives, prose, summaries** over the `STUB`/`TODO`/`TKTK` markers.
- **Cite real sources** with `[@key]` — and add the entry to
  [`references.bib`](../docs/manuscript/references.bib) **and** to
  `CITATION_KEYS` in [`src/textbook/constants.py`](../src/textbook/constants.py)
  so the integrity test keeps `references.bib` in sync. The namespace is
  closed at 31 `mendez2026*` corpus keys today; extend both sides together.
- **Link key terms** with `[**term**](#gl:<anchor>)` — defined in
  [`glossary.md`](../docs/manuscript/glossary.md); new permanent anchors go in
  both `glossary.md` and `GLOSSARY_ANCHORS` (44 anchors today).
- **Cross-reference, never number.** Use `[@fig:..]`, `[@tbl:..]`, `[@eq:..]`,
  `[@sec:..]`. Do not type "Figure 4.1" — pandoc-crossref assigns the numbers.
- **Never retype math.** New worked equations belong as tested functions in
  [`src/textbook/models.py`](../src/textbook/models.py); the chapter shows the
  equation and points to the function (see the worked exemplars below).
- **Replace the placeholder figure** with a real, data-driven one when ready
  (see the [visualization guide](visualization_guide.md)) — keep the same
  `<part_id>_<stem>.png` filename.
- **Anchor headline numbers.** Numeric claims quoted from sources go into the
  `data/` evidence registry (`numeric_facts.yaml` / `claim_ledger.yaml` with
  their `_evidence_*` chunks, ≤ 256 items per list) so the render's evidence
  registry can verify them.

Check fill progress at any time:

```bash
uv run python scripts/audit_textbook_quality.py      # stub + word counts per chapter
```

## 3. Keep it green

Run the gates after each batch of edits (full detail in the
[testing guide](testing_guide.md)):

```bash
uv run --extra dev python -m pytest tests/test_manuscript_integrity.py
uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90
uv run python scripts/audit_textbook_quality.py --require-complete
```

The integrity tests fail fast on a missing required section, an undefined
citation or glossary anchor, or a chapter/lab/question that the config declares
but disk is missing — so the contract stays enforced, not aspirational.
`--require-complete` is the zero-stub gate the whole book passes today; any
scaffolded-but-unfilled chapter will fail it until filled.

## Worked exemplars

Three filled chapters show the target shape for new prose:

- [`part_0/octave-map.md`](../docs/manuscript/part_0/octave-map.md) — a
  data-driven map chapter; note how the source's ambiguous notation is
  resolved by implementing both conventions behind
  `textbook.models.octave_term(omega0, n, convention)`.
- [`part_I/fractal-constant.md`](../docs/manuscript/part_I/fractal-constant.md)
  — a model-derivation chapter around the golden-ratio formalism.
- [`part_III/frontiers.md`](../docs/manuscript/part_III/frontiers.md) — a
  source-backed synthesis chapter that maps and cites the papers it
  integrates.

## 4. Scale to hundreds or thousands of pages

The scaffold is built to grow without drifting. To go big:

- **Add parts and chapters in `config.yaml`**, then re-run
  `scaffold_chapter.py`. The TOC, numbering, lab/question wiring, and figure
  filenames all extend automatically because they are derived from the config —
  there is nothing to renumber by hand.
- **Repeat sections within a chapter.** The contract specifies the *minimum*
  (one figure, one equation, one table, one diagram, the required headings). A
  long chapter is many worked formalisms, figures, tables, and `## H2` sections —
  each with its own `{#fig:..}`/`{#eq:..}`/`{#tbl:..}` label so cross-refs stay
  unambiguous as the book lengthens.
- **Push computation into `src/` and tests.** Every new formalism or figure is a
  tested function in `models.py` + `plots.py`, not logic in a script. This keeps
  the 90% coverage gate meaningful and the figures deterministic at any scale.
- **Chunk the evidence registry.** Bulk numeric facts / claims spill into
  `data/numeric_facts_evidence_*.yaml` / `data/claim_ledger_evidence_*.yaml`
  files, never into a single list longer than 256 items.
- **Lean on the audit table.** `audit_textbook_quality.py` reports stub and word
  counts per chapter, so you always know which chapters are still skeletons and
  which are full — your burn-down for a large book.
- **Run the audit CLI in strict mode (default) in CI.** Pass `--lenient` only
  for partial-tree progress checks; a complete book has no business running
  lenient.

Because structure, numbering, references, glossary, and figure paths are all
contract-checked from one config, a 1,000-page book obeys exactly the same rules
as today's 30 chapters — you only ever add content, never re-plumb the book.
