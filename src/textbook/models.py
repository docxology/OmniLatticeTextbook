"""Domain-neutral computational backbone — the worked formalisms.

These are the tested, reusable functions a textbook's figures and worked
examples should call (thin-orchestrator rule: scripts never reimplement maths).
They are deliberately generic — logistic growth, saturating response,
exponential decay, a linear model, and descriptive statistics — so any
discipline can reuse them or replace them with subject-specific equivalents.

Corpus-facing formalisms — the golden-ratio octave stack, catalog size, prime
parity, holographic rhyme, metrological overlap, and friends — back the book's
worked equations; each docstring names the corpus paper it backs.

All functions are pure and deterministic: same inputs -> same outputs.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray

PHI: float = (1.0 + math.sqrt(5.0)) / 2.0
r"""Golden-ratio constant $\Phi \approx 1.618$ — El Gran Sol's Fractal constant [mendez2026masterSynthesis]."""


def logistic_growth(t: ArrayLike, *, r: float, carrying_capacity: float, initial: float) -> NDArray[np.float64]:
    r"""Logistic growth $N(t) = K / (1 + ((K - N_0)/N_0)\,e^{-rt})$.

    Args:
        t: Time points.
        r: Intrinsic growth rate (``r > 0``).
        carrying_capacity: Saturation level ``K`` (``K > 0``).
        initial: Initial value ``N_0`` (``0 < N_0 <= K``).

    Returns:
        Population/quantity at each time in ``t``.
    """
    if r <= 0:
        raise ValueError("r must be positive")
    if carrying_capacity <= 0:
        raise ValueError("carrying_capacity must be positive")
    if not 0 < initial <= carrying_capacity:
        raise ValueError("initial must satisfy 0 < initial <= carrying_capacity")
    t_arr = np.asarray(t, dtype=np.float64)
    k = carrying_capacity
    a = (k - initial) / initial
    return (k / (1.0 + a * np.exp(-r * t_arr))).astype(np.float64)


def saturating_response(
    x: ArrayLike, *, maximum: float, half_saturation: float, hill: float = 1.0
) -> NDArray[np.float64]:
    r"""Hill / Michaelis-Menten-style saturating response.

    $y = y_{max}\, x^{n} / (k^{n} + x^{n})$ with Hill coefficient ``n``.

    Args:
        x: Non-negative input values.
        maximum: Asymptotic maximum ``y_max`` (``> 0``).
        half_saturation: Input at half-maximal response ``k`` (``> 0``).
        hill: Hill coefficient ``n`` (``> 0``); 1.0 is Michaelis-Menten.
    """
    if maximum <= 0:
        raise ValueError("maximum must be positive")
    if half_saturation <= 0:
        raise ValueError("half_saturation must be positive")
    if hill <= 0:
        raise ValueError("hill must be positive")
    x_arr = np.asarray(x, dtype=np.float64)
    if np.any(x_arr < 0):
        raise ValueError("x must be non-negative")
    xn = np.power(x_arr, hill)
    result = maximum * xn / (np.power(half_saturation, hill) + xn)
    return np.asarray(result, dtype=np.float64)


def exponential_decay(t: ArrayLike, *, initial: float, rate: float) -> NDArray[np.float64]:
    r"""Exponential decay $y = y_0\, e^{-\lambda t}$."""
    if initial < 0:
        raise ValueError("initial must be non-negative")
    if rate < 0:
        raise ValueError("rate must be non-negative")
    t_arr = np.asarray(t, dtype=np.float64)
    return initial * np.exp(-rate * t_arr)


def half_life(rate: float) -> float:
    r"""Half-life $t_{1/2} = \ln 2 / \lambda$ for a decay ``rate`` (``> 0``)."""
    if rate <= 0:
        raise ValueError("rate must be positive")
    return float(np.log(2.0) / rate)


