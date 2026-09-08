# Lab — Humans as Omniversal Reality Bridges {#sec:lab_part_III_reality-bridge}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) build the Φ-keyed octave ladder of the
reality-bridge filing by hand and verify it against
`textbook.models.octave_term` and `textbook.models.phi_powers`, (2) compute
the cognitive-router throttle column and its routed-to-today shares with
`textbook.models.transduction_brake`, and (3) run the paper's reference
implementation and articulate — in one written paragraph — exactly what the
bridge/router/wormhole filing claims and what its honesty-first scope rules
out [@mendez2026realityBridge].

## Background

Linked chapter: [@sec:part_III_reality-bridge]. The 28 August 2026 ship-blog
note files humans as the routing layer of the Infinite Octaves catalogue — a
[**reality-bridge**](#gl:reality-bridge), a cognitive router, and an awareness
wormhole — keyed by the octave-step relation $O_{n+1} = O_n \cdot \Phi$
(the chapter's [@eq:part_III_reality-bridge_octave], backed by
`textbook.models.octave_term`) [@mendez2026realityBridge]. The note states the
router's throttling topologically, without an equation; the chapter
formalises it as the exponential decay of
[@eq:part_III_reality-bridge_throttle], reusing the tested
`transduction_brake` family. Nothing in this lab touches physics hardware or
neurology: every move is arithmetic on filed values — the construct is the
filing, not spacetime.

## Procedure

1. **Hand-build the octave ladder.** Using $\Phi = 1.6180339887$ and
   $\Omega_0 = 1$, multiply successively from
   [@eq:part_III_reality-bridge_octave]: $\Omega_1 = 1.618034$,
   $\Omega_2 = 2.618034$, $\Omega_3 = 4.236068$, $\Omega_4 = 6.854102$ (pinned
   values from the book's computational backbone), continuing by repeated
   multiplication to $\Omega_5 = 11.090170$ and $\Omega_6 = 17.944272$. Keep
   six decimal places.
2. **Hand-compute the throttle column.** With $A_0 = 1$ and $k = 1$, evaluate
   $A(n) = e^{-n}$ for $n = 1 \ldots 6$. Write each value and its
   routed-to-today complement $1 - e^{-n}$ next to the ladder column. The
   first two are the pinned calibration points: $A(1) = 0.367879$,
   $A(2) = 0.135335$.
3. **Check against the model.** In a Python session, call
   `textbook.models.octave_term(omega0=1.0, n, convention="exponent")` for
   $n = 1 \ldots 6$ and `textbook.models.transduction_brake([1, 2, 3, 4, 5, 6], 1.0, 1.0)`, and
   compare both to your hand columns. Repeat step 1's check with
   `convention="subscript"` and record how badly it diverges at low indices
   ($\Omega_1 = 1$ vs. $1.618034$).
4. **Walk a route.** A guest question enters at the museum frame and is
   routed three hops deep (router menu, then the hospitality path to the
   Creator Studio). Using [@tbl:part_III_reality-bridge_routing], state the
   routed-to-today share of attention at each hop and confirm the two shares
   sum to one with the background share — the router *allocates*, it does not
   delete.
5. **Run the reference implementation.** From the repository root, run
   `npm run research:synthobs-human-omniversal-reality-bridge`. *Before*
   running it, write down your prediction of the fixture-lock line; the
   chapter says the passing state is 10/10. Run it and compare prediction to
   observation.

## Analysis

Summarise the six throttle values of step 2 with
`textbook.models.descriptive_statistics`, and add the structural checks that
matter more than any summary statistic:

- the **ratio check**: $\Omega_{n+1}/\Omega_n = \Phi$ exactly for every $n$ in
  $1..6$ — the harmonic filing grammar the note names
  [@mendez2026realityBridge];
- the **complement check**: $A(n) + (1 - A(n)) = 1$ at every depth, i.e. the
  router role conserves attention between "what matters today" and the grand
  arc of 8,019 catalogue entries (`textbook.models.catalog_size`);
- the **convention gap**: at index 4 the exponent convention gives
  $\Omega_4 = 6.854102$ while the subscript convention gives $F_5/F_4 = 5/3
  \approx 1.666667$ — the same divergence the y-chromosome chapter pins down
  in [@sec:part_III_y-chromosome], and the reason the note's printed
  recurrence $O_n \times \Phi$ must be read as the exponent form;
- the **fixture observation**: whether the reference implementation reported
  the predicted 10/10 lock, and what any deviation would mean (a filing
  contract change, not a routing result).

Close the analysis with the honesty statement in your own words, then check
it against the source: catalog topology and narrative routing — not hardware
teleport, not clinical proof of neural quantum wormholes, not $\Phi$ replacing
physics constants; Valet Pru bridges by awareness, not by breaking spacetime;
and human emergency still outranks every metaphor [@mendez2026realityBridge].

## Computational Workflow

```python
from textbook.models import (
    octave_term, phi_powers, transduction_brake, catalog_size,
    descriptive_statistics,
)

# Step 3: the exponent-convention ladder behind [@tbl:part_III_reality-bridge_routing]
ladder = [octave_term(omega0=1.0, n=n, convention="exponent") for n in range(7)]
print(ladder)
# expected: [1.0, 1.618034, 2.618034, 4.236068, 6.854102, 11.090170, 17.944272]
print(phi_powers(6))  # the same Φ^n column

# Step 3 (continued): the throttle column, A_0 = 1, k = 1
brake = transduction_brake([1, 2, 3, 4, 5, 6], 1.0, 1.0)
print(brake)
# expected: [0.367879, 0.135335, 0.049787, 0.018316, 0.006738, 0.002479]

# Step 4: routed-to-today shares at hops 1-3
shares = 1 - brake[:3]
print(shares)
# expected: [0.632121, 0.864665, 0.950213] (to 6 d.p.)

# The filing surface the router keeps in the background
print(catalog_size())  # 99 × 81 = 8019

# Analysis: summarise the six throttle values
print(descriptive_statistics(brake))

# Step 5 (shell, not Python): the paper's own fixture lock
#   npm run research:synthobs-human-omniversal-reality-bridge
# predict the fixture line before running: expect 10/10.
```

## Deliverable

A one-page lab note containing: your two hand columns (ladder and throttle),
the model-checked values, the routed-to-today shares for the three-hop route
of step 4, your predicted vs. observed fixture-lock line, and the one
paragraph separating what the filing *is* (catalog topology and narrative
routing keyed by $\Phi \approx 1.618$ as design language) from what it
*disclaims* (hardware teleport, clinical wormholes, $\Phi$ replacing physics
constants) [@mendez2026realityBridge].

## Reflection

1. The note's filing card says "You are not a passive screen in someone
   else's simulation." In filing terms, what does *routing* buy the human
   that *passive receiving* would not — and which of the three roles carries
   that weight?
2. Your ladder column grows by a fixed factor while your throttle column
   shrinks at a fixed rate. Why is it honest for the book to formalise one
   directly from the note's equation and the other only as interpretation?
3. Where would a study that *measured* human attention routing sit in the
   corpus's narrative-empirical-operational tiers, and what would have to
   change in the note's wording the day such a measurement were actually
   executed?
