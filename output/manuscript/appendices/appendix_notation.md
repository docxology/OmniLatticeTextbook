# Appendix B — Notation and Symbols {#sec:appendix_notation}

<!-- chapter-metadata-badge -->
> Reference appendix · Symbol glossary for the worked models.

This appendix lists the symbols used by the worked formalisms of the Infinite
Octaves Omni-Lattice and by the tested implementations in
[`src/textbook/models.py`](../../../src/textbook/models.py). Keep it in sync with
the parameter tables (`{#tbl:...}`) in the chapters: every symbol that appears
in an equation `{#eq:...}` should have a row here. Corpus symbols are filed
exactly as the papers file them — as [catalog
architecture](../glossary.md#gl:catalog-architecture) vocabulary
[@mendez2026digitsMaster; @mendez2026masterSynthesis].

## Conventions

- Scalars are italic lowercase (e.g. *n*, *t*); sets and spaces are uppercase.
- Subscript `0` denotes a base or initial value (e.g. $\Omega_0$, $P_0$).
- "Filed as" is the corpus's own verb: it marks a catalog filing, not a
  physical derivation ([honesty-first](../glossary.md#gl:honesty-first)).
- Units are stated where the underlying mathematics has them; most catalog
  quantities are dimensionless filing labels.

## Core Omni-Lattice Symbols

| Symbol | Name | Appears in | Units | Notes |
| --- | --- | --- | --- | --- |
| $\Phi$ | El Gran Sol's Fractal Constant (golden ratio) | `phi_powers`, `octave_term`, `phi_dual` | dimensionless | $(1+\sqrt{5})/2 \approx 1.6180339887$; architectural key, not a replacement for $\hbar, c, G$ [@mendez2026masterSynthesis] |
| $\Phi^n$ | golden-ratio powers | `phi_powers` | dimensionless | $1.618034, 2.618034, 4.236068, 6.854102, 11.090170, 17.944272$ for $n = 1..6$ |
| $\varphi_{\mathrm{fib}}(n)$ | Fibonacci ratio | `phi_fibonacci` | dimensionless | $F_{n+1}/F_n$; $\varphi_{\mathrm{fib}}(5) = 8/5 = 1.6$, $\varphi_{\mathrm{fib}}(10) = 89/55 \approx 1.618182$ |
| $\Omega_n$ | octave term at index $n$ | `octave_term` | dimensionless | Printed ambiguously as "Ωn = Φn · Ω0"; exponent reading $\Omega_n = \Phi^n \Omega_0$ vs subscript reading $\Omega_n = \varphi_{\mathrm{fib}}(n)\,\Omega_0$ — both implemented [@mendez2026primeParity] |
| $\Omega_0$ | base octave term | `octave_term` | dimensionless | value at $n = 0$ |
| $n$ | octave index / tier | all octave models | dimensionless | octaves are bands $01$–$99$; $n = 1$ is the binary CMOS tier [@mendez2026cmosProtonic] |
| $d$ | digit (0–9) | digit × octave filing | dimensionless | coarse bins labelling kinds of pattern [@mendez2026digitsMaster] |
| $81$ | precision register width | `catalog_size` | digits | per-octave digit precision of the master register |
| $8{,}019$ | holographic catalog size | `catalog_size` | entries | $99 \times 81$; "for dashboards and agent routing, not for measuring magma" [@mendez2026digitsMaster] |
| $k$ | node index; brake constant | `net_zero_balance` context; `transduction_brake` | index; 1/time | $k = 0$ is the zero-octave node ([node k0](../glossary.md#gl:node-k0)) [@mendez2026zeroOctave]; in `transduction_brake` $k$ is the drag rate |
| $2$ | sole-even prime (binary dyad anchor) | `prime_parity_partition`, `unique_address` | dimensionless | the only even prime; anchors the binary layer [@mendez2026primeParity] |
| $p_n$ | the $n$-th prime (odd primes as irreducible sets) | `prime_parity_partition`, `unique_address` | dimensionless | first ten odd primes: 3, 5, 7, 11, 13, 17, 19, 23, 29, 31 |
| $c$ | speed of light, filed as transduction line / viscous floor | `transduction_brake` narrative | 1 (filing) | catalog filing, not relativity retirement [@mendez2026eddyMirror; @mendez2026viscosityLight] |
| $v_0$, $k$ | initial speed, drag rate | `transduction_brake` | speed; 1/time | $v(t) = v_0 e^{-kt}$; $v_0 = 1, k = 1 \Rightarrow v(1) \approx 0.367879$, $v(2) \approx 0.135335$ |
| $h$ | Planck's constant ("Planck's grain") | `metrological_overlap` narrative | J·s | first of the five-constant map [@mendez2026metrologicalOverlap] |
| $\nu_{\mathrm{HI}}$, $\lambda_{\mathrm{HI}}$ | hydrogen-line clock frequency, wavelength | `metrological_overlap` narrative | Hz; length | "hydrogen wave clock" of the five-constant map |
| $m_{\mathrm{catalog}}$ | catalog mass sum | `metrological_overlap` narrative | filing label | explicitly not identified with electron or proton mass |
| $A$, $B$ | label sets | `metrological_overlap` | sets | overlap $= |A \cap B| / |A \cup B|$; $\mathrm{overlap}(\{a,b\},\{b,c\}) = 0.5$ |
| $W(n)$ | metabolic work tensor | macro-protein filing | filing label | organisms filed on band $\theta_{\mathrm{bio}} \in [13,17]$ [@mendez2026macroProtein] |
| $\theta_{\mathrm{bio}}$ | logarithmic length ratio (biology band) | `goldilocks_band` narrative | dimensionless | $[13, 17]$ on the octave ladder |
| $A$, $B$ | label sets | `metrological_overlap` | sets | min-normalized overlap $|A \cap B| / \min(|A|,|B|)$; $\mathrm{overlap}(\{a,b\},\{b,c\}) = 0.5$ |
| $(a, b)$ | prime base, exponents | `unique_address` | lists | injective encoding $\prod p_i^{e_i}$; `unique_address([2,3],[2,1]) = 12` |
| $x$, $e$ | exposure, density parameters | `densification` | dimensionless | $D = D_0 + r\,\ln(1 + x)$; $D_0 = 1, r = 1, x = 4 \Rightarrow 1 + \ln 5 \approx 2.609438$ |
| $r$ | linear filing rate | `lattice_linear_profile` | 1/step | lattice-linear ramp of the PDVSA gateway [@mendez2026pdvsaGateway] |
| $x_i, y_j$ | spatial coordinates | `holographic_rhyme_field`, `xd_yd_combine` | dimensionless | four-pillar interference field; $\mathrm{xD} \pm \mathrm{yD}$ cross-scale summation |
| $x$ | duality argument | `phi_dual` | dimensionless | $\Phi$ duality pair $x \cdot \Phi$ and $x / \Phi$ [@mendez2026protonTheater] |

## Template-Legacy Symbols

The backbone also retains the template's general model functions; their
symbols appear in the format gallery and in the mathematical review.

| Symbol | Name | Appears in | Units | Notes |
| --- | --- | --- | --- | --- |
| *t* | time / independent variable | all dynamic models | s (or chapter unit) | continuous argument of growth/decay models |
| *N* | state quantity / population | `logistic_growth` | dimensionless | state of the modelled quantity |
| *N*₀ | initial state | `logistic_growth`, `exponential_decay` | dimensionless | value at $t = 0$ |
| *r* | intrinsic growth rate | `logistic_growth` | 1/time | drives sigmoid saturation at *K* |
| *K* | carrying capacity | `logistic_growth` | dimensionless | saturation level |
| *λ* (lambda) | decay constant | `exponential_decay`, `half_life` | 1/time | $N(t) = N_0 e^{-\lambda t}$ |
| *t*½ | half-life | `half_life` | time | $t_{1/2} = \ln 2 / \lambda$ |
| *V*max | maximum response | `saturating_response` | response unit | asymptote of the saturating curve |
| *K*ₘ | half-saturation constant | `saturating_response` | input unit | input giving $V_{\max}/2$ |
| *x*, *y* | paired observations | `linear_fit` | data unit | least-squares inputs |
| *m*, *b* | slope, intercept | `linear_fit` | derived | fitted trend parameters |
| *μ*, *σ* | mean, standard deviation | `descriptive_statistics` | data unit | first descriptors of any observable |

## Reused Greek Letters

- **$\Phi$** — always El Gran Sol's Fractal Constant $\approx 1.618$ in corpus
  context. (The Higgs papers also use $\Phi_{\mathrm{Higgs}}$ for the Higgs
  field with $\langle\Phi\rangle \approx 246$ GeV as a PDG literature anchor —
  always subscripted, never confused with the catalog key
  [@mendez2026higgsGate].)
- **$\varphi$** — the Fibonacci ratio family $\varphi_{\mathrm{fib}}(n)$, and
  $\Delta\varphi = \pi/2$ for the planetary-core catalog phase flip
  [@mendez2026planetaryCore].
- **$\lambda$** — decay constant in the legacy models; $\lambda_{\mathrm{HI}}$
  (subscripted) is the hydrogen wavelength in the metrological overlap.

See also: [Appendix C — Mathematical Review](appendix_math_review.md) for the
worked numbers behind these rows.
