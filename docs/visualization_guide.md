# Visualization Guide

All figures and diagrams are generated **deterministically** from `src/` — never
edited by hand. Re-running the generators reproduces
byte-stable artifacts, which keeps renders reproducible and tests honest.

## Figures: `src/visualization`

[`src/visualization/plots.py`](../src/visualization/plots.py) produces these
kinds of matplotlib figure:

1. **Worked figures** — four generic figures driven by the tested formalisms in
   [`src/textbook/models.py`](../src/textbook/models.py):
   - `plot_logistic_growth`
   - `plot_saturating_response`
   - `plot_exponential_decay`
   - `plot_linear_fit`
2. **Canonical chapter figures** — `generate_chapter_figures()` emits one
   uniquely named figure per chapter: all **30** chapters of this book have
   source-bound, deterministic figures under their
   `<part_id>_<stem>.png` filenames (see `output/figures/`).

`generate_all_figures(output_dir, config=None)` produces all of them. The shared
helpers [`src/visualization/_scaffold.py`](../src/visualization/_scaffold.py)
(`new_figure`, `save_figure`) keep styling and the save path consistent and
deterministic.

The committed cover image
[`manuscript/assets/cover/omnilattice_cover.png`](../docs/manuscript/assets/cover/omnilattice_cover.png)
is itself a deterministic, tested artifact: a lattice of ninety-nine octave
bands keyed by the golden-ratio constant, with nine digit drawers and the
zero-octave node at the origin. Regenerate it by calling `cover_art(output_dir)`
from [`src/visualization/plots.py`](../src/visualization/plots.py)
(byte-stable nested modular blocks), then copy the result over the tracked asset.

### The filename contract

Each chapter figure is named **`<part_id>_<stem>.png`** — for example
`part_0_octave-map.png`, `part_I_fractal-constant.png`. This exactly matches the
image path the chapter references:

```markdown
![Overview schematic …](../../output/figures/part_0_octave-map.png){#fig:part_0_octave-map width=90%}
```

Because the filename is derived from the same `ChapterRef` the manuscript uses,
a newly scaffolded chapter's figure path resolves the moment you run the
generator — no manual wiring.

### Generating figures

```bash
uv run python scripts/generate_figures.py                 # → output/figures/
uv run python scripts/generate_figures.py --output-dir <dir>
```

[`scripts/generate_figures.py`](../scripts/generate_figures.py) is a thin
orchestrator: it calls `generate_all_figures`, optionally
`generate_gallery_figures` (into `output/figures/gallery/`), writes
`figure_registry.json`, and prints each output path.

### Format gallery: `gallery_specs.yaml`

[`gallery_specs.yaml`](../src/visualization/gallery_specs.yaml) drives the appendix
format gallery the same way `diagram_specs.yaml` drives Mermaid diagrams.

## Diagrams: `src/mermaid`

[`src/mermaid/`](../src/mermaid) renders Mermaid diagrams from
[`diagram_specs.yaml`](../src/mermaid/diagram_specs.yaml), which holds **31**
specs (`concept_map`, the book's chapter-specific diagrams, and the generic
kind-examples):

- `load_specs()` reads the spec list.
- `build_flowchart()` / `build_source()` turn a spec into Mermaid source.
- `generate_all_diagrams(output_dir, specs_path=None)` writes every diagram. If
  the Mermaid CLI `mmdc` is available (`mmdc_available()`), each diagram renders
  to **PNG**; otherwise it falls back to a `.mmd` source file so a build never
  hard-fails on a missing optional tool.

```bash
uv run python scripts/generate_diagrams.py
```

Note: these are the *standalone* diagram assets. The **inline** `` ```mermaid ``
blocks required inside every chapter (31 of them across the 30 chapters —
`living-pem.md` carries two — plus five in `appendix_format_gallery.md`) are
rendered by the document renderer at build time, not by this generator.

## Render-time hydration

Before the monorepo render stage consumes the manuscript, run the hydration
script:

```bash
uv run python scripts/z_generate_manuscript_variables.py
```

It copies `docs/manuscript/` → `output/manuscript/` byte-for-byte (deterministic;
this book carries no `{{variable}}` placeholders; existing files are
overwritten, extraneous files left so partial renders stay inspectable). The
pipeline prefers the injected `output/manuscript/` tree — see
`infrastructure.rendering._manuscript_source.resolve_manuscript_dir` — which
keeps the inline-Mermaid artifact directory at
`output/figures/mermaid_inline/`, exactly like first-class pipeline projects.
Never edit `output/manuscript/` directly; it is regenerated.

## Rendering Mermaid diagrams to images (PDF/HTML)

Inline ```` ```mermaid ```` blocks are rendered to images at build time by the
monorepo render pipeline using the Mermaid CLI (`mmdc`), which needs a
Chrome/Chromium binary. Two ways to point it at one:

1. Set `PUPPETEER_EXECUTABLE_PATH` (or `CHROME_EXECUTABLE_PATH`) to your browser
   binary before rendering, or
2. Drop a local `.puppeteer.json` at the project root — this repository ships
   one (git-ignored, since it holds a machine-specific path):

   ```json
   {
     "executablePath": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
     "args": ["--no-sandbox", "--disable-setuid-sandbox"]
   }
   ```

   Adjust `executablePath` to this machine's Chrome/Chromium; the
   `--no-sandbox` args matter in CI and root containers.

Without a reachable browser, diagrams degrade gracefully to fenced code blocks in
the output and `src/mermaid` writes `.mmd` source instead of PNG — the build
never hard-fails. With it, the combined PDF embeds the rendered inline diagrams.

## Adding a real figure for a chapter

All 30 chapter figures are already real and source-bound. When you add a
chapter (see the [authoring guide](authoring_guide.md)):

1. **Put the math in `src/`.** Add the computation to
   [`src/textbook/models.py`](../src/textbook/models.py) (or a new tested module)
   — never in the script. Add a test for it (no mocks; real numbers).
2. **Add a plot function** in `plots.py` that imports the model function, builds
   the figure with `_scaffold.new_figure`, and saves it with `save_figure` under
   the **same filename** the chapter references: `<part_id>_<stem>.png`. Override
   the placeholder by registering it in `generate_chapter_figures`.
3. **Regenerate** with `uv run python scripts/generate_figures.py` and confirm
   `output/figures/<part_id>_<stem>.png` exists.
4. **Update the chapter** so the figure caption and the `<!-- alt: ... -->`
   comment describe the real figure (the image path is already correct).
5. **Run the visualization tests** (see the [testing guide](testing_guide.md)):
   `uv run --extra dev python -m pytest tests/test_visualization.py`.

Keep figures deterministic: fixed seeds, fixed sizes via `new_figure`, no
timestamps or randomised colours. The same input must always produce the same
PNG.
