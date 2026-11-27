# Lab — Kinematic Set-Recycling: The Truckee Protocol {#sec:lab_part_III_kinematic-recycling}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) partition a finite asset set by hand
with the round-robin recycling rule of
[@eq:part_III_kinematic-recycling_round-robin] from
[@sec:part_III_kinematic-recycling] and verify your partition against the
tested `textbook.models.round_robin` function, (2) evaluate the Fourier
velocity scale fixture ([@eq:part_III_kinematic-recycling_velocity-scale])
numerically for a $\Phi$-spaced family of speeds, and (3) index the three
experiential octave states on the $\Phi$-power ladder using
`textbook.models.octave_term` in both conventions.

## Background

Linked chapter: [@sec:part_III_kinematic-recycling]. The chapter's central
filing is that one physical set — the Truckee River corridor kit — yields
multiple experiential realities through velocity, which the corpus files as an
**octave multiplier** under $\Phi \approx 1.618$
[@mendez2026setRecycling]. The formal machinery is small and entirely
deterministic: the round-robin rule $\sigma(i) = i \bmod n_{\mathrm{sets}}$
recycles index space without allocating a single new asset, and the Fourier
velocity scale fixture rescales both the spectral argument ($\omega/v$) and
the amplitude ($1/\lvert v\rvert$) whenever the mover's speed changes. The
paper ships a standalone reference implementation at
<https://github.com/FractiAI/synthobs-kinematic-set-recycling-truckee>,
re-runnable as `npm run research:synthobs-kinematic-set-recycling-truckee`
[@mendez2026setRecycling]. Keep the paper's own scope in view throughout:
this is catalog architecture — engine shelf #21 — not psychophysics lab QED,
not infinite XR memory savings, and not NOAA causation by AR14524/AR14527;
the Fair Exchange clause applies. Everything you compute here is bookkeeping
for a recycling catalog, not a measurement of perception.

## Procedure

1. **Run the reference implementation.** Clone the standalone repository
   above and run `npm run research:synthobs-kinematic-set-recycling-truckee`.
   In your notebook, list which of the five digest claims
   (C-kinematic-set-recycling-1 through 5) the output actually exercises —
   the one-set-many-realities filing, the three octave states, the Fourier
   velocity scale, the zero-new-asset framing, the shelf placement — and
   which remain narrative filings with no executable counterpart.
2. **Recycle a nine-item set by hand.** Take the chapter's Truckee kit: nine
   indexed items $0, \dots, 8$ and $n_{\mathrm{sets}} = 3$ experiential sets
   (stationary · pedestrian · cyclist). Apply
   $\sigma(i) = i \bmod 3$ item by item and write the three sets down. Your
   hand result must be: stationary $\{0, 3, 6\}$, pedestrian $\{1, 4, 7\}$,
   cyclist $\{2, 5, 8\}$ — exactly the partition in
   [@tbl:part_III_kinematic-recycling_partition].
3. **Break the balance on purpose.** Repeat step 2 with a 10-item set
   (indices $0, \dots, 9$) and then an 11-item set. Confirm that the spare
   items land deterministically — item 9 ($9 \bmod 3 = 0$) joins set 0 to
   give 4/3/3, and item 10 ($10 \bmod 3 = 1$) joins set 1 to give 4/4/3 —
   so the rule is deterministic, not magically even.
4. **Evaluate the Fourier velocity scale for $\Phi$-spaced speeds.** With the
   illustrative unit-base profile $F(x) = \cos x$ (the corpus leaves $F$
   abstract; this choice is plainly illustrative) and $\omega = 1$, compute
   $\tilde{S}_v(1) = \cos(1/v)/\lvert v \rvert$ by hand for
   $v \in \{1, \Phi, \Phi^2\}$, using $\Phi \approx 1.618034$:
   - $v = 1$: argument $1$, amplitude $1$ → $\cos 1 \approx 0.540302$.
   - $v = \Phi$: argument $1/\Phi \approx 0.618034$, amplitude
     $\approx 0.618034$ → $\approx 0.503710$.
   - $v = \Phi^2$: argument $1/\Phi^2 \approx 0.381966$, amplitude
     $\approx 0.381966$ → $\approx 0.354439$.
