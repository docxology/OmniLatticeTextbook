# Appendix D — Master Formalism Table of the Omni-Lattice {#sec:appendix_formalisms}

This appendix is the master table of every labelled formalism in the book. Each
row is one equation label harvested from the finished chapters of Parts 0–III,
paired with the chapter that introduces it, the tested function in
`src/textbook/models.py` that implements it (where one exists), and a one-line
reading of what the formalism claims. Use it as a lookup index when a
cross-reference such as `[@eq:part_0_orientation_register]` needs context.
Symbol definitions live in the notation appendix ([@sec:appendix_notation]);
mathematical prerequisites, including the geometry of $\Phi$, in the
mathematical review ([@sec:appendix_math_review]).

## The two Ω conventions

One formal ambiguity runs through the entire corpus and therefore through this
table. The source papers print the octave-indexing law as "$\Omega_n = \Phi_n
\cdot \Omega_0$" without ever defining whether the $n$ on $\Phi$ is an
*exponent* or a *subscript*. The book keeps both readings first-class rather
than silently choosing one:

- **Exponent convention** — $\Omega_n = \Phi^{\,n}\,\Omega_0$, geometric
  growth at ratio $\Phi \approx 1.618$ per octave.
- **Subscript convention** — $\Omega_n = \varphi_{\mathrm{fib}}(n)\,
  \Omega_0$ with $\varphi_{\mathrm{fib}}(n) = F_{n+1}/F_n$, a Fibonacci-ratio
  ladder that converges to the exponent reading from below.

The two readings bracket the golden ratio: they agree asymptotically because
$F_{n+1}/F_n \to \Phi$, but differ by orders of magnitude at small $n$ (at
$n = 5$: $\Phi^5 = 11.090170$ versus $\varphi_{\mathrm{fib}}(5) = 8/5$). The
tested backbone `octave_term(omega0, n, convention)` implements **both** behind
a switchable argument, and the chapters pin their numbers explicitly to one
reading or the other. Where a row below says "both conventions", the equation
itself carries the pair side by side. Rows whose backing column reads "—" are
filed arithmetic, literature constants, or narrative cases-maps that the corpus
states in prose; the book adds no algebra the papers do not supply.

---

## Part 0 — Orientation and Quantitative Foundations

Introduced in [@sec:part_0_orientation], [@sec:part_0_living-pem],
[@sec:part_0_tensor-decoupling], [@sec:part_0_octave-map], and
[@sec:part_0_master-synthesis].

