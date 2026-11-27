# Lab — El Gran Sol's Fractal Constant {#sec:lab_part_I_fractal-constant}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

<!-- What the learner will be able to do after this lab. -->

After this lab you will be able to: (1) evaluate the powers of El Gran Sol's Fractal
constant $\Phi \approx 1.618$ by hand and confirm them with
`textbook.models.phi_powers`; (2) evaluate **both** conventions of the corpus's octave
recursion sketch with `textbook.models.octave_term` and explain why the ambiguity matters
numerically; (3) run two of the corpus's replayable fixture suites and predict their lock
counts before observing them.

## Background

Linked chapter: [@sec:part_I_fractal-constant]. The chapter formalised the corpus's
recursion sketch $\Omega_n = \Phi_n \cdot \Omega_0$, printed ambiguously in the prime-parity
paper — whether $\Phi$ carries an exponent or a subscript is ambiguous as printed
[@mendez2026primeParity]. The book files both readings as
[@eq:part_I_fractal-constant_octave-term]: exponent, $\Omega_n = \Phi^n\,\Omega_0$, and
subscript, $\Omega_n = \varphi_{\text{fib}}(n)\,\Omega_0$. The same constant keys the
digit-filing duality of Proton Space (1) and Electron Theater (2)
[@mendez2026protonTheater] and the palindrome-scaling law
[@eq:part_I_fractal-constant_palindrome] $P_n = P_0 \cdot \Phi^n$ from the Y-chromosome
manifestation paper [@mendez2026yChromosome]. Today you walk all three filings by hand, then
let the tested functions keep you honest.

## Procedure

1. **Build the Φ ladder by hand.** Starting from $\Phi = 1.6180339887$, multiply
   repeatedly by $\Phi$ to fill the table for $n = 1,\dots,6$. Predict before you compute:
   each entry is the previous entry times $\Phi$. You should obtain $1.618034$, $2.618034$,
   $4.236068$, $6.854102$, $11.090170$, $17.944272$.
2. **Add the Fibonacci convergents.** Compute the ratios $F_{n+1}/F_n$ from the Fibonacci
   sequence $1, 1, 2, 3, 5, 8, 13, 21, \dots$: the 5th ratio is $8/5 = 1.6$ and the 10th is
   $89/55 \approx 1.618182$. Note how they climb toward $\Phi$ from below — the overlay
   series plotted in [@fig:part_I_fractal-constant].
3. **Split the primes.** For the limit $31$, partition the primes into the sole-even
   anchor $\{2\}$ and the odd classes $\{3, 5, 7, 11, 13, 17, 19, 23, 29, 31\}$. Count the
   classes: one anchor, ten odd primes. This is the parity scaffold behind
   `textbook.models.prime_parity_partition(31)` [@mendez2026primeParity].
4. **Scale the palindrome arms.** With $P_0 = 1$, apply $P_n = P_0 \cdot \Phi^n$ for
   $n = 1,\dots,8$ (reuse step 1 and extend two steps: $\Phi^7 \approx 29.034442$,
   $\Phi^8 \approx 46.978714$). These index the MSY palindrome arms P1–P8 as catalog
   geometry [@mendez2026yChromosome] — filing labels, not measured biological spacing.
5. **Run the corpus suites (optional, needs the research checkout).** If you have the
   corpus research tree available, predict the lock counts, then re-run and observe:
   - `npm run research:synthobs-infinite-octave-prime-parity` — predict **9/9** replayable
     fixtures [@mendez2026primeParity];
   - `npm run research:synthobs-y-chromosome-holographic-manifestation` — predict a
     **10/10** fixture lock [@mendez2026yChromosome].
   Record predicted vs. observed for each. If the suites are unavailable, treat the
   predictions as the digest's recorded claims.

## Analysis

<!-- Summarise results with textbook.models.descriptive_statistics. -->

Compare your hand-built ladder with the tested backbone. The ratios of consecutive
hand-built entries should all be $1.618034\ldots$ to six decimals; feed your six ladder
values to `textbook.models.descriptive_statistics` and confirm the ratio column is constant
before the last digit of rounding. For the two recursion conventions at $\Omega_0 = 275$,
$n = 5$, your analysis table should show exponent $\approx 3{,}049.80$ filing units vs.
subscript exactly $440$ filing units — a factor of roughly $6.9$ between readings of the
*same printed sentence*. State in one written line which convention you would file as the
"catalog octave" reading and why the corpus's decision to print the ambiguity, not resolve
it, is the honesty-first choice. Finally, check your prime partition against the counts of
step 3: exactly one sole-even anchor, ten odd-prime irreducible sets under $31$.

## Computational Workflow

```python
from textbook import models

# Step 1: the Phi ladder (expected: 1.618034, 2.618034, 4.236068,
# 6.854102, 11.090170, 17.944272)
ladder = models.phi_powers(6)

# Step 2: Fibonacci ratios (expected: phi_fib(5) = 1.6,
# phi_fib(10) ≈ 1.618182)
ratio_5 = models.phi_fibonacci(5)
ratio_10 = models.phi_fibonacci(10)

# Both conventions of the octave recursion sketch, Omega_0 = 275, n = 5
omega_exp = models.octave_term(275, 5, "exponent")    # expected ≈ 3049.797
omega_sub = models.octave_term(275, 5, "subscript")   # expected 440.0

# Step 3: the parity partition (sole-even anchor vs odd classes)
partition = models.prime_parity_partition(31)

# Step 4: palindrome arms P1..P8 from the same powers of Phi
arms = [models.phi_powers(8)[n - 1] for n in range(1, 9)]
```

## Reflection

1. The exponent and subscript conventions diverge by a factor of ~6.9 at $n = 5$. What
   does that divergence tell you about the cost of silently "resolving" an ambiguity the
   source flagged deliberately?
2. The Y-chromosome paper insists the palindrome scaling is "catalog geometry … not random
   drift labels" while also disclaiming any measured fractal dimension. Where exactly does
   the line between *filing* and *measurement* sit in $P_n = P_0 \cdot \Phi^n$?
3. The prime dyad (2) and the digit dyad (1 and 2) both route through the same constant.
   What would have to be true of the corpus for that convergence to be more than filing
   convenience — and does any source paper claim it is?
