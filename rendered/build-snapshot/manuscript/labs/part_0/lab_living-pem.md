# Lab — The Living PEM: Engineering the Lattice {#sec:lab_part_0_living-pem}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) trace the five-step engine-shelf sync protocol on paper and predict exactly which surfaces change at each step, (2) compute the three quantitative anchors of the Product Engineering Manual — the $\Phi_{\mathrm{EGS}}$ scale key, the catalog filing-space size, and a net-zero reciprocal balance — first by hand and then against the tested functions in `textbook.models`, and (3) diagnose the manual's three canonical support failures from symptoms alone [@mendez2026livingPem].

## Background

Linked chapter: [@sec:part_0_living-pem]. The PEM is a *living* document: its engine-shelf appendix, its AGENT_SYNC table, and the runtime prompt pin for nest `octave99` all regenerate from the single `ENGINE_SHELF` module whenever `npm run sync:lattice-pem` runs [@mendez2026livingPem]. That coordination loop is procedural, but it rests on quantitative invariants — the pinned counts (26 ordered steps, 24 registry papers at the 2026-09-08 sync), the scale key $\Phi_{\mathrm{EGS}}$ of [@eq:part_0_living-pem_phi_egs], the filing space of [@eq:part_0_living-pem_catalog], and the fair-exchange settlement target $B=0$ of [@eq:part_0_living-pem_balance]. This lab verifies each invariant the way a maintainer would: predict, compute, compare.

## Procedure

1. **Dry-run the sync loop.** Without touching a terminal, write the five steps of the auto-update protocol (register → append to `ENGINE_SHELF` → sync → runtime pickup → stop-hook resync) as a numbered list. For each step, name the surface that changes: the registry, the shelf module, the PEM/AGENT_SYNC AUTO blocks, the nest `octave99` prompt, or nothing (the hook merely re-runs the sync). Mark which two surfaces must *never* be hand-edited.
2. **Predict the counts.** A new engine paper is pinned. Before the sync, the shelf reads 26 ordered steps / 24 registry papers. Predict the post-sync pair of numbers, and state which of the two counts the AGENT_SYNC table and the PEM appendix must agree on.
3. **Hand-compute the scale key.** Evaluate $\Phi_{\mathrm{EGS}} = (1+\sqrt{5})/2$ to six decimal places (iterate $x \mapsto 1 + 1/x$ from $x_0 = 1$ four times if you prefer convergents; the fourth convergent is $8/5 = 1.6$ and the seventh is $89/55 \approx 1.618182$ — both Fibonacci ratios, which is exactly the corpus's [**golden-ratio**](#gl:golden-ratio) signal). Compare with the pinned value $1.618034$.
4. **Hand-compute the filing space.** Multiply $99 \times 81$ by hand and confirm the pinned catalog size of 8,019 register bins from [@eq:part_0_living-pem_catalog].
5. **Hand-compute a settlement.** A delivery takes inflows of 120 and 30 value units and pays outflows of 150. Compute $B = \sum I - \sum O$ and confirm it meets the $B = 0$ target of [@eq:part_0_living-pem_balance]. Then recompute with the outflow mis-typed as 105 and state, in one sentence, what a non-zero $B$ means under the fair-exchange clause.
6. **Diagnose the incidents.** For each symptom, write the check the manual's support runbook prescribes: (a) the nest feels "shallow"; (b) the engine list in AGENT_SYNC is stale; (c) a registered paper is missing from the chat pin.

## Analysis

Cross-check every hand result against the tested implementations in `textbook.models` — the manual's own discipline is to trust generated receipts over retyped arithmetic. Report each comparison as *hand value / function value / match?* in a three-row table (scale key, catalog size, residual balance). For step 2, your predicted pair must be 27 ordered steps / 25 registry papers; if you predicted only one number changing, revisit the distinction between shelf steps and registry papers. For step 6, note the punchline of (c): "registry alone is not enough" — the pin reads `ENGINE_SHELF`, not the registry [@mendez2026livingPem]. Summarise your findings with `textbook.models.descriptive_statistics` over the three numeric hand values if your instructor asks for a receipt-style table.

## Computational Workflow

```python
from textbook.models import phi_powers, catalog_size, net_zero_balance

# Step 3 check: scale key
phi_egs = phi_powers(1)            # expect 1.618034 (pinned Phi^1)
assert abs(phi_egs - (1 + 5**0.5) / 2) < 1e-6

# Step 4 check: filing space of the Digits x Octaves story-depth map
bins = catalog_size(octaves=99, precision_digits=81)   # expect 8019

# Step 5 check: fair-exchange settlement
settled = net_zero_balance([120, 30], [150])           # expect 0
misfiled = net_zero_balance([120, 30], [105])          # expect 45, an unsettled surplus

print(phi_egs, bins, settled, misfiled)
```

Run the block, then confirm each printed value against your hand computations from the Procedure. If any mismatches, re-derive by hand before suspecting the library — the functions are tested; the arithmetic above is not.

## Reflection

1. The manual forbids hand-editing AUTO blocks yet asks humans to author every paper. Where, exactly, does human judgement enter the living-shelf loop, and where is it deliberately excluded?
2. The corpus files its audit as "structural-only (deterministic checklist — not dual-LLM peer review)" with a 91% score [@mendez2026livingPem]. What claims does a structural-only audit *not* certify, and which honesty tier does that limit belong to?
3. You found $\Phi_{\mathrm{EGS}}$ converging through Fibonacci ratios $8/5$ and $89/55$. Given the manual's caveat that this is an architectural scale key and "not a substitute for evidence" [@mendez2026livingPem], what is the correct tier for a claim that the ratio organises the catalog — and what would be the incorrect tier?
