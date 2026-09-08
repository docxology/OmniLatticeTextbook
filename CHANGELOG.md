# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/) and this project adheres to
[Semantic Versioning](https://semver.org/).

## 0.1.0 — 2026-09-08

First release of **The Infinite Octaves Omni-Lattice Textbook** — *A Modular
Synthesis of the SynthOBS Engine Papers* by Prudencio Mendez: the template
scaffold forked from
[docxology/template_textbook](https://github.com/docxology/template_textbook)
and filled to a complete, gate-green textbook.

### Added

- **Filled manuscript** — 4 parts → 30 chapters (5/6/8/11 across part_0,
  part_I, part_II, part_III), each with its matching lab and question bank
  (30 + 30), a unit intro per part, and 7 appendices (authoring guide,
  notation, math review, master formalism table, format gallery, master
  glossary, index of key terms). Zero stubs: the filled-manuscript gate
  (`scripts/audit_textbook_quality.py --require-complete`) passes.
- **Real bibliography** — 31 `mendez2026*` citation keys from the SS
  Vibelandia engine-paper corpus (`references.bib`, mirrored in
  `CITATION_KEYS`); 44 glossary anchors (`glossary.md`, mirrored in
  `GLOSSARY_ANCHORS`).
- **Omni-Lattice formalisms** — `src/textbook/models.py` now exposes 23
  tested functions, adding the corpus formalisms (`octave_term` with both
  conventions, `catalog_size`, `prime_parity_partition`,
  `holographic_rhyme_field`, `xd_yd_combine`, `transduction_brake`,
  `metrological_overlap`, `net_zero_balance`, `lattice_linear_profile`,
  `goldilocks_band`, `unique_address`, `round_robin`, `densification`,
  `phi_powers`, `phi_fibonacci`, `phi_dual`) to the generic backbone.
- **Deterministic visuals** — 30 canonical chapter figures
  (`<part_id>_<stem>.png`) plus a deterministic cover
  (`assets/cover/omnilattice_cover.png`); 31 spec-driven Mermaid diagrams in
  `src/mermaid/diagram_specs.yaml`; 31 inline ```` ```mermaid ```` blocks
  across the chapters plus the format-gallery appendix.
- **Evidence registry** — `data/claim_ledger.yaml` and
  `data/numeric_facts.yaml` with the `*_evidence_b/c.yaml` chunk files
  (≤ 256 items per list), compiled by the monorepo pipeline into
  `output/reports/evidence_registry.json`.
- **Render-time hydration** — `scripts/z_generate_manuscript_variables.py`
  copies `docs/manuscript/` → `output/manuscript/` so the monorepo render
  stage consumes the injected manuscript like first-class pipeline projects
  (inline-Mermaid artifacts at `output/figures/mermaid_inline/`).
- **Multi-format rendering** — PDF, HTML, EPUB, and DOCX render green
  through the monorepo pipeline as project `working/OmniLatticeTextbook`.
- **Documentation set** — README, AGENTS, STANDALONE, TODO, and the
  `docs/` guides rewritten to describe this fork as it exists.

### Not yet

- **DOI / first deposit** — `config.yaml` publication fields and the
  `CITATION.cff` / `.zenodo.json` / `codemeta.json` DOI slots are
  intentionally blank; see [`STANDALONE.md`](STANDALONE.md) and
  [`TODO.md`](TODO.md).