@dataclass(frozen=True)
class LinearFit:
    """Result of an ordinary least-squares line fit."""

    slope: float
    intercept: float
    r_squared: float

    def predict(self, x: ArrayLike) -> NDArray[np.float64]:
        """Evaluate the fitted line at ``x``."""
        return self.slope * np.asarray(x, dtype=np.float64) + self.intercept


def linear_fit(x: ArrayLike, y: ArrayLike) -> LinearFit:
    """Ordinary least-squares fit of ``y = slope * x + intercept``.

    Returns a :class:`LinearFit` carrying slope, intercept, and the coefficient
    of determination ``r_squared``.
    """
    x_arr = np.asarray(x, dtype=np.float64)
    y_arr = np.asarray(y, dtype=np.float64)
    if x_arr.shape != y_arr.shape:
        raise ValueError("x and y must have the same shape")
    if x_arr.size < 2:
        raise ValueError("need at least two points")
    slope, intercept = np.polyfit(x_arr, y_arr, 1)
    predicted = slope * x_arr + intercept
    ss_res = float(np.sum((y_arr - predicted) ** 2))
    ss_tot = float(np.sum((y_arr - np.mean(y_arr)) ** 2))
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return LinearFit(slope=float(slope), intercept=float(intercept), r_squared=r_squared)


def descriptive_statistics(values: ArrayLike) -> dict[str, float]:
    """Return mean, standard deviation (population), min, max, and count."""
    arr = np.asarray(values, dtype=np.float64)
    if arr.size == 0:
        raise ValueError("values must be non-empty")
    return {
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "count": float(arr.size),
    }


def normalize_unit_interval(values: ArrayLike) -> NDArray[np.float64]:
    """Min-max scale ``values`` into ``[0, 1]``.

    A constant input maps to all-zeros (degenerate range handled explicitly).
    """
    arr = np.asarray(values, dtype=np.float64)
    if arr.size == 0:
        raise ValueError("values must be non-empty")
    lo = float(np.min(arr))
    hi = float(np.max(arr))
    if hi == lo:
        return np.zeros_like(arr)
    return ((arr - lo) / (hi - lo)).astype(np.float64)


def phi_powers(n: int) -> NDArray[np.float64]:
    r"""Return $[\Phi^1, \ldots, \Phi^n]$ for the golden-ratio constant ``PHI``.

    Backs the golden-ratio-keyed digits × octaves master register [mendez2026digitsMaster]; structural model, not a physical claim.

    Args:
        n: Highest power to emit (``n >= 0``; 0 yields an empty array).

    Returns:
        Array of the ``n`` powers ``PHI**1`` through ``PHI**n``.

    Raises:
        ValueError: If ``n`` is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return (PHI ** np.arange(1, n + 1, dtype=np.float64)).astype(np.float64)


def phi_fibonacci(n: int) -> float:
    r"""Return $F(n+1)/F(n)$, the Fibonacci ratio converging to $\Phi$.

    Backs the golden-ratio key of the digits × octaves map [mendez2026digitsMaster]; structural model, not a physical claim.

    Args:
        n: Index with ``n >= 1``; the sequence is $F(0) = 0$, $F(1) = 1$, iterated without recursion.

    Returns:
        The ratio $F(n+1)/F(n)$ (1.0 for ``n == 1``, alternating around $\Phi$ thereafter).

    Raises:
        ValueError: If ``n < 1``.
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    lower, upper = 0, 1
    for _ in range(n):
        lower, upper = upper, lower + upper
    return upper / lower


