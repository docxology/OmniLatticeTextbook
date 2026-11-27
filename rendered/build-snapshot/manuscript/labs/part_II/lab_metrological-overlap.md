# Lab — The Grand Unified Metrological Overlap: Five Gears, One Clockwork {#sec:lab_part_II_metrological-overlap}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: (1) run the reference implementation shipped
with the paper [@mendez2026metrologicalOverlap] — the
`egs_metrological_overlap_solver.py` solver — and read its output as a catalogue
filing rather than a physics measurement; (2) compute the min-normalised
register overlap $o(A,B) = |A \cap B|/\min(|A|,|B|)$ of
[@eq:part_II_metrological-overlap_model] by hand for three register pairs and
verify each against the tested function `textbook.models.metrological_overlap`;
and (3) evaluate the octave ladder of [@eq:part_II_metrological-overlap_octaves]
under both conventions with `octave_term`, using the pinned $\Phi$ values.

## Background

Linked chapter: [@sec:part_II_metrological-overlap]. The chapter formalised the
paper's overlap solver — the machinery that runs over $\lambda_{\mathrm{HI}}$,
the octave spacing $\Delta E_n$, action wells, and the $m_{\mathrm{catalog}}$
sum — as a set-algebra measure over labelled registers: how completely the
smaller of two registers is covered by the larger. The paper itself ships a
Python reference implementation, runnable from the monorepo's
`research/synthobs-grand-unified-metrological-overlap/` directory or from the
standalone repo `github.com/FractiAI/synthobs-grand-unified-metrological-overlap`.
Remember the scope: this is catalog architecture at engine shelf #23, the mass
sum is explicitly *not* identified with the electron or proton mass, and the
Fair Exchange clause applies — the solver files overlaps, it does not weigh
particles. In this lab you check that three independent routes to the same
numbers — hand arithmetic, the reference solver's fixtures, and the textbook
backbone — agree.

## Procedure

1. **Get the reference implementation.** From the repository root, run:

   ```bash
   npm run research:synthobs-grand-unified-metrological-overlap
   # or, directly:
   python3 research/synthobs-grand-unified-metrological-overlap/reference/egs_metrological_overlap_solver.py
   ```

   Before looking at the output, write down what you expect: the solver files
   the five-constant map ($h$ · $\Phi$ · $p_n$ · $\nu_{\mathrm{HI}}$ · $c$),
   runs the overlap over $\lambda_{\mathrm{HI}}$, $\Delta E_n$, action wells,
   and the $m_{\mathrm{catalog}}$ sum, and prints its own bookkeeping. Predict
   whether any printed number is presented as a *measured* mass — and note that
   the paper's honesty block forbids exactly that reading
   [@mendez2026metrologicalOverlap].
