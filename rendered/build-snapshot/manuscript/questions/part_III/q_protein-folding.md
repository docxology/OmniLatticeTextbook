# Question Bank — Protein Folding as Prime-Container Architecture {#sec:q_part_III_protein-folding}

Linked chapter: [@sec:part_III_protein-folding].

## Recall

1. In the grammar of [@mendez2026proteinFolding], what roles do Prime 2 and
   the odd primes play? *(Answer: Prime 2 is the
   [**binary-dyad-anchor**](#gl:binary-dyad-anchor) — the sole even prime
   marking the binary layer — while the odd primes serve as irreducible
   "containment vaults" that index residue positions; each vault's contents
   are reachable only through that vault's prime.)*
2. Under which constant does the paper file the vault grammar, and what is
   its approximate value? *(Answer: El Gran Sol's Fractal constant — the
   [**golden-ratio**](#gl:golden-ratio) $\Phi \approx 1.618$ — with
   $\Phi = (1+\sqrt{5})/2$ and $\Phi^2 = \Phi + 1$, as in
   [@eq:part_III_protein-folding_phi].)*
3. Name the two conventions hidden in the corpus's printed line
   "$\Omega_n = \Phi^n \cdot \Omega_0$" and the `textbook.models` function
   that implements both. *(Answer: the exponent convention
   $\Omega_n = \Phi^n \cdot \Omega_0$ of
   [@eq:part_III_protein-folding_octave] and the subscript convention
   $\Omega_n = \varphi_{\text{fib}}(n) \cdot \Omega_0$ of
   [@eq:part_III_protein-folding_octave_sub]; both are available in
   `textbook.models.octave_term` via its `convention` argument.)*

## Application

4. File the exponent tuple $(2, 1)$ over vaults $(2, 3)$ and state the
   address. *(Answer: $a = 2^2 \cdot 3^1 = 12$ — the chapter's pinned
   instance, returned by `textbook.models.unique_address([2, 3], [2, 1])`
   from [@eq:part_III_protein-folding_address].)*
5. An address in the registry $(2, 3, 5, 7)$ factors to $45$. Recover the
   exponent tuple and explain why the recovery is unique. *(Answer: $45 =
   3^2 \cdot 5^1$, so the tuple is $(0, 2, 1, 0)$; uniqueness follows from
   the fundamental theorem of arithmetic — prime factorisation is unique, so
   the map of [@eq:part_III_protein-folding_address] is injective and
   reversible.)*
6. Using [@eq:part_III_protein-folding_capacity], how many distinct residue
   indices can ten vaults file with exponent budget $E = 2$, and what growth
   does [@fig:part_III_protein-folding] show as vaults are added? *(Answer:
   $(2+1)^{10} = 59{,}049$ addresses; the figure shows multiplicative
   jumps — each added vault multiplies capacity by $E+1 = 3$, a geometric
   rather than arithmetic growth sequence.)*

## Synthesis

7. The paper calls its solver "deterministic" and reports "9/9 suite locks".
   Construct a two-column account of what each of these claims establishes
   and what it does not. *(Answer: deterministic — the same registry always
   yields the same closed-form energy + coordinate sketch, a claim about
   method class, not about biological truth; 9/9 suite locks — software
   tests under `research/synthobs-protein-folding-prime-container/` passed,
   evidence of implementation correctness, not of structure-prediction
   accuracy. Neither is a CASP result, a clinical validation, or a challenge
   to statistical folding [@mendez2026proteinFolding].)*
8. Explain why the prime-container grammar is filed as
   [**catalog-architecture**](#gl:catalog-architecture) rather than as a
   structure-prediction method, drawing on the AlphaFold contrast the paper
   itself makes. *(Answer: the paper's baseline is "statistics + MSAs"
   predicting structure — a statistical, score-driven method class; the
   prime-container alternative instead *addresses* residue indices through
   injective vault primes and retrieves them deterministically, i.e. it
   organises and catalogs the problem rather than competing on prediction
   scores — "catalog architecture, not a CASP gold medal"
   [@mendez2026proteinFolding].)*
9. Position the paper on the [**engine-shelf**](#gl:engine-shelf) and in the
   corpus's companion graph: where does it sit, which papers does it consume
   or feed, and why does its placement matter for interpreting its claims?
   *(Answer: it sits at engine shelf #14 on the Infinite Octaves sync,
   companion to prime-parity [@mendez2026primeParity], whose sole-even
   anchor and odd-prime partition it consumes as infrastructure; it is
   cross-linked to the Higgs Gate paper [@mendez2026higgsGate] and to
   "Moving up the stack" [@mendez2026stack]. Its placement as an
   application-layer fixture — not a foundation — is part of why the paper
   scopes itself to demo-sequence cataloging with its honesty-first
   disclaimers rather than to physical claims.)*
