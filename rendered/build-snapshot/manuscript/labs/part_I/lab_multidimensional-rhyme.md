# Lab — Multi-Dimensional Holographic Rhyme {#sec:lab_part_I_multidimensional-rhyme}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to:

1. Re-run the paper's locked research suite (`npm run research:synthobs-multidimensional-holographic-rhyme`) and predict — before observing — its reported 9/9 lock count [@mendez2026mdRhyme].
2. Compute xD±yD combined dimension indices by hand and confirm them with `textbook.models.xd_yd_combine`.
3. Evaluate the four-pillar holographic rhyme field at fixture points by hand and confirm the values with `textbook.models.holographic_rhyme_field`.
4. Articulate, in one written paragraph, why these checks are catalog checks (filing consistency), not physics tests.

## Background

Linked chapter: [@sec:part_I_multidimensional-rhyme].

The source paper files an **xD±yD summation engine** with finite encode fixtures on engine shelf #19, expanding the four-pillar holographic rhyme of [@sec:part_I_holographic-rhyme] [@mendez2026mdRhyme]. It gives no equation; the model lives in its prose ("Cross-scale summation across **xD±yD** under **Φ ≈ 1.618** files holography as bidirectional Infinite Octave encoding") and its shipped artifacts: fixtures and a 9/9-locked suite under `research/synthobs-multidimensional-holographic-rhyme/` [@mendez2026mdRhyme]. This lab makes those artifacts tangible: you will run the suite, then reproduce its *style* of locking by computing exact fixture values yourself — first by hand, then with the tested backbone in `textbook.models`. Remember the corpus's own honesty clause: this is catalog architecture, not AdS/CFT falsification [@mendez2026mdRhyme].

## Procedure

1. **Predict the lock count.** From the digest's "What landed" list, write down how many suite locks the paper reports and under which directory. Keep the answer covered until Step 2 finishes.
2. **Run the reference implementation.** From the standalone repository `FractiAI/synthobs-multidimensional-holographic-rhyme` [@mendez2026mdRhyme], run:
   ```bash
   npm run research:synthobs-multidimensional-holographic-rhyme
   ```
   Observe the suite result and compare with your Step-1 prediction. If the suite reports anything other than 9/9, stop and record the discrepancy — that is a filing-consistency fact about the catalog, and interesting in exactly the way the corpus intends.
3. **Hand-compute the combine fixtures.** Using $d_{\pm} = x \pm y$ (the formalisation in [@eq:part_I_multidimensional-rhyme_xdyd] of the chapter), compute on paper:
   - $d_+$ for $x = 5$, $y = 3$ (expect $8$);
   - $d_-$ for $x = 5$, $y = 3$ (expect $2$);
   - $d_+$ for $x = 13$, $y = 8$ (expect $21$ — also a Fibonacci number).
4. **Hand-evaluate the parent field.** For the four-pillar field of [@eq:part_I_multidimensional-rhyme_field] with $\lambda = 1$, evaluate $f_4(0, 0)$ and $f_4(1/2, 0)$ by hand. For the origin, every cosine argument is $0$, so each pillar contributes $1$ and the sum is $4$. For $(1/2, 0)$, the four directional cosines are $\cos(\pi) = -1$, $\cos(0) = +1$, $\cos(-\pi) = -1$, $\cos(0) = +1$, cancelling to $0$.
5. **Confirm with the tested backbone.** Verify every hand value against `textbook.models`, as in the Computational Workflow below. A mismatch means your hand arithmetic moved off the ladder — re-derive before proceeding.

## Analysis

Tabulate your four combine values and two field values against the function outputs. Every row should agree exactly; the fixtures are finite, exact, and reproducible, which is precisely what makes them suitable as *encode fixtures* in the paper's sense [@mendez2026mdRhyme]. Then summarise the residuals (function minus hand value) with
`textbook.models.descriptive_statistics` — for a correct run, every residual is $0$ and the summary is degenerate (all zeros), which is the point: the filing either locks or it does not.

Interpretation guardrail: observing $8 = 5 + 3$ and $2 = 5 - 3$ land on the Fibonacci ladder is standard Fibonacci arithmetic; calling that closure the *reason* for the corpus's "bidirectional" language is your reading, not the paper's claim. Keep the two registers separate in your write-up, exactly as the chapter does.

## Computational Workflow

```python
import numpy as np
from textbook.models import xd_yd_combine, holographic_rhyme_field

# Combine fixtures (expected: 8, 2, 21)
print(xd_yd_combine(5, 3, sign=+1))   # 8
print(xd_yd_combine(5, 3, sign=-1))   # 2
print(xd_yd_combine(13, 8, sign=+1))  # 21

# Field fixtures, four pillars, wavelength 1 (expected: 4.0 and 0.0)
print(holographic_rhyme_field(np.array([[0.0]]), np.array([[0.0]]),
                              pillars=4, wavelength=1.0))   # [[4.]]
print(holographic_rhyme_field(np.array([[0.5]]), np.array([[0.0]]),
                              pillars=4, wavelength=1.0))   # [[0.]]
```

Optional extension: the engine's `sign` argument is validated — `xd_yd_combine(5, 3, sign=0)` raises `ValueError`. Confirm this and note that a fixture suite would lock that behaviour too: a filing that accepted arbitrary signs would not be bidirectional, it would be undefined.

## Reflection

1. The paper reports **9/9 suite locks** [@mendez2026mdRhyme]. What would it mean, in catalog terms, for the suite to report 8/9 — and why is that a different kind of failure than a failed physics experiment?
2. You computed $f_4(1/2, 0) = 0$: a nodal line where the summed field cancels. What does the *differenced* encoding $d_- = x - y$ do at $x = y$, and how does that echo the zero-balance theme of the Topology of the Void filing named on the same board [@mendez2026mdRhyme]?
3. Write the honesty clause from memory, then check it against the chapter. Which of the three explicit "nots" was hardest to state precisely, and why does the corpus need all three?