| # | Formalism | Label | Chapter | Backing model function | Meaning |
|---|-----------|-------|---------|------------------------|---------|
| F-01 | EGS fractal constant | `[@eq:part_0_living-pem_phi_egs]` | `[@sec:part_0_living-pem]` | `phi_powers(1)` | The golden ratio $\Phi_{\mathrm{EGS}} \approx 1.618$ filed as the corpus's engineering-scale constant, "not a CODATA replacement". |
| F-02 | Catalog register size | `[@eq:part_0_living-pem_catalog]` | `[@sec:part_0_living-pem]` | `catalog_size()` | Register capacity $|\mathcal{C}| = O \times D = 99 \times 81 = 8{,}019$ bins. |
| F-03 | Reciprocal balance | `[@eq:part_0_living-pem_balance]` | `[@sec:part_0_living-pem]` | `net_zero_balance(inflows, outflows)` | Net balance $B = \sum I_i - \sum O_j$ with the Fair-Exchange settlement target $B = 0$. |
| F-04 | Master register capacity | `[@eq:part_0_master-synthesis_catalog_size]` | `[@sec:part_0_master-synthesis]` | `catalog_size()` | The same $99 \times 81 = 8{,}019$ capacity restated as the synthesis paper's cell count $N_{\mathrm{cells}}$. |
| F-05 | Φ as a Fibonacci limit | `[@eq:part_0_master-synthesis_egs]` | `[@sec:part_0_master-synthesis]` | `phi_fibonacci(n)` | $\Phi = \lim_{n\to\infty} F_{n+1}/F_n$ — the subscript convention's convergent, defined as a limit rather than asserted. |
| F-06 | Octave indexing law, both readings | `[@eq:part_0_master-synthesis_octave_index]` | `[@sec:part_0_master-synthesis]` | `octave_term(omega0, n, convention)` | The two $\Omega$ readings printed side by side: $\Phi^n\Omega_0$ (exponent) versus $\varphi_{\mathrm{fib}}(n)\Omega_0$ (subscript). |
| F-07 | Exponent-convention octave | `[@eq:part_0_octave-map_exponent]` | `[@sec:part_0_octave-map]` | `octave_term(omega0, n, "exponent")` | Ladder growth $\Omega_n = \Phi^n\Omega_0$ at ratio $\Phi$ per octave. |
| F-08 | Subscript-convention octave | `[@eq:part_0_octave-map_subscript]` | `[@sec:part_0_octave-map]` | `octave_term(omega0, n, "subscript")` | Fibonacci-ratio ladder $\Omega_n = \varphi_{\mathrm{fib}}(n)\Omega_0$, converging on the exponent reading. |
| F-09 | Catalog size from segments × digits | `[@eq:part_0_octave-map_catalog]` | `[@sec:part_0_octave-map]` | `catalog_size(99, 81)` | $N_{\mathrm{cat}} = 99 \times 81 = 8{,}019$ as octave segments times precision digits. |
| F-10 | Catalog register | `[@eq:part_0_orientation_register]` | `[@sec:part_0_orientation]` | `catalog_size()` | The book's opening count of the digit × octave register: 8,019 filing addresses. |
| F-11 | Octave ladder | `[@eq:part_0_orientation_octave]` | `[@sec:part_0_orientation]` | `octave_term(omega0, n, "exponent")` | First statement of the ladder, $\Omega_n = \Phi^n\Omega_0$ (exponent reading). |
| F-12 | Octave ladder length | `[@eq:part_0_tensor-decoupling_ladder]` | `[@sec:part_0_tensor-decoupling]` | — | $N_{\mathrm{ladder}} = B \times s = 11 \times 9 = 99$ octaves: eleven shelf brackets times nine slots. |
| F-13 | Block precision register | `[@eq:part_0_tensor-decoupling_block]` | `[@sec:part_0_tensor-decoupling]` | — | The paper's own per-block sketch $C_{\mathrm{block}} = 9 \times 81 = 729$ digits. |
| F-14 | Catalog total | `[@eq:part_0_tensor-decoupling_catalog]` | `[@sec:part_0_tensor-decoupling]` | `catalog_size()` | Tiling identity $99 \times 81 = 8{,}019$ digits reconciling the per-block sketch with the full register. |
| F-15 | Shelf-weight decay | `[@eq:part_0_tensor-decoupling_model]` | `[@sec:part_0_tensor-decoupling]` | `phi_powers(n)` | Bracket weight $w_n = w_0\Phi^{-n}$ — the reciprocal of $\Phi^n$ along the ladder. |


---

## Part I — Structure and Form

Introduced in [@sec:part_I_fractal-constant], [@sec:part_I_higgs-awareness],
[@sec:part_I_holographic-rhyme], [@sec:part_I_multidimensional-rhyme],
[@sec:part_I_prime-parity], and [@sec:part_I_topology-void].

