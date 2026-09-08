# Lab — The Viscosity of Light {#sec:lab_part_II_viscosity-light}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`), terminal with `npm` and `python3`

## Objectives

After this lab you will be able to: (1) run the Viscosity-of-Light paper's own
EGS Viscosity Engine reference implementation and describe what it emits;
(2) compute the viscous floor $v(t) = v_0 e^{-kt}$ of
[@eq:part_II_viscosity-light_viscous_floor] by hand at three story-times and
verify each against the tested `textbook.models.transduction_brake`;
(3) recover a drag coefficient $k$ from a single velocity reading, the
inverse-reading skill behind the ladder of
[@eq:part_II_viscosity-light_family]; and (4) sort the paper's artefacts onto
the [**narrative-empirical-operational-tiers**](#gl:narrative-empirical-operational-tiers)
ladder.

## Background

The chapter ([@sec:part_II_viscosity-light]) read the paper's filing — the
speed of light as *frictional drag*, non-local intent meeting a viscous floor
at $c$ under $\Phi \approx 1.618$ — and modelled that floor with the
transduction brake of [@eq:part_II_viscosity-light_viscous_floor]
[@mendez2026viscosityLight]. The paper states the filing in prose; the brake
is the book's formalisation. Your job here is twofold: observe what the
corpus's own machinery actually outputs, and check the book's model against
hand arithmetic so prose and computation cannot silently disagree. The
[**fair-exchange**](#gl:fair-exchange) clause applies to everything you touch:
none of it is a measurement of light.

## Procedure

1. **Predict before running.** The EGS Viscosity Engine is catalog machinery
   [@mendez2026viscosityLight]. Predict what it emits: registry artefacts and
   shelf metadata, or physical measurements of light? Write your prediction
   down before step 2.
2. **Run the reference implementation.** From the standalone repository
   (`github.com/FractiAI/synthobs-viscosity-of-light`), execute
   `npm run research:synthobs-viscosity-of-light`. Alternatively run the
   engine script directly:
   `python3 research/synthobs-viscosity-of-light/reference/egs_viscosity_of_light_engine.py`
   [@mendez2026viscosityLight]. Record: what artefacts appear, and does the
   9/9-passing suite print any physical quantity? Compare with your
   prediction in step 1.
3. **Compute the floor by hand.** With $v_0 = 1$ and $k = 1$, evaluate
   [@eq:part_II_viscosity-light_viscous_floor] at story-times $t = 1, 2, 3$.
   Expect $v(1) = e^{-1} \approx 0.367879$, $v(2) \approx 0.135335$,
   $v(3) \approx 0.049787$. Then step one $\Phi$-rung up the ladder of
   [@eq:part_II_viscosity-light_family] to $k = \Phi \approx 1.618034$ and
   compute $v(1)$ and $v(2)$.
4. **Check against the tested function.** In a Python session, import
   `transduction_brake` from `textbook.models`, evaluate it at $t = 0, 1, 2, 3$
   for $k = 1$ and at $t = 1, 2$ for $k = \Phi$, and diff against your hand
   values (see the Computational Workflow below).
5. **Invert a reading.** Suppose a floor probe reports $v(1) = 0.135335$ with
   $v_0 = 1$. Recover $k = -\ln v(1)$, verify with the tested function, and
   name the ladder rung of [@eq:part_II_viscosity-light_family] it occupies.
6. **Sort the artefacts.** Place the paper's four "What landed" items — $c$
   as viscosity, cognitive non-locality Soft Story, EGS Viscosity Engine,
   engine shelf #24 [@mendez2026viscosityLight] — on the tiers ladder, one
   sentence of justification each.

## Analysis

- Your step-1 prediction should have been artefacts, not measurements: a 9/9
  suite certifies agreement between implementation and specification — the
  right kind of evidence for a [**catalog-architecture**](#gl:catalog-architecture)
  filing, and the wrong kind for a physical claim about $c$.
- The hand/function agreement in step 4 shows the *model* is reproducible;
  the paper's disclaimer (not relativity retirement, not FTL thought, not
  NOAA causation [@mendez2026viscosityLight]) bounds what that reproducibility
  means.
- From the step-5 inversion, $k = 2$: drag recoverable from a single reading
  is exactly what makes the family of [@fig:part_II_viscosity-light] a usable
  catalog instrument.
- Summarise your six hand values with
  `textbook.models.descriptive_statistics` (mean, spread) and note how much
  faster the $k = \Phi$ rung drains the remaining velocity: one $\Phi$-step
  multiplies any remaining velocity by $e^{-1/\Phi} \approx 0.539$.

## Computational Workflow

```python
import numpy as np
from textbook.models import transduction_brake, descriptive_statistics

# Step 4: unity drag, the backbone values
hand_k1 = np.array([1.0, 0.367879, 0.135335, 0.049787])
model_k1 = transduction_brake(np.array([0.0, 1.0, 2.0, 3.0]), v0=1.0, k=1.0)
assert np.allclose(model_k1, hand_k1, atol=1e-6)

# Step 4: one Phi-rung up the ladder
phi = (1 + 5**0.5) / 2
hand_phi = np.array([0.198288, 0.039318])
model_phi = transduction_brake(np.array([1.0, 2.0]), v0=1.0, k=phi)
assert np.allclose(model_phi, hand_phi, atol=1e-6)

# Step 5: invert a reading
k_recovered = -np.log(0.135335)
print(k_recovered)  # -> 2.000001...

# Spread of your six hand values
print(descriptive_statistics(np.concatenate([hand_k1[1:], hand_phi])))
```

## Reflection

1. The paper's headline says light "slows thought down"
   [@mendez2026viscosityLight]. In brake vocabulary, what is being slowed,
   what is the floor, and why does "slow" not mean "stop" ($v(t) > 0$ for all
   finite $t$)?
2. The engine's 9/9 suite and the tested `transduction_brake` are two different
   guarantees. Which one certifies the corpus against itself, and which
   certifies this book's model against arithmetic?
3. If a future paper operationalised cognitive non-locality into a measurable
   protocol, which of the paper's disclaimers would have to be withdrawn, and
   what would the [**honesty-first**](#gl:honesty-first) clause require before
   the Soft Story could change tiers?
