# Build and verify the textbook

The [manuscript configuration](manuscript/config.yaml) declares the front
matter, part and chapter order, labs, question banks, glossary and appendices.
The pinned renderer reads that configuration and its companion files. The
[retained build](../rendered/README.md) records an earlier edition.

Use uv, Python 3.14 for the Template environment, Pandoc 3.14 with a
matching pandoc-crossref, XeLaTeX, BibTeX and Poppler. Install Linux
Libertine, Linux Biolinum and DejaVu Sans Mono and the TeX packages in the
[preamble](manuscript/preamble.md), including `soul` for the shared renderer and the TeX distribution's `tufte.bst`
bibliography style.
Inline diagrams require Mermaid CLI 12.2.0 (`mmdc`) and a compatible Chrome
or Chromium installation that can open Mermaid CLI's packaged local page.
Set `PUPPETEER_EXECUTABLE_PATH` to your browser executable if Mermaid
cannot discover it. On workers that require an approved sandboxed launch
profile, place that profile in `.puppeteer.json` at the disposable project
root or one of its ancestor directories. The pinned Mermaid profile expects
`NODE_PATH` and `NODE_OPTIONS` to be unset.

## Render from a committed checkout

Run this from the project root. The temporary checkout keeps current
render outputs separate from the retained edition and your working files.

```bash
set -e
source_checkout="$(pwd -P)"
source_commit="$(git rev-parse HEAD)"
scratch="$(mktemp -d)"
renderer="$scratch/template"
project="$renderer/projects/working/OmniLatticeTextbook"

git clone https://github.com/docxology/template.git "$renderer"
git -C "$renderer" checkout --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
mkdir -p "$renderer/projects/working"
git clone "$source_checkout" "$project"
git -C "$project" checkout --detach "$source_commit"

cd "$project"
mkdir -p output/figures
cp -a rendered/build-snapshot/figures/. output/figures/
ln -s ../output docs/output

cd "$renderer"
uv sync --locked --python 3.14
cd "$project"
PYTHONPATH=src "$renderer/.venv/bin/python" - <<'PYTHON'
from pathlib import Path
from visualization.registry import write_figure_registry

write_figure_registry(Path("docs/manuscript"), Path("output/figures"))
PYTHON
"$renderer/.venv/bin/python" scripts/analysis.py
cd "$renderer"
unset NODE_PATH NODE_OPTIONS
uv run --no-sync python scripts/pipeline/stage_03_render.py \
  --skip-manuscript-hydration --project working/OmniLatticeTextbook
uv run --no-sync python scripts/pipeline/stage_04_validate.py \
  --project working/OmniLatticeTextbook
printf '%s\n' "$project/output"
```

The build starts with the retained chapter and gallery figures and
regenerates their accessibility registry from the current source.
The generated `docs/output` link resolves chapter-relative figure paths and routes inline Mermaid assets into the fresh project
output. This book has no substitution variables, so the pinned renderer
can read `docs/manuscript/` directly. The legacy byte-copy command remains
available for integrations that specifically use an injected manuscript.

Find the combined editions under `output/pdf/`, `output/web/index.html`,
`output/docx/`, and `output/epub/`. Read the current source composition,
validation, evidence and provenance reports under `output/reports/`.
Slides are disabled in the configuration. The PDF uses numeric citations to
disambiguate the same-author, same-year corpus. The bibliography retains all
original records and URLs; web and office editions use Pandoc's citations.

## Recompute figures and check the model examples

The [visualization guide](visualization_guide.md) explains the standalone
figure and diagram scripts. To regenerate all assets, run them in a separate
worktree because the figure producer also writes the configured cover in
`docs/manuscript/assets/cover/`. Keep the retained snapshot intact.

From a textbook checkout, use the local tools for the complete-manuscript
audit and model fixtures.

```bash
uv run --locked python scripts/audit_textbook_quality.py --require-complete
uv run --locked --extra dev python -m pytest tests/test_models.py
```

The [testing guide](testing_guide.md) gives the broader integration and
coverage commands. These tests verify the mathematical fixtures and the
declared document contract. Claims from the source corpus retain the
evidence boundaries stated in the textbook.
