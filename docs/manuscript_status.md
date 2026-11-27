# Manuscript Status

- **Project:** OmniLatticeTextbook
- **Manuscript title:** The Infinite Octaves Omni-Lattice Textbook — A Modular
  Synthesis of the SynthOBS Engine Papers
- **Author:** Daniel Ari Friedman (FractiAI) — synthesising the engine papers
  of Prudencio Mendez (FractiAI · SS Vibelandia)
- **Location:** [Canonical manuscript sources](manuscript/README.md).
- **Type:** Active publication-target manuscript (30 numbered section files +
  4 unit intros + 7 appendices; closed 31-key `references.bib`).
- **Status file purpose:** a per-repo pointer documenting whether this repository
  carries a research manuscript, where it lives, and what would change that status.

## Status: FILLED — complete as of 2026-09-08

| Component | Declared | Filled | Stubs |
| --- | --- | --- | --- |
| Parts (units) | 4 | 4 (+ 4 unit intros) | 0 |
| Chapters | 30 | 30 | 0 |
| Labs | 30 | 30 | 0 |
| Question banks | 30 | 30 | 0 |
| Reference appendices | 6 (A–E, G) | 6 | 0 |
| Master glossary (Appendix F) | 44 anchors | 44 | 0 |
| Bibliography | 31 `mendez2026*` keys | 31 | 0 (no placeholders) |

- **Provenance:** forked from
  [docxology/template_textbook](https://github.com/docxology/template_textbook);
  every engine-shelf paper of the corpus maps to exactly one chapter
  (with the config's documented exceptions: the Singularity Crystal chapter
  covers the paper plus node k=0; PDVSA Gateway Ops covers the live page plus
  the mockup note; the framework pages feed the Part 0 orientation and Living
  PEM chapters). Synthesis chapters (`fractal-constant`, `frontiers`) are
  analytic, source-backed integrations.
- **Checks:** the [testing guide](testing_guide.md) defines structural,
  mathematical and coverage gates. The [pinned build guide](rendering.md)
  records how to validate the current checkout.
- **Retained editions:** the [archive](../rendered/README.md) preserves the
  earlier PDF, HTML, DOCX and EPUB with their corresponding build receipts.
- **Evidence:** headline numbers are anchored by `data/numeric_facts.yaml` +
  `data/claim_ledger.yaml` (with `*_evidence_b/c.yaml` chunks, ≤ 256 items per
  list), compiled into `output/reports/evidence_registry.json`. The
  [compatibility ledger](../data/claim_ledger_evidence_d.yaml) binds additional
  table tokens to the models, worked examples, or source index.
- **Publication:** not yet deposited — `config.yaml` publication fields and the
  `CITATION.cff` / `.zenodo.json` / `codemeta.json` DOI slots are intentionally
  blank. See [`STANDALONE.md`](publication.md).

**What would change this status:** structural edits to `config.yaml`
(new chapters/parts must be scaffolded and filled before the zero-stub gate
passes again), a broken contract test or audit, or a first deposit (which adds
DOIs to `config.yaml` and the citation sidecars).