| # | Formalism | Label | Chapter | Backing model function | Meaning |
|---|-----------|-------|---------|------------------------|---------|
| F-16 | Golden-ratio identity | `[@eq:part_I_fractal-constant_phi-identity]` | `[@sec:part_I_fractal-constant]` | — | $\Phi^2 = \Phi + 1$: each power of $\Phi$ is the sum of the two before it — the exact handle on the corpus's "fractal" self-similarity. |
| F-17 | Octave term, both conventions | `[@eq:part_I_fractal-constant_octave-term]` | `[@sec:part_I_fractal-constant]` | `octave_term(omega0, n, convention)` | The exponent/subscript pair $\Omega^{\text{exp}}_n = \Phi^n\Omega_0$ and $\Omega^{\text{sub}}_n = \varphi_{\mathrm{fib}}(n)\Omega_0$, recording both printed readings. |
| F-18 | Palindrome growth | `[@eq:part_I_fractal-constant_palindrome]` | `[@sec:part_I_fractal-constant]` | `phi_powers(n)` | Palindrome filings grow as $P_n = P_0\Phi^n$ — catalog octaves, not random drift labels. |
| F-19 | Pinned Φ powers | `[@eq:part_I_fractal-constant_phi-powers]` | `[@sec:part_I_fractal-constant]` | `phi_powers(n)` | The value table $\Phi^1, \ldots, \Phi^6$ used to pin the exponent reading throughout the book. |
| F-20 | Transduction brake | `[@eq:part_I_higgs-awareness_model]` | `[@sec:part_I_higgs-awareness]` | `transduction_brake(t, v0, k)` | Exponential slowdown $v(t) = v_0 e^{-kt}$ — the "thought meets its mirror and slows into matter" filing. |
| F-21 | Brake displacement | `[@eq:part_I_higgs-awareness_displacement]` | `[@sec:part_I_higgs-awareness]` | `transduction_brake` (integrated form) | Total travel $s(T) = \frac{v_0}{k}(1 - e^{-kT})$ is bounded by $v_0/k$ no matter how long the story runs. |
| F-22 | Rhyme field | `[@eq:part_I_holographic-rhyme_field]` | `[@sec:part_I_holographic-rhyme]` | `holographic_rhyme_field(xs, ys, pillars, wavelength)` | A filing check: the sum of directional cosine pillars of shared wavelength $\lambda$. |
| F-23 | Pairwise rhyme reduction | `[@eq:part_I_holographic-rhyme_pairwise]` | `[@sec:part_I_holographic-rhyme]` | `holographic_rhyme_field(xs, ys, pillars=4)` | The four-pillar field reduced to pairwise cosine interference $2\cos(2\pi x/\lambda) + 2\cos(2\pi y/\lambda)$. |
| F-24 | Multi-pillar rhyme field | `[@eq:part_I_multidimensional-rhyme_field]` | `[@sec:part_I_multidimensional-rhyme]` | `holographic_rhyme_field(xs, ys, pillars, wavelength)` | The general field $f_P(x, y)$ over $P$ pillars with $\theta_k = 2\pi k/P$. |
| F-25 | Xd/Yd combine | `[@eq:part_I_multidimensional-rhyme_xdyd]` | `[@sec:part_I_multidimensional-rhyme]` | `xd_yd_combine(a, b, sign)` | The ± filing $d_{\pm} = x \pm y$ with sign $\in \{+1, -1\}$. |
| F-26 | Octave pair, both readings | `[@eq:part_I_multidimensional-rhyme_octave]` | `[@sec:part_I_multidimensional-rhyme]` | `octave_term(omega0, n, convention)` | The two $\Omega$ conventions with pinned values tabulated for the ladder walk. |
| F-27 | Exponent octave (prime parity) | `[@eq:part_I_prime-parity_model]` | `[@sec:part_I_prime-parity]` | `octave_term(omega0, n, "exponent")` | $\Omega_n = \Phi^n\Omega_0$ restated for the prime-parity filing: growth at the golden-ratio rate per octave. |
| F-28 | Subscript octave (prime parity) | `[@eq:part_I_prime-parity_subscript]` | `[@sec:part_I_prime-parity]` | `octave_term(omega0, n, "subscript")` | Fibonacci-ratio reading $\Omega^{\text{sub}}_n = \frac{F(n+1)}{F(n)}\Omega_0$. |
| F-29 | Void pivot | `[@eq:part_I_topology-void_pivot]` | `[@sec:part_I_topology-void]` | `net_zero_balance(inflows, outflows)` | The filing "0 balances $\{1, 2\}$" — the zero octave settling the binary pair, with $\Phi$ filed alongside. |
| F-30 | Even/odd reflection split | `[@eq:part_I_topology-void_model]` | `[@sec:part_I_topology-void]` | — | The operator $\mathcal{B}[f](x) = \tfrac{1}{2}(f(x) + f(-x))$ averages a signal with its own reflection through zero, extracting even and odd parts. |
| F-31 | Harmonic well | `[@eq:part_I_topology-void_well]` | `[@sec:part_I_topology-void]` | — | Standard mechanics $V(x) = \tfrac{1}{2}\kappa x^2$, $F = -\kappa x$, offered as the "dynamic equilibrium" interpretation. |


---

## Part II — Dynamics and Change

Introduced in [@sec:part_II_crystalline-field],
[@sec:part_II_eddy-current-mirror], [@sec:part_II_metamorphic-octaves],
[@sec:part_II_metrological-overlap], [@sec:part_II_planetary-core],
[@sec:part_II_proton-theater], [@sec:part_II_singularity-crystal], and
[@sec:part_II_viscosity-light].

