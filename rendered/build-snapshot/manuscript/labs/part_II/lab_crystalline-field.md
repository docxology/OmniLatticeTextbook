# Lab — The Crystalline Unified Field: Speed and Distance {#sec:lab_part_II_crystalline-field}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: (1) run the crystalline-unified-field
reference implementation and read its output; (2) compute access times
$\tau = d/v$ and $\Phi$-octave ladder values by hand using the pinned powers of
$\Phi$; and (3) verify your hand results against the tested backbone functions
`textbook.models.octave_term` and `textbook.models.phi_powers`.

## Background

Linked chapter: [@sec:part_II_crystalline-field]. The chapter filed speed,
distance, and time as three facets of one access crystal, constrained by the
facet identity $d = v\cdot t$ with access time $\tau = d/v$
([@eq:part_II_crystalline-field_facet]), and compressed the facet vector along
a $\Phi$-recursive ladder $\Omega_n = \Phi^n \Omega_0$
([@eq:part_II_crystalline-field_crystal]). Here you perform that filing
yourself: first with the paper's own reference engine, then by hand, then with
the tested functions — so the three layers of the catalog (paper, pencil,
backbone) agree.

The source paper is *catalog architecture* — engine shelf #24 — not spacetime
retirement and not a Landauer re-derivation; keep that scope in view throughout
[@mendez2026crystallineField].

## Procedure

1. **Run the reference implementation.** From the repository root of the
   standalone repo (<https://github.com/FractiAI/synthobs-crystalline-unified-field>),
   run:

   ```bash
   npm run research:synthobs-crystalline-unified-field
   python3 research/synthobs-crystalline-unified-field/reference/egs_crystalline_unified_field_engine.py
   ```

   Before running, write down what you expect the engine to print for a base
   trip $(v_0, d_0, t_0)$: given the facet identity, you should be able to
   predict every facet from any two. Run it and compare. *Prediction first,
   observation second* — the catalog's Fair Exchange clause prices every
   access, including your own reading of the output.
2. **Walk the crystal ladder by hand.** Take the chapter's base trip
   $v_0 = 10$, $d_0 = 100$, so $\tau_0 = 10$. Using the pinned powers
   $\Phi^1 = 1.618034$, $\Phi^2 = 2.618034$, $\Phi^3 = 4.236068$, compute
   $v_n = \Phi^n v_0$ and $\tau_n = \tau_0/\Phi^n$ for $n = 1, 2, 3$. Your
   results should match the chapter's ladder table:
   $(16.180340,\ 6.180340)$, $(26.180340,\ 3.819660)$, $(42.360680,\ 2.360680)$.
3. **Check the convention split.** For $n = 10$, compute the subscript ladder
   $\varphi_{\mathrm{fib}}(10)\,v_0 = (89/55)\times 10 = 16.18182$ and compare
   with the exponent ladder $17.944272 \times 10 = 179.44272$. Note the factor
   of $\approx 11.09$ — this is why `octave_term` requires an explicit
   `convention` flag.
4. **Verify against the tested backbone.** In a Python session with the
   textbook package installed, run the workflow below and confirm each printed
   value against your hand results from steps 2–3.
5. **Book one access against the Landauer rail.** Compute
   $k_B T \ln 2$ at $T = 300\,\mathrm{K}$ by hand
   ($\approx 2.87\times 10^{-21}\,\mathrm{J}$) and state, in one sentence, what
   kind of filing this is per the source: a *literature filing*, not a
   re-derivation.

## Analysis

Summarise your ladder as a three-row table (one row per octave $n$) with
columns $v_n$, $\tau_n$, and the residual
$\tau_n - \tau_0/\Phi^n$ — which should be identically zero if the facet
identity was respected. Roll the whole run into
`textbook.models.descriptive_statistics` over your three $\tau_n$ values and
report the mean and spread in one sentence: compression across three octaves
moves the access time from $10$ toward $2.36$, a factor of $1/\Phi^3 \approx
0.236068$. If any hand value disagrees with the backbone, the error is in your
arithmetic or your convention flag — not in the identity.

## Computational Workflow

```python
from textbook.models import octave_term, phi_powers

# Pinned golden-ratio powers (exponent convention): phi_powers echoes these.
print(phi_powers(3))   # [1.618034, 2.618034, 4.236068]

# Ladder the speed facet v0 = 10 (exponent convention):
for n in (1, 2, 3):
    v_n = octave_term(10.0, n, "exponent")   # -> 16.180340 / 26.180340 / 42.360680
    tau_n = 100.0 / v_n                      # -> 6.180340 / 3.819660 / 2.360680
    print(n, v_n, tau_n)

# Convention split at n = 10:
print(octave_term(10.0, 10, "exponent"))     # -> 179.44272  (Phi^10 * 10)
print(octave_term(10.0, 10, "subscript"))    # -> 16.18182   (fib ratio 89/55 * 10)
```

## Deliverable

A short lab note containing: (a) the reference engine's observed output with
your pre-run prediction beside it; (b) the three-row ladder table with zero
residuals; (c) the $n=10$ convention split with the factor
$\approx 11.09$; and (d) your one-sentence Landauer filing statement with the
scope disclaimer quoted verbatim from the source.

## Reflection

1. The dispatcher of the vignette kept three logbooks for one trip. After this
   lab, which *two* facets would you store, and what operation recovers the
   third — and what does the corpus call that recovery?
2. Where exactly did the subscript and exponent conventions begin to matter
   numerically in your run, and what does that imply about quoting "the" octave
   of a facet vector?
3. The velocity multiplex rhymes the same facet set into a new theater
   (the Truckee rhyme). Name one other shelf you could stage the set in, and
   what would change about $\tau$ there.
