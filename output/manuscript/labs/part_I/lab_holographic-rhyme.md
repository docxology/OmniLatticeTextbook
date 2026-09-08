# Lab — Holographic Rhyme: The Four-Pillar Fractal {#sec:lab_part_I_holographic-rhyme}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) re-run the paper's reference
implementation, `npm run research:synthobs-holographic-rhyme-fractal`, and say
what "9/9 suite locks" means for it [@mendez2026holographicRhyme]; (2) evaluate
the four-pillar interference field ([@eq:part_I_holographic-rhyme_field]) by
hand at lattice stations using its $P = 4$ closed form
([@eq:part_I_holographic-rhyme_pairwise]); and (3) verify every hand value
against `textbook.models.holographic_rhyme_field`, so that prose and code
cannot silently disagree.

## Background

Linked chapter: [@sec:part_I_holographic-rhyme]. The corpus files a fractal —
under $\Phi \approx 1.618$ — as a [**holographic rhyme**](#gl:holographic-rhyme)
with four locked filing labels: repeating · self-similar · self-correcting ·
recursive [@mendez2026holographicRhyme]. The paper itself states no equation;
this lab uses the book's structural model, the four-pillar field of
`textbook.models.holographic_rhyme_field`, in which each filing label is
carried by one plane wave of wavelength $\lambda$ and the rhyme score at
$(x, y)$ is the sum of all four contributions. The Honesty clause still
applies throughout: this is [**catalog architecture**](#gl:catalog-architecture),
not Mandelbrot retirement, not measured 0% ECC, not clinical homeostasis QED.

## Procedure

1. **Run the reference suite.** From the project root of the standalone suite
   (`FractiAI/synthobs-holographic-rhyme-fractal`), execute:

   ```bash
   npm run research:synthobs-holographic-rhyme-fractal
   ```

   Before running, write down your prediction of what "9/9 suite locks"
   reports. Then run it and compare: the paper files *nine of nine* test locks
   for its own research suite [@mendez2026holographicRhyme] — a statement about
   the suite's self-consistency, not about any physical measurement.

2. **Hand-evaluate the field at $\lambda = \Phi$.** Take the pinned value
   $\Phi = 1.6180339887$ as the wavelength. Using the closed form
   [@eq:part_I_holographic-rhyme_pairwise],
   $f(x, y) = 2\cos(2\pi x/\lambda) + 2\cos(2\pi y/\lambda)$, compute $f$ by
   hand at the six stations of [@tbl:part_I_holographic-rhyme_samples]:

   | Station | $x/\lambda$ | $y/\lambda$ | Your hand value |
   | ------- | ----------- | ----------- | --------------- |
   | $(0,\, 0)$ | $0$ | $0$ | — |
   | $(\lambda/4,\, 0)$ | $0.25$ | $0$ | — |
   | $(\lambda/4,\, \lambda/4)$ | $0.25$ | $0.25$ | — |
   | $(\lambda/2,\, \lambda/2)$ | $0.5$ | $0.5$ | — |
   | $(\lambda,\, 0)$ | $1$ | $0$ | — |
   | $(\lambda,\, \lambda/2)$ | $1$ | $0.5$ | — |

   *Expected outputs:* $+4,\ +2,\ 0,\ -4,\ +4,\ 0$ in that order. If a hand
   value differs, re-check the argument of each cosine before touching code —
   the function is tested; your algebra is not.

3. **Verify against the tested function.** Confirm each of your six hand
   values with the workflow in the Computational Workflow section below, then
   extend the comparison to a grid and check the field's global bounds.

## Analysis

Summarise the grid computation with
`textbook.models.descriptive_statistics`, as in the workflow below. On a
$301 \times 301$ grid over $[0,\, 3\lambda]^2$ the expected summary is:

```json
{"mean": 0.013289036544849956, "std": 2.003297466004164,
 "min": -4.0, "max": 4.0, "count": 90601.0}
```

Interpret each number in filing language: the mean near zero says rhyme and
disagreement balance across the catalogue — the same balance-seeking posture
the corpus files as self-correcting; the extremes exactly $\pm 4$ say that
full agreement and full cancellation are both *attained* at lattice nodes; the
standard deviation $\approx 2.003$ reflects the two doubled axis rhymes of
[@eq:part_I_holographic-rhyme_pairwise]. Note how close the std is to $2$ but
that it is not exactly $2$ — explain why in your notes.

## Computational Workflow

```python
import numpy as np
from textbook.models import holographic_rhyme_field, descriptive_statistics

phi = 1.6180339887  # the pinned golden-ratio wavelength
lam = phi

# Step 3: verify the six hand stations.
stations = [(0, 0), (lam/4, 0), (lam/4, lam/4),
            (lam/2, lam/2), (lam, 0), (lam, lam/2)]
for x, y in stations:
    f = holographic_rhyme_field(np.array([[x]]), np.array([[y]]),
                                pillars=4, wavelength=lam)
    print(f"({x:.6f}, {y:.6f}) -> {f[0,0]:+.6f}")
# Expected: +4.000000, +2.000000, +0.000000, -4.000000, +4.000000, +0.000000

# Analysis: field summary over [0, 3*lam]^2.
gx, gy = np.meshgrid(np.linspace(0, 3*lam, 301), np.linspace(0, 3*lam, 301))
F = holographic_rhyme_field(gx, gy, pillars=4, wavelength=lam)
print(descriptive_statistics(F.ravel()))
```

## Reflection

- The paper insists the four pillars are "catalog filing labels," not
  equations. After computing with them, do you find the filing reading or the
  interference reading more load-bearing — and what would you lose by keeping
  only one?
- Your six hand values were identical for $\lambda = \Phi$ and would be for
  $\lambda = 1$. What, then, does the paper's "under $\Phi \approx 1.618$"
  actually contribute, given the Honesty clause's scope limits?
- Where did the model *dis*agree with a prediction you made — and does the
  [**honesty-first**](#gl:honesty-first) posture of
  [@mendez2026holographicRhyme] change how you record that disagreement?