def octave_term(omega0: float, n: int, convention: str = "exponent") -> float:
    r"""Compute the octave term $\Omega_n$ relative to the base octave $\Omega_0$.

    Backs the octave recursion formalism [mendez2026primeParity]; structural model, not a physical claim.

    The corpus prints "$\Omega_n = \Phi_n \cdot \Omega_0$" with the $\Phi$ exponent/subscript
    notation ambiguous, so both readings are first-class: ``"exponent"`` gives
    $\Omega_n = \Phi^n \Omega_0$ and ``"subscript"`` gives $\Omega_n$ = ``phi_fibonacci(n)`` $\cdot\,\Omega_0$.

    Args:
        omega0: Base octave term $\Omega_0$.
        n: Octave index (``n >= 1`` for the subscript convention).
        convention: ``"exponent"`` or ``"subscript"``.

    Returns:
        $\Omega_n$ under the chosen convention.

    Raises:
        ValueError: If ``convention`` is neither ``"exponent"`` nor ``"subscript"``, or the
            index is out of range for the subscript convention.
    """
    if convention == "exponent":
        return float(PHI**n * omega0)
    if convention == "subscript":
        return float(phi_fibonacci(n) * omega0)
    raise ValueError("convention must be 'exponent' or 'subscript'")


def catalog_size(octaves: int = 99, precision_digits: int = 81) -> int:
    """Return the holographic catalog size as the product ``octaves * precision_digits``.

    Backs the holographic catalog size formalism (99 × 81 = 8,019) [mendez2026digitsMaster]; structural model, not a physical claim.

    Args:
        octaves: Number of octave shelves (``> 0``).
        precision_digits: Width of the precision register (``> 0``).

    Returns:
        The catalog size in catalog entries.

    Raises:
        ValueError: If either factor is not positive.
    """
    if octaves <= 0:
        raise ValueError("octaves must be positive")
    if precision_digits <= 0:
        raise ValueError("precision_digits must be positive")
    return octaves * precision_digits


def prime_parity_partition(limit: int) -> dict[str, list[int]]:
    """Partition the primes below ``limit`` into the sole-even prime 2 and the odd primes.

    Backs the sole-even parity of 2 / odd-primes-as-irreducible-sets formalism [mendez2026primeParity]; structural model, not a physical claim.

    Args:
        limit: Exclusive upper bound of the primes listed.

    Returns:
        ``{"sole_even": [2] when 2 < limit, "odd": [odd primes < limit]}``, via a simple sieve.

    Raises:
        ValueError: If ``limit`` is negative.
    """
    if limit < 0:
        raise ValueError("limit must be non-negative")
    if limit < 3:
        return {"sole_even": [], "odd": []}
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for prime in range(2, math.isqrt(limit - 1) + 1):
        if sieve[prime]:
            sieve[prime * prime :: prime] = [False] * len(range(prime * prime, limit, prime))
    return {"sole_even": [2], "odd": [p for p in range(3, limit, 2) if sieve[p]]}


def holographic_rhyme_field(
    xs: ArrayLike, ys: ArrayLike, pillars: int = 4, wavelength: float = 1.0
) -> NDArray[np.float64]:
    r"""Sum plane-wave cosines over ``pillars`` evenly spaced directions.

    $f(x, y) = \sum_{k=0}^{P-1} \cos\!\left(2\pi\,(x\cos\theta_k + y\sin\theta_k)/\lambda\right)$
    with $\theta_k = 2\pi k / P$.

    Backs the four-pillar holographic rhyme filing [mendez2026holographicRhyme]; structural model, not a physical claim.

    Args:
        xs: x coordinates, broadcastable against ``ys``.
        ys: y coordinates, broadcastable against ``xs``.
        pillars: Number of directional pillars $P$ (``> 0``).
        wavelength: Plane-wave wavelength $\lambda$ (``> 0``).

    Returns:
        The summed interference field with the broadcast shape of ``xs`` and ``ys``.

    Raises:
        ValueError: If ``pillars`` or ``wavelength`` is not positive.
    """
    if pillars <= 0:
        raise ValueError("pillars must be positive")
    if wavelength <= 0:
        raise ValueError("wavelength must be positive")
    x_arr = np.asarray(xs, dtype=np.float64)
    y_arr = np.asarray(ys, dtype=np.float64)
    field = np.zeros(np.broadcast_shapes(x_arr.shape, y_arr.shape), dtype=np.float64)
    for k in range(pillars):
        theta = 2.0 * np.pi * k / pillars
        field += np.cos(2.0 * np.pi * (x_arr * np.cos(theta) + y_arr * np.sin(theta)) / wavelength)
    return field


