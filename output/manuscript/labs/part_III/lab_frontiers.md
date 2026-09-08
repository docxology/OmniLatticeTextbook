# Lab — Frontiers and the Research Program {#sec:lab_part_III_frontiers}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) classify corpus claims into the
[**narrative-empirical-operational-tiers**](#gl:narrative-empirical-operational-tiers),
(2) write one falsifiable check per claim, (3) assemble your own open-problem
ledger as a table, and (4) verify pinned values with `textbook.models` the same
way the chapter's worked formalisms do.

## Background

This lab operationalises [@sec:part_III_frontiers]. The chapter's closing
argument is that the corpus's [**honesty-first**](#gl:honesty-first) discipline
is not decoration — it *is* the research program. Every claim is filed in a
tier: **narrative** (metaphor and framing that coordinates people),
**empirical** (numbers a model recomputes), or **operational** (commands and
fixtures a machine replays) [@mendez2026masterSynthesis]. An open-problem
ledger turns that filing system into a personal instrument: instead of reading
about open problems, you pick claims, tier them, and attach a check that could
actually fail.

Both frontier papers scope themselves for you. The invisible-frontier paper
disclaims that Φ ≈ 1.618 replaces physics constants — EGS ≈ 1.618 is design
language, a master filing key filed as architecture, not a lab proof
[@mendez2026invisibleFrontier]. The moving-up-the-stack paper labels its deal
sizes "scenario anchors", not audited appraisals, and its corrected band
$12B–$28B is valuation framing, not a market oracle [@mendez2026stack]. Your
checks therefore never confirm or refute a metaphor; they test the recomputable
parts of a claim and record which parts are irreducibly narrative.

## Procedure

1. Pick three corpus claims from the digests behind [@sec:part_III_frontiers].
   Suitable candidates (substitutions welcome):
   - **Claim A** — the [**omni-lattice**](#gl:omni-lattice) catalog size:
     99 octaves × 81 precision digits = 8,019 entries.
   - **Claim B** — the invisible-frontier suite's "9/9 fixture lock" for
     `npm run research:synthobs-invisible-frontier-gates-ai`.
   - **Claim C** — the new-layer valuation band $12B–$28B, corrected from the
     $4.2B–$7.5B peer-shelf misread.
2. Tier each claim: narrative, empirical, or operational. Expect C to be
   narrative (scenario anchors), A empirical (a pinned value a function
   recomputes), and B operational (a fixture run).
3. Define one falsifiable check per claim — replay a fixture suite, recompute a
   pinned value, or re-derive a table from the source paper. A check with no
   possible failing outcome is not falsifiable; rewrite it.
4. Run each check. Machine checks go through the workflow below; manual checks
   go through your notebook.
5. Record all three rows in your ledger table, and place each claim on the
   open-problems quadrant map of [@fig:part_III_frontiers] by estimated value
   × effort.

Your ledger should look like this filled-in template:

| # | Claim (digest ID) | Tier | Falsifiable check | Result |
| --- | --- | --- | --- | --- |
| A | Catalog size 99 × 81 = 8,019 | empirical | `catalog_size() == 8019` recomputes the pinned product | pass |
| B | 9/9 fixture lock, gates-ai suite | operational | run `npm run research:synthobs-invisible-frontier-gates-ai`; all 9 fixtures pass | pass/fail |
| C | New-layer band $12B–$28B | narrative | re-derive the band from the premium table; confirm the source explicitly rejects the $4.2B–$7.5B peer-shelf misread | pass/fail |

## Analysis

Score each check twice: a pass/fail outcome, and a 0/1
machine-replayability flag (1 = the check runs with no human judgement).
Summarise both score columns with `textbook.models.descriptive_statistics` and
note the gap between them: a claim can pass its check while scoring 0 on
replayability — exactly what its tier label predicted. Claims that fail their
checks or resist tiering move to a second table: your open problems, one line
each, with the observation that would resolve them.

## Computational Workflow

```python
from textbook.models import catalog_size, octave_term, descriptive_statistics

# Check A — recompute the pinned catalog size.
assert catalog_size() == 8019            # 99 octaves × 81 precision digits

# Check B — both conventions behind the ambiguous print "Ωn = Φn·Ω0"
print(octave_term(1, 5, convention="exponent"))   # 11.090170…  (Φ^5 · Ω0)
print(octave_term(1, 5, convention="subscript"))  # 1.6         ((8/5) · Ω0)

# The conventions diverge as n grows: at n = 10 the subscript ratio has only
# reached 89/55 ≈ 1.618182, while the exponent reading gives Φ^10 ≈ 122.991869.
```

## Reflection

1. Which of your three claims survived as operational, and which could not be
   checked at all without leaving the
   [**catalog-architecture**](#gl:catalog-architecture) framework entirely?
2. Your check on Claim C can only confirm that the source is internally
   consistent. What observation in the world — not the corpus — would have to
   exist before the $12B–$28B framing could move up to empirical?
3. The corpus prints "Ωn = Φn·Ω0" with the Φ exponent/subscript ambiguous, so
   `octave_term` implements both conventions. Why must a reproducibility ledger
   record *which* convention produced a number?
