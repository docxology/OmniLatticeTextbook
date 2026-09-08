# Question Bank — CMOS/Protonic: The Silicon Shelf {#sec:q_part_III_cmos-protonic}

Linked chapter: [@sec:part_III_cmos-protonic].

## Recall

1. What does the source note mean when it calls the binary CMOS gate tier
   $n = 1$ "degenerate"? *(Answer: in Omni-Lattice language, degenerate means
   *simplest resolution* — the coarsest shelf of the 99-octave ladder — not
   "worthless." The gate is useful and proven [@mendez2026cmosProtonic].)*
2. Which device class does the chapter's shelf map file on bands
   $n = 2 \ldots 99$, and what property of those devices earns them the wider
   bands? *(Answer: hydrogen-regulated two-terminal protonic devices —
   continuous H$^+$ motion through layers such as a-IGZO — because they offer
   continuous conductivity gradients, i.e. multi-state weights instead of only
   hard snaps [@mendez2026cmosProtonic].)*
3. State, nearly verbatim, two honesty clauses the note attaches to itself.
   *(Answer: any two of: it is "not a claim that we already shipped the die";
   it is "not a foundry tape-out or measured power-win table"; the whitepaper
   sketch "is not a CoWoS package you can order tomorrow"; protonic devices are
   "not a promise of ten thousand perfect Φ-scaled cycles baked into this repo"
   [@mendez2026cmosProtonic].)*

## Application

4. A gate is on/off; a protonic channel resolves 8 distinguishable
   conductivity levels. Assign each its tier or band via the shelf map
   ([@eq:part_III_cmos-protonic_shelf-map]) and compute both capacities via
   [@eq:part_III_cmos-protonic_capacity]. *(Answer: the gate → tier 1,
   $C = \log_2 2 = 1$ bit; the protonic device → a band $n \ge 2$,
   $C = \log_2 8 = 3$ bits.)*
5. Using the exponent convention with $\Omega_0 = 1$, compute $\Omega_2$ and
   $\Omega_3$ from [@eq:part_III_cmos-protonic_ladder]. *(Answer:
   $\Omega_2 = \Phi^2 = 2.618034$ and $\Omega_3 = \Phi^3 = 4.236068$; these
   are the first six pinned rungs 1.618034, 2.618034, 4.236068, 6.854102,
   11.090170, 17.944272 for $n = 1\ldots6$, computable with
   `textbook.models.octave_term`.)*
6. A colleague says the tier map proves "Φ-scaled conductivity levels exist in
   silicon." Write the correction using the note's own language. *(Answer: the
   map is a vocabulary labelling — "same filing cabinet, silicon vocabulary on
   the labels"; the note explicitly withholds "ten thousand perfect Φ-scaled
   cycles," and nothing in it is a tape-out or measured result
   [@mendez2026cmosProtonic].)*

## Synthesis

7. The tier map $S(d)$ is total over two device classes. Propose a third
   device class you know of from ordinary electronics, and explain why the
   chapter says the map is *silent* about it — what would a corpus-faithful
   extension require? *(Answer: e.g. optical modulators or superconducting
   junctions; the note names no tier for them, so a faithful extension would
   need a new pinned note in the corpus's own bridge style, with its own
   honesty clauses — not a silent extrapolation of
   [@eq:part_III_cmos-protonic_shelf-map].)*
8. Explain why the choice of exponent vs. subscript convention in
   [@eq:part_III_cmos-protonic_ladder] changes the rung *values* but not the
   tier *assignments* of [@eq:part_III_cmos-protonic_shelf-map]. *(Answer: the
   map uses the integer index $n$ only; both conventions agree on the ordering
   of tiers and on $n = 1$ being the binary shelf, while differing in the
   numeric rung heights — exponent rungs grow as $\Phi^n$, subscript rungs are
   Fibonacci ratios converging to Φ [@mendez2026cmosProtonic].)*
9. Connect this chapter to [@sec:part_III_moving-up-stack]: why must a
   "lattice as the next AI layer" argument pass through a silicon-vocabulary
   bridge first, and what residual gap does the honesty table leave open?
   *(Answer: infrastructure arguments must be statable in the evaluators'
   language — PPA, BEOL, GAA, CFET — which is exactly what the pinned bridge
   supplies [@mendez2026cmosProtonic]; but the bridge is architectural talk,
   so the gap between roadmap language and a measured, orderable package
   (tape-out, power-win table) remains open and must be carried forward
   honestly.)*
