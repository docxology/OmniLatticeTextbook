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

## Workflowz review — 2026-11-10

- [ ] **WFZ-1 — P1 — Make manuscript hydration remove stale files from its managed output tree.** **Observable outcome:** after a source Markdown file is deleted or renamed, rerunning hydration removes its old counterpart from `output/manuscript/`, which is the preferred render input, while unrelated generated artifacts remain intact. **Evidence:** hydration deliberately overwrites files but leaves extraneous files in place (`scripts/z_generate_manuscript_variables.py:10-13`), while the render pipeline prefers the injected `output/manuscript/` tree (`AGENTS.md:82-90`). **Behavioral acceptance probe (repository root):** add a real-temporary-directory regression test named for this behavior and run `uv run --extra dev python -m pytest tests/test_paths_io.py -k hydration_mirror_removes_stale_files`; the test must hydrate twice around a source-file deletion, assert that the stale output file is gone, and assert that an `output/figures/` sentinel is unchanged. **Dependencies/constraints:** restrict pruning to the owned `output/manuscript/` tree, preserve deterministic byte-for-byte copying, and retain inspectable partial renders only behind an explicit opt-in if that authoring mode is still needed.

- [ ] **WFZ-2 — P2 — Require an explicit draft mode for unknown-chapter placeholder figures.** **Observable outcome:** normal generation for this declared-complete book fails with a nonzero, chapter-specific error when no bespoke builder exists; an explicit draft/placeholder option still produces the neutral figure for authoring. **Evidence:** unknown chapters currently fall back to a neutral placeholder (`src/visualization/plots.py:8-10`), implemented by `placeholder_overview` (`src/visualization/plots.py:95-96`) with replacement-needed text (`src/visualization/plots.py:112`), despite the book being described as complete (`README.md:22-26`). **Behavioral acceptance probe (repository root):** add a subprocess-level CLI regression test and run `uv run --extra dev python -m pytest tests/test_visualization.py -k unknown_chapter_placeholder_mode`; it must show that the default unknown-chapter invocation exits nonzero without publishing a placeholder, while explicit placeholder mode succeeds and writes the expected PNG. **Dependencies/constraints:** preserve `placeholder_overview` as an intentional authoring aid, keep existing chapter-to-filename mappings unchanged, and document the draft-only switch; this finding does not assert that any current chapter already uses the fallback.

- [ ] **WFZ-3 — P3 — Document the full companion scope of `--require-complete` in CLI help.** **Observable outcome:** `scripts/audit_textbook_quality.py --help` explicitly tells users that completeness failures cover labs and question banks as well as unit intros and chapters. **Evidence:** the current help mentions only audited unit intros or chapters (`scripts/audit_textbook_quality.py:30-34`), but the audit also reads companion files and records their stub markers as problems (`src/textbook/audit.py:112-117`), a behavior exercised by the question-bank fixture in `tests/test_audit_extra.py:105-129`. **Behavioral acceptance probe (repository root):** run `uv run python -c 'import subprocess, sys; p = subprocess.run([sys.executable, "scripts/audit_textbook_quality.py", "--help"], check=True, capture_output=True, text=True); assert "lab" in p.stdout.lower() and "question" in p.stdout.lower()'` and preserve the semantic regression check with `uv run --extra dev python -m pytest tests/test_audit_extra.py`. **Dependencies/constraints:** documentation-only change; do not weaken or remove the existing companion-file failure behavior.

- [ ] **WFZ-4 — P3 — Pin the uv development interpreter to Python 3.15.2.** **Observable outcome:** a fresh development sync selects the exact preferred patch interpreter rather than any interpreter in the 3.15 line, improving development reproducibility without changing the package's advertised compatibility floor. **Evidence:** the current development pin is only `3.15` (`.python-version:1`), independently of the distributable `>=3.11` requirement (`pyproject.toml:20`). **Behavioral acceptance probe (repository root):** run `uv run python -c 'import sys; assert sys.version_info[:3] == (3, 15, 2), sys.version'`. **Dependencies/constraints:** change only the development pin and verify uv can resolve it with the existing lockfile; retain `requires-python = ">=3.11"` and do not upgrade dependencies without separate evidence. If an actual deployment, fixture, dependency, or scientific-reproducibility constraint prevents 3.15.2, document that constraint instead of forcing the pin.
