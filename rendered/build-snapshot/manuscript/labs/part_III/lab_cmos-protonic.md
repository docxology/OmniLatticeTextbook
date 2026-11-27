# Lab — CMOS/Protonic: The Silicon Shelf {#sec:lab_part_III_cmos-protonic}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) place a device class on the
silicon-shelf tier map from the chapter, (2) compute the first six rungs of the
octave ladder under both the exponent and subscript conventions with
`textbook.models.octave_term`, and (3) compute state capacities for two-state
and multi-state devices by hand and check them numerically — all while keeping
the source paper's honesty-first boundary visible: we are doing catalogue
arithmetic, not device measurement [@mendez2026cmosProtonic].

## Background

Linked chapter: [@sec:part_III_cmos-protonic]. The chapter's tier map
([@eq:part_III_cmos-protonic_shelf-map]) files a two-state CMOS gate at octave
tier $n = 1$ and hydrogen-regulated protonic two-terminal devices on bands
$n = 2 \ldots 99$. The tiers index the Φ ladder of
[@eq:part_III_cmos-protonic_ladder], and the capacity reading of
[@eq:part_III_cmos-protonic_capacity] turns "multi-state weights instead of
only hard snaps" into a number: $C = \log_2 m$ bits per device. This lab runs
that arithmetic — and, just as importantly, marks where the arithmetic *stops*
being licensed, because the source note is a vocabulary bridge, not a measured
power-win table [@mendez2026cmosProtonic].

## Procedure

1. **Hand-compute the ladder rungs.** With $\Omega_0 = 1$, compute
   $\Phi^n$ for $n = 1, 2, 3$ by hand using $\Phi = 1.6180339887$ and the
   identity $\Phi^{n+1} = \Phi^n + \Phi^{n-1}$. You should get
   $\Phi^1 = 1.618034$, $\Phi^2 = \Phi + 1 = 2.618034$,
   $\Phi^3 = \Phi^2 + \Phi = 4.236068$. Note the shortcut: multiply by Φ or
   add the previous two rungs — both give the same rung.
2. **Check against the model.** In Python, verify with `phi_powers` and both
   `octave_term` conventions:

   ```python
   from textbook.models import octave_term, phi_powers

   [round(p, 6) for p in phi_powers(6)]
   # → [1.618034, 2.618034, 4.236068, 6.854102, 11.09017, 17.944272]

   [octave_term(1.0, n, "exponent") for n in range(1, 7)]
   # → same six values: Ω_n = Φ^n · Ω_0

   [octave_term(1.0, n, "subscript") for n in range(1, 7)]
   # → Fibonacci-ratio rungs: 1.0, 2.0, 1.5, 1.666..., 1.6, 1.625, ...
   #   (φ_fib(n) = F(n+1)/F(n); e.g. φ_fib(5) = 8/5 = 1.6,
   #    φ_fib(10) = 89/55 ≈ 1.618182)
   ```

3. **Compute capacities by hand.** Using $C = \log_2 m$: a binary gate
   ($m = 2$) → $C = 1$ bit; a four-level protonic device → $C = 2$ bits; a
   sixteen-level protonic device → $C = 4$ bits. Write down, for each row, the
   tier or band the chapter's shelf map assigns.
4. **File the devices.** Build a two-row filing table — device class vs.
   $S(d)$, $m$, $C$ — for the binary CMOS gate and a protonic device with
   $m = 16$. This table is your deliverable (below).
5. **Mark the boundary.** Next to your table, write the honesty clause each
   row must carry: the note files device classes; it does *not* measure how
   many states any band delivers, and protonic devices are "still physics-class
   devices" [@mendez2026cmosProtonic].

## Analysis

Compare the two conventions from step 2. The exponent convention grows without
bound ($\Phi^{99}$ is astronomically large), while the Fibonacci-ratio
subscript convention converges toward Φ itself. The corpus prints
"Ωn = Φn·Ω0", which is ambiguous between the two; the chapter and
[@sec:part_0_octave-map] keep both readings alive. State in one sentence which
convention your filing table assumes and why the choice does not affect the
*tier assignment* (the map $S$ uses the integer index $n$, not the rung value
$\Omega_n$). Summarise your capacity column with
`textbook.models.descriptive_statistics` if you extended it to more values of
$m$ — the spread between $C = 1$ bit and $C = 4$ bits is the quantitative
shadow of "multi-state weights instead of only hard snaps."

## Computational Workflow

```python
from textbook.models import octave_term, phi_powers

# 1. Ladder rungs for the silicon shelf's first six tiers (exponent conv.)
rungs = [octave_term(1.0, n, "exponent") for n in range(1, 7)]
assert [round(r, 6) for r in rungs] == [
    1.618034, 2.618034, 4.236068, 6.854102, 11.09017, 17.944272]

# 2. Capacity column C = log2(m) for a chosen resolution ladder
import math
capacity = {m: math.log2(m) for m in (2, 4, 16)}
# → {2: 1.0, 4: 2.0, 16: 4.0}

# 3. Filing: shelf map S(d) by device class (from the chapter, not computed)
shelf = {"binary CMOS gate": 1, "protonic (m = 16)": "2…99"}

# TODO(extension): add a protonic m = 256 row; what is C, and which band?
```

## Deliverable

A two-row filing table (device class, $S(d)$, $m$, $C$, honesty clause) plus
your hand-derived values for $\Phi^1, \Phi^2, \Phi^3$ and the three capacity
values, each checked against the `textbook.models` outputs shown above.

## Reflection

1. The chapter calls tier 1 *degenerate* in the sense of *simplest resolution*.
   After computing $C = 1$ bit for the binary gate, does "simplest" feel like a
   criticism or a description — and what would be lost by reading it as
   criticism?
2. Your capacity numbers came from *your* choice of $m$. Which parts of this
   lab are corpus-licensed (the tier map, the ladder, the quoted phrases) and
   which are standard-information-theory readings you supplied?
3. If a foundry evaluator asked "where is the chip?", what — precisely, per the
   source note — would you have to say the bridge is and is not?
