# OmniLatticeTextbook TODO

This backlog is future-only. The book itself is complete (30 chapters, 30
labs, 30 question banks, 4 unit intros, 7 appendices, zero stubs; all gates
green). Each row below needs an owner, a proving artifact, an acceptance
command, and a negative control before it is scoped.

## Integrity and structure invariants (standing)

- Keep `docs/manuscript/config.yaml` as the only source of truth for parts,
  chapters, appendices, labs, and question banks.
- Keep the closed 31-key / 44-anchor namespaces (`CITATION_KEYS`,
  `GLOSSARY_ANCHORS`) in lockstep with `references.bib` / `glossary.md`.
- Keep the structured scaffold audit (`textbook.audit.run_manuscript_audit`)
  covering orphan part markdown, unit intros, and strict-CLI failures.
- Keep the evidence-registry chunking convention (`data/*_evidence_*.yaml`,
  ≤ 256 items per list) so every bulk fact/claim stays machine-verifiable.

## Upcoming

| ID | Status | Size | Dependency | Next action / unblock condition | Proving artifact | Acceptance command | Negative control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEPOSIT-1 | open | M | GitHub repo access | First deposit: push to `docxology/OmniLatticeTextbook`, create the Zenodo deposit from `.zenodo.json`, record the minted concept/version DOIs in `config.yaml` (`publication.*`, `published_artifacts`) and the blank DOI fields of `CITATION.cff` / `.zenodo.json` / `codemeta.json`; then regenerate the README publishing status honestly | Zenodo DOI + updated config | `uv run python scripts/audit_textbook_quality.py --require-complete` | No DOI in `config.yaml` ⇒ README keeps "not yet deposited" |
| CI-1 | open | M | DEPOSIT-1 | Add a GitHub Actions workflow running the standalone gates on push/PR: pytest with coverage (`--cov=src --cov-fail-under=90`) and `audit_textbook_quality.py --require-complete` | `.github/workflows/ci.yml` with green run | `uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90` locally mirrored in CI | PR touching a chapter contract without tests ⇒ CI red |
| LABTEST-1 | open | L | none | Translate the labs' `npm run …` reference-implementation suites from the corpus papers into repo-level tests (or explicitly pinned, documented skips), so lab procedures have executable counterparts alongside the `textbook.models` reference values | New test modules under `tests/` | `uv run --extra dev python -m pytest tests/ --cov=src --cov-fail-under=90` | A lab whose hand-check numbers drift from `models.py` fails |
| UPSTREAM-1 | open | S | monorepo review | Upstream the evidence-registry chunking pattern (256-item list cap ⇒ `*_evidence_*.yaml` sibling chunks) into `template_textbook` docs/scaffold so future forks inherit it; sync `docs/manuscript/AGENTS.md`/`SYNTAX.md` naming accordingly | Upstream PR to docxology/template_textbook | Upstream CI green | Fresh fork from template without chunking docs ⇒ large ledgers silently exceed the cap |

## Documentation and signposting gaps (standing)

- Keep README, AGENTS, and the docs/ guides accurate to the live structure:
  if chapter/part counts, namespaces, or gate commands change, update them in
  the same change.
- The bundled agent skill (`.agents/skills/template-textbook/SKILL.md`) still
  carries template-era commands; refresh it (or re-scope it to the fork) when
  next touched.

## Backlog status

Rows remain open until the acceptance command and negative control pass in the
same source revision. A blocked row is a deliberate boundary, not a skipped
success.
