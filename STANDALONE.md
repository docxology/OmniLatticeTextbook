# Standalone Provenance & Publication-Prep Guide

## Provenance

This repository is a **filled fork** of
[docxology/template_textbook](https://github.com/docxology/template_textbook),
the modular book scaffold of the
[docxology/template](https://github.com/docxology/template) monorepo.

Fork history (see `git log`):

1. **Scaffold** — "Scaffold OmniLatticeTextbook from docxology/template_textbook":
   the template's engine (`src/textbook/`, `src/visualization/`, `src/mermaid/`),
   thin `scripts/`, no-mocks `tests/`, and structural contract were inherited
   unchanged in shape; the identity moved to The Infinite Octaves Omni-Lattice
   Textbook (author Prudencio Mendez, corpus of the SS Vibelandia engine papers).
2. **Authoring** — "Author the Infinite Octaves Omni-Lattice textbook: 30
   chapters, tested formalisms, deterministic figures": all 30 chapters, 30 labs,
   and 30 question banks were filled against the contract; the real bibliography
   (31 `mendez2026*` citation keys) replaced the template's placeholder keys; the
   glossary grew to 44 anchors; `src/textbook/models.py` gained the
   Omni-Lattice formalisms (23 tested functions); chapter figures and the cover
   were generated deterministically; the evidence registry (`data/`) was
   populated and chunked.

The book renders **PDF / HTML / DOCX / EPUB** green through the monorepo
pipeline as project `working/OmniLatticeTextbook` and passes the filled-manuscript
gate (`scripts/audit_textbook_quality.py --require-complete`) with zero stubs.

## Publication identity

- Book: **The Infinite Octaves Omni-Lattice Textbook** — *A Modular Synthesis of
  the SynthOBS Engine Papers*
- Author: Prudencio Mendez (SS Vibelandia · SynthOBS Autonomous Agent Program)
- Source repository: [docxology/OmniLatticeTextbook](https://github.com/docxology/OmniLatticeTextbook)
- Config version: `0.1.0` (software/deposit version declared in
  `docs/manuscript/config.yaml`)
- **DOI: none yet** — see below.

## What is already prepared

Citation sidecars live at the project root and are filled except for
identifiers that only a deposit can mint:

- [`CITATION.cff`](CITATION.cff) — CFF 1.2.0 metadata (author, ORCID,
  license CC-BY-4.0, repository URL, title); `doi:` is **empty**.
- [`.zenodo.json`](.zenodo.json) — Zenodo deposit metadata (creators,
  description, license, upload type); the `isVersionOf` DOI is **empty**.
- [`codemeta.json`](codemeta.json) — CodeMeta 2.0 record; `identifier` is
  **empty**.
- `docs/manuscript/config.yaml` → `publication:` — `doi`, `version_doi`, and
  `version_record` are empty and `published_artifacts` is `{}`; the
  `zenodo_description` and keywords are already written.

These blanks are intentional: **no DOI has been minted for this fork**. Do not
fabricate or cite identifiers that do not exist; the README's publication
status is honest by construction because it is derived from these empty
fields.

## What a first deposit would do

1. **GitHub.** Push this repository to `docxology/OmniLatticeTextbook` (the
   `repository_url` / `github_repository` already declared in `config.yaml`
   and the sidecars).
2. **Zenodo.** Create a Zenodo deposit from the GitHub release (or upload the
   archive directly) using `.zenodo.json`; mint the concept DOI and the first
   version DOI.
3. **Record the identifiers** in exactly two places:
   - `config.yaml` → `publication.doi`, `publication.version_doi`,
     `publication.version_record`, and `published_artifacts` (the durable
     identifiers other tooling reads);
   - the blank DOI fields in `CITATION.cff`, `.zenodo.json`, and
     `codemeta.json`.
4. **Regenerate the publishing status** (or write it honestly by hand) so the
   README's status block reflects the deposit. Until then the README states
   "not yet deposited".
5. Optionally register additional artifacts (GitHub Pages build, OSF, and so
   on) in `published_artifacts` as they come into existence — never before.

## Validation commands

From this project root:

```bash
uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90
uv run python scripts/scaffold_chapter.py
uv run python scripts/generate_figures.py
uv run python scripts/generate_diagrams.py
uv run python scripts/audit_textbook_quality.py --require-complete
```

Rendering and validation through the shared pipeline, from the
[docxology/template](https://github.com/docxology/template) monorepo root with
this repository at `projects/working/OmniLatticeTextbook`:

```bash
uv run python scripts/pipeline/stage_03_render.py --project working/OmniLatticeTextbook
uv run python scripts/pipeline/stage_04_validate.py --project working/OmniLatticeTextbook
```

## Standalone vs. monorepo boundary

The project-local scaffold, tests, figures, diagrams, and audits do **not**
require the monorepo's `infrastructure/` layer — everything above runs
standalone. The monorepo adds the render pipeline (PDF/HTML/EPUB/DOCX via
pandoc + pandoc-crossref, hydration of the injected manuscript, inline-Mermaid
rendering through `mmdc` + Chrome), the evidence-registry compiler
(`output/reports/evidence_registry.json`), and cross-project validation.