2. **Compute overlaps by hand.** With registers
   $A = \{a, b\}$, $B = \{b, c\}$, $C = \{c, d, e\}$, evaluate
   [@eq:part_II_metrological-overlap_model] three times:
   $o(A,B) = |\{b\}|/\min(2,2) = 0.5$ (the backbone's pinned case),
   $o(B,C) = |\{c\}|/\min(2,3) = 0.5$, and
   $o(A,C) = 0.0$.
3. **Verify against the textbook backbone.** In a Python session:

   ```python
   from textbook.models import metrological_overlap

   metrological_overlap({"a", "b"}, {"b", "c"})      # expect 0.5  (pinned)
   metrological_overlap({"b", "c"}, {"c", "d", "e"}) # expect 0.5
   metrological_overlap({"a", "b"}, {"c", "d", "e"}) # expect 0.0
   ```

   Confirm the function agrees with your hand values exactly.
4. **Walk the octave ladder, both conventions.** By [@eq:part_II_metrological-overlap_octaves]
   with $\Omega_0 = 1$: the exponent convention gives
   $\Omega_5 = \Phi^5 \approx 11.090170$ and the subscript convention gives
   $\Omega_5 = 8/5 = 1.6$; at $n = 10$ they give $\Phi^{10}\Omega_0$ versus
   $\varphi_{\mathrm{fib}}(10) = 89/55 \approx 1.618182$. Compute the
   exponent value with `octave_term(1.0, 5, convention="exponent")` and check
   the subscript values against the pinned Fibonacci ratios.

## Analysis

Summarise your results in a table mirroring
[@tbl:part_II_metrological-overlap_worked] of the chapter, with one column per
route (hand, `textbook.models`, reference solver where it prints comparable
overlaps). All routes must agree where they overlap; if they do not, suspect
your hand arithmetic first and the calibration second. Then extend the matrix:
add the chapter's register pair $R_{\mathrm{HI}} = \{\nu_{\mathrm{HI}},
\lambda_{\mathrm{HI}}, \Delta E_n\}$ versus $R_c = \{c, \lambda_{\mathrm{HI}}\}$
(hand expectation $0.5$) and the richer pair with $\Delta E_n$ added to
$R_c$ (hand expectation $2/3 \approx 0.666667$), and sketch the $3\times 3$
overlap heat cells for $\{R_{\mathrm{HI}}, R_c, R_p\}$ with
$R_p = \{p_n, p_{n+1}\}$. Finish with
`textbook.models.descriptive_statistics` over your computed overlap values and
note that the mean is pulled upward by the diagonal's $1.0$s — a reminder that
an overlap matrix is dominated by self-overlap unless you mask it.

## Computational Workflow

```python
from textbook.models import metrological_overlap, octave_term, descriptive_statistics

# Steps 2-3: hand-checked overlaps (pinned case first)
print(metrological_overlap({"a", "b"}, {"b", "c"}))       # 0.5
print(metrological_overlap({"b", "c"}, {"c", "d", "e"}))  # 0.5
print(metrological_overlap({"a", "b"}, {"c", "d", "e"}))  # 0.0

# Chapter registers: hydrogen clock vs light's brake
HI  = {"nu_HI", "lambda_HI", "dE_n"}
C   = {"c", "lambda_HI"}
Cp  = {"c", "lambda_HI", "dE_n"}
print(metrological_overlap(HI, C))    # 0.5
print(metrological_overlap(HI, Cp))   # 0.666666...

# Step 4: the octave ladder, both conventions, Omega_0 = 1
print(octave_term(1.0, 5, convention="exponent"))   # 11.090170  (Phi^5)
print(octave_term(1.0, 5, convention="subscript"))  # 1.6        (8/5)
print(octave_term(1.0, 10, convention="subscript")) # 1.618182   (89/55)

# Analysis: summarise the overlap values (diagonal included)
vals = [metrological_overlap(x, y) for x in (HI, C, HI) for y in (HI, C, HI)]
print(descriptive_statistics(vals))
```

## Reflection

1. The paper's honesty block disclaims "Standard Model retirement" and any
   claim that the $m_{\mathrm{catalog}}$ sum equals the electron or proton mass
   [@mendez2026metrologicalOverlap]. After running the solver yourself, which
   specific outputs could a careless reader over-interpret physically — and how
   does the Fair Exchange clause pre-empt that reading?
2. The overlap is min-normalised: a two-entry register fully contained in a
   ten-entry register scores $1.0$, while sharing nine of ten entries the other
   way scores $0.9$. In catalog terms, what does the smaller register's
   dominance mean for how the corpus's agents should route a query between two
   shelves?
3. The solver's four outputs ($\lambda_{\mathrm{HI}}$, $\Delta E_n$, action
   wells, $m_{\mathrm{catalog}}$) are filed at very different levels — a
   wavelength, a ladder spacing, a minimum, a ledger total. Write two sentences
   on why filing them in *one* solver is a catalog-architecture move rather
   than a physics claim, citing the paper's scope block.
