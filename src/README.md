# `src/` — the textbook engine

All business logic for this template lives here. Following the repository's
**thin-orchestrator rule**, every algorithm, validation, formula, and rendering
routine is implemented in `src/` (tested), and the files in `scripts/` only
import these functions to handle I/O and orchestration. Scripts never implement
logic.

## Layout

| Package / module | Responsibility |
| --- | --- |
| `textbook/constants.py` | The structural contract: `CITATION_KEYS` (31), `GLOSSARY_ANCHORS` (44), `REQUIRED_SECTION_HEADINGS`, `REQUIRED_TOKENS`, `STUB_MARKERS`. |
| `textbook/config.py` | `load_config`, `iter_chapters`, `validate_config` — read `docs/manuscript/config.yaml`, the single source of truth. |
| `textbook/toc.py` | Chapter numbering and part/chapter label generation. |
| `textbook/content.py` | The meta-template engine: `scaffold_chapter`, `scaffold_lab`, `scaffold_question_bank`, `validate_chapter`, `count_stub_markers`, `count_words`. |
| `textbook/models.py` | The worked formalisms (23 tested functions): the generic backbone (`logistic_growth`, `saturating_response`, `exponential_decay`, `half_life`, `linear_fit`, `descriptive_statistics`, `normalize_unit_interval`) plus the Omni-Lattice corpus formalisms (`octave_term`, `catalog_size`, `prime_parity_partition`, `holographic_rhyme_field`, and the rest). |
| `textbook/analysis.py` | Canonical worked-example parameters and deterministic summary generation; persisted inputs travel with outputs. |
| `visualization/` | Deterministic matplotlib figure generators (the generic worked figures, the gallery, and the 30 canonical chapter figures). See [`visualization/README.md`](visualization/README.md). |
| `mermaid/` | Mermaid diagram sources + PNG/`.mmd`-fallback renderer driven by `diagram_specs.yaml`. See [`mermaid/README.md`](mermaid/README.md). |
| `textbook_paths.py` | Project-root and output-directory resolution. |
| `textbook_io.py` | Atomic text writes (`write_text_atomic`) and small file helpers. |
| `textbook_logging.py` | `get_logger` — consistent logging across scripts and modules. |
| `textbook_visuals.py` | Shared figure-style helpers used by `visualization/`. |

## Design

The engine is **data-driven from `docs/manuscript/config.yaml`**. Chapters, labs, and
question banks are declared in config; `textbook.config` reads them, `textbook.toc`
numbers them, and `textbook.content` scaffolds and validates them against the
contract in `textbook.constants`. To grow the book you edit `config.yaml`, not the
engine.

## Coverage

Project source carries the coverage minimum declared in `pyproject.toml`. Read
the live test/coverage report rather than copying a volatile count here. Add
logic with a matching test under [`../tests/`](../tests/) before wiring it into
a script.

```bash
uv run --extra dev python -m pytest ../tests --cov=src --cov-report=term-missing
```
