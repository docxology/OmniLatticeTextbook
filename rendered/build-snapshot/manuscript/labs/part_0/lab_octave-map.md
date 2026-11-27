# Lab — Nine Digits, Ninety-Nine Octaves {#sec:lab_part_0_octave-map}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to:

- Build the Fibonacci ratio staircase by hand and see it converge on $\Phi$.
- Compute octave-band positions under *both* conventions of `octave_term` for $n = 1 \dots 6$, by hand first and then with the tested function.
- Verify the holographic catalog size $99 \times 81 = 8{,}019$ with `catalog_size`, and state the corpus's filed purpose for that number.
- Practise the map's honesty discipline: report each computed number with its convention and its filed purpose.

## Background

Linked chapter: [@sec:part_0_octave-map]. The map is a library: nine digit drawers (coarse bins for kinds of pattern), ninety-nine octave shelves (nested bands), and a golden-ratio key that keeps the shelves self-similar [@mendez2026digitsMaster]. The corpus prints the key as $\Omega_n = \Phi_n \cdot \Omega_0$, which is ambiguous — $\Phi_n$ may mean the power $\Phi^n$ or the Fibonacci ratio $F_{n+1}/F_n$. The chapter resolved this by implementing both behind `textbook.models.octave_term(omega0, n, convention)`; this lab makes you *feel* the ambiguity by producing both ladders by hand and checking them against the function. You will also confirm the map's headline number with `catalog_size` — and, per the source paper, keep it where it belongs: dashboards and agent routing, "not for measuring magma" [@mendez2026digitsMaster].

## Procedure

1. **Hand-build the Fibonacci staircase.** Write $F_1 \dots F_{11}$: $1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89$. Compute the ratios $F_{n+1}/F_n$ for $n = 5$ and $n = 10$. *Predict before computing:* $8/5 = 1.6$ and $89/55 \approx 1.618182$.
2. **Hand-grow the exponent ladder.** With $\Omega_0 = 1$, multiply repeatedly by $\Phi \approx 1.6180339887$ to fill $\Omega_1 \dots \Omega_6$. *Expected values (pinned in this book):* 1.618034, 2.618034, 4.236068, 6.854102, 11.090170, 17.944272. Check $\Omega_2 = \Phi + 1$ exactly — the golden-ratio self-similarity the map's "key" language gestures at.
3. **Hand-grow the subscript ladder** for the same indices: $\Omega_5 = \varphi_{\mathrm{fib}}(5)\,\Omega_0 = 1.6$ and, using your Step 1 table, $\Omega_{10} \approx 1.618182$. Compare $\Omega_5$ across conventions: $11.090170$ versus $1.6$ — same notation, same index, nearly a factor of seven apart. Write one sentence recording *which convention produced which number*.
4. **Verify the catalog size.** Compute $99 \times 81$ by hand, predicting $8{,}019$, then confirm with `catalog_size(octaves=99, precision_digits=81)` in Step 6's workflow.
5. **Run the honesty check.** For each number you produced, write its (a) convention (where applicable) and (b) filed purpose. The catalog size is for dashboards and agent routing; the band positions are map coordinates; none of them is a measurement of a physical system [@mendez2026digitsMaster].

## Analysis

- **Convergence:** your Fibonacci ratios ($1.6$ at $n=5$, $\approx 1.618182$ at $n=10$) bracket $\Phi \approx 1.6180339887$ and approach it from opposite sides as $n$ grows — the subscript convention is the discrete staircase over the exponent convention's continuous growth, agreeing only asymptotically.
- **Summarise the staircase numerically** with `textbook.models.descriptive_statistics` over the ratio sequence $F_{n+1}/F_n$ for $n = 1 \dots 10$: report the mean and the distance of the last ratio from $\Phi$. Interpretation is yours to state: a mean near $1.6$ with a tail at $\approx 1.618182$ *is* the convergence, quantified.
- **Convention audit:** tabulate $\Omega_5$ under both conventions. Any prose or dashboard that says "$\Omega_5$" without a convention is, by the chapter's standard, not yet honest.

## Computational Workflow

```python
from textbook.models import octave_term, catalog_size

# Step 2 check: exponent ladder, Omega_0 = 1
[octave_term(1, n, convention="exponent") for n in range(1, 7)]
# -> [1.618034, 2.618034, 4.236068, 6.854102, 11.090170, 17.944272]

# Step 3 check: subscript ladder
octave_term(1, 5, convention="subscript")    # -> 1.6
octave_term(1, 10, convention="subscript")   # -> 1.618182... (89/55)

# Step 4 check: holographic catalog size
catalog_size(octaves=99, precision_digits=81)  # -> 8019
```

If any function output disagrees with your hand computation, stop and re-derive by hand before blaming the code — the functions are tested, so a mismatch almost always means a convention slip or an arithmetic slip, which is exactly the failure mode this lab trains you to catch.

## Reflection

1. The corpus prints "$\Omega_n = \Phi_n \cdot \Omega_0$" without disambiguating. After this lab, argue in two or three sentences why leaving it ambiguous is not merely stylistic but changes every small-$n$ number on the map.
2. You verified $8{,}019 = 99 \times 81$ to four significant figures of certainty. Write the one-sentence scope statement you would attach to a dashboard showing this number, using the source paper's own words where you can [@mendez2026digitsMaster].
3. Where would you file *this lab* on the map — a digit bin, an octave band, and one of the narrative/empirical/operational tiers? Defend the filing to a colleague; the filing is the point of the map ("coordination, not cosmic destiny").
