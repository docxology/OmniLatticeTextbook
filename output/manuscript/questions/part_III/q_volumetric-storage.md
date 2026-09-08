# Question Bank — Prime-Indexed Volumetric Storage {#sec:q_part_III_volumetric-storage}

Linked chapter: [@sec:part_III_volumetric-storage].

## Recall

1. What baseline do incumbent flash and disk stacks pay, and to which codes
   and index structures does the paper attribute it? *(Answer: a 15–30%+
   parity tax attributed to Reed–Solomon / LDPC error-correction coding,
   plus the wait on LBA / B⁺ tree addressing structures
   [@mendez2026volumetricStorage].)*
2. In the paper's grammar, what roles do Prime 2 and the odd primes play?
   *(Answer: Prime 2 is the binary base channel; odd primes are the
   irreducible volumetric vaults — irreducible because a prime factorises no
   further [@mendez2026volumetricStorage].)*
3. State the paper's honesty-first disclaimer in full. *(Answer: "this is
   *catalog architecture*, not a JEDEC drop-in, not measured 0% ECC on NAND,
   and not a claim that shipping controllers are obsolete"; additionally the
   closed-form encode is a fixture, not FTL firmware, and the solar labels
   AR3664 ("Helios-Prime") and AR3590 ("Borealis") are story filing
   characters [@mendez2026volumetricStorage].)*

## Application

4. Compute the vault address for the prime vector $(2, 3, 5)$ with exponent
   vector $(2, 0, 1)$, then factor the result to recover the exponents.
   *(Answer: $A = 2^2 \cdot 3^0 \cdot 5^1 = 20$; factoring $20 = 2^2 \cdot 5$
   recovers $(2, 0, 1)$ because prime factorisation is unique — the encoding
   of [@eq:part_III_volumetric-storage_address] is injective.)*
5. A vault grid uses $m = 4$ primes with exponents in $\{0, 1, 2\}$. How many
   distinct addresses can it hold, and which equation in the chapter gives
   this? *(Answer: $(K+1)^m = 3^4 = 81$ distinct addresses, by
   [@eq:part_III_volumetric-storage_capacity].)*
6. Using the $\Phi$-ruler reading of
   [@eq:part_III_volumetric-storage_phiruler], place the address $A = 12$
   between two `phi_powers` rungs and give the reading in $\Phi$-steps.
   *(Answer: $\log_{\Phi} 12 = \ln 12 / \ln \Phi \approx 5.16$ $\Phi$-steps;
   $12$ sits between the $\Phi^5 \approx 11.090170$ and
   $\Phi^6 \approx 17.944272$ rungs.)*

## Synthesis

7. The paper's parity-tax contrast is filed as catalog architecture, yet the
   same note reports a 9/9 suite-locked implementation with millisecond
   encodes. Assemble the chapter's evidence into a one-paragraph account of
   what has actually been demonstrated — and what has not. *(Answer: what is
   demonstrated is a working fixture: the unique-address encoding runs as a
   closed-form encode in milliseconds for demo chunks and passes a 9/9
   suite lock under `research/synthobs-prime-indexed-volumetric-storage/`,
   filed on engine shelf #15 as a companion to prime-parity and the protein
   prime-container. What has *not* been demonstrated — by the paper's own
   disclaimer — is any hardware result: it is not a JEDEC drop-in, there is
   no measured 0% ECC on NAND, no claim that shipping controllers are
   obsolete, and the timings are fixture timings rather than FTL firmware
   performance [@mendez2026volumetricStorage].)*
8. Why does the injectivity of [@eq:part_III_volumetric-storage_address]
   let the catalog drop the LBA / B⁺-tree lookup that incumbent stacks
   "wait on", and what carries the equivalent role for Prime 2? *(Answer:
   because prime factorisation is unique, an address *is* its own
   factorisation — recovering the exponent vector needs no separate index
   structure, which is the role LBA / B⁺ trees play in incumbent stacks;
   Prime 2 carries the binary base channel, the substrate role anchored by
   the sole-even-anchor grammar of prime-parity
   [@mendez2026primeParity].)*
9. The protein folding paper runs "the same prime-vault grammar in the
   biology catalog". Sketch how one grammar can serve both a storage filing
   and a biological filing, and name the property that makes the sharing
   coherent. *(Answer: both filings use the same injective
   prime-exponent encoding — odd primes as irreducible containers and
   unique products as addresses — with the domain supplying the exponent
   assignment; the shared property is the uniqueness of prime
   factorisation, which guarantees no address collisions in either
   catalog, and the protein prime-container chapter works the same
   machinery [@mendez2026proteinFolding].)*
