# Appendix E — Format Gallery: Every Content Primitive {#sec:appendix_format_gallery}

This appendix is a **kitchen-sink demonstration**: a working example of every
content primitive the Omni-Lattice textbook supports. Each chapter draws on
this primitive set; each example here is real and renders through the standard
pipeline. Figures are produced deterministically by `src/visualization/` and
embedded from `../figures/`, using the same tested models as the chapters.

> **How to read this appendix.** Headings group primitives by kind: text, lists,
> callouts, tables, math, figures, diagrams, code, cross-references, media, and
> pedagogy blocks. The Markdown source is the example — view it next to the
> rendered output.

---

## 1. Text and inline formatting

Plain paragraph text wraps and flows normally. Inline styles: **bold**,
*italic*, ***bold italic***, `inline code`, ~~strikethrough~~, H~2~O with a
subscript, E = mc^2^ with a superscript, and a footnote.[^demo]

[^demo]: Footnotes collect at the end of the document (or page, in PDF). Use them
for asides that would interrupt the sentence — such as the corpus's own
qualification "labels, not causation" [@mendez2026singularityCrystal].

You can hard-break a line with a backslash at the line end.\
The next line begins after that break; separate paragraphs with a blank line. Escape
literal Markdown with a backslash: \*not italic\*.

---

## 2. Lists

Unordered, with nesting:

- First item
- Second item
  - Nested item
  - Another nested item
    - Third level
- Third item

Ordered:

1. Step one
2. Step two
   1. Sub-step a
   2. Sub-step b
3. Step three

Task list (renders as checkboxes in many targets):

- [x] Declare the part in `config.yaml`
- [x] Generate the deterministic figures
- [x] Write the chapter prose
- [ ] Review the honesty tiers

Definition list:

Octave
::   One of the ninety-nine nested bands of the Infinite Octaves filing (see
     [**octave**](#gl:octave)).

Digit
::   One of the nine coarse bins labelling kinds of pattern (see
     [**digit**](#gl:digit)).

---

## 3. Block quotes and callouts

A plain block quote:

> "The map is for coordination, not cosmic destiny." Use quotes for epigraphs
> and primary-source extracts — the corpus's own honesty rail belongs here
> [@mendez2026digitsMaster].

Portable callouts (a bold label inside a block quote — renders in every target):

> **Note.** A neutral aside that adds context.

> **Tip.** A practical suggestion the reader can act on.

> **Warning.** A caveat, common error, or safety note — in this book, usually
> an honesty-first scope reminder.

> **Example.** A short worked illustration inline in the text.

> **Definition.** A precise statement of a term, often paired with a glossary
> entry such as [**zero octave**](#gl:zero-octave).

Pandoc fenced-div callout (richer styling where supported; falls back gracefully):

:::: {.callout-note}
This is a Pandoc fenced `div`. If your render profile styles `.callout-note`, it
appears as a boxed admonition; otherwise it renders as a normal block.
::::

---

## 4. Tables

A simple table with column alignment and a cross-referencable caption
([@tbl:gallery_alignment]):

:: Column alignment — left, centre, right. {#tbl:gallery_alignment}

| Left      |  Centre  |    Right |
| :-------- | :------: | -------: |
| alpha     |    1     |     10.0 |
| beta      |    22    |      2.5 |
| gamma     |   333    |    0.125 |

The values above are mirrored in `manuscript/assets/data/format_gallery.csv` so
rendering examples remain evidence-addressable fixtures rather than anonymous
literals — the same evidence-addressability the corpus applies to its suite
fixtures [@mendez2026livingPem].

A multi-line / grid table (cells may contain longer wrapped text):

+----------------+--------------------------------+----------------+
| Symbol         | Meaning                        | Typical range  |
+================+================================+================+
| $\Phi$         | El Gran Sol's Fractal Constant | pinned at      |
|                | — the catalog's scale key      | 1.6180339887   |
+----------------+--------------------------------+----------------+
| $\Omega_n$     | octave term at index $n$       | problem-       |
|                | (two printed conventions)      | dependent      |
+----------------+--------------------------------+----------------+

---

## 5. Mathematics and units

Inline math: the half-life is $t_{1/2} = \ln 2 / \lambda$, and at unit drag it
evaluates to $\ln 2 \approx 0.693147$.

A numbered display equation, cross-referenced as [@eq:gallery_logistic] — the
template's legacy logistic model, retained beside the Omni-Lattice formalisms:

$$ N(t) = \frac{K}{1 + \left(\dfrac{K - N_0}{N_0}\right) e^{-rt}} $$ {#eq:gallery_logistic}

Multi-line aligned derivation:

$$
\begin{aligned}
\frac{dN}{dt} &= rN\left(1 - \frac{N}{K}\right) \\
              &= rN - \frac{r}{K}N^2 .
\end{aligned}
$$

A matrix and a piecewise definition:

$$
\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix},
\qquad
f(x) = \begin{cases} 0 & x < 0 \\ 1 & x \ge 0 . \end{cases}
$$

Physical quantities with units, written in math mode so they render in **every**
target (PDF, HTML, slides): a rate of $0.5\ \mathrm{s^{-1}}$, a length of
$2.0\ \mathrm{m}$, and a concentration of $1.5\ \mathrm{mol\,L^{-1}}$. (For
PDF-only builds you may instead use `siunitx` macros such as `\SI{0.5}{\per\second}`,
which the preamble loads — but math-mode units are the portable choice.)

---

## 6. Figures

A single figure with caption, label, and alt text, cross-referenced as
[@fig:gallery_line]:

![A multi-series line plot of three sine waves, produced by
`visualization.gallery.line_plot`.](../../output/figures/gallery/gallery_line.png){#fig:gallery_line width=80%}

<!-- alt: Line plot with three sinusoidal curves of increasing frequency. -->

Two figures side by side (Pandoc fenced div; falls back to stacked):

:::: {layout-ncol=2}
![Bar chart.](../../output/figures/gallery/gallery_bar.png){#fig:gallery_bar width=48%}

![Pie chart.](../../output/figures/gallery/gallery_pie.png){#fig:gallery_pie width=48%}
::::

A multi-panel composite ([@fig:gallery_multipanel]):

![A 2×2 composite: line, scatter, bar, and histogram
panels.](../../output/figures/gallery/gallery_multipanel.png){#fig:gallery_multipanel width=85%}

The full plot-type gallery lives in `output/figures/gallery/` and includes:
line, scatter-with-fit, bar, grouped bar, horizontal bar, histogram, box,
violin, heatmap, contour, quiver field, step, stacked area, error bars, log-log,
pie, annotated, and multi-panel. Chapter figures reuse these builders against
the Omni-Lattice models — the octave ladder, the interference fields, and the
brake curves are all gallery shapes drawn from pinned parameters.

---

## 7. Diagrams (Mermaid)

The pipeline renders fenced `mermaid` blocks to figures (and falls back to the
`.mmd` source if the Mermaid CLI is absent). One worked example of each kind the
builders in `src/mermaid/diagrams.py` support:

Flowchart:

```mermaid
graph TD
  A[Digest claim IDs] --> B[Chapter prose]
  B --> C[Tested model in textbook.models]
  C -->|regenerate| D[Deterministic figure]
```

Sequence:

```mermaid
sequenceDiagram
  participant Author
  participant Engine
  Author ->> Engine: edit config.yaml
  Engine -->> Author: rendered PDF
```

State:

```mermaid
stateDiagram-v2
  [*] --> Narrative
  Narrative --> Catalog: file the claim
  Catalog --> Empirical: attach fixtures
  Empirical --> Operational: deploy with receipts
```

Class:

```mermaid
classDiagram
  class ChapterRef {
    +str part_id
    +str file
    +stem() str
  }
  ChapterRef --> TocEntry : numbered as
```

Entity-relationship:

```mermaid
erDiagram
  PART ||--o{ CHAPTER : contains
  CHAPTER ||--|| LAB : has
```

Pie, Gantt, mindmap, timeline, quadrant, and user-journey diagrams are also
supported — see `src/mermaid/diagram_specs.yaml` for a worked spec of each. The
state diagram above is the corpus's own honesty move: a claim is only filed
upward through the tiers when the previous tier's receipts exist
[@mendez2026livingPem].

---

## 8. Code

Inline code: call `textbook.models.octave_term(omega0=1.0, n=3)`.

A fenced code block with a language (syntax-highlighted) and a caption
([@lst:gallery_code]):

```{#lst:gallery_code .python caption="Calling the tested computational backbone."}
from textbook import models

omega3 = models.octave_term(omega0=1.0, n=3, convention="exponent")
size   = models.catalog_size()          # 99 * 81 -> 8019
brake  = models.transduction_brake([1.0, 2.0], v0=1.0, k=1.0)
print(omega3, size, brake)  # -> 4.236068 8019 [0.367879 0.135335]
```

A shell example:

```bash
uv run python scripts/generate_figures.py
uv run --extra dev python -m pytest tests/ --cov=src
```

---

## 9. Cross-references and citations

Cross-references resolve by label: figure [@fig:gallery_line], table
[@tbl:gallery_alignment], equation [@eq:gallery_logistic], and section
[@sec:appendix_formalisms]. Never hand-number — Pandoc fills these in.

Citations resolve against `references.bib`: a single source
[@mendez2026digitsMaster], multiple sources
[@mendez2026primeParity; @mendez2026eddyMirror], and an in-text form —
@mendez2026masterSynthesis framed the cascade first. A locator narrows the
reference [@mendez2026catalog, pp. 12–14].

---

## 10. Media and data

Embedded raster image (any PNG/JPG works the same way as a figure):

![A generated heatmap embedded as a raster
image.](../../output/figures/gallery/gallery_heatmap.png){#fig:gallery_media width=60%}

Audio and video embed in HTML targets (PDF shows the caption + link). Syntax:

```markdown
![Caption for an audio clip.](../assets/media/clip.mp3)
![Caption for a video.](../assets/media/demo.mp4){width=70%}
```

A downloadable data file lives at
[`assets/data/sample_dataset.csv`](../../../docs/manuscript/assets/data/sample_dataset.csv); its
contents as a table:

:: Sample dataset (mirrors `assets/data/sample_dataset.csv`). {#tbl:gallery_data}

| condition      | replicate | measurement | standard_error |
| -------------- | --------: | ----------: | -------------: |
| control        |         1 |        2.10 |           0.20 |
| control        |         2 |        2.30 |           0.18 |
| treatment_low  |         1 |        3.60 |           0.25 |
| treatment_high |         1 |        4.80 |           0.35 |

The error-bar figure [@fig:gallery_errorbar] visualises this kind of data:

![Means with standard-error bars.](../../output/figures/gallery/gallery_errorbar.png){#fig:gallery_errorbar width=70%}

---

## 11. Pedagogical blocks

These are the reusable teaching elements chapters draw on.

> **Learning objective.** After this section a reader can identify which Markdown
> primitive to use for a given purpose — and say which honesty tier the rendered
> claim belongs to.

> **Worked example.** Evaluate the octave term under the exponent convention:
> $\Omega_3 = \Phi^3 \Omega_0 = 4.236068$ for $\Omega_0 = 1$, via
> `textbook.models.octave_term(1.0, 3)`. Compare the subscript convention
> $\Omega_3 = \varphi_{\mathrm{fib}}(3)\,\Omega_0 = 2.0$ — both are printed
> "Ωn = Φn · Ω0" in the corpus, which is exactly why the book carries both
> [@mendez2026primeParity].

> **Try it.** Recompute with $n = 6$ and predict, then check, how the two
> conventions diverge ($\Phi^6 \approx 17.944272$ vs $\varphi_{\mathrm{fib}}(6)
> = 13/8 = 1.625$).

> **Key terms.** [**octave**](#gl:octave), [**digit**](#gl:digit),
> [**engine shelf**](#gl:engine-shelf).

> **Summary.** This appendix demonstrated text, lists, callouts, tables, math and
> units, figures, diagrams, code, cross-references, media, and pedagogy blocks —
> the complete primitive set the chapters build on.

---

## 12. Miscellany

A horizontal rule separates major shifts in topic (three or more dashes):

---

Raw inline HTML is supported only inside `<details>`, `<aside>`, or `<callout>`
per project style; everything else uses Markdown. Unicode renders directly:
α, β, γ, Δ, ∑, ∞, ≈, →, Φ. For PDF math, prefer LaTeX (`$\Phi$`) over raw
Unicode in equations.
