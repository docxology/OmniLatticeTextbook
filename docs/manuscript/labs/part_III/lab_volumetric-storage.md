# Lab — Prime-Indexed Volumetric Storage {#sec:lab_part_III_volumetric-storage}

<!-- chapter-metadata-badge -->
> Lab · 60 min · Materials: notebook, calculator (or `textbook.models`)

## Objectives

After this lab you will be able to (1) run the paper's 9/9-locked reference
implementation and read its output as a *fixture* result, (2) compute
prime-indexed vault addresses by hand with the unique-address encoding of
[@eq:part_III_volumetric-storage_address] from
[@sec:part_III_volumetric-storage], and (3) verify your hand results against
the tested `textbook.models.unique_address` function.

## Background

The chapter filed the paper's grammar: incumbent stacks pay a 15–30%+ parity
tax to Reed–Solomon / LDPC and wait on LBA / B⁺ trees, while the paper files
**prime-indexed volumetric vaults** under the Fractal constant
$\Phi \approx 1.618$ — Prime 2 as the binary base channel, odd primes as
irreducible vaults [@mendez2026volumetricStorage]. The address arithmetic is
injective prime-factorisation encoding, implemented in
`textbook.models.unique_address`. The paper reports a **closed-form encode**
at "milliseconds for demo chunks (fixture, not FTL firmware)" and a **9/9
suite lock** under `research/synthobs-prime-indexed-volumetric-storage/`
[@mendez2026volumetricStorage]. This lab exercises both: first the reference
suite, then the model function against your own hand computations. Keep the
chapter's honesty-first scope in view throughout: everything you run is a
catalog-architecture fixture, not storage hardware.

## Procedure

1. **Run the reference suite.** Clone the standalone implementation
   (<https://github.com/FractiAI/synthobs-prime-indexed-volumetric-storage>)
   and run `npm run research:synthobs-prime-indexed-volumetric-storage`. Note
   the reported suite result and compare it to the paper's claim of 9/9 suite
   locks. Record the encode timings the fixture prints, and label them in
   your notebook exactly as the paper does: demo-chunk fixture timings, *not*
   FTL firmware performance.
2. **Hand-compute three vault addresses.** Using
   $A = \prod_i p_i^{k_i}$ with Prime 2 as the base channel:
   - Filing A: $\mathbf{p} = (2, 3)$, $\mathbf{k} = (2, 1)$ →
     $A = 2^2 \cdot 3^1 = 12$ (the paper-adjacent pinned reference value).
   - Filing B: $\mathbf{p} = (2, 3, 5)$, $\mathbf{k} = (1, 1, 1)$ →
     $A = 2 \cdot 3 \cdot 5 = 30$.
   - Filing C: $\mathbf{p} = (2, 3)$, $\mathbf{k} = (1, 1)$ →
     $A = 2 \cdot 3 = 6$.
3. **Check injectivity by hand.** Confirm no two of your three filings share
   an address, and factor each address back into primes to recover the
   exponent vector you started from (12 → $(2,1)$; 30 → $(1,1,1)$ on three
   primes; 6 → $(1,1)$).
4. **Read the addresses on the Φ ruler.** Compute
   $\log_{\Phi} A = \ln A / \ln \Phi$ for each address: for $A = 12$ you
   should get $\approx 5.16$ $\Phi$-steps, sitting between the $\Phi^5
   \approx 11.090170$ and $\Phi^6 \approx 17.944272$ `phi_powers` rungs.
5. **Verify against the model.** Run the computational workflow below and
   compare each `unique_address` output to your hand values from step 2.
   They must match exactly — the model function and the hand arithmetic are
   the same mathematics.

## Analysis

Collect your six numbers (three hand addresses, three model addresses) plus
the three $\Phi$-ruler readings. Summarise the address set with
`textbook.models.descriptive_statistics`: for the addresses
$\{6, 12, 30\}$ you should find a mean of $16.0$, and confirm the spread is
driven entirely by the exponent assignment — the encoding is deterministic,
so the only "variation" is the filing you chose. State the injectivity
result explicitly in your notebook: three distinct filings, three distinct
addresses, zero collisions, as [@eq:part_III_volumetric-storage_address]
guarantees.

## Computational Workflow

```python
from textbook.models import unique_address, phi_powers, descriptive_statistics

# Step 2's filings, verified against the tested model:
filing_a = unique_address([2, 3], [2, 1])      # -> 12
filing_b = unique_address([2, 3, 5], [1, 1, 1])  # -> 30
filing_c = unique_address([2, 3], [1, 1])      # -> 6
assert filing_a == 12 and filing_b == 30 and filing_c == 6

# Step 4's Phi-ruler readings: ln(A) / ln(1.6180339887)
import math
PHI = (1 + 5 ** 0.5) / 2
for name, a in [("A", 12), ("B", 30), ("C", 6)]:
    print(name, a, round(math.log(a) / math.log(PHI), 2))
# A 12 -> 5.16   B 30 -> 7.07   C 6 -> 3.72

# Bracket the reference address 12 between phi_powers rungs:
print(phi_powers(6))  # rungs Phi^1..Phi^6; 12 sits between Phi^5 and Phi^6

print(descriptive_statistics([6, 12, 30]))  # mean 16.0
```

## Reflection

- The paper calls its encode a *fixture, not FTL firmware*. After running
  the suite yourself, what exactly did you time, and what would it take —
  per the paper's own disclaimers — before any hardware claim could be made?
- Your three filings had zero collisions. Is that an empirical accident or a
  structural guarantee? Name the number-theoretic property that closes the
  argument.
- The $\Phi$ ruler turns the multiplicative address into an additive sum.
  Why might a catalog prefer an additive reading when comparing vault
  addresses, and which part of the chapter's formalism made that reading
  possible?