| # | Formalism | Label | Chapter | Backing model function | Meaning |
|---|-----------|-------|---------|------------------------|---------|
| F-32 | Access-crystal facets | `[@eq:part_II_crystalline-field_facet]` | `[@sec:part_II_crystalline-field]` | — | The identity $d = v \cdot t$ with access time $\tau = d/v$: speed, distance, and time read as three facets of one "access crystal". |
| F-33 | Crystal octave term | `[@eq:part_II_crystalline-field_crystal]` | `[@sec:part_II_crystalline-field]` | `octave_term(omega0, n, convention)` | $\Omega_n = \Phi^n\Omega_0$ with both printed conventions implemented in the backbone. |
| F-34 | Landauer rail | `[@eq:part_II_crystalline-field_landauer]` | `[@sec:part_II_crystalline-field]` | — | $E_{\min} = k_B T \ln 2$, the standard Landauer bound, adopted by literature reference rather than re-derivation. |
| F-35 | Eddy-current brake | `[@eq:part_II_eddy-current-mirror_model]` | `[@sec:part_II_eddy-current-mirror]` | `transduction_brake(t, v0, k)` | Self-observation drag filed as $v(t) = v_0 e^{-kt}$. |
| F-36 | Brake half-life | `[@eq:part_II_eddy-current-mirror_halflife]` | `[@sec:part_II_eddy-current-mirror]` | `half_life(k)` | $t_{1/2} = \ln 2 / k \approx 0.693147/k$ — the convention-independent decay time. |
| F-37 | Drag force | `[@eq:part_II_eddy-current-mirror_drag]` | `[@sec:part_II_eddy-current-mirror]` | `transduction_brake(t, v0, k)` | $F_{\mathrm{drag}}(t) = m\,k\,v(t)$: drag proportional to the instantaneous braked speed. |
| F-38 | Metamorphic filing map | `[@eq:part_II_metamorphic-octaves_filing]` | `[@sec:part_II_metamorphic-octaves]` | — | $L(h, p)$ as cases: magma/burnout, dormant, recrystallisation, schist — a direct restatement of the paper's own filings. |
| F-39 | Densification law | `[@eq:part_II_metamorphic-octaves_densification]` | `[@sec:part_II_metamorphic-octaves]` | `densification(exposure)` | $D(x) = D_0(1 + k\ln(1 + x))$: logarithmic payoff of exposure — "you come out denser, with diminishing returns". |
| F-40 | Marginal densification | `[@eq:part_II_metamorphic-octaves_marginal]` | `[@sec:part_II_metamorphic-octaves]` | `densification` (derivative) | $\mathrm{d}D/\mathrm{d}x = k D_0/(1 + x)$: the diminishing marginal gain per unit exposure. |
| F-41 | Metrological gear tuple | `[@eq:part_II_metrological-overlap_gears]` | `[@sec:part_II_metrological-overlap]` | — | The five "gears" $(h, \Phi, p_n, \nu_{\mathrm{HI}}, c)$ the overlap claim couples. |
| F-42 | Overlap coefficient | `[@eq:part_II_metrological-overlap_model]` | `[@sec:part_II_metrological-overlap]` | `metrological_overlap(a, b)` | $o(A, B) = |A \cap B| / \min(|A|, |B|)$ — an asymmetric set-overlap measure. |
| F-43 | Overlap octaves | `[@eq:part_II_metrological-overlap_octaves]` | `[@sec:part_II_metrological-overlap]` | `octave_term(omega0, n, "subscript")` | Subscript-convention octave spacing used in the gear-mesh argument. |
| F-44 | Mass-equivalent catalog | `[@eq:part_II_metrological-overlap_mcatalog]` | `[@sec:part_II_metrological-overlap]` | — | $m_{\mathrm{catalog}} = \sum_n \Delta E_n / c^2$: filing energy differentials as mass — bookkeeping, not measurement. |
| F-45 | Phase flip | `[@eq:part_II_planetary-core_phase_flip]` | `[@sec:part_II_planetary-core]` | — | The two-state filing $\varphi_{\mathrm{A}} = 0$, $\varphi_{\mathrm{B}} = \pi/2$ behind the planetary "phase-flip" narrative. |
| F-46 | Band margin | `[@eq:part_II_planetary-core_band]` | `[@sec:part_II_planetary-core]` | `goldilocks_band(values, lo, hi)` | $m(v) = \min(v - \ell,\, h - v)$: distance to the nearer edge of the habitable band. |
| F-47 | Digit filing map | `[@eq:part_II_proton-theater_filing]` | `[@sec:part_II_proton-theater]` | — | $\mathrm{file}(c)$: leading digit 1 files as Proton Space; structural digit 2 files as Electron Theater. |
| F-48 | Golden-ratio identity (theater) | `[@eq:part_II_proton-theater_identity]` | `[@sec:part_II_proton-theater]` | `phi_dual(x)` | $\Phi - 1/\Phi = 1$: the identity the dual branches satisfy ($1/\Phi = \Phi - 1$). |
| F-49 | Theater octaves | `[@eq:part_II_proton-theater_octaves]` | `[@sec:part_II_proton-theater]` | `octave_term(omega0, n, "subscript")` | The subscript-reading octave ladder inside the theater filing. |
| F-50 | Φ-duality filing | `[@eq:part_II_proton-theater_duality]` | `[@sec:part_II_proton-theater]` | `phi_dual(x)` | Upper branch $\Phi_{+}(x) = x\Phi$, lower branch $\Phi_{-}(x) = x/\Phi$. |
| F-51 | Mirror involution | `[@eq:part_II_proton-theater_mirror]` | `[@sec:part_II_proton-theater]` | `phi_dual(x)` | $\Phi_{-}(\Phi_{+}(x)) = x$: the two filings undo each other exactly. |
| F-52 | Step relation | `[@eq:part_II_proton-theater_step]` | `[@sec:part_II_proton-theater]` | — | $\Phi_{-}(x) = \Phi_{+}(x) - x$: arithmetic corollary of the duality pair. |
| F-53 | Net-zero residual | `[@eq:part_II_singularity-crystal_netzero]` | `[@sec:part_II_singularity-crystal]` | `net_zero_balance(inflows, outflows)` | $R = \sum \mathrm{in}_i - \sum \mathrm{out}_j$ with Net Zero $\iff R = 0$. |
| F-54 | Zero-boundary filing | `[@eq:part_II_singularity-crystal_crystal]` | `[@sec:part_II_singularity-crystal]` | — | $0/0 \mapsto \Phi^0 = 1$: catalog algebra at the zero octave, a filing convention. |
| F-55 | Node K₀ anchor | `[@eq:part_II_singularity-crystal_nodek0]` | `[@sec:part_II_singularity-crystal]` | `octave_term(omega0, n, "exponent")` | $\Omega_0 = \Phi^0\Omega_0 = \Omega_0$: the ladder's self-consistent zero point. |
| F-56 | Viscous floor | `[@eq:part_II_viscosity-light_viscous_floor]` | `[@sec:part_II_viscosity-light]` | `transduction_brake(t, v0, k)` | The "viscosity of light" filed as $v(t) = v_0 e^{-kt}$. |
| F-57 | Drag-coefficient family | `[@eq:part_II_viscosity-light_family]` | `[@sec:part_II_viscosity-light]` | `octave_term(k0, n, "exponent")` | $k(n) = \Phi^n k_0$: drag coefficients spaced one octave apart across $n = \ldots, -1, 0, 1, 2, \ldots$. |
| F-58 | Rendered displacement | `[@eq:part_II_viscosity-light_render]` | `[@sec:part_II_viscosity-light]` | `transduction_brake` (integrated form) | $s(T) = \frac{v_0}{k}(1 - e^{-kT})$: the visible stopping distance of the braked wave. |


