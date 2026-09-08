# Lab — Moving Up the Stack: Lattice as the Next AI Layer {#sec:lab_part_III_moving-up-stack}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`), Node.js for the reference suite

## Objectives

After this lab you will be able to: (1) run the paper's standalone valuation suite and locate its scenario anchors in its output; (2) recompute the new-layer band statistics by hand and verify them with `textbook.models.descriptive_statistics`; (3) test shelf-membership of the anchors with `textbook.models.goldilocks_band`; and (4) articulate, in your own words, which outputs are framing and which would have to be measurements.

## Background

Linked chapter: [@sec:part_III_moving-up-stack]. The chapter formalised the paper's valuation thesis as a band $\mathcal{B}_{\text{new}} = [\$12\text{B}, \$28\text{B}]$ derived from two scenario anchors, $A_{\text{hub}} = \$12.9\text{B}$ and $A_{\text{IDE}} = \$60.0\text{B}$ ([@eq:part_III_moving-up-stack_band]), and rejected the peer-shelf misread band $[\$4.2\text{B}, \$7.5\text{B}]$. The paper's reference implementation packages exactly this derivation: it is the Infinite Octaves engine shelf #13 suite at `github.com/FractiAI/synthobs-moving-up-the-stack-valuation` [@mendez2026stack]. Here you run it, then reproduce its arithmetic yourself so that the band is something you computed, not something you believed.

Throughout, keep the paper's own scope label in view: the numbers are **scenario anchors** for the climb — "valuation *framing*, not an audited appraisal or securities offer" [@mendez2026stack]. The skill this lab practises is reproducing a derivation *while* honouring its disclaimers.

## Procedure

2. **Recompute the band statistics by hand.** From the anchors only: floor ratio $12/12.9 \approx 0.930$; ceiling ratio $28/60 \approx 0.467$; peer midpoint $(4.2+7.5)/2 = 5.85$; new-layer midpoint $(12+28)/2 = 20.0$; midpoint ratio $20.0/5.85 \approx 3.42$. Write each number down *before* checking it — the point is that every quantity in the paper's derivation is reachable from the two anchors plus the printed band edges.
3. **Verify with the model library.** Feed the two band midpoints (and the four band edges) through `textbook.models.descriptive_statistics` and confirm your hand values: the midpoint set $\{5.85,\ 20.0\}$ and the edge set $\{4.2, 7.5, 12, 28\}$ both have mean $12.925$. This equality is not a coincidence but an algebraic identity — the mean of two intervals' midpoints always equals the mean of their four endpoints — and precisely because it is forced by arithmetic it carries *no* evidential weight about which band is correct. Say so explicitly in your notes: identities are not evidence.
4. **Test shelf membership.** Use `textbook.models.goldilocks_band` to check which of the values $\{4.2, 7.5, 12, 28, 60\}$ (in $B) fall inside the interval $[V_{\min}, V_{\max}] = [12, 28]$ and which fall inside the "climb corridor" $[A_{\text{hub}}, A_{\text{IDE}}] = [12.9, 60]$. Expected: only $12$ and $28$ sit in the band (the band's own edges); only $28$ and $60$ sit strictly inside the corridor, with $12$ just *below* the corridor floor — the band floor is "near" hub gravity, not at it.
5. **Sketch the token accounting.** From [@eq:part_III_moving-up-stack_cooling], pick your own $m$, $T_{\text{loop}}$, $B$, and $s+p$ (the chapter's worked example uses $m=10$, $40{,}000$, $5{,}000$, $2{,}500$) and compute $\kappa$. Confirm $\kappa > 1$ for any $T_{\text{loop}} > B/m + (s+p)$; identify the break-even fleet size.

## Analysis

Summarise your results in a three-row table: quantity, hand value, library value. Then answer, in writing: (a) which of your numbers are *derived from the corpus's printed values*, and which are *illustrative choices of yours* (the token accounting is the latter); (b) what the paper would need to publish for the band to become an appraisal rather than framing (audited transaction data, at minimum); (c) why the sunspot count 90.9 and the node label Hero Jo appear in the paper's filing but in *none* of your computations — they are filing / ops labels, "not causal dollar drivers" [@mendez2026stack].

## Computational Workflow

```python
from textbook.models import descriptive_statistics, goldilocks_band, net_zero_balance

# Step 3 — band statistics (values in $B)
band_edges = [4.2, 7.5, 12.0, 28.0]          # peer band then new-layer band
midpoints  = [(4.2 + 7.5) / 2, (12.0 + 28.0) / 2]   # 5.85, 20.0
print(descriptive_statistics(midpoints))     # mean = 12.925
print(descriptive_statistics(band_edges))    # mean = 12.925

# Step 4 — shelf membership
print(goldilocks_band([4.2, 7.5, 12.0, 28.0, 60.0], lo=12.0, hi=28.0))
# -> only 12.0 and 28.0 fall inside the new-layer band

# Fair-exchange bookkeeping analogue: acknowledged vs delivered value
# net_zero_balance(inflows, outflows) -> residual; nonzero residual is
# exactly what the paper's Fair Exchange Clause says may be refunded.
print(net_zero_balance([20.0], [20.0]))      # residual 0.0
```

Run the same checks against the suite's own output from step 1; where a number differs, re-derive by hand before suspecting either source.

## Reflection

1. The paper corrected *itself* from $4.2B–$7.5B to $12B–$28B. What kind of error was that — arithmetic, scope, or shelving — and what does the correction teach about reading valuations of platform-layer products?
2. Your $\kappa$ value in step 5 is illustrative. What measurement would turn it from an illustration into a test of the paper's "cool token burn" claim?
3. The band floor ($12B) sits *below* the hub anchor ($12.9B) and the ceiling ($28B) far below the IDE anchor ($60B). Argue whether a band that overlaps neither anchor's exact value can still be "anchored" by them — and what "floor near hub-layer gravity" must therefore mean.
