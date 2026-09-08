# Lab — The Macro-Protein Work Engine {#sec:lab_part_III_macro-protein}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`), Node.js for the reference suite

## Objectives

After this lab you will be able to: (1) evaluate the octave term $\Omega_n$
across the biological band $\theta_{\mathrm{bio}} \in [13, 17]$ under both
printed conventions and read them off the output curve of
[@fig:part_III_macro-protein]; (2) apply the band predicate of
[@eq:part_III_macro-protein_band] to candidate tier values; (3) compute a
Kleiber-style $3/4$-power metabolic ratio by hand and state exactly what kind
of claim the source note makes about that law
[@mendez2026macroProtein]; and (4) run the paper's reference suite, predict
its outcome, and articulate what a suite lock does and does not evidence.

## Background

Linked chapter: [@sec:part_III_macro-protein]. There we formalised the filing
of [@mendez2026macroProtein]: organisms as
[**macro-protein**](#gl:macro-protein) work engines, metabolic work labeled
$W(n) = w_0 \cdot \Omega_n$ per [@eq:part_III_macro-protein_model], the
organism placed on the Infinite Octave ladder at band $[13, 17]$ per
[@eq:part_III_macro-protein_band], and **Kleiber $\approx 3/4$ · WBE** cited
as *compatible published-scaling locks* — framing only, explicitly not
re-derived. This lab makes the filing do work: you will *walk the band*,
*predicate membership in it*, and *stress the boundary between a filing
label, published allometry, and a software test*. Everything here is
[**catalog-architecture**](#gl:catalog-architecture) practice — the note
itself disclaims "life is 'solved,'" organism-is-one-protein, and any
laboratory Kleiber re-derivation — so keep the
[**honesty-first**](#gl:honesty-first) framing throughout: you are exercising
an octave-indexed filing, not measuring metabolism.

## Procedure

1. **Walk the band by hand.** With $\Omega_0 = 1$, compute $\Omega_n$ for
   $n = 13$ and $n = 17$ under the exponent convention ($\Omega_n = \Phi^n
   \cdot \Omega_0$; from the standard arithmetic of
   $\Phi = (1+\sqrt5)/2$, expect $\approx 521.002$ and $\approx 3571.000$).
   Then under the subscript convention ($\Omega_n = \varphi_{\mathrm{fib}}(n)
   \cdot \Omega_0$ with $\varphi_{\mathrm{fib}}(n) = F_{n+1}/F_n$): expect
   $377/233 \approx 1.618026$ and $2584/1597 \approx 1.618034$. Write all
   four values down before touching a keyboard; check them in the
   Computational Workflow step.
2. **Predicate the band.** A filing exercise hands you candidate tier values
   $\{12.6,\ 13.9,\ 16.2,\ 17.4\}$. By hand, decide which lie in $[13, 17]$
   (there should be exactly two). Then confirm the membership mask with
   `textbook.models.goldilocks_band` — the interval predicate the chapter
   borrows from the corpus's Goldilocks band filing
   [@mendez2026planetaryCore]. Repeat with a candidate set of your own.
3. **Run the reference suite.** From the corpus repositories, execute:

   ```bash
   npm run research:synthobs-macro-protein-work-engine
   ```

   The source note reports **9/9 suite locks** under
   `research/synthobs-macro-protein-work-engine/` [@mendez2026macroProtein].
   *Predict the outcome before running*: how many locks should pass, and what
   would a failing lock mean here — a biochemical refutation or a software
   regression? The standalone suite lives at
   `github.com/FractiAI/synthobs-macro-protein-work-engine` if you want to
   read what the application companion actually implements.
4. **Kleiber cross-check.** Using [@eq:part_III_macro-protein_kleiber],
   compute the metabolic-rate ratio for a $1000$-fold body-mass increase
   ($1000^{3/4} \approx 177.83$) and for the mouse-to-elephant $2 \times
   10^5$-fold ratio used in the chapter ($\approx 5318$). Then answer in one
   written sentence: which of these numbers is a corpus result, and which is
   published allometry the note merely cites?
5. **Read the output curve.** Open [@fig:part_III_macro-protein] and identify
   both curves. Which convention makes the biology band geometrically
   "high on the ladder," and which makes it nearly flat? Mark on the figure
   where your two surviving band candidates from Step 2 would sit.

## Analysis

Summarise your band walk in a table ($n$, exponent value, subscript value,
convention gap) and note that the gap grows from $\sim 521$-fold at $n = 13$
to $\sim 3571$-fold at $n = 17$: the two printed readings of "$\Omega_n =
\Phi_n \cdot \Omega_0$" diverge multiplicatively with $n$, which is why
`textbook.models.octave_term` exposes the convention as an explicit argument.
Report your band-predicate runs alongside the hand-decided memberships — they
must agree exactly, since the predicate is a plain interval test. Aggregate
your Kleiber ratios with `textbook.models.descriptive_statistics` if you
extended the mass ratios, and observe the sublinearity: each $10^4$-fold mass
increase yields only a $\sim 10^3$-fold metabolic increase under the $3/4$
exponent. Finally, write three sentences placing the whole lab on the note's
own terms: what was exercised (an octave-indexed work filing, a band
predicate, published-scaling arithmetic), and what was not (no metabolic
measurement, no Kleiber derivation, no claim that organisms are literally one
protein — "catalog architecture" [@mendez2026macroProtein]).

## Computational Workflow

```python
from textbook.models import octave_term, goldilocks_band

# Step 1 checks — your hand values should match exactly:
print(octave_term(1, 13, "exponent"))   # → 521.0019193787257
print(octave_term(1, 17, "exponent"))   # → 3571.000280033584
print(octave_term(1, 13, "subscript"))  # → 1.6180257510729614
print(octave_term(1, 17, "subscript"))  # → 1.6180338134001253

# Step 2 check — the band predicate over your candidate tiers:
print(goldilocks_band([12.6, 13.9, 16.2, 17.4], 13, 17))
# → [False, True, True, False]  (exactly your two hand-picked values)
```

Compare every printed value with your hand computation. If any disagree, the
error is in your arithmetic — the functions are the tested reference.

## Reflection

1. The note files $W(n)$ as a work tensor but prints no closed form for it;
   the chapter's $W(n) = w_0 \cdot \Omega_n$ is a *reading* that makes the
   label computable. In two sentences: what does that reading buy, and why
   must it be flagged as interpretation rather than presented as the paper's
   formula?
2. You ran a suite with a predicted 9/9 outcome. What kind of evidence is a
   passing suite about the macro-protein filing — and what kind of evidence
   about living bodies is it not?
3. The note's solar labels AR3664 ("Helios-Prime") and AR3590 ("Borealis")
   are, per the note itself, "story filing characters"
   [@mendez2026macroProtein]. Where else in this lab did a filing metaphor
   (work engine, biology band, vault habit) risk being read as a physical
   claim, and how did you keep the boundary visible?