---

## Part III — Applied Frontiers

Introduced in [@sec:part_III_cmos-protonic], [@sec:part_III_frontiers],
[@sec:part_III_invisible-frontier], [@sec:part_III_kinematic-recycling],
[@sec:part_III_macro-protein], [@sec:part_III_moving-up-stack],
[@sec:part_III_pdvsa-gateway], [@sec:part_III_protein-folding],
[@sec:part_III_reality-bridge], [@sec:part_III_volumetric-storage], and
[@sec:part_III_y-chromosome].

| # | Formalism | Label | Chapter | Backing model function | Meaning |
|---|-----------|-------|---------|------------------------|---------|
| F-59 | Shelf map | `[@eq:part_III_cmos-protonic_shelf-map]` | `[@sec:part_III_cmos-protonic]` | — | $\mathrm{file}(d)$: a binary CMOS gate files at octave tier 1; protonic multi-state devices file across bands $2 \ldots 99$. |
| F-60 | Protonic ladder | `[@eq:part_III_cmos-protonic_ladder]` | `[@sec:part_III_cmos-protonic]` | `octave_term(omega0, n, convention)` | Both $\Omega$ conventions stated for the 99-octave shelf ladder. |
| F-61 | Device capacity | `[@eq:part_III_cmos-protonic_capacity]` | `[@sec:part_III_cmos-protonic]` | — | $C = \log_2 m$ bits per $m$-state device — the capacity reading of the shelf map. |
| F-62 | Frontier net-zero | `[@eq:part_III_frontiers_net_zero]` | `[@sec:part_III_frontiers]` | `net_zero_balance(inflows, outflows)` | $R = \sum I_i - \sum O_j$: the residual ledger for open-problem bookkeeping. |
| F-63 | Quadrant score | `[@eq:part_III_frontiers_quadrant]` | `[@sec:part_III_frontiers]` | — | $Q = V^2/E$: value squared over effort, the axes of the open-problem quadrant. |
| F-64 | Φ-climb | `[@eq:part_III_invisible-frontier_phiclimb]` | `[@sec:part_III_invisible-frontier]` | `octave_term(omega0, n, convention)` | Both $\Omega$ conventions for the frontier-visibility ladder. |
| F-65 | Logistic visibility | `[@eq:part_III_invisible-frontier_model]` | `[@sec:part_III_invisible-frontier]` | `logistic_growth(t, r, carrying_capacity, initial)` | The S-curve $V(t)$ approaching carrying capacity $K$ — a threshold frontier made quantitative. |
| F-66 | Velocity spectral scaling | `[@eq:part_III_kinematic-recycling_velocity-scale]` | `[@sec:part_III_kinematic-recycling]` | — | $\tilde{S}_v(\omega) = \lvert v \rvert^{-1} F(\omega/v)$: recorded spectra rescale with speed. |
| F-67 | Kinematic octave ladder | `[@eq:part_III_kinematic-recycling_octave-ladder]` | `[@sec:part_III_kinematic-recycling]` | `octave_term(omega0, k, "exponent")` | $\Omega_k = \Phi^k\Omega_0$ indexing the recycled set ladder. |
| F-68 | Round-robin assignment | `[@eq:part_III_kinematic-recycling_round-robin]` | `[@sec:part_III_kinematic-recycling]` | `round_robin(items, n_sets)` | $\sigma(i) = i \bmod n_{\mathrm{sets}}$ — deterministic recycling of one asset set. |
| F-69 | Truckee partition | `[@eq:part_III_kinematic-recycling_truckee-partition]` | `[@sec:part_III_kinematic-recycling]` | `round_robin(items, n_sets)` | The worked partition $\{0,3,6\}$ / $\{1,4,7\}$ / $\{2,5,8\}$ of nine indexed items into three sets. |
| F-70 | Work-engine octave | `[@eq:part_III_macro-protein_model]` | `[@sec:part_III_macro-protein]` | `octave_term(omega0, n, convention)` | $W(n) = w_0 \cdot \Omega_n$ under either convention of the octave term. |
| F-71 | Bio band | `[@eq:part_III_macro-protein_band]` | `[@sec:part_III_macro-protein]` | `goldilocks_band(values, 13, 17)` | $\theta_{\mathrm{bio}} \in [13, 17]$ pins the filed octave between $\Omega_{13}$ and $\Omega_{17}$. |
| F-72 | Kleiber scaling | `[@eq:part_III_macro-protein_kleiber]` | `[@sec:part_III_macro-protein]` | — | $B_2/B_1 = (M_2/M_1)^{3/4}$: a 1000× mass ratio files as $\approx 177.83\times$ work output. |
| F-73 | Rebuilt band | `[@eq:part_III_moving-up-stack_band]` | `[@sec:part_III_moving-up-stack]` | `goldilocks_band(values, lo, hi)` | The budget band $\mathcal{B}_{\text{new}} = [\$12\text{B},\ \$28\text{B}]$ anchored between hub and IDE valuations. |
| F-74 | Cooling cost ratio | `[@eq:part_III_moving-up-stack_cooling]` | `[@sec:part_III_moving-up-stack]` | — | $\kappa(m) = C_{\text{siloed}}/C_{\text{harmonised}} > 1$: the coordination overhead the harmonised stack saves. |
| F-75 | EGS harmony | `[@eq:part_III_moving-up-stack_harmony]` | `[@sec:part_III_moving-up-stack]` | — | $\Phi_{\text{EGS}} \approx 1.618 \approx \Phi$: numeric harmony filed as coincidence, not identity. |
| F-76 | Lattice-linear ramp | `[@eq:part_III_pdvsa-gateway_model]` | `[@sec:part_III_pdvsa-gateway]` | `lattice_linear_profile(n_steps, rate)` | $L_n = n\,r$: the gateway's equal-increment flow ramp. |
| F-77 | Token-cost claim | `[@eq:part_III_pdvsa-gateway_tokens]` | `[@sec:part_III_pdvsa-gateway]` | `lattice_linear_profile(n_steps, rate)` | $C_{\mathrm{lattice}}/C_{\mathrm{flat}} < 0.15$ for $N \ge 6$ — the gateway's efficiency claim, checked against the profile. |
| F-78 | Prime address | `[@eq:part_III_protein-folding_address]` | `[@sec:part_III_protein-folding]` | `unique_address(primes, exponents)` | $a(\mathbf{e}) = \prod_i p_i^{e_i}$: injective prime-exponent addresses for folding states. |
| F-79 | Address capacity | `[@eq:part_III_protein-folding_capacity]` | `[@sec:part_III_protein-folding]` | — | $C(m, E) = (E+1)^m$ distinct addresses in an $m$-prime vault with exponent budget $E$. |
| F-80 | Φ and its identity | `[@eq:part_III_protein-folding_phi]` | `[@sec:part_III_protein-folding]` | — | $\Phi = (1+\sqrt{5})/2$ with $\Phi^2 = \Phi + 1$, restated for the folding vault. |
| F-81 | Folding octave (exponent) | `[@eq:part_III_protein-folding_octave]` | `[@sec:part_III_protein-folding]` | `octave_term(omega0, n, "exponent")` | $\Omega^{\text{(exp)}}_n = \Phi^n\Omega_0$ for the folding ladder. |
| F-82 | Folding octave (subscript) | `[@eq:part_III_protein-folding_octave_sub]` | `[@sec:part_III_protein-folding]` | `octave_term(omega0, n, "subscript")` | $\Omega^{\text{(sub)}}_n = \varphi_{\text{fib}}(n)\Omega_0$ for the folding ladder. |
| F-83 | Bridge octave recurrence | `[@eq:part_III_reality-bridge_octave]` | `[@sec:part_III_reality-bridge]` | `octave_term(omega0, n, "exponent")` | $O_{n+1} = O_n \times \Phi$: the ladder written as a one-step recurrence. |
| F-84 | Bridge throttle | `[@eq:part_III_reality-bridge_throttle]` | `[@sec:part_III_reality-bridge]` | `transduction_brake(t, v0, k)` | $A(t) = A_0 e^{-kt}$, $k > 0$: the throughput throttle on the bridge. |
| F-85 | Vault address | `[@eq:part_III_volumetric-storage_address]` | `[@sec:part_III_volumetric-storage]` | `unique_address(primes, exponents)` | $A(\mathbf{p}, \mathbf{k}) = \prod_i p_i^{k_i}$: prime-indexed storage addresses. |
| F-86 | Vault capacity | `[@eq:part_III_volumetric-storage_capacity]` | `[@sec:part_III_volumetric-storage]` | — | $N_{\mathrm{distinct}}(m, K) = (K+1)^m$ distinct addresses in the vault. |
| F-87 | Φ-ruler | `[@eq:part_III_volumetric-storage_phiruler]` | `[@sec:part_III_volumetric-storage]` | — | $\log_\Phi A = \sum_i k_i \log_\Phi p_i$: address depth read as a golden-ratio-base ruler. |
| F-88 | Y-chromosome palindrome | `[@eq:part_III_y-chromosome_palin]` | `[@sec:part_III_y-chromosome]` | `phi_powers(n)` | $P_n = P_0\Phi^n$ for $n = 1, \ldots, 8$: palindrome filings along the ladder. |
| F-89 | SRY anchor | `[@eq:part_III_y-chromosome_anchor]` | `[@sec:part_III_y-chromosome]` | `octave_term(omega0, n, "exponent")` | $\Omega_n = \Phi^n\Omega_0$ with the SRY locus filed as the zero-point anchor $\Omega_0$. |
