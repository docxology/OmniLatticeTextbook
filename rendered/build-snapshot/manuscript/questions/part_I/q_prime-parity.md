# Question Bank — Prime-Parity: The Sole-Even Anchor {#sec:q_part_I_prime-parity}

Linked chapter: [@sec:part_I_prime-parity]. Answers are derivable from the
chapter and its lab; the pinned constants are $\Phi = 1.6180339887$ and the
first ten odd primes 3, 5, 7, 11, 13, 17, 19, 23, 29, 31.

## Recall

1. What is the sole-even parity of 2, and what filing role does the Infinite
   Octaves grammar assign to it? *(Answer: 2 is the only even prime; the corpus
   files that uniqueness as the **binary dyad anchor**, the fixed member of the
   binary side of the prime table [@mendez2026primeParity].)*
2. What does the corpus mean by "odd primes act as irreducible minimum sets"?
   *(Answer: each odd prime is an irreducible minimal container/label — a set
   that cannot be composed from smaller filed sets, usable as a minimal unit of
   addressing; irreducibility is the fundamental-theorem property that makes
   prime-power addresses injective.)*
3. Recite the paper's octave recursion formula and name the ambiguity it is
   printed with. *(Answer: $\Omega_n = \Phi_n \cdot \Omega_0$, printed
   "Ωn = Φn · Ω0"; it is ambiguous whether $\Phi$ carries an exponent
   ($\Omega_n = \Phi^n \Omega_0$) or a subscript ($\Omega_n =
   F(n{+}1)/F(n)\,\Omega_0$), so `octave_term` keeps both conventions
   first-class.)*

## Application

4. Using `textbook.models.prime_parity_partition`, what are the two classes for
   primes below 32, and how large is the anchor class for *any* cutoff above 2?
   *(Answer: `{'sole_even': [2], 'odd': [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]}`;
   the anchor class is always exactly the singleton `[2]` whenever 2 lies below
   the cutoff — the data form of the sole-even theorem.)*
5. With $\Omega_0 = 1$, compute $\Omega_5$ under the exponent convention and
   $\Omega_{10}$ under the subscript convention, then verify with
   `octave_term`. *(Answer: exponent: $\Phi^5 = 11.090170$; subscript: the
   Fibonacci ratio $89/55 \approx 1.618182$; both are returned by
   `octave_term(1.0, n, convention)` with the matching `convention`
   argument.)*
6. Build one injective address that uses the anchor and one odd irreducible
   set, and explain why it is unique. *(Answer:
   `unique_address([2, 3], [2, 1]) = 2^2 · 3^1 = 12`; by the fundamental
   theorem of arithmetic no other prime-power product yields 12, so the address
   is unique — the anchor supplies the binary base, the odd set the first
   irreducible container.)*

## Synthesis

7. The exponent and subscript readings of $\Omega_n = \Phi_n \cdot \Omega_0$
   differ by more than a factor of six at $n = 5$ yet converge as $n$ grows.
   Explain why, and what the reference implementation's refusal to choose tells
   you about the corpus's honesty-first convention. *(Answer:
   $F(n{+}1)/F(n) \to \Phi$, so the subscript ladder tends to the first step of
   the exponential ladder; at small $n$ the Fibonacci ratios lag well below
   $\Phi$ (1.6 at $n=5$ vs 11.090170 for $\Phi^5$ with $\Omega_0=1$). Keeping
   both conventions first-class — instead of silently normalising — preserves
   the source text's ambiguity rather than papering over it, which is the
   honesty-first disclosure convention applied to notation itself.)*
8. A colleague claims the prime-parity paper "proves QED from primes and
   underwrites ultra-secure crypto hardware." Correct them using the paper's
   own scope statements. *(Answer: the paper's disclaimer states it is
   "catalog math + filing labels" — it does not prove QED from primes, rewrite
   NOAA heliophysics, or ship ultra-secure crypto hardware; the solar labels
   AR3664 ("Helios-Prime") and AR3590 ("Borealis") are story characters for
   timing talk, not cosmic proof certificates [@mendez2026primeParity].)*
9. Trace the parity filing forward through the corpus: name two downstream
   chapters that consume the binary dyad anchor or the odd irreducible sets,
   and one companion chapter the paper is shelf-pinned beside. *(Answer:
   the CMOS/protonic bridge maps the anchor into the binary shelf
   ([@sec:part_III_cmos-protonic]), and the volumetric-vault and
   protein-folding grammars reuse odd-prime irreducible containers via
   `unique_address` ([@sec:part_III_volumetric-storage],
   [@sec:part_III_protein-folding]); the paper is pinned beside Higgs Gate and
   the EGS Lattice-Linear gateway companion on shelf slot 11
   [@mendez2026primeParity].)*
