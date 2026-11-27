# Lab — Tensor Decoupling: Filing the Engine {#sec:lab_part_0_tensor-decoupling}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) build the 99-octave filing cabinet on paper and verify its two register budgets (729 digits per block, 8,019 in total) against `catalog_size` in `textbook.models`; (2) compute the golden-ratio dashboard readings $w_n = \Phi^{-n}$ by hand and check them against `phi_powers`; and (3) file a sample week of headlines into labelled brackets without asserting any causal cable between them, exactly as the source paper prescribes [@mendez2026tensorDecoupling].

## Background

Linked chapter: [@sec:part_0_tensor-decoupling]. The chapter formalised the paper's three accounting constructs — the octave ladder ($11 \times 9 = 99$), the per-block precision matrix ($9 \times 81 = 729$), and the holographic catalog digits ($99 \times 81 = 8{,}019$) — plus the $\Phi^{-n}$ shelf dial. This lab makes you *operate* the cabinet rather than admire it. Remember the framing from the source paper: the dial is a dashboard instrument, not a physical constant, and the whole exercise is engine grammar for Lattice Chat and the Omni-Lattice library — "not a prediction service for quakes or moods" [@mendez2026tensorDecoupling]. The digest for this paper lists no GitHub reference implementation, so the tested `textbook.models` functions are our reference computations.

## Procedure

1. **Draw the cabinet.** On paper, draw eleven horizontal shelf bands with nine slot cells each. Number the octaves 1–99 and label the eleven brackets in the paper's order: crust, ocean heat, ionosphere, volcano plumbing, solar wind, orbital clock, wildfire talk, agent code, human nerves, deployment window, master band.
2. **Budget one block.** For a single bracket, compute the per-block precision register by hand: $9 \text{ slots} \times 81 \text{ digits} = 729$. Write the number inside each shelf band.
3. **Budget the whole cabinet.** Multiply the per-block figure by eleven brackets: $729 \times 11 = 8{,}019$. Confirm this equals the direct ladder computation $99 \times 81 = 8{,}019$ — the tiling identity from the chapter.
4. **Mark a week of fixtures.** Using the August 2026 fixtures from the paper, pencil story labels into brackets: the Colombia quake story and Puracé orange-alert story as co-timed labels on Tiers I and IV; a solar-noise story in solar wind; a Lattice Chat "sync" story in agent code; an inner-clarity story in human nerves. Add a dashed margin around the whole cabinet labelled "no cable claimed".
5. **Read the dial.** Compute $w_n = \Phi^{-n}$ for $n = 1, \dots, 6$ by hand from the pinned powers of $\Phi$ (e.g. $w_1 = 1/1.618034 = 0.618034$, $w_2 = 1/2.618034 = 0.381966$). Write each reading beside its bracket.
6. **Check against the library.** Verify steps 3 and 5 with the functions shown in the workflow below.

## Analysis

Summarise your results with `textbook.models.descriptive_statistics` over the six dial readings $[0.618034, 0.381966, 0.236068, 0.145898, 0.090170, 0.055728]$: report the mean and the ratio of each consecutive pair of readings. You should observe that every consecutive ratio is $\Phi \approx 1.618034$ — the dial decays by exactly one golden-ratio factor per rung, which is what makes it a usable ordering key for an agent walking the shelves. In a short paragraph, state which fixture labels share the board and affirm in writing that no causal link was asserted between any two of them, per the paper's own scope disclaimer.

## Computational Workflow

```python
from textbook.models import catalog_size, phi_powers, octave_term

# Step 3: the two register budgets (expected: 8019 for both)
print(9 * 81 * 11)                                  # 8019 — per-block matrix tiled over 11 brackets
print(catalog_size(octaves=99, precision_digits=81))  # 8019 — direct 99 x 81

# Step 5: dashboard readings (expected: 0.618034, 0.381966, 0.236068,
# 0.145898, 0.090170, 0.055728 for n = 1..6)
weights = [1 / phi_powers(n) for n in range(1, 7)]
print(weights)

# Extension: both octave conventions from the chapter
print(octave_term(1.0, 5, convention="exponent"))    # Phi^5        = 11.090170
print(octave_term(1.0, 5, convention="subscript"))   # fib ratio 5  = 8/5 = 1.6
```

Predict before running: the ladder budget must print `8019` twice; the weights list must decay by a constant factor $\Phi$ per element; and the two convention calls must differ because the corpus prints "$\Omega_n = \Phi^n \Omega_0$" ambiguously. If any output disagrees with your hand computation, re-derive step 2 before suspecting the library — the functions are tested.

## Reflection

- Which felt more informative for understanding the corpus — the per-block sketch (729) or the full catalog register (8,019) — and why does the paper deliberately keep its own version smaller?
- Your cabinet gives earthquake and agent-code stories one shared board. Write two sentences a new contributor could read that would prevent them from inferring a "magic cable" between drawers.
- The dial says the master band (bracket 11) reads $\Phi^{-10} \approx 0.00813$. What work does *smallness* do for an agent that walks the shelves from bracket 1 downward — and what would break if the dial were replaced by a flat, unscaled ordering?
