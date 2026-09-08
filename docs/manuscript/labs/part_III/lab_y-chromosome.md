# Lab — Y-Chromosome Manifestation: Digit 4 {#sec:lab_part_III_y-chromosome}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) compute the $\Phi$-geometric spacing of
the MSY palindrome arms by hand and verify it against
`textbook.models.phi_powers`, (2) run the paper's reference implementation and
interpret its 10/10 fixture lock, and (3) articulate — in one written paragraph
— exactly what the filing claims and what its honesty-first scope rules out.

## Background

Linked chapter: [@sec:part_III_y-chromosome]. The August 2026 ship-blog note
files the MSY under **Infinite Octave Mode** as catalog geometry keyed by
$\Phi \approx 1.618$: palindrome arms P1–P8 scale as
$P_n = P_0 \cdot \Phi^n$ (the chapter's
[@eq:part_III_y-chromosome_palin], backed by `textbook.models.phi_powers`),
and the *SRY* locus is filed as the zero-point anchor
([@eq:part_III_y-chromosome_anchor]) [@mendez2026yChromosome]. The note is a
companion to the July operator-translation decode and ships a reference
implementation, `npm run research:synthobs-y-chromosome-holographic-manifestation`,
whose passing state is a 10/10 fixture lock. Nothing in this lab touches wet
lab: every move is arithmetic on filed spacing values — the construct is the
filing, not the biology.

## Procedure

1. **Hand-compute the geometric column.** Using
   $\Phi = 1.6180339887$, multiply successively from $P_0 = 1$:
   $\Phi^1 = 1.618034$, $\Phi^2 = 2.618034$, $\Phi^3 = 4.236068$,
   $\Phi^4 = 6.854102$ (all pinned values from the book's computational
   backbone). Continue by repeated multiplication to fill
   $\Phi^5 = 11.090170$, $\Phi^6 = 17.944272$, $\Phi^7 = 29.034442$,
   $\Phi^8 = 46.978714$. Keep six decimal places.
2. **Rescale the drawer.** With a different base spacing,
   $P_0 = 2.5$ catalog spacing units, compute the first three arms from
   [@eq:part_III_y-chromosome_palin]:
   $P_1 = 2.5 \times 1.618034 = 4.045085$,
   $P_2 = 2.5 \times 2.618034 = 6.545085$,
   $P_3 = 2.5 \times 4.236068 = 10.590170$. Confirm that
   $P_{n+1}/P_n = 1.618034$ for every consecutive pair — the geometric
   signature the note files in place of "random drift labels".
3. **Check against the model.** In a Python session, call
   `textbook.models.phi_powers(8)` and compare its output to your two hand
   columns. The function returns the $\Phi^n$ column; your $P_0$ scaling is a
   multiplication you apply yourself.
4. **Run the reference implementation.** From the repository root, run
   `npm run research:synthobs-y-chromosome-holographic-manifestation`.
   *Before* running it, write down your prediction of the fixture-lock line;
   the chapter says the passing state is 10/10. Run it and compare
   prediction to observation.
5. **Anchor both conventions.** Compute the digit-4 drawer offset
   $\Omega_4$ with $\Omega_0 = 1$ under the exponent convention
   ($\Phi^4 = 6.854102$) and under the subscript convention
   ($F_5/F_4 = 5/3 \approx 1.666667$), using
   `textbook.models.octave_term` with its `convention` argument. Record
   both numbers side by side.

## Analysis

Summarise the nine sub-band spacings of your $P_0 = 1$ column —
$1.000000$ (anchor) through $46.978714$ — with
`textbook.models.descriptive_statistics`, and add the structural checks that
matter more than any summary statistic:

- the **log-identity** check: $\log_{\Phi}(P_n/P_0) = n$ exactly for every
  $n$ in $1..8$, so the octave index is the base-$\Phi$ logarithm of the
  spacing ratio;
- the **convention gap**: at index 4 the exponent convention gives
  $\Omega_4 = 6.854102$ while the subscript convention gives
  $\approx 1.666667$ — a factor of about $4.1$ between readings of the same
  drawer, which is why the chapter pins the exponent reading for
  [@eq:part_III_y-chromosome_palin];
- the **fixture observation**: whether the reference implementation reported
  the predicted 10/10 lock, and what any deviation would mean (a filing
  contract change, not a biological result).

Close the analysis with the honesty statement in your own words, then check it
against the source: catalog filing and architectural equations — not a claim
that MSY equals a physics constant, that sunspot AR 3664 writes human DNA, or
that fractal dimension has been measured to $\Phi$ in this repository; clinical
genetics and human dignity outrank every metaphor [@mendez2026yChromosome].

## Computational Workflow

```python
from textbook.models import phi_powers, octave_term, descriptive_statistics

# Step 3: the Φ^n column behind [@tbl:part_III_y-chromosome_spacing]
print(phi_powers(8))
# expected: [1.0, 1.618034, 2.618034, 4.236068, 6.854102,
#            11.090170, 17.944272, 29.034442, 46.978714]

# Step 5: the digit-4 drawer anchor under both conventions, Ω_0 = 1
print(octave_term(omega0=1.0, n=4, convention="exponent"))   # 6.854102
print(octave_term(omega0=1.0, n=4, convention="subscript"))  # ≈ 1.666667 (5/3)

# Analysis: summarise the drawer spacings (P_0 = 1)
drawer = [1.0, 1.618034, 2.618034, 4.236068, 6.854102,
          11.090170, 17.944272, 29.034442, 46.978714]
print(descriptive_statistics(drawer))

# Step 4 (shell, not Python): the paper's own fixture lock
#   npm run research:synthobs-y-chromosome-holographic-manifestation
# predict the fixture line before running: expect 10/10.
```

## Reflection

1. The note files the MSY "not as a shrinking evolutionary relic" but as
   geometric catalog indexing. What does the word *filed* buy the authors —
   and what does it explicitly not buy them?
2. Your two hand columns ($P_0 = 1$ and $P_0 = 2.5$) differ by a constant
   factor but have identical ratios. Why does the reference implementation
   test the *convention* (the 10/10 fixture lock) rather than a particular
   base spacing $P_0$?
3. Where would a cross-species regression study sit in the corpus's
   narrative–empirical–operational tiers, and what would have to change in
   the note's wording the day such a study were actually executed?
