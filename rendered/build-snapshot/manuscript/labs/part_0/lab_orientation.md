# Lab — The SS Vibelandia Program and the Omni-Lattice Corpus {#sec:lab_part_0_orientation}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`), a web browser

## Objectives

After this lab you will be able to (1) navigate the corpus's two anchor pages — the ship's front door and the Reading Room catalog — and quote their honesty clauses verbatim, (2) locate the 24 [**engine-shelf**](#gl:engine-shelf) papers this book covers and the two application companions that stay off the shelf, (3) file any catalog item into the correct narrative / empirical / operational [**tier**](#gl:narrative-empirical-operational-tiers), (4) compute the [**master register**](#gl:master-register)'s size by hand and verify it against `textbook.models.catalog_size`, and (5) map each region of the engine shelf to the part of this book that covers it.

## Background

Linked chapter: [@sec:part_0_orientation]. The corpus self-describes as [**catalog architecture**](#gl:catalog-architecture) — a filing and protocol grammar for coordinating agents, dashboards, and conversation, explicitly not established physics — and its two anchor pages state that status themselves [@mendez2026ship; @mendez2026catalog]. Rather than take the chapter's word for it, this lab has you survey the shelves yourself: walk the ship's homepage, browse the Reading Room, and touch the numbers (24 pins, 195 distinct items, $99 \times 81$ register bins) where they live. One reading rule governs every step, and it is the corpus's own [**honesty-first**](#gl:honesty-first) clause: read each item's scope disclaimer before filing it anywhere. And keep the [**Fair Exchange**](#gl:fair-exchange) framing throughout: a receipt for every exchange, with hand values matched against the tested functions rather than trusted on retyped arithmetic.

## Procedure

1. **Board the ship and enter the library.** Open the ship homepage (`https://www.ssvibelandiaquestfest24x365.com`) and quote the first sentence of the honesty rail — "This page is art and hospitality. Φ ≈ 1.618 is our nesting language." — plus the host identity line, Valet Pru · XY Human Reality Bridge/Router · Player 1, "the human host — not a bot gate" [@mendez2026ship]. Then open the catalog URL (`https://www.ssvibelandiaquestfest24x365.com/papers`), the Reading Room, and quote its own honesty note: "Cover art is AI-generated poster hospitality from each paper's abstract focus — not empirical proof" [@mendez2026catalog]. Record both quotes verbatim.
2. **Locate the engine shelf and the companions.** In the Reading Room, find the "Featured picks — Start here" shelf and the per-category shelves below it. Identify the 24 engine-shelf papers — the 2026-09-08 sync pins 24 registry papers in ordered shelf slots, laid out by shelf number in [@fig:part_0_orientation] — and confirm their `engine` tags in the item metadata. Then locate the two application companions this book files in Part III: the PDVSA Gateway Ops live project page and its mockup note [@mendez2026pdvsaGateway; @mendez2026pdvsaMockup]. Verify the corpus's own rule at the shelf's edge: application companions stay off the engine shelf [@mendez2026livingPem]. Record where each of the two actually appears.
3. **Classify three arbitrary items by tier.** Pick any three catalog items that catch your eye. For each, read its "Honesty first" clause and abstract, then file it as *narrative* (story, poster, or voyage filing), *empirical* (fixtures, suite locks, reference-implementation runs), or *operational* (protocol, runbook, sync procedure). Justify each label with one quoted phrase from the item's own text — not from its poster art. If an item seems to straddle two tiers, write down exactly which phrase pulls it each way; the ambiguity is data.
4. **Size the master register by hand.** On paper, multiply the octave count by the register width: $99 \times 81 = 8{,}019$ register bins. This is the filing space of the digits × octaves map — the whole cabinet the corpus addresses. Write the number down before touching a keyboard.
5. **Map shelf regions to the book.** Using the shelf timeline of [@fig:part_0_orientation] and the engine-pin ordering locked by the living PEM (CMOS/protonic bridge first, then tensor decoupling, then master synthesis plus the digits master, then the later engine parts, then companions) [@mendez2026livingPem], record which part of this book covers each region: the engineering-bridge / tensor-filing / master-synthesis region belongs to Part 0; the constants, primes, rhyme, void, and Higgs Gate region to Part I; the physical filing papers — viscosity of light, eddy-current mirror, crystalline field, metrological overlap, metamorphic octaves, planetary core, singularity crystal — to Part II; and the silicon shelf through the reality bridge and the companions to Part III.

## Analysis

Report your three tier classifications as a three-row table: item, quoted honesty phrase, tier, one-sentence justification. Then assemble the survey receipt — the four counts your walk produced: 24 engine pins, 2 application companions, 195 distinct catalog items [@mendez2026catalog], and the 8,019-cell register — and summarise them with `textbook.models.descriptive_statistics`. The summary is deliberately trivial; the discipline it rehearses is not. Every number you carry out of the corpus should be one you can reproduce from the shelves or from a tested function [@mendez2026livingPem]. If your hand value of 8,019 disagrees with `catalog_size()`, re-derive by hand before suspecting the library — the function is tested; the arithmetic above is not.

## Computational Workflow

```python
from textbook.models import catalog_size, descriptive_statistics

# Step 4 check: the register's floor plan (hand value: 99 * 81 = 8019)
hand = 99 * 81
computed = catalog_size(octaves=99, precision_digits=81)   # expect 8019
assert hand == computed == 8019

# Analysis: the survey receipt — pins, companions, catalog items, register bins
receipt = [24, 2, 195, catalog_size()]
print(descriptive_statistics(receipt))
```

Confirm the printed size against your hand computation, then attach the receipt summary to your lab note.

## Reflection

1. The honesty rail files Φ ≈ 1.618 as "our nesting language" [@mendez2026ship]. After walking the shelves yourself, which of your three tier labels does that clause itself deserve — and what would it cost the catalog to mislabel it?
2. The two PDVSA companions carry empirics of their own yet are filed off the shelf [@mendez2026pdvsaGateway; @mendez2026pdvsaMockup]. What does the corpus gain by separating engine pins from application companions — and what would a reader lose if the shelf mixed them?
3. Under the Fair Exchange clause, "value exchanged is fluid and may be partially refunded based on resonance and overall delivery" [@mendez2026ship]. Treat your survey receipt as the delivery: which of the five objectives did the walk actually settle, and which deserve a second pass?
