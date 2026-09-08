# Lab — Metamorphic Octaves: Densification {#sec:lab_part_II_metamorphic-octaves}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: (1) run the metamorphic-octaves reference
implementation and observe its 9/9 fixture lock; (2) compute the densification
curve of [@eq:part_II_metamorphic-octaves_densification] by hand at four
exposures and confirm each against `textbook.models.densification`; and
(3) file three scenarios using the Goldilocks-lock map of
[@eq:part_II_metamorphic-octaves_filing] from the linked chapter
([@sec:part_II_metamorphic-octaves]).

## Background

The ship-blog paper "When life cooks you, you can come out denser" borrows the
mud → shale → schist story as a filing cabinet for people and software under Φ
[@mendez2026metamorphic]. Its filing rule weighs **personal heat** (identity
shake-ups, grief, the body at its limit, holding two true things at once)
against **professional heat** (too many roles, zero-mock gates, scarce money
and time, public stakes). Heat without a container files as magma/burnout;
pressure without heat is "just sitting there"; heat plus constraint files as
recrystallisation, maturing across 99 catalog octaves into the schist label.
The chapter reads that cumulative story as the logarithmic densification curve
drawn in [@fig:part_II_metamorphic-octaves]. In this lab you run the paper's
own fixture suite, then verify the curve's pinned checkpoints — including
$D(4) = 1 + \ln 5 \approx 2.609438$ — the way the corpus itself does: by
running the tests, not by trusting prose.

## Procedure

1. **Run the reference implementation.** Clone
   `github.com/FractiAI/synthobs-tbme-metamorphic-octaves` and run
   `npm run research:synthobs-tbme-metamorphic-octaves`. Record the suite
   result: the expected outcome is the **9/9 fixture lock**
   [@mendez2026metamorphic]. Write down what the nine fixtures pin (the
   paper's labels and map), before you compute anything yourself.
2. **Compute the checkpoints by hand.** With $D_0 = 1$ and $k = 1$, evaluate
   $D(x) = 1 + \ln(1+x)$ at $x = 1, 2, 4, 8$ using $\ln 2 \approx 0.693147$,
   $\ln 3 \approx 1.098612$, $\ln 5 \approx 1.609438$,
   $\ln 9 \approx 2.197225$. Expected values: **1.693147, 2.098612,
   2.609438, 3.197225** — the exposure-4 value is the book's pinned fixture.
3. **Check against the tested function.** In Python, call
   `textbook.models.densification(exposure, density0=1, rate=1)` for the same
   four exposures and compare to your hand values to at least six decimals.
   Do not re-implement the formula — call the tested function, exactly as the
   corpus runs its own fixtures rather than recomputing them.
4. **Measure the marginal gain.** From your four values, compute the
   successive differences $D(x{+}1) - D(x)$ and compare them with the
   prediction $D'(x) = 1/(1+x)$ of [@eq:part_II_metamorphic-octaves_marginal]
   evaluated at $x = 1, 2, 4$ (predicted: 0.5, 1/3 ≈ 0.333333, 0.2). Note the
   direction of drift and what it implies about "cooking longer."
5. **File three scenarios.** Using the Goldilocks lock, label each: (a) a
   colleague juggling three roles under public deadlines, no personal
   upheaval; (b) a friend in sustained grief *and* on a zero-mock-gated
   project; (c) an uncontained identity shake-up with no directional
   pressure. Cite the branch of [@eq:part_II_metamorphic-octaves_filing] you
   used for each, and check your labels against the fixture labels you
   recorded in step 1.

## Analysis

Summarise your four computed densities with
`textbook.models.descriptive_statistics` and report mean, spread, and range.
Interpret: the *levels* rise without bound, but the *increments* fall — which
is exactly the honesty-first reading that the paper files "a way to file, not
a prophecy" and never claims "you become unbreakable rock"
[@mendez2026metamorphic]. If any hand value disagrees with the function by
more than rounding, stop and find the arithmetic slip before continuing; the
fixtures are the ground truth.

## Computational Workflow

```python
from textbook.models import densification, descriptive_statistics

exposures = (1, 2, 4, 8)
values = [densification(x, density0=1, rate=1) for x in exposures]
print(values)          # -> [1.693147..., 2.098612..., 2.609438..., 3.197225...]
print(descriptive_statistics(values))

# Marginal gains versus the model's prediction 1/(1+x):
gains = [values[i + 1] - values[i] for i in range(len(values) - 1)]
preds = [1 / (1 + x) for x in (1, 2, 4)]
print(list(zip(gains, preds)))
```

Expected marginal gains: 0.405465, 0.510826, 0.587787 — each below the
$\ln 2 \approx 0.693147$ ceiling that doubling-exposure gains approach from
below, and each smaller than the previous *unit* gain would suggest if
densification were linear. Confirm this drift matches your step-4 hand
computation.

## Reflection

1. The schist label requires heat *and* directional pressure sustained "across
   99 catalog octaves." Why does a snapshot filing (one drawer, one moment)
   fail to capture it, and what does that imply for agents that route on this
   grammar?
2. You computed that each extra unit of exposure buys less than the last.
   How would you explain that to a reader tempted to read the curve as
   promising eventual "unbreakable rock" — the exact claim the paper refuses
   to make [@mendez2026metamorphic]?
3. Which furnace does your own working life supply most readily, and what
   would the Goldilocks lock say is *missing* from a filing that has only
   that one axis? Remember the paper's own caution: the catalog needs both
   axes — it does not ask you to seek either as a lifestyle.
