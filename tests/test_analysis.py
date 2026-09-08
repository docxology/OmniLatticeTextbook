"""Tests for the source-owned worked-example analysis."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from textbook.analysis import (
    DECAY_PARAMETERS,
    LOGISTIC_PARAMETERS,
    build_worked_model_summary,
    load_case_study_observations,
)

from textbook.models import (
    PHI,
    catalog_size,
    densification,
    goldilocks_band,
    holographic_rhyme_field,
    lattice_linear_profile,
    metrological_overlap,
    net_zero_balance,
    octave_term,
    phi_dual,
    phi_fibonacci,
    phi_powers,
    prime_parity_partition,
    round_robin,
    transduction_brake,
    unique_address,
    xd_yd_combine,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET = PROJECT_ROOT / "docs" / "manuscript" / "assets" / "data" / "sample_dataset.csv"


def test_worked_model_summary_retains_inputs_and_outputs() -> None:
    summary = build_worked_model_summary(DATASET)

    assert summary["logistic_growth"]["parameters"] == LOGISTIC_PARAMETERS
    assert summary["exponential_decay"]["parameters"] == DECAY_PARAMETERS
    assert summary["logistic_growth"]["N"][0] == LOGISTIC_PARAMETERS["initial"]
    assert summary["logistic_growth"]["N"][-1] < LOGISTIC_PARAMETERS["carrying_capacity"]
    assert summary["exponential_decay"]["y"][0] == DECAY_PARAMETERS["initial"]
    assert summary["case_study"]["condition_means"] == pytest.approx(
        {
            "control": 2.2,
            "treatment_low": 3.5,
            "treatment_high": 4.95,
        }
    )
    assert round(summary["case_study"]["linear_fit"]["slope"], 3) == 1.375
    assert round(summary["case_study"]["linear_fit"]["r_squared"], 3) == 0.999
    assert round(summary["case_study"]["extrapolation"]["linear_prediction"], 1) == 6.3


def test_worked_model_summary_is_deterministic() -> None:
    assert build_worked_model_summary(DATASET) == build_worked_model_summary(DATASET)


def test_worked_model_summary_accepts_portable_source_provenance() -> None:
    summary = build_worked_model_summary(DATASET, source_label="docs/manuscript/assets/data/sample_dataset.csv")

    assert summary["case_study"]["source"] == "docs/manuscript/assets/data/sample_dataset.csv"


def test_case_study_observations_retain_measurements_and_uncertainty() -> None:
    observations = load_case_study_observations(DATASET)

    assert len(observations) == 6
    assert observations[0].condition == "control"
    assert observations[0].replicate == 1
    assert observations[0].measurement == pytest.approx(2.10)
    assert observations[0].standard_error == pytest.approx(0.20)


@pytest.mark.parametrize(
    "contents, message",
    [
        ("condition,replicate,measurement\ncontrol,1,2.1\n", "missing required columns"),
        (
            "condition,replicate,measurement,standard_error\ncontrol,bad,2.1,0.2\n",
            "invalid numeric data",
        ),
        ("condition,replicate,measurement,standard_error\n,1,2.1,0.2\n", "blank condition"),
        (
            "condition,replicate,measurement,standard_error\ncontrol,0,2.1,0.2\n",
            "non-positive replicate",
        ),
        (
            "condition,replicate,measurement,standard_error\ncontrol,1,2.1,-0.2\n",
            "invalid measurement or standard error",
        ),
        (
            "condition,replicate,measurement,standard_error\ncontrol,1,2.1,0.2\ncontrol,1,2.3,0.1\n",
            "duplicate condition/replicate",
        ),
        ("condition,replicate,measurement,standard_error\n", "contains no observations"),
    ],
)
def test_case_study_observations_fail_closed(tmp_path: Path, contents: str, message: str) -> None:
    dataset = tmp_path / "case_study.csv"
    dataset.write_text(contents, encoding="utf-8")

    with pytest.raises(ValueError, match=message):
        load_case_study_observations(dataset)


# --- Corpus formalism models (src/textbook/models.py) ------------------------


def test_phi_constant_matches_closed_form() -> None:
    assert PHI == pytest.approx(1.618033988749895)
    assert PHI == pytest.approx((1.0 + 5.0**0.5) / 2.0)


def test_phi_powers_match_hand_checked_powers() -> None:
    # Φ² = Φ + 1, Φ³ = 2Φ + 1, Φ⁴ = 3Φ + 2 — the defining identity of Φ.
    np.testing.assert_allclose(
        phi_powers(4), [PHI, PHI + 1.0, 2.0 * PHI + 1.0, 3.0 * PHI + 2.0], rtol=0, atol=1e-12
    )
    np.testing.assert_allclose(
        phi_powers(10),
        [
            1.618034,
            2.618034,
            4.236068,
            6.854102,
            11.090170,
            17.944272,
            29.034442,
            46.978714,
            76.013156,
            122.991869,
        ],
        rtol=0,
        atol=5e-7,
    )
    assert phi_powers(0).shape == (0,)
    with pytest.raises(ValueError, match="non-negative"):
        phi_powers(-1)


def test_phi_fibonacci_matches_consecutive_fibonacci_ratios() -> None:
    assert phi_fibonacci(1) == 1.0
    assert phi_fibonacci(5) == pytest.approx(8 / 5)
    assert phi_fibonacci(10) == pytest.approx(89 / 55)
    with pytest.raises(ValueError, match="at least 1"):
        phi_fibonacci(0)


def test_octave_term_supports_both_notation_conventions() -> None:
    assert octave_term(1.0, 5) == pytest.approx(5.0 * PHI + 3.0)  # Φ⁵ = 5Φ + 3
    assert octave_term(2.0, 5) == pytest.approx(2.0 * (5.0 * PHI + 3.0))
    assert octave_term(2.0, 5, convention="subscript") == pytest.approx(3.2)  # F(6)/F(5) = 8/5
    assert octave_term(7.0, 0) == 7.0
    with pytest.raises(ValueError, match="convention"):
        octave_term(1.0, 1, convention="rms")


def test_catalog_size_defaults_to_8019() -> None:
    assert catalog_size() == 8019
    assert catalog_size(octaves=10, precision_digits=10) == 100
    with pytest.raises(ValueError, match="positive"):
        catalog_size(octaves=0)


def test_prime_parity_partition_splits_sole_even_from_odd_primes() -> None:
    assert prime_parity_partition(20) == {"sole_even": [2], "odd": [3, 5, 7, 11, 13, 17, 19]}
    assert prime_parity_partition(3) == {"sole_even": [2], "odd": []}
    assert prime_parity_partition(2) == {"sole_even": [], "odd": []}
    with pytest.raises(ValueError, match="non-negative"):
        prime_parity_partition(-1)


def test_holographic_rhyme_field_constructive_at_origin() -> None:
    field = holographic_rhyme_field([0.0, 0.5], [0.0, 0.0])
    assert field[0] == pytest.approx(4.0)  # all four pillars in phase at the origin
    assert field[1] == pytest.approx(0.0)  # pairwise cancellation half a wavelength out
    grid = holographic_rhyme_field([[0.0]], [[0.0]], pillars=7, wavelength=2.0)
    assert grid.shape == (1, 1)
    assert grid[0, 0] == pytest.approx(7.0)
    with pytest.raises(ValueError, match="pillars"):
        holographic_rhyme_field([0.0], [0.0], pillars=0)


def test_xd_yd_combine_sum_difference_and_rejection() -> None:
    assert xd_yd_combine(5, 3) == 8
    assert xd_yd_combine(5, 3, sign=-1) == 2
    with pytest.raises(ValueError, match="sign must be"):
        xd_yd_combine(5, 3, sign=0)
    with pytest.raises(ValueError, match="sign must be"):
        xd_yd_combine(5, 3, sign=2)


def test_transduction_brake_decays_exponentially() -> None:
    np.testing.assert_allclose(
        transduction_brake([0.0, 1.0, 2.0], v0=1.0, k=1.0),
        [1.0, 0.367879, 0.135335],
        rtol=0,
        atol=5e-7,
    )
    assert transduction_brake([0.0], v0=3.0, k=2.0)[0] == pytest.approx(3.0)
    with pytest.raises(ValueError, match="positive"):
        transduction_brake([0.0], k=0.0)


def test_metrological_overlap_normalizes_by_the_smaller_set() -> None:
    assert metrological_overlap({"a", "b"}, {"b", "c"}) == pytest.approx(0.5)
    assert metrological_overlap({"a", "b"}, {"a", "c", "d"}) == pytest.approx(0.5)
    assert metrological_overlap({"a", "b"}, {"a", "b"}) == 1.0
    assert metrological_overlap({"x"}, {"y"}) == 0.0
    assert metrological_overlap(set(), {"y"}) == 0.0


def test_net_zero_balance_flags_only_exact_ledger_residuals() -> None:
    assert net_zero_balance({"sales": 100.0, "grant": 50.0}, {"rent": 90.0, "fees": 60.0}) == 0.0
    assert net_zero_balance({"sales": 5.0}, {"rent": 3.0}) == pytest.approx(2.0)
    assert net_zero_balance({}, {}) == 0.0


def test_lattice_linear_profile_is_a_linear_ramp() -> None:
    np.testing.assert_allclose(lattice_linear_profile(4, 0.5), [0.5, 1.0, 1.5, 2.0])
    assert lattice_linear_profile(0, 0.5).shape == (0,)
    with pytest.raises(ValueError, match="non-negative"):
        lattice_linear_profile(-1, 0.5)


def test_goldilocks_band_boundaries_are_inclusive() -> None:
    mask = goldilocks_band([0.0, 0.5, 1.0, 1.5], 0.5, 1.0)
    assert mask.tolist() == [False, True, True, False]
    assert mask.dtype == np.bool_
    with pytest.raises(ValueError, match="lo must not exceed hi"):
        goldilocks_band([0.0], 1.0, 0.0)


def test_unique_address_multiplies_prime_powers() -> None:
    assert unique_address([2, 3], [2, 1]) == 12
    assert unique_address([5], [3]) == 125
    assert unique_address([], []) == 1
    with pytest.raises(ValueError, match="equal length"):
        unique_address([2, 3], [2])
    with pytest.raises(ValueError, match="positive"):
        unique_address([0, 3], [1, 1])
    with pytest.raises(ValueError, match="non-negative"):
        unique_address([2, 3], [1, -1])


def test_round_robin_partition_is_deterministic() -> None:
    first = round_robin(list(range(7)), 3)
    assert first == [[0, 3, 6], [1, 4], [2, 5]]
    assert round_robin(list(range(7)), 3) == first
    assert round_robin(["a", "b"], 4) == [["a"], ["b"], [], []]
    with pytest.raises(ValueError, match="positive"):
        round_robin([1], 0)


def test_densification_grows_logarithmically() -> None:
    assert densification(0.0) == pytest.approx(1.0)
    assert densification(1.0) == pytest.approx(1.693147, abs=1e-6)  # 1 + ln 2
    np.testing.assert_allclose(
        densification([0.0, 3.0], density0=0.5, rate=2.0), [0.5, 3.272589], rtol=0, atol=5e-7
    )


def test_phi_dual_splits_into_phi_multiple_and_fraction() -> None:
    upper, lower = phi_dual(2.0)
    assert upper == pytest.approx(3.236068, abs=1e-6)  # 2Φ
    assert lower == pytest.approx(1.236068, abs=1e-6)  # 2/Φ = 2(Φ − 1)
    assert upper * lower == pytest.approx(4.0)  # (xΦ)(x/Φ) = x²


def test_corpus_models_are_deterministic() -> None:
    assert phi_powers(6).tolist() == phi_powers(6).tolist()
    assert holographic_rhyme_field([0.1, 0.2], [0.3, 0.4]).tolist() == holographic_rhyme_field(
        [0.1, 0.2], [0.3, 0.4]
    ).tolist()
    assert round_robin(list("abcde"), 2) == round_robin(list("abcde"), 2)
