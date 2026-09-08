# Lab — Protein Folding as Prime-Container Architecture {#sec:lab_part_III_protein-folding}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`), Node.js for the reference suite

## Objectives

After this lab you will be able to: (1) file residue-index addresses with the
prime-container grammar by hand and verify them with
`textbook.models.unique_address`; (2) run the paper's reference suite and
predict its outcome before running it; (3) compute the addressing capacity of
a vault registry and interpret the growth sequence of
[@fig:part_III_protein-folding]; and (4) articulate, in your own words, the
scope boundary the source paper draws around all of this
[@mendez2026proteinFolding].

## Background

Linked chapter: [@sec:part_III_protein-folding]. In that chapter we formalised
the grammar of [@mendez2026proteinFolding]: Prime 2 as the
[**binary-dyad-anchor**](#gl:binary-dyad-anchor), odd primes as irreducible
containment vaults, and the address formalism of
[@eq:part_III_protein-folding_address] — injective and reversible, hence a
catalog rather than a hash. This lab makes the grammar do work: you will
*file* addresses, *retrieve* them by factoring, and *stress* the capacity
product of [@eq:part_III_protein-folding_capacity]. Everything here is
[**catalog-architecture**](#gl:catalog-architecture) practice on demo
sequences — the paper itself files its solver as "fixture, not PDB
replacement" — so keep the [**honesty-first**](#gl:honesty-first) framing:
you are exercising a deterministic addressing scheme, not predicting protein
structures.

## Procedure

1. **Hand-file two addresses.** Using the registry $(2, 3, 5, 7)$ from the
   chapter's worked example:
   - the exponent tuple $(1, 2, 0, 0)$ gives $a = 2^1 \cdot 3^2 \cdot 5^0
     \cdot 7^0 = 18$;
   - the exponent tuple $(0, 1, 1, 0)$ gives $a = 3 \cdot 5 = 15$.
   Write both products out before touching a keyboard. Check your answers in
   the Computational Workflow step.
2. **Retrieve by factoring.** Take the address $45$ and factor it against the
   same registry: $45 = 3^2 \cdot 5^1$, so the exponent tuple is $(0, 2, 1,
   0)$. Confirm that re-filing that tuple returns 45 — the round trip that
   makes the map a catalog. Try one address of your own and trade it with a
   partner: can they recover your tuple uniquely? (They always can; say why
   in one sentence using the fundamental theorem of arithmetic.)
3. **Run the reference suite.** From the corpus repositories, execute:

   ```bash
   npm run research:synthobs-protein-folding-prime-container
   ```

   The source paper reports **9/9 suite locks** under
   `research/synthobs-protein-folding-prime-container/`
   [@mendez2026proteinFolding]. *Predict the outcome before running*: how
   many locks should pass, and what does a lock failing here mean — a
   biochemical refutation or a software regression? The standalone suite
   lives at `github.com/FractiAI/synthobs-protein-folding-prime-container`
   if you want to read the closed-form energy + coordinate sketch the paper
   describes as running "in milliseconds on CPU for demo sequences".
4. **Read the capacity curve.** Open [@fig:part_III_protein-folding] and
   identify the multiplicative jumps as each vault prime is added. Then
   compute, by hand, the capacity of a ten-vault registry with exponent
   budget $E = 2$: $(2+1)^{10} = 59{,}049$ distinct residue indices.

## Analysis

Summarise your filed/retrieved addresses in a table (registry, exponent
tuple, address, recovered tuple) and compute the round-trip success rate —
it should be 100%, and the *reason* (uniqueness of prime factorisation) is
the load-bearing property, not the count. Aggregate your capacity numbers
with `textbook.models.descriptive_statistics` if you extended the registry
beyond ten vaults, and note that the growth is geometric in vault count, not
arithmetic: doubling the vaults squares the addressable space. Finally, write
three sentences placing the whole exercise on the corpus's own terms: what
was demonstrated (deterministic, injective, reversible addressing for demo
sequences), and what was not (no structure prediction, no clinical claim, no
challenge to statistical folding — "catalog architecture, not a CASP gold
medal" [@mendez2026proteinFolding]).

## Computational Workflow

```python
from textbook.models import unique_address

# Step 1 checks — your hand products should match exactly:
print(unique_address([2, 3, 5, 7], [1, 2, 0, 0]))  # → 18
print(unique_address([2, 3, 5, 7], [0, 1, 1, 0]))  # → 15
print(unique_address([2, 3], [2, 1]))              # → 12 (chapter's pinned instance)

# Step 2 check — re-file the factored tuple for 45:
print(unique_address([2, 3, 5, 7], [0, 2, 1, 0]))  # → 45
```

Compare every printed value with your hand computation. If any disagree, the
error is in your arithmetic — the function is the tested reference.

## Reflection

1. The address map is injective *and* reversible; a modulo hash is neither.
   In two sentences, why does the corpus file the prime scheme as a catalog
   rather than a hash, and what does that buy a deterministic solver?
2. You ran a suite with a predicted 9/9 outcome. What *kind* of evidence is
   a passing software suite about the prime-container grammar — and what
   kind of evidence about proteins is it not?
3. The paper's solar filing characters AR3664 ("Helios-Prime") and AR3590
   ("Borealis") are, per the paper itself, "story filing characters — not
   NOAA proof that stars fold proteins" [@mendez2026proteinFolding]. Where
   else in this lab did a filing metaphor risk being read as a physical
   claim, and how did you keep the boundary visible?
