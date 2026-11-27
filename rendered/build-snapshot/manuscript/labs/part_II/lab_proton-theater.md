# Lab — Proton Space, Electron Theater, and Φ Duality {#sec:lab_part_II_proton-theater}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: (1) file a decimal constant through the
digit-filing map of [@eq:part_II_proton-theater_filing] by inspecting its
leading and structural digits; (2) compute the Φ-duality pair
$(x\Phi,\; x/\Phi)$ of [@eq:part_II_proton-theater_duality] by hand for
several values; (3) verify the mirror identities of
[@eq:part_II_proton-theater_mirror] against the tested
`textbook.models.phi_dual`; and (4) run the paper's reference suite and
interpret its reported 9/9 suite locks [@mendez2026protonTheater].

## Background

Linked chapter: [@sec:part_II_proton-theater]. The chapter's filing map routes
constants with leading digit 1 into [**Proton Space**](#gl:proton-space) and
constants with structural digit 2 into
[**Electron Theater**](#gl:electron-theater), all under the filing constant
$\Phi \approx 1.618$ [@mendez2026protonTheater]. The book's quantitative
backbone for the duality is the mirror pair $\Phi_{+}(x) = x\Phi$,
$\Phi_{-}(x) = x/\Phi$, whose product identity
$\Phi_{+}(x)\Phi_{-}(x) = x^{2}$, ratio identity
$\Phi_{+}(x)/\Phi_{-}(x) = \Phi^{2}$, and involution
$\Phi_{-}(\Phi_{+}(x)) = x$ are stated in [@eq:part_II_proton-theater_mirror]
and plotted in [@fig:part_II_proton-theater]. In this lab you check every one
of those claims with your own hands first, and with the tested function
second — the catalog's [**honesty-first**](#gl:honesty-first) discipline
applied to arithmetic.

## Procedure

1. **File two constants.** Take $e = 2.718\ldots$ and $\pi = 3.141\ldots$.
   The Proton Space trigger fires on leading digit 1 — neither constant has
   it. The Electron Theater trigger fires on *structural* 2, which the
   corpus identifies with the sole-even prime and $2\pi$ — not on "any value
   whose leading digit happens to be 2". We read the map as: $e$ (leading
   digit 2) does not file on the structural trigger, and $\pi$ files in
   neither drawer. Then confirm the positive cases: $\Phi = 1.618\ldots$
   (leading digit 1 → Proton Space) and $2\pi$ (the structural-2 symbol
   itself → Electron Theater). Write down, for each of the four constants,
   which drawer it enters or why it enters none — and mark which judgements
   are the corpus's and which are your interpretive read.
2. **Compute duality pairs by hand.** For $x = 1, 2, 3$, compute
   $\Phi_{+}(x) = x\Phi$ and $\Phi_{-}(x) = x/\Phi$ using $\Phi = 1.618034$
   and $1/\Phi = 0.618034$. You should get:
   - $x = 1$: $(1.618034,\; 0.618034)$
   - $x = 2$: $(3.236068,\; 1.236068)$
   - $x = 3$: $(4.854102,\; 1.854102)$
3. **Verify the mirror identities.** For each $x$: check the product
   $\Phi_{+}(x)\,\Phi_{-}(x) = x^{2}$ (for $x = 3$: $4.854102 \times
   1.854102 = 9.000\ldots$); check the ratio
   $\Phi_{+}(x)/\Phi_{-}(x) = \Phi^{2} = 2.618034$; and check the involution
   $\Phi_{-}(\Phi_{+}(x)) = x$ by dividing your upper filing by $\Phi$.
4. **Verify the step identity.** Confirm that $\Phi_{-}(x) = \Phi_{+}(x) - x$
   ([@eq:part_II_proton-theater_step]) holds for all three values — for
   $x = 3$: $4.854102 - 3 = 1.854102$. ✓
5. **Run the reference implementation.** From the paper's standalone wiring
   (`FractiAI/synthobs-proton-space-electron-theater`), re-run the filing
   suite with `npm run research:synthobs-proton-space-electron-theater` and
   record the suite result — the paper reports **9/9 suite locks**
   [@mendez2026protonTheater]. State what a "lock" checks: that the digit
   filing routes as the paper claims, not that any physical constant is
   derived.

## Analysis

Summarise your three hand-computed pairs in a table with columns
$x$, $\Phi_{+}(x)$, $\Phi_{-}(x)$, $\Phi_{+}\Phi_{-}$, and
$\Phi_{-}(\Phi_{+}(x))$, then compute the mean and spread of the ratio
$\Phi_{+}(x)/\Phi_{-}(x)$ across the three rows with
`textbook.models.descriptive_statistics`. The ratio column should be constant
at $\Phi^{2} \approx 2.618034$ to display precision — a *constant ratio* is
exactly what makes the two branches of [@fig:part_II_proton-theater] straight
lines on a log axis, offset by $\pm\ln\Phi \approx \pm 0.481212$ about the
identity. If any row deviates, re-derive it before touching the code: the
tested function is never wrong about arithmetic, only your transcriptions
can be.

## Computational Workflow

```python
from textbook.models import phi_dual, PHI

PHI  # 1.618033988749895

# Step 2-3: hand values vs tested function
for x in (1, 2, 3):
    upper, lower = phi_dual(x)
    print(x, upper, lower,
          upper * lower,        # expect x**2
          upper / lower,        # expect PHI**2 ≈ 2.618034
          phi_dual(upper)[1])   # expect x — involution closes

# Step 4: step identity Phi_-(x) = Phi_+(x) - x
upper, lower = phi_dual(3)
print(upper - 3 == lower)      # True
```

Predict before running: the printed products should be $1, 4, 9$, the ratios
all $2.618034$, and the involutions $1, 2, 3$.

## Reflection

1. The duality pair is an involution — filing the upper image back down
   returns the original value. Why is information preservation a sensible
   design requirement for a catalog that advertises
   [**honesty-first**](#gl:honesty-first) bookkeeping?
2. The paper disclaims any CODATA/SI derivation from $\Phi$, any ħ
   leading-digit causation, any QED dyad proof, and any zero-crosstalk quantum
   hardware [@mendez2026protonTheater]. Which of your lab activities touched
   physics, and which only touched filing?
3. You found constants ($e$, $\pi$) that enter no drawer. What does the
   existence of unfiled values tell you about the coverage claim of a
   two-drawer map — and where in the corpus might digit 3 and beyond be
   filed? (Hint: the prime-parity companion [@mendez2026primeParity] and
   [@sec:part_I_prime-parity].)