5. **Index the octave states.** Using the exponent convention, confirm the
   ladder of [@eq:part_III_kinematic-recycling_octave-ladder] at
   $\Omega_0 = 1$: state 0 (stationary) sits at $\Phi^0 = 1$, state 1
   (pedestrian) at $\Phi^1 \approx 1.618034$, state 2 (cyclist) at
   $\Phi^2 \approx 2.618034$ — the first three rungs of the pinned
   $\Phi^n$ sequence $1.618034, 2.618034, 4.236068, 6.854102, 11.090170,
   17.944272$. Then read the same three slots in the subscript convention
   ($\varphi_{\mathrm{fib}}$ ratios: $1, 1, 2$) and note the coarsening —
   the ambiguity `octave_term` exposes as a switchable convention.
6. **Verify against the model.** Run the computational workflow below and
   check every `round_robin` and `octave_term` output against your hand
   values from steps 2–5. They must match exactly.

## Analysis

Collect your three recycled partitions (9, 10, and 11 items) and your three
fixture values. Summarise the set sizes $\{3, 3, 3\}$, $\{4, 3, 3\}$, and
$\{4, 4, 3\}$ with `textbook.models.descriptive_statistics`: for the
balanced nine-item case the mean is $3.0$ with zero spread, for ten items
the mean is $\approx 3.333$ with spread (standard deviation) $\approx 0.471$,
and for eleven items the mean is $\approx 3.667$ with spread $\approx 0.577$
— the partition is deterministic, so the only "variation" is the item count
you chose. State the zero-new-asset result explicitly in your notebook:
across all three partitions, every presented item is drawn from the original
set and the "new assets purchased" column is empty — the ledger nets to zero
in the sense of `net_zero_balance` from
[@sec:part_II_singularity-crystal]. Finally,
confirm the double-rescaling property of step 4: each $\Phi$-step in speed
moves the fixture's argument *and* its amplitude by $1/\Phi \approx
0.618034$ simultaneously, which is the formal content of "velocity becomes
an octave multiplier" as filed in the chapter.

## Computational Workflow

```python
from textbook.models import round_robin, octave_term, descriptive_statistics

# Steps 2-3: recycle the Truckee kit at three sizes, verified against the model:
assert round_robin(list(range(9)), 3) == [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
assert round_robin(list(range(10)), 3) == [[0, 3, 6, 9], [1, 4, 7], [2, 5, 8]]
assert round_robin(list(range(11)), 3) == [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8]]

# Step 4: Fourier velocity scale, F(x) = cos x, omega = 1, Phi-spaced speeds:
import math
PHI = (1 + 5 ** 0.5) / 2
for v in [1.0, PHI, PHI ** 2]:
    print(round(v, 6), round(math.cos(1 / v) / abs(v), 6))
# 1.0       -> 0.540302
# 1.618034  -> 0.50371
# 2.618034  -> 0.354439

# Step 5: the octave ladder in both conventions:
print([octave_term(1, k, convention="exponent") for k in range(3)])
# [1, 1.6180339887..., 2.6180339887...]
print([octave_term(1, k, convention="subscript") for k in range(3)])
# [1, 1, 2]

print(descriptive_statistics([3, 3, 3]))  # mean 3.0, zero spread
```

## Reflection

- The paper's zero-new-asset framing is a workflow observation about Lattice
  Chat / XR pipelines, not a compression theorem. After running the
  partitions yourself, explain in one sentence why
  [@eq:part_III_kinematic-recycling_round-robin] saves no memory at all —
  what, exactly, does it move, and what does it not shrink?
- The fixture is defined for $\lvert v \rvert > 0$, yet the corpus files the
  stationary mover as state 0 of the same set. In the light of the
  [**Topology of the Void**](#gl:topology-of-the-void) reading of zero as a
  live state ([@sec:part_I_topology-void]), why is it coherent — and why is
  it *necessary* for honesty — that the chapter assigns the stationary state
  no numerical limit?
- Write the Fair Exchange sentence you would attach to a claim that faster
  walking *feels* twice as rich. What does the clause forbid, and which of
  the paper's four "not" clauses does your sentence echo?
