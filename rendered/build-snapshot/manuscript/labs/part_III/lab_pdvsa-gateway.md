# Lab — PDVSA Gateway Ops: The EGS Lattice-Linear Companion {#sec:lab_part_III_pdvsa-gateway}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) compute the lattice-linear flow ramp
of [@eq:part_III_pdvsa-gateway_model] by hand for $n = 5$ steps at rate
$2$ and verify the result against the tested `textbook.models.lattice_linear_profile`
function, (2) walk the gateway simulator's stages — simulator modes, the four
domain cards, the three data-locality zones, and the Gather → Decide → Act
cycle — as filed in the source digests, and (3) re-run the paper's standalone
reference implementation and classify which digest claims its output actually
exercises.

## Background

Linked chapter: [@sec:part_III_pdvsa-gateway]. The chapter's central filing is
an honesty-first one: PDVSA Gateway Ops is a *simulator and catalog map* — not
live PDVSA telemetry and not a Protokol Sistemas contract audit — filed on the
[**engine shelf**](#gl:engine-shelf) as the enterprise gateway companion
[@mendez2026pdvsaMockup]. Its console concept, the [**Lattice-Linear**](#gl:lattice-linear)
Gateway, replaces silo-hopping across Production · Field · Compliance · Export
with one shared brief joined on a single incident object
[@mendez2026pdvsaGateway]. On the console, $\Phi \approx 1.618$ plays the role
of *routing grammar* [@mendez2026pdvsaMockup]; the flow ramp the gateway
executes, however, is exactly linear — step $i$ carries flow $i \cdot r$, so
the $n$-th value sits at $n \cdot r$ with no compounding. Everything you
compute here is bookkeeping for that routing grammar, not a measurement of an
oilfield.

## Procedure

1. **Run the reference implementation.** Clone the standalone repository,
   <https://github.com/FractiAI/synthobs-pdvsa-gateway-ops-mockup>, and run
   `npm run research:synthobs-pdvsa-gateway-ops-mockup`, which re-runs the
   nest's empirics E1–E6 [@mendez2026pdvsaMockup]. In your notebook, list
   which of the digest claims the output exercises — the simulator framing,
   the nine clickable takeaways, the engine-shelf filing — and which remain
   narrative filings with no executable counterpart.
2. **Compute the ramp by hand.** Apply the flow ramp of
   [@eq:part_III_pdvsa-gateway_model], $F_i = i \cdot r$, with $n = 5$ and
   $r = 2$, step by step: $F_1 = 1 \times 2 = 2$, $F_2 = 4$, $F_3 = 6$,
   $F_4 = 8$, $F_5 = 10$. Write the ramp down: $2, 4, 6, 8, 10$.
3. **Ramp at the grammar constant.** Repeat with $r = \Phi \approx
   1.618034$ for the first three steps: $F_1 = 1.618034$, $F_2 = 3.236068$,
   $F_3 = 4.854102$. Note what this does *not* do: the values are $i\Phi$,
   not $\Phi^i$ — the golden ratio enters as a per-step increment (routing
   grammar), not as the octave ladder's compounding exponent.
4. **Walk the gateway stages.** From the simulator digest, trace the console
   end to end and annotate each stage: the mode switches (Split · Today only
   · Gateway only; scenario stepper "Scenario 1 · Morning brief"); the four
   domain cards — Production (ERP), Field (SCADA), Compliance (Legal),
   Export (Logistics) — joined on one incident object, where clicking a
   domain pulls it into the shared brief while the others stay lit, with no
   tab reset; the three data-locality zones — Plant systems (the ERP/SCADA
   enclosure) ↔ Integration bridge ("Lattice joins domains here") ↔
   Partners & export ("safe summary out · no core dump"); the ops decision
   cycle Gather → Decide → Act ("signals in" → "one next action" → "execute
   & notify"), the console face of the MCA cycle Metabolize → Crystallize →
   Animate; and the desks on the call (Sources desk; Field & Production;
   Compliance; Partner/Export) [@mendez2026pdvsaGateway;
   @mendez2026pdvsaMockup].
5. **Verify against the model.** Run the computational workflow below and
   check every `lattice_linear_profile` output against your hand values from
   steps 2–3. They must match exactly.

## Analysis

Collect your two hand ramps. For the rate-2 ramp $[2, 4, 6, 8, 10]$, summarise
with `textbook.models.descriptive_statistics`: the mean is $6.0$, the
population standard deviation is $\sqrt{8} \approx 2.828427$, with minimum
$2$ and maximum $10$ — and the only reason the spread is nonzero is your
choice of $r$; the profile is deterministic. State the linearity result
explicitly: $F_n = n \cdot r$, so doubling $r$ doubles every value, and the
$n$-th step of the $\Phi$-ramp (step 3) sits at $n\Phi$ — *not* at $\Phi^n$
($\Phi^3 \approx 4.236068$), which is the octave ladder of
[@sec:part_0_octave-map], a different construct. Finally, mark the stage map
of step 4 against the chapter's scope section: the enclosure/continuity
filing ("SNA Core does not dump into every Edge handoff") is what the
"no core dump" zone enforces, and every numeric takeaway you met — context
cost under 15% of flat token dumps at $N \geq 6$, the $K = 12$ coherence
fixture — is a labelled simulator gain backed by companion empirics, not a
measured oilfield SLA [@mendez2026pdvsaGateway].

## Computational Workflow

```python
from textbook.models import lattice_linear_profile, descriptive_statistics
import math

PHI = (1 + 5 ** 0.5) / 2

# Steps 2-3: hand ramps, verified against the model:
assert list(lattice_linear_profile(5, 2.0)) == [2.0, 4.0, 6.0, 8.0, 10.0]
print([round(v, 6) for v in lattice_linear_profile(3, PHI)])
# [1.618034, 3.236068, 4.854102]   # i*Phi, not Phi**i

# Analysis: summary statistics of the rate-2 ramp:
print(descriptive_statistics(lattice_linear_profile(5, 2.0)))
# mean 6.0, std 2.828427..., min 2.0, max 10.0, count 5.0

# Cross-check: the octave ladder would give Phi**3 here — a different construct:
print(round(PHI ** 3, 6))  # 4.236068
```

## Reflection

- The simulator's efficiency and savings cards claim one executive thread
  replaces $N$ ticket queues and that gateway context cost stays under 15%
  of flat token dumps at $N \geq 6$ [@mendez2026pdvsaGateway]. Write the one
  sentence you would attach to each claim to make its evidentiary status
  honest — what is labelled, and what would have to be measured to upgrade it?
- After steps 3 and the cross-check: the ramp is $i \cdot r$ while the octave
  ladder is $\Phi^n$. Why does the corpus need *both* — what does each
  construct route or rank — and which one does the gateway actually execute?
- The Partners & export zone promises "safe summary out · no core dump".
  In the light of the honesty-first scope ([@sec:part_III_pdvsa-gateway]),
  what does that boundary protect, and which corpus filing does it echo?