def xd_yd_combine(a: int, b: int, sign: int = 1) -> int:
    """Combine two dimension indices as ``a + b`` (``sign=1``) or ``a - b`` (``sign=-1``).

    Backs the xD±yD cross-scale summation engine [mendez2026mdRhyme]; structural model, not a physical claim.

    Args:
        a: Left dimension index.
        b: Right dimension index.
        sign: ``1`` for summation, ``-1`` for subtraction.

    Returns:
        The combined dimension index.

    Raises:
        ValueError: If ``sign`` is neither ``1`` nor ``-1``.
    """
    if sign == 1:
        return a + b
    if sign == -1:
        return a - b
    raise ValueError("sign must be 1 or -1")


def transduction_brake(t: ArrayLike, v0: float = 1.0, k: float = 1.0) -> NDArray[np.float64]:
    r"""Exponential braking $v(t) = v_0\,e^{-kt}$ — the eddy-mirror / viscosity damping analogy.

    Backs the transduction-line braking analogy (eddy-current mirror) [mendez2026eddyMirror]; structural model, not a physical claim.

    Args:
        t: Time points.
        v0: Initial speed $v_0$.
        k: Braking rate $k$ (``> 0``).

    Returns:
        Speed at each time in ``t``.

    Raises:
        ValueError: If ``k`` is not positive.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    t_arr = np.asarray(t, dtype=np.float64)
    return (v0 * np.exp(-k * t_arr)).astype(np.float64)


def metrological_overlap(a: set, b: set) -> float:
    r"""Return the min-normalized overlap $|A \cap B| / \min(|A|, |B|)$ of two sets.

    Backs the five-constant metrological overlap solver [mendez2026metrologicalOverlap]; structural model, not a physical claim.

    Args:
        a: First set.
        b: Second set.

    Returns:
        The overlap fraction in ``[0, 1]``; ``0.0`` when either set is empty.
    """
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def net_zero_balance(inflows: dict[str, float], outflows: dict[str, float]) -> float:
    r"""Return the residual $\sum$ inflows $-\sum$ outflows; the ledger nets to zero iff it is 0.

    Backs the Net Zero field-cancellation equilibrium filing [mendez2026singularityCrystal]; structural model, not a physical claim.

    Args:
        inflows: Named inflow amounts.
        outflows: Named outflow amounts.

    Returns:
        The balance residual (``0.0`` for a net-zero ledger, e.g. empty books).
    """
    return float(sum(inflows.values()) - sum(outflows.values()))


def lattice_linear_profile(n_steps: int, rate: float) -> NDArray[np.float64]:
    """Return the linear ramp ``rate * [1 .. n_steps]`` of the lattice-linear gateway.

    Backs the EGS Lattice-Linear Gateway console profile [mendez2026pdvsaGateway]; structural model, not a physical claim.

    Args:
        n_steps: Number of ramp steps (``n >= 0``; 0 yields an empty array).
        rate: Per-step increment.

    Returns:
        Array ``[rate, 2*rate, ..., n_steps*rate]``.

    Raises:
        ValueError: If ``n_steps`` is negative.
    """
    if n_steps < 0:
        raise ValueError("n_steps must be non-negative")
    return rate * np.arange(1, n_steps + 1, dtype=np.float64)


def goldilocks_band(values: ArrayLike, lo: float, hi: float) -> NDArray[np.bool_]:
    """Return a boolean mask marking ``lo <= v <= hi`` — the "just right" band.

    Backs the Goldilocks equilibrium band filing [mendez2026planetaryCore]; structural model, not a physical claim.

    Args:
        values: Candidate values.
        lo: Inclusive lower bound.
        hi: Inclusive upper bound.

    Returns:
        Boolean mask, ``True`` where the value sits inside the inclusive band.

    Raises:
        ValueError: If ``lo > hi``.
    """
    if lo > hi:
        raise ValueError("lo must not exceed hi")
    arr = np.asarray(values)
    return (arr >= lo) & (arr <= hi)


def unique_address(primes: list[int], exponents: list[int]) -> int:
    r"""Return the fundamental-theorem address $\prod_i p_i^{e_i}$.

    Backs the prime-indexed volumetric vault addressing grammar [mendez2026volumetricStorage]; structural model, not a physical claim.

    Args:
        primes: Prime channels (each ``> 0``).
        exponents: Non-negative integer exponents aligned with ``primes``.

    Returns:
        The unique integer address (``1`` for empty channel lists).

    Raises:
        ValueError: If the lists differ in length, a prime is not positive, or an exponent is negative.
    """
    if len(primes) != len(exponents):
        raise ValueError("primes and exponents must have equal length")
    if any(p <= 0 for p in primes):
        raise ValueError("primes must be positive")
    if any(e < 0 for e in exponents):
        raise ValueError("exponents must be non-negative")
    address = 1
    for prime, exponent in zip(primes, exponents):
        address *= prime**exponent
    return address


def round_robin(items: list, n_sets: int) -> list[list]:
    """Partition ``items`` deterministically round-robin into ``n_sets`` ordered lists.

    Backs the kinematic set-recycling filing (one set, many states) [mendez2026setRecycling]; structural model, not a physical claim.

    Args:
        items: Items to distribute; input order is preserved within each set.
        n_sets: Number of sets (``>= 1``).

    Returns:
        Exactly ``n_sets`` lists; item ``i`` lands in set ``i % n_sets``.

    Raises:
        ValueError: If ``n_sets`` is not positive.
    """
    if n_sets <= 0:
        raise ValueError("n_sets must be positive")
    sets: list[list] = [[] for _ in range(n_sets)]
    for index, item in enumerate(items):
        sets[index % n_sets].append(item)
    return sets


def densification(exposure: ArrayLike, density0: float = 1.0, rate: float = 1.0) -> NDArray[np.float64]:
    r"""Logarithmic densification $d = d_0 + r\,\ln(1 + \text{exposure})$.

    Backs the metamorphic densification filing (heat plus constraint leaves you denser) [mendez2026metamorphic]; structural model, not a physical claim.

    Args:
        exposure: Exposure amount(s); ``>= -1`` elementwise for real-valued output.
        density0: Initial density $d_0$.
        rate: Densification rate $r$.

    Returns:
        Density after each exposure.
    """
    exposure_arr = np.asarray(exposure, dtype=np.float64)
    return density0 + rate * np.log1p(exposure_arr)


def phi_dual(x: float) -> tuple[float, float]:
    r"""Return the structural duality pair $(x\Phi,\; x/\Phi)$.

    Backs the golden-key $\Phi$ duality of the singularity crystal filing [mendez2026singularityCrystal]; structural model, not a physical claim.

    Args:
        x: Value to split into its $\Phi$-multiple and $\Phi$-fraction parts.

    Returns:
        Tuple ``(x * PHI, x / PHI)``.
    """
    return x * PHI, x / PHI


__all__ = [
    "LinearFit",
    "PHI",
    "catalog_size",
    "densification",
    "descriptive_statistics",
    "exponential_decay",
    "goldilocks_band",
    "half_life",
    "holographic_rhyme_field",
    "lattice_linear_profile",
    "linear_fit",
    "logistic_growth",
    "metrological_overlap",
    "net_zero_balance",
    "normalize_unit_interval",
    "octave_term",
    "phi_dual",
    "phi_fibonacci",
    "phi_powers",
    "prime_parity_partition",
    "round_robin",
    "saturating_response",
    "transduction_brake",
    "unique_address",
    "xd_yd_combine",
]
