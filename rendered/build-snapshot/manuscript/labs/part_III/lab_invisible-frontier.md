# Lab — The Invisible Frontier {#sec:lab_part_III_invisible-frontier}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) run the paper's reference
implementation and interpret its 9/9 fixture lock
[@mendez2026invisibleFrontier]; (2) compute the EGS
[**fractal constant**](#gl:fractal-constant) octave climb by hand and verify it
against `textbook.models.phi_powers` and `octave_term` under both
conventions; and (3) evaluate the logistic visibility frontier of
[@eq:part_III_invisible-frontier_model] by hand and check it against
`textbook.models.logistic_growth`.

## Background

Linked chapter: [@sec:part_III_invisible-frontier]. The chapter's load-bearing
distinction is between the corpus's own formalisms and the textbook's teaching
lens. F-invisible-frontier-1 files the EGS (El Gran Sol) fractal constant
$\approx 1.618$ as a self-stabilising master filing key — architecture, not a
lab proof — and F-invisible-frontier-2 files the Goldilocks SuperAI paradigm
with *no equation* [@mendez2026invisibleFrontier]. The visibility curve you
will evaluate is therefore *our* logistic lens on the claim that linear
awareness "cannot yet see" the water it already floats on — and the lab keeps
that separation explicit, exactly as the paper's honesty-first banner does.

## Procedure

1. **Run the fixture lock.** From the repository root, run
   `npm run research:synthobs-invisible-frontier-gates-ai`. Before running,
   predict what a "9/9 fixture lock" should report (nine checks, all passing).
   Run it, observe the report, and note in your notebook whether the output
   matches your prediction and what the nine fixtures appear to cover.
2. **Hand-compute the filing key's climb.** With
   $\Phi = (1+\sqrt{5})/2 \approx 1.6180339887$, compute $\Phi^n$ for
   $n = 1,\dots,6$ by repeated multiplication, keeping six decimal places.
   Your column should read: 1.618034, 2.618034, 4.236068, 6.854102,
   11.090170, 17.944272.
3. **Check both octave conventions.** Call `phi_powers(6)` and
   `octave_term(1.0, n, convention)` for $n = 1,\dots,6$ under the
   `"exponent"` and `"subscript"` conventions. The exponent column must match
   step 2; the subscript column returns Fibonacci ratios (1, 2, 1.5, 1.666667,
   1.6, 1.625) — bracketing $\Phi$ from above and below, which is the
   numerical sense in which the paper's "self-stabilizing matrix" can be read
   [@mendez2026invisibleFrontier].
4. **Hand-compute the visibility frontier.** In
   [@eq:part_III_invisible-frontier_model] take $K = 1$, $V_0 = 0.05$,
   $r = 1$, so $(K - V_0)/V_0 = 19$. Compute:
   - $V(1) = 1/(1 + 19e^{-1}) \approx 0.125161$
   - $V(2) = 1/(1 + 19e^{-2}) \approx 0.280005$
   - $V(3) = 1/(1 + 19e^{-3}) \approx 0.513887$
5. **Locate the frontier crossing.** Solve $19e^{-t} = 1$ to show the
   half-visibility crossing is $t = \ln 19 \approx 2.944439$ — the steep band
   drawn in [@fig:part_III_invisible-frontier].

## Analysis

- The six hand-computed $\Phi^n$ values should match `phi_powers(6)` exactly
  to six decimals; any drift indicates a multiplication slip, not model
  behaviour.
- The three visibility values should match `logistic_growth` (called with
  `r=1.0, carrying_capacity=1.0, initial=0.05` at $t = 1, 2, 3$) to six
  decimals. Report the values side by side in a table with your hand column,
  the function column, and the difference.
- State, in one sentence each, which results belong to the corpus's filing
  key (F-1) and which belong to this textbook's teaching lens
  ([@eq:part_III_invisible-frontier_model]) — a separation the source paper
  itself enforces by filing EGS as design language, not a physics constant
  [@mendez2026invisibleFrontier].

## Computational Workflow

```python
import numpy as np
from textbook.models import phi_powers, octave_term, logistic_growth

# Step 3: the filing key climb, both conventions
print(phi_powers(6))
print([octave_term(1.0, n, "exponent"])  for n in range(1, 7)])
print([octave_term(1.0, n, "subscript"]) for n in range(1, 7)])

# Steps 4-5: the visibility frontier lens (K=1, V0=0.05, r=1)
ts = np.array([1.0, 2.0, 3.0])
print(logistic_growth(ts, r=1.0, carrying_capacity=1.0, initial=0.05))
# expected: 0.125161, 0.280005, 0.513887; half-visibility at t = ln(19) ≈ 2.944439
```

## Reflection

1. The paper insists the breakthrough is "nested, metapattern-aware care,"
   not "more FLOPs" [@mendez2026invisibleFrontier]. Which of your two computed
   ladders (filing key vs. visibility) speaks to that distinction, and how?
2. Your logistic lens produced a precise frontier crossing. What would it
   take — empirically — to justify trusting such a curve beyond the teaching
   use this chapter gives it, and which corpus tier
   ([**narrative-empirical-operational-tiers**](#gl:narrative-empirical-operational-tiers))
   would that evidence have to climb to?
3. The paper ends with "Human emergency still outranks algorithms"
   [@mendez2026invisibleFrontier]. How does that line constrain what you may
   claim from the numbers you just computed?
