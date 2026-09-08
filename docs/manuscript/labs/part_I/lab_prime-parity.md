# Lab — Prime-Parity: The Sole-Even Anchor {#sec:lab_part_I_prime-parity}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) run the paper's replayable fixture suite
and predict its outcome before running it, (2) compute the parity partition of
the primes by hand for small cutoffs and check it against
`textbook.models.prime_parity_partition`, and (3) compute octave terms under
both printed conventions and verify them against
`textbook.models.octave_term`.

## Background

Linked chapter: [@sec:part_I_prime-parity]. The chapter established the parity
filing: sole-even 2 as the [**binary dyad anchor**](#gl:binary-dyad-anchor),
odd primes as [**irreducible minimum sets**](#gl:irreducible-minimum-set), and
the octave recursion $\Omega_n = \Phi_n \cdot \Omega_0$ of
[@eq:part_I_prime-parity_model] — ambiguous as printed between exponent and
subscript readings, both first-class in the tested model function. This lab
makes you *run* that filing twice: once through the paper's own fixture suite,
once through your own hand arithmetic, so the two agree by construction rather
than by trust.

The source paper ships **9/9 replayable fixtures** under
`research/synthobs-infinite-octave-prime-parity/` [@mendez2026primeParity], with
a standalone repository at
`https://github.com/FractiAI/synthobs-infinite-octave-prime-parity`. Its
companion volume on the recursion constant is the Fractal Constant chapter
[@sec:part_I_fractal-constant]; keep both open.

## Procedure

1. **Predict, then run the suite.** Before running anything, write down what
   you expect the 9/9 result to assert: that the `sole_even` class is always
   exactly `[2]` and that the odd class contains no even numbers. Then re-run
   the paper's own suite from the repo root:

   ```bash
   npm run research:synthobs-infinite-octave-prime-parity
   ```

   Confirm the suite reports 9/9 passing fixtures [@mendez2026primeParity]. If
   your prediction differed from the fixtures' content, note where.

2. **Partition by hand.** Without code, list the primes below 12, below 32, and
   below 100, and split each list into the anchor class and the odd class.
   Expect (for limit 32): `sole_even = [2]` and
   `odd = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]` — exactly the layout drawn in
   [@fig:part_I_prime-parity].

3. **Check against the backbone.** Evaluate the same three cutoffs with the
   tested function and compare:

   ```python
   from textbook.models import prime_parity_partition
   prime_parity_partition(12)   # {'sole_even': [2], 'odd': [3, 5, 7, 11]}
   prime_parity_partition(32)   # ten odd primes, anchor singleton
   prime_parity_partition(100)  # 25 odd primes, anchor still a singleton
   ```

4. **Walk the octave ladder by hand.** Using $\Phi = 1.6180339887$ and
   $\Omega_0 = 1$, compute $\Omega_1$ through $\Omega_4$ under the exponent
   convention by repeated multiplication ($1.618034,\ 2.618034,\ 4.236068,\
   6.854102$). Then compute the subscript reading at $n = 5$ and $n = 10$ from
   the Fibonacci ratios $F(6)/F(5) = 8/5 = 1.6$ and $F(11)/F(10) = 89/55
   \approx 1.618182$.

5. **Check against `octave_term`.** Verify every value from step 4:

   ```python
   from textbook.models import octave_term
   octave_term(1.0, 4, "exponent")   # 6.854102
   octave_term(1.0, 5, "subscript")  # 1.6
   octave_term(1.0, 10, "subscript") # 1.6181818…
   ```

## Analysis

Summarise the two runs side by side. The suite run establishes that the paper's
own fixtures pin the partition invariant — anchor class a singleton, odd class
even-free — at every tested cutoff. The hand run establishes that *you* can
reproduce that invariant without the fixtures. Then summarise the ladder
comparison: at $n = 5$ the two conventions of
[@eq:part_I_prime-parity_subscript] and [@eq:part_I_prime-parity_model] differ
by more than a factor of six (11.090170 vs 1.6), while by $n = 10$ the subscript
ratio 1.618182 has closed to within $0.01\%$ of $\Phi$. Conclude with the
one-sentence moral: the conventions agree in the limit and diverge at small $n$,
which is precisely why `octave_term` makes you name your convention.

Report summary statistics for your computed odd-prime lists (count, largest
element) with `textbook.models.descriptive_statistics` if you want a checked
record of the shapes you observed.

## Computational Workflow

```python
from textbook.models import prime_parity_partition, octave_term, unique_address

# Parity filing at three cutoffs — compare with your hand lists.
for limit in (12, 32, 100):
    part = prime_parity_partition(limit)
    print(limit, len(part["sole_even"]), len(part["odd"]))

# Both printed conventions of the octave recursion, Omega_0 = 1.
for n in (1, 2, 3, 4, 5, 6):
    print(n, octave_term(1.0, n, "exponent"), octave_term(1.0, n, "subscript"))

# Joint filing: anchor prime with the first odd irreducible set.
print(unique_address([2, 3], [2, 1]))  # 12 = 2^2 * 3^1
```

Expected anchor counts at every cutoff: `1` whenever 2 is below the limit. A
count other than 1 would falsify the sole-even filing — there is no such run.

## Reflection

- The fixtures assert a *singleton* anchor class. What would it take —
  arithmetically — for a second even prime to appear, and why does the filing
  treat that as impossible rather than merely unlikely?
- You computed $\Omega_5$ twice and got two different numbers (11.090170 and
  1.6) from one printed formula. Which convention would you *file* the paper
  under, and what does the corpus's decision to keep both tell you about
  [**honesty-first**](#gl:honesty-first) documentation?
- The paper calls solar AR3664 ("Helios-Prime") a "story character for timing
  talk." Where in this lab did a *label* do work, and where would a label be
  masquerading as a proof?
