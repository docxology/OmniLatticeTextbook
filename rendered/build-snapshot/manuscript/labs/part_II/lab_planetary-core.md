# Lab — Planetary Core and the Goldilocks Bands {#sec:lab_part_II_planetary-core}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: run the planetary-core reference
implementation and observe its 9/9 fixture lock; file two telemetry slots and
verify the $\Delta\varphi = \pi/2$ catalog phase flip of
[@eq:part_II_planetary-core_phase_flip]; and classify a value trace against a
Goldilocks band by hand with [@eq:part_II_planetary-core_band], confirming
every classification with `textbook.models.goldilocks_band`.

## Background

Linked chapter: [@sec:part_II_planetary-core]. The chapter established that
the paper by [@mendez2026planetaryCore] files deep-Earth headlines as a
*filing cabinet*, not as seismology: the outer-core flow reversal and the
inner-core backtracking become the two telemetry slots of a rotor story, the
rotor story carries a 90° catalog phase flip, and "Old Earth → Goldilocks
Earth" is catalog talk for high-friction vs coherent execution labels. This
lab walks the filing end-to-end — first with the paper's own reference
implementation, then with the book's tested model functions — so you can see
that every number produced is a property of the catalog entry, never of the
planet. Keep the honesty-first clause in view throughout: no dataset is
re-hosted, and no holographic timeline switch is claimed as measured physics.

## Procedure

1. **Run the reference implementation.** From the standalone repository
   (`github.com/FractiAI/synthobs-tbme-planetary-core-goldilocks`), run
   `npm run research:synthobs-tbme-planetary-core-goldilocks`. Predict before
   you look: the paper states the run ends in a **9/9 fixture lock**
   [@mendez2026planetaryCore]. Record the fixture names it prints and confirm
   the count is 9/9 — this is the paper's own verification gate, the same
   gate vocabulary the CMB mirror story invokes.
2. **File the two telemetry slots.** In your notebook, draw the rotor circle
   of [@eq:part_II_planetary-core_phase_flip]: pin slot A (outer-core flow
   reversal, a Pacific liquid-iron surge filed as westward → eastward) at
   $\varphi_{\mathrm{A}} = 0$ and slot B (inner-core backtracking, seismic
   travel times filed as a slowdown through zero relative velocity) at
   $\varphi_{\mathrm{B}} = \pi/2$. Compute $\Delta\varphi$ and convert it to
   degrees: $\Delta\varphi = \pi/2\ \text{rad} = 90°$.
3. **Classify a trace by hand.** Take the chapter's trace
   $v = [\,0.12,\; 0.31,\; 0.48,\; 0.62,\; 0.77,\; 0.91\,]$ with band edges
   $\ell = 0.35$, $h = 0.85$. For each value, apply
   [@eq:part_II_planetary-core_band]: write $\chi(v)$ and, for in-band
   values, the margin $m(v) = \min(v - \ell,\; h - v)$. Your hand result
   should be $\chi = [\,0, 0, 1, 1, 1, 0\,]$ with margins
   $m = \{0.13, 0.23, 0.08\}$ for the three in-band points.
4. **Confirm with the tested function.** Check your hand classification
   against the backbone (see the Computational Workflow below). Every
   disagreement means a hand error — the function is the tested reference.
5. **Interpretive check (clearly labelled as reading, not physics).** The
   second slot is described as a slowdown *through zero* relative velocity.
   Evaluate `textbook.models.transduction_brake(t, v0=1, k=1)` at $t = 1$ and
   $t = 2$ and confirm $v(1) \approx 0.367879$ and $v(2) \approx 0.135335$.
   State in one sentence why this exponential-brake reading is an
   interpretive rhyme with [@sec:part_II_eddy-current-mirror], not a claim
   the paper makes about the inner core.

## Analysis

Summarise the trace with `textbook.models.descriptive_statistics`: the mean of
the six values is $0.535$, and the band decision rests entirely on where the
policy edges $\ell$ and $h$ are drawn. Move the edges to $\ell = 0.30$,
$h = 0.95$ and re-classify: $v_2 = 0.31$ and $v_6 = 0.91$ now enter the band,
so $\chi$ becomes $[\,0, 1, 1, 1, 1, 1\,]$. Nothing about the *values* changed
— only the filing policy did. Write two sentences on what this tells you
about "Old Earth → Goldilocks Earth": the flip is a change of execution label
under a chosen band, exactly the catalog talk of
[@mendez2026planetaryCore], and never a claim about the planet.

## Computational Workflow

```python
from textbook.models import (
    goldilocks_band,
    transduction_brake,
    descriptive_statistics,
)

# Step 3-4: hand classification vs tested function
trace = [0.12, 0.31, 0.48, 0.62, 0.77, 0.91]
goldilocks_band(trace, lo=0.35, hi=0.85)
# -> [0, 0, 1, 1, 1, 0]           (matches your hand result)

goldilocks_band(trace, lo=0.30, hi=0.95)
# -> [0, 1, 1, 1, 1, 1]           (policy change, not new data)

# Step 5: interpretive brake reading (ours, not the paper's formalism)
transduction_brake(1.0, v0=1.0, k=1.0)
# -> 0.367879...
transduction_brake(2.0, v0=1.0, k=1.0)
# -> 0.135335...

# Analysis: summarise the trace
descriptive_statistics(trace)
# -> mean 0.535, plus spread measures; policy edges decide the labels
```

## Reflection

1. Which of your five procedure steps produced a number *about the Earth*,
   and which produced a number *about the filing*? (Expect: none of the
   first kind.)
2. The 9/9 fixture lock is a verification gate for the *catalog entry*. What
   would it mean to confuse it with an empirical validation of a geophysics
   claim, and which honesty-first disclaimer rules that out?
3. If you had to file a fresh deep-Earth headline tomorrow, which telemetry
   slot would it join, and what would you need to check before pinning it to
   $\varphi_{\mathrm{A}}$ or $\varphi_{\mathrm{B}}$?
