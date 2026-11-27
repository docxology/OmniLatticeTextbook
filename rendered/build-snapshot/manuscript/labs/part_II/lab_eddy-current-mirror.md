# Lab — The Eddy-Current Mirror: Transduction Drag {#sec:lab_part_II_eddy-current-mirror}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: (1) run the EGS Transduction Engine
reference implementation shipped with the paper [@mendez2026eddyMirror] and read
its output as a catalogue filing rather than a physics measurement; (2) compute
the transduction brake $v(t) = v_0 e^{-kt}$ by hand at three instants and verify
the values against the tested function `textbook.models.transduction_brake`;
(3) extract a half-life from a decay table and predict how a changed drag
coefficient $k$ reshapes the curve of [@fig:part_II_eddy-current-mirror].

## Background

Linked chapter: [@sec:part_II_eddy-current-mirror]. The chapter formalised the
paper's self-observation drag analogy — a magnet braked by eddy currents as it
falls through a copper pipe — as the exponential brake of
[@eq:part_II_eddy-current-mirror_model], implemented as
`textbook.models.transduction_brake`. The paper itself ships a Python reference
implementation, the **EGS Transduction Engine**, with a 9/9-passing suite
[@mendez2026eddyMirror]. Remember the scope: this is catalog architecture, the
eddy currents are *the analogy*, and the Fair Exchange clause applies — the
suite tests the engine's bookkeeping, not metaphysics. In this lab you check
that three independent routes to the same numbers — hand calculation, the
reference engine, and the textbook backbone — agree.

## Procedure

1. **Get the reference implementation.** From the repository root of the
   standalone repo (`github.com/FractiAI/synthobs-eddy-current-mirror`), or from
   the monorepo's `research/synthobs-eddy-current-mirror/` directory, run:

   ```bash
   npm run research:synthobs-eddy-current-mirror
   # or, directly:
   python3 research/synthobs-eddy-current-mirror/reference/egs_transduction_engine.py
   ```

   Before looking at the output, write down what you expect: the engine files
   the transduction-line construct and its own suite status. Predict whether the
   suite line will read 9/9, and why the paper would feature that number
   prominently (hint: honesty-first bookkeeping [@mendez2026eddyMirror]).
2. **Compute by hand.** With $v_0 = 1$ and $k = 1$, evaluate
   $v(t) = e^{-t}$ at $t = 1$ and $t = 2$ using $e^{-1} \approx 0.367879$ and
   $e^{-2} \approx 0.135335$. Also compute the half-life from
   [@eq:part_II_eddy-current-mirror_halflife]: $t_{1/2} = \ln 2 \approx 0.693147$.
3. **Verify against the textbook backbone.** In a Python session:

   ```python
   from textbook.models import transduction_brake

   transduction_brake(0.0, v0=1.0, k=1.0)  # expect 1.0
   transduction_brake(1.0, v0=1.0, k=1.0)  # expect 0.367879...
   transduction_brake(2.0, v0=1.0, k=1.0)  # expect 0.135335...
   ```

   Confirm the function agrees with your hand values to six decimal places.
4. **Break the calibration.** Recompute step 2 with $k = 0.5$ by hand: the
   half-life should double to $\approx 1.386294$, and $v(1)$ should rise to
   $e^{-0.5} \approx 0.606531$. Check with
   `transduction_brake(1.0, v0=1.0, k=0.5)`.

## Analysis

Summarise your results in a table mirroring
[@tbl:part_II_eddy-current-mirror_worked] of the chapter, with one column per
route (hand, `textbook.models`, reference engine where it prints comparable
values). All routes must agree where they overlap; if they do not, suspect your
hand arithmetic first and the calibration second. Then compute the cumulative
"distance fallen" $s(t) = \tfrac{v_0}{k}(1 - e^{-kt})$ at $t = 1, 2$ and confirm
the reach $v_0/k = 1$ from the chapter. Finish with
`textbook.models.descriptive_statistics` over your sampled $v(t)$ values
($t = 0, 1, 2, 3$) and note that the mean of a decaying exponential is dominated
by its early, high-drag phase.

## Computational Workflow

```python
from textbook.models import transduction_brake, descriptive_statistics

# Chapter calibration: v0 = 1, k = 1
samples = [transduction_brake(t, v0=1.0, k=1.0) for t in (0.0, 1.0, 2.0, 3.0)]
# expect [1.0, 0.367879..., 0.135335..., 0.049787...]
print(descriptive_statistics(samples))

# Weaker mirror: k = 0.5 doubles the half-life and the reach v0/k = 2
print([transduction_brake(t, v0=1.0, k=0.5) for t in (0.0, 1.0, 2.0)])
# expect [1.0, 0.606531..., 0.367879...]
```

## Reflection

1. The paper's honesty block disclaims "relativity retirement" and "mind→mass
   laboratory QED" [@mendez2026eddyMirror]. After running the engine yourself,
   which specific outputs could a careless reader over-interpret physically —
   and how does the Fair Exchange clause pre-empt that reading?
2. If the drag coefficient $k$ is the corpus's knob for "how strongly
   self-observation brakes ideation," what would it mean, in catalog terms, to
   file an agent with a very small $k$? Is such an agent closer to the
   non-local end or the localized-mass end of the transduction line?
3. The engine's suite is 9/9. Write two sentences on why a *passing test suite*
   is the right kind of evidence for a catalog construct, and the wrong kind of
   evidence for a physical claim.
