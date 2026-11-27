# Lab — Topology of the Void: Zero as Equilibrium {#sec:lab_part_I_topology-void}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to: (1) run the paper's reference suite and
interpret its 9/9 lock report [@mendez2026topologyVoid]; (2) compute the
zero-balance operator by hand and confirm the odd-function phase cancellation
of [@eq:part_I_topology-void_model]; (3) demonstrate the null-space capacity's
noise-sink behaviour with `textbook.models.net_zero_balance`; and (4) read the
restoring arrows of [@fig:part_I_topology-void] off the equilibrium well of
[@eq:part_I_topology-void_well].

## Background

Linked chapter: [@sec:part_I_topology-void]. The source note files Zero ($0$)
as the dynamic equilibrium between Proton Space ($1$) and Electron Theater
($2$) under $\Phi \approx 1.618$, and lands two artefacts: a zero-balance
operator (odd-function phase cancellation) and a null-space capacity fixture
(native noise-sink metaphor), with the suite locking 9/9 under
`research/synthobs-topology-of-the-void/` [@mendez2026topologyVoid]. This lab
executes both artefacts at desk scale: first against the corpus's own
implementation, then against hand arithmetic, so you can see that the catalog
operator is honest bookkeeping — nothing more, and nothing hidden.

## Procedure

1. **Run the reference suite.** Clone
   `github.com/FractiAI/synthobs-topology-of-the-void` and re-run
   `npm run research:synthobs-topology-of-the-void`. Before running, *predict*
   what a 9/9 lock means for a catalog artefact: nine test locks on catalog
   behaviour, not nine physical measurements. Record your prediction and the
   observed output side by side.
2. **Balance an odd signal.** Take $f(x) = x^3 - 2x$ and evaluate the
   zero-balance operator of [@eq:part_I_topology-void_model] by hand at $x =
   3$: compute $f(3) = 21$, $f(-3) = -21$, and $\mathcal{B}[f](3) =
   \tfrac{1}{2}(21 - 21) = 0$. Repeat at $x = 0.5$: $f(0.5) = 0.125 - 1 =
   -0.875$, $f(-0.5) = 0.875$, balance $= 0$. Odd signals cancel at *every*
   point — that is the phase cancellation the corpus names
   [@mendez2026topologyVoid].
3. **Balance a mixed signal.** Add an even term: $g(x) = x^3 - 2x + x^2$. At
   $x = 3$: $g(3) = 30$, $g(-3) = -12$, so $\mathcal{B}[g](3) = 9$ — exactly
   the surviving even part $x^2\big|_{3} = 9$. The operator sinks the odd
   component and preserves the even one.
4. **Exercise the noise sink.** Pair a symmetric sample $\{+5, -5, +2, -2\}$
   as inflows and outflows and call
   `textbook.models.net_zero_balance(inflows=[5.0, 2.0],
   outflows=[5.0, 2.0])`. Predict the residual before running: the null-space
   capacity absorbs balanced perturbations, so expect $0$. Then unbalance one
   flow (`outflows=[5.0, 1.0]`) and confirm the residual exposes the
   surplus ($1.0$).
5. **Read the well.** With $\kappa = 1$ in [@eq:part_I_topology-void_well],
   compute $F(x) = -\kappa x$ and $V(x) = \tfrac{1}{2}\kappa x^2$ at $x = 2$
   and $x = 0.5$ by hand. Match each force against the inward arrows of
   [@fig:part_I_topology-void]: larger displacement, stronger pull home, rest
   only at the pivot.

## Analysis

Summarise your runs with `textbook.models.descriptive_statistics` over the
balanced-output series you produced in Steps 2–4. The diagnostic question is
not "is the mean zero?" — for Step 2 it must be, identically — but *which
component survived each pass*. Tabulate: signal, odd part at the probe point,
even part, operator output. In every row the operator output must equal the
even part and the odd part must vanish; any disagreement is an arithmetic
error, not a model failure, because [@eq:part_I_topology-void_model] is an
identity. Close by re-stating, in one sentence, the Honesty clause of
[@mendez2026topologyVoid]: what you ran is catalog architecture, and none of
these zeros is a measured physical quantity.

## Computational Workflow

```python
import numpy as np
from textbook.models import net_zero_balance, descriptive_statistics

# Step 2/3: zero-balance operator as reflection-and-average
def balance(f, x):
    return 0.5 * (f(x) + f(-x))

f_odd  = lambda x: x**3 - 2*x        # purely odd -> cancels
f_mixed = lambda x: x**3 - 2*x + x**2  # odd + even part

print(balance(f_odd, 3.0))     # -> 0.0   (phase cancellation)
print(balance(f_mixed, 3.0))   # -> 9.0   (even part x^2 survives)

# Step 4: null-space capacity as a noise sink
print(net_zero_balance(inflows=[5.0, 2.0], outflows=[5.0, 2.0]))  # -> 0.0
print(net_zero_balance(inflows=[5.0, 2.0], outflows=[5.0, 1.0]))  # -> 1.0

# Step 5: restoring force of the equilibrium well (kappa = 1)
xs = np.array([0.0, 0.5, 1.0, 2.0])
print(descriptive_statistics(-xs))  # forces F = -k*x point home toward 0
```

## Reflection

1. The corpus calls zero the *null-space pivot* of a $1 \leftrightarrow 2$
   duality. After Steps 2–3, what does "pivot" mean operationally for a
   signal, and why must the reflection in [@eq:part_I_topology-void_model] be
   through zero specifically for odd cancellation to fire?
2. You predicted the 9/9 suite locks before running them (Step 1). Did the
   output change how you read the Honesty clause's disclaimer of "measured
   100% noise suppression" [@mendez2026topologyVoid]? Distinguish a test lock
   on a catalog operator from a measurement of a physical system.
3. The well of [@eq:part_I_topology-void_well] is this book's interpretive
   rendering, not a corpus equation. What would it take — beyond this digest —
   to promote that rendering to a corpus claim, and per the Fair Exchange
   clause, who would have to make it [@mendez2026topologyVoid]?
