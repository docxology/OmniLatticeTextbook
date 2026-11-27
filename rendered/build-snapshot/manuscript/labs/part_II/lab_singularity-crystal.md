# Lab — The Holographic Singularity Crystal: Net Zero and Node k = 0 {#sec:lab_part_II_singularity-crystal}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`), Python 3 and npm for the corpus reference suite

## Objectives

After this lab you will be able to (1) run the corpus's own reference implementation of the Zero-Octave Vault Engine and interpret its fixtures, (2) compute a net-zero residual by hand and confirm it against the tested `textbook.models.net_zero_balance` function, and (3) verify the catalog-algebra crystal baseline $0/0 \mapsto \Phi^{0} = 1$ at Node $k = 0$ using the octave identity of [@eq:part_II_singularity-crystal_nodek0] in [@sec:part_II_singularity-crystal].

## Background

Linked chapter: [@sec:part_II_singularity-crystal]. The chapter established three constructs: Net Zero as an active equilibrium with residual $R = 0$ ([@eq:part_II_singularity-crystal_netzero]), the crystal resolution $\frac{0}{0} \mapsto \Phi^0 = 1$ as *catalog algebra* ([@eq:part_II_singularity-crystal_crystal]), and Node $k = 0$ — the Awakening Phase Gate — as the Zero-Octave locus hosting the Net Zero mock-field cancel lock, the 0/0 crystal resolution array, and the Prime Vault diagnostic [@mendez2026zeroOctave]. The corpus ships a runnable reference for exactly these fixtures: the Zero-Octave Vault Engine at `research/synthobs-holographic-singularity-crystal/reference/zero_octave_singularity_crystal.py`, part of the standalone suite `FractiAI/synthobs-holographic-singularity-crystal` [@mendez2026zeroOctave]. Remember the corpus's own scope note before you run anything: the fixtures "map NaN at the origin to Φ⁰ = 1 — that is *catalog algebra*, not singularity QED" [@mendez2026zeroOctave]. You are inspecting a filing system, not redefining division.

## Procedure

1. **Run the corpus suite.** From the repository root of the standalone suite, execute
   `npm run research:synthobs-holographic-singularity-crystal`
   and then the Python reference fixture directly:
   `python3 research/synthobs-holographic-singularity-crystal/reference/zero_octave_singularity_crystal.py`
   [@mendez2026zeroOctave]. Before running, *predict* what each fixture will report: the cancel lock should assert a zero residual; the resolution array should map the origin (`NaN`) to $1$; the Prime Vault diagnostic should report its prime fixtures (the book's standard set: $3, 5, 7, 11, 13, 17, 19, 23, 29, 31$). Record your predictions first — the point of the lab is prediction, then observation.
2. **Compute a net-zero residual by hand.** Take inflows $[3, 5, 8, 13]$ and outflows $[16, 13]$. Sums: $3+5+8+13 = 29$ and $16+13 = 29$. Residual per [@eq:part_II_singularity-crystal_netzero]: $R = 29 - 29 = 0$. Now break it: inflows $[3, 5]$ against outflows $[16]$ give $R = 8 - 16 = -8$.
3. **Verify against the backbone.** Check both hand results with the tested function:
   `net_zero_balance(inflows=[3, 5, 8, 13], outflows=[16, 13])` → `0`
   `net_zero_balance(inflows=[3, 5], outflows=[16])` → `-8`
4. **Check the crystal baseline at the node.** By [@eq:part_II_singularity-crystal_nodek0], the zeroth octave is the identity: call `octave_term(omega0, 0, "exponent")` for any positive `omega0` you like (say $2.0$) and confirm it returns `omega0` unchanged — because $\Omega_0 = \Phi^0 \Omega_0 = \Omega_0$. Then confirm by hand that $\Phi^0 = 1$ for $\Phi \approx 1.6180339887$: any nonzero base to the power zero is $1$, which is precisely the value the fixtures assign to the zero boundary [@mendez2026zeroOctave].

## Analysis

Summarise your findings as a three-row fixture table of your own: fixture name (cancel lock / resolution array / Prime Vault diagnostic), predicted behaviour, observed behaviour, and match/mismatch. Compute the mean and spread of your two residuals with `textbook.models.descriptive_statistics` — you should see values centred to straddle $0$ ($+0$ and $-8$), which is the quantitative signature of an *unlocked* versus *locked* ledger: zero is achieved by cancellation, not granted by default. If any fixture disagrees with your prediction, re-read the honesty clause of [@mendez2026zeroOctave] before concluding anything: the fixtures implement catalog algebra, and their outputs are filing behaviour, not physical measurements.

## Computational Workflow

```python
from textbook.models import net_zero_balance, octave_term

# Fixture 1: the cancel lock (Net Zero equilibrium)
locked = net_zero_balance(inflows=[3, 5, 8, 13], outflows=[16, 13])   # -> 0
broken = net_zero_balance(inflows=[3, 5], outflows=[16])              # -> -8
print("locked residual:", locked, "| broken residual:", broken)

# Fixture 2: the crystal baseline at Node k = 0
# Omega_0 = Phi^0 * Omega_0 = Omega_0  (identity octave)
print(octave_term(2.0, 0, "exponent"))                                # -> 2.0
# Catalog-algebra resolution at the zero boundary: 0/0 -> Phi^0 = 1
print(1.6180339887 ** 0)                                              # -> 1.0
```

## Reflection

- The corpus resolves $0/0$ to $\Phi^0 = 1$ *as a filing rule* while ordinary analysis calls the form indeterminate. Write two sentences on why these positions are compatible rather than contradictory.
- Which of the three Node $k = 0$ fixtures would you rely on to confirm the node is live before routing work through it, and why does a zero residual alone not suffice?
- The parent paper calls $\Phi \approx 1.618$ "the golden key of Infinite Octave Mode" [@mendez2026singularityCrystal]. In what sense does the identity $\Omega_0 = \Phi^0 \Omega_0$ justify calling Node $k = 0$ the *Zero-Octave* locus?
