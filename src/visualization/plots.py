"""Figure generators — every figure the manuscript references is produced here.

* **Worked-model figures** visualise the tested functions in
  :mod:`textbook.models` (the formalisms readers should trust and reuse).
* **Chapter figures** — one bespoke, deterministic figure per chapter, named
  ``<part_id>_<stem>.png`` to match the ``\\includegraphics`` path emitted by
  ``textbook.content.scaffold_chapter``. Every chapter in the canonical figure
  plan (``research/AUTHORING_BRIEF.md`` §6) has a shared, parametrized builder
  below; unknown chapters fall back to a neutral placeholder so the filename
  contract keeps cross-references valid.
* **Unit-intro maps** — one deterministic part-overview figure per unit
  opening, named ``<part_id>_unit-intro.png`` (see :func:`generate_intro_figures`).
* **Cover art** — the deterministic book cover referenced by ``book.cover``
  in ``docs/manuscript/config.yaml``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from textbook import models
from textbook.config import iter_chapters, load_config
from textbook_logging import get_logger
from textbook_paths import MANUSCRIPT

from ._scaffold import BLUE, GRAY, GREEN, ORANGE, PURPLE, SERIES, VERMILLION, new_figure, save_figure

logger = get_logger(__name__)


def plot_logistic_growth(output_dir: Path) -> Path:
    """Logistic growth curve from ``models.logistic_growth``."""
    t = np.linspace(0, 12, 200)
    fig, ax = new_figure()
    for color, r in zip(SERIES, (0.4, 0.7, 1.1)):
        y = models.logistic_growth(t, r=r, carrying_capacity=100.0, initial=5.0)
        ax.plot(t, y, color=color, label=f"r = {r}")
    ax.axhline(100.0, color=GRAY, linestyle="--", linewidth=0.8, label="K = 100")
    ax.set_xlabel("time (model units)")
    ax.set_ylabel("quantity N(t)")
    ax.set_title("Logistic growth")
    ax.legend()
    return save_figure(fig, output_dir, "logistic_growth")


def plot_saturating_response(output_dir: Path) -> Path:
    """Hill-style saturating response from ``models.saturating_response``."""
    x = np.linspace(0, 10, 200)
    fig, ax = new_figure()
    for color, n in zip(SERIES, (1.0, 2.0, 4.0)):
        y = models.saturating_response(x, maximum=1.0, half_saturation=3.0, hill=n)
        ax.plot(x, y, color=color, label=f"n = {n}")
    ax.set_xlabel("input x")
    ax.set_ylabel("response y")
    ax.set_title("Saturating (Hill) response")
    ax.legend()
    return save_figure(fig, output_dir, "saturating_response")


def plot_exponential_decay(output_dir: Path) -> Path:
    """Exponential decay with annotated half-life."""
    t = np.linspace(0, 10, 200)
    rate = 0.5
    y = models.exponential_decay(t, initial=100.0, rate=rate)
    fig, ax = new_figure()
    ax.plot(t, y, color=BLUE, label="decay")
    t_half = models.half_life(rate)
    ax.axvline(t_half, color=ORANGE, linestyle="--", linewidth=0.9, label=f"t½ = {t_half:.2f}")
    ax.set_xlabel("time")
    ax.set_ylabel("amount")
    ax.set_title("Exponential decay")
    ax.legend()
    return save_figure(fig, output_dir, "exponential_decay")


def plot_linear_fit(output_dir: Path) -> Path:
    """Scatter with an OLS line from ``models.linear_fit`` (deterministic data)."""
    x = np.linspace(0, 10, 25)
    # Deterministic pseudo-noise (no RNG) so the figure is byte-stable.
    noise = np.sin(x * 1.7) * 1.5
    y = 2.0 * x + 3.0 + noise
    fit = models.linear_fit(x, y)
    fig, ax = new_figure()
    ax.scatter(x, y, color=GREEN, s=18, label="data")
    ax.plot(x, fit.predict(x), color=BLUE, label=f"fit: y={fit.slope:.2f}x+{fit.intercept:.2f}")
    ax.set_xlabel("x (predictor)")
    ax.set_ylabel("y (response)")
    ax.set_title(f"Linear fit (R² = {fit.r_squared:.3f})")
    ax.legend()
    return save_figure(fig, output_dir, "linear_fit")

def placeholder_overview(title: str, output_dir: Path, filename: str) -> Path:
    """A neutral, titled placeholder figure for a not-yet-illustrated chapter."""
    fig, ax = new_figure(width=6.4, height=3.6)
    ax.axis("off")
    ax.text(
        0.5,
        0.62,
        title,
        ha="center",
        va="center",
        fontsize=15,
        weight="bold",
        wrap=True,
    )
    ax.text(
        0.5,
        0.34,
        "Placeholder overview figure — replace via src/visualization/plots.py",
        ha="center",
        va="center",
        fontsize=9,
        color=GRAY,
    )
    fig.patch.set_edgecolor(BLUE)
    fig.patch.set_linewidth(2)
    return save_figure(fig, output_dir, filename)


def cover_art(output_dir: Path, *, title: str = "The Template Textbook", subtitle: str = "") -> Path:
    """Render a deterministic cover image: nested modular blocks + title.

    The nesting (book -> parts -> chapters -> sections) visually states the
    template's organising idea. Deterministic, so the cover is byte-stable.
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    fig, ax = plt.subplots(figsize=(6.4, 8.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12.5)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    # Nested rounded rectangles, largest (book) to smallest (section).
    palette = [BLUE, GREEN, ORANGE, "#8E44AD"]
    for i, color in enumerate(palette):
        inset = i * 0.9
        box = FancyBboxPatch(
            (1.0 + inset, 2.2 + inset),
            8.0 - 2 * inset,
            6.5 - 2 * inset,
            boxstyle="round,pad=0.1,rounding_size=0.25",
            linewidth=2.2,
            edgecolor=color,
            facecolor="none",
        )
        ax.add_patch(box)
    labels = ["Book", "Part", "Chapter", "Section"]
    for i, (label, color) in enumerate(zip(labels, palette)):
        ax.text(1.35 + i * 0.9, 8.35 - i * 0.9, label, color=color, fontsize=10, weight="bold")

    ax.text(5, 11.4, title, ha="center", va="center", fontsize=21, weight="bold")
    if subtitle:
        ax.text(5, 10.5, subtitle, ha="center", va="center", fontsize=10, color=GRAY, wrap=True)
    ax.text(5, 1.1, "A modular, fillable scaffold", ha="center", va="center", fontsize=11, style="italic", color=GRAY)
    return save_figure(fig, output_dir, "template_textbook_cover")




# ---------------------------------------------------------------------------
# Canonical chapter figures (research/AUTHORING_BRIEF.md §6)
#
# One deterministic builder per enabled chapter, keyed by ``(part_id, stem)``.
# Builders are thin compositions over a few shared helpers plus the tested
# functions in :mod:`textbook.models`; none of them consume randomness, so
# every rendered PNG is byte-stable for a fixed matplotlib version.
# ---------------------------------------------------------------------------


def _heatmap_figure(
    matrix,
    *,
    title,
    xlabel,
    ylabel,
    cmap="viridis",
    vmin=None,
    vmax=None,
    colorbar_label="value",
):
    """Shared parametrized heatmap frame: imshow + colorbar on the house style."""
    fig, ax = new_figure()
    image = ax.imshow(matrix, origin="lower", cmap=cmap, vmin=vmin, vmax=vmax, aspect="auto")
    fig.colorbar(image, ax=ax, label=colorbar_label)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(False)
    return fig, ax


def _style_axis(ax) -> None:
    """Apply the house grid/spine style of :func:`new_figure` to an extra axes."""
    ax.grid(True, linestyle=":", linewidth=0.6, color=GRAY, alpha=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def _two_figure(width: float = 7.2, height: float = 4.0, width_ratios=(3.0, 2.0)):
    """Return a main + secondary two-panel composite on the house style."""
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(width, height), gridspec_kw={"width_ratios": width_ratios})
    for ax in axes:
        _style_axis(ax)
    return fig, axes


def _corner_note(ax, text: str, *, loc: str = "upper left") -> None:
    """Pin a small gray honesty/annotation note inside the axes frame."""
    x, ha = (0.02, "left") if loc.endswith("left") else (0.98, "right")
    y, va = (0.95, "top") if loc.startswith("upper") else (0.05, "bottom")
    ax.text(x, y, text, transform=ax.transAxes, fontsize=8, color=GRAY, ha=ha, va=va)


def plot_engine_shelf_timeline(output_dir: Path) -> Path:
    """part_0_orientation — engine-shelf timeline: 24 papers by shelf number."""
    shelves = np.arange(1, 25)
    fig, (ax, side) = _two_figure(width=7.2, height=3.4, width_ratios=(2.6, 1.0))
    ax.vlines(shelves, 0.0, 1.0, color=GRAY, linewidth=1.0)
    ax.scatter(shelves, np.ones(shelves.shape), color=BLUE, s=32, zorder=3)
    ax.set_xlim(0, 25)
    ax.set_ylim(0, 1.35)
    ax.set_xticks(shelves)
    ax.set_yticks([])
    ax.set_xlabel("engine-shelf number")
    ax.set_ylabel("papers")
    ax.set_title("Engine-shelf timeline: 24 papers positioned by shelf number")
    _corner_note(ax, "one engine paper per shelf — the corpus is complete")
    # Secondary panel: cumulative coverage over the shelf sequence.
    side.step(shelves, shelves, where="post", color=ORANGE, linewidth=1.8)
    side.scatter(shelves, shelves, color=BLUE, s=12, zorder=3)
    side.set_xticks((1, 8, 16, 24))
    side.set_yticks((1, 8, 16, 24))
    side.set_xlabel("shelves traversed")
    side.set_ylabel("cumulative papers")
    side.set_title("Cumulative coverage", fontsize=10)
    return save_figure(fig, output_dir, "part_0_orientation")


def plot_living_pem_ladder(output_dir: Path) -> Path:
    """part_0_living-pem — PEM engineering lifecycle as a staged ladder plot."""
    stages = np.arange(1, 6)
    fig, (ax, side) = _two_figure()
    ax.step(stages, stages, where="post", color=BLUE, linewidth=2.0, label="lifecycle path")
    ax.scatter(stages, stages, color=ORANGE, s=30, zorder=3, label="stage node")
    for stage in stages:
        ax.annotate(f"stage {stage}", (stage, stage), textcoords="offset points", xytext=(4, 6), fontsize=8)
    ax.set_xticks(stages)
    ax.set_yticks(stages)
    ax.set_xlabel("lifecycle step")
    ax.set_ylabel("stage")
    ax.set_title("Living PEM engineering lifecycle as a staged ladder")
    ax.legend(loc="lower right", fontsize=8)
    _corner_note(ax, "each rung is reviewed before the next opens")
    # Secondary panel: schematic per-stage review effort (deterministic, illustrative only).
    effort = 0.5 * stages + 0.5
    side.bar(stages, effort, color=GREEN, width=0.6)
    side.set_xticks(stages)
    side.set_xlabel("lifecycle step")
    side.set_ylabel("review effort (schematic)")
    side.set_title("Per-stage review effort", fontsize=10)
    return save_figure(fig, output_dir, "part_0_living-pem")


def plot_register_bins_heatmap(output_dir: Path) -> Path:
    """part_0_tensor-decoupling — digit × octave filing heatmap (9 × 99 register bins)."""
    digits = np.arange(1, 10)
    octaves = np.arange(1, 100)
    bins = (digits[:, None] * octaves[None, :]) % 9
    fig, ax = _heatmap_figure(
        bins,
        title="Digit × octave filing: 9 × 99 register bins (residue-0 bins outlined)",
        xlabel="octave index (1–99)",
        ylabel="digit drawer (1–9)",
    )
    ax.set_xticks((0, 24, 49, 74, 98), labels=("1", "25", "50", "75", "99"))
    ax.set_yticks(np.arange(9), labels=[str(d) for d in digits])
    rows, cols = np.nonzero(bins == 0)
    ax.scatter(cols, rows, marker="s", s=9, facecolors="none", edgecolors=VERMILLION, linewidths=0.7)
    _corner_note(ax, f"9 × 99 bins filed → catalog_size(99, 81) = {models.catalog_size():,}", loc="upper right")
    return save_figure(fig, output_dir, "part_0_tensor-decoupling")


def plot_crosslink_adjacency_heatmap(output_dir: Path) -> Path:
    """part_0_master-synthesis — cross-link adjacency heatmap of the 24 shelf papers."""
    papers = 24
    index = np.arange(papers)
    gap = np.abs(index[:, None] - index[None, :])
    ring = np.minimum(gap, papers - gap)
    adjacency = (ring <= 2).astype(float)
    fig, (ax, side) = _two_figure(width=7.2, height=4.0, width_ratios=(2.0, 1.0))
    image = ax.imshow(adjacency, origin="lower", cmap="Blues", vmin=0.0, vmax=1.0, aspect="auto")
    fig.colorbar(image, ax=ax, label="cross-link")
    ax.set_title("Cross-link adjacency of the 24 shelf papers (schematic ring order)")
    ax.set_xlabel("paper index (shelf order)")
    ax.set_ylabel("paper index (shelf order)")
    ax.grid(False)
    ax.set_xticks((0, 5, 11, 17, 23), labels=("1", "6", "12", "18", "24"))
    ax.set_yticks((0, 5, 11, 17, 23), labels=("1", "6", "12", "18", "24"))
    _corner_note(ax, "cross-link when ring distance ≤ 2 (diagonal = self-link)", loc="upper right")
    # Secondary panel: cross-link degree per paper (±2 ring neighbours, self excluded).
    degree = adjacency.sum(axis=1) - 1.0
    side.bar(index, degree, color=BLUE, width=0.8)
    side.set_ylim(0, 5)
    side.set_xlabel("paper index (shelf order)")
    side.set_ylabel("cross-link degree")
    side.set_title("Degree per paper", fontsize=10)
    return save_figure(fig, output_dir, "part_0_master-synthesis")


def plot_octave_ladder(output_dir: Path) -> Path:
    """part_0_octave-map — 99-octave ladder with Φ-spaced band boundaries."""
    indices = np.arange(1, 100)  # φ_fibonacci(0) is undefined — the ladder starts at octave 1
    exponent = np.array([models.octave_term(1.0, int(n), "exponent") for n in indices])
    subscript = np.array([models.octave_term(1.0, int(n), "subscript") for n in indices])
    fib = np.array([models.phi_fibonacci(int(n)) for n in indices])
    fig, (ax, side) = _two_figure(width=7.2, height=4.6)
    ax.semilogy(indices, exponent, color=BLUE, linewidth=1.8, label=r"$\Omega_n = \Phi^n\,\Omega_0$ (exponent)")
    ax.semilogy(indices, subscript, color=ORANGE, linewidth=1.4, label=r"$\Omega_n = \varphi_{fib}(n)\,\Omega_0$ (subscript)")
    ax.set_xlabel("octave index n")
    ax.set_ylabel(r"band boundary $\Omega_n$ (log scale)")
    ax.set_title("99-octave ladder with Φ-spaced band boundaries")
    ax.legend(fontsize=7)
    _corner_note(ax, "exponent convention grows geometrically; subscript follows Fibonacci")
    # Fibonacci-ratio overlay panel: F(n+1)/F(n) converging to Φ.
    side.plot(indices, fib, color=GREEN, linewidth=1.6, label=r"$\varphi_{fib}(n) = F(n+1)/F(n)$")
    side.axhline(models.PHI, color=VERMILLION, linestyle="--", linewidth=1.0, label=f"Φ = {models.PHI:.6f}")
    side.set_ylim(0.9, 2.2)
    side.set_xlabel("octave index n")
    side.set_ylabel("Fibonacci ratio")
    side.set_title("Fibonacci-ratio overlay → Φ", fontsize=10)
    side.legend(fontsize=7, loc="center right")
    return save_figure(fig, output_dir, "part_0_octave-map")


def plot_phi_growth_fibonacci(output_dir: Path) -> Path:
    """part_I_fractal-constant — Φ^n growth on log scale with Fibonacci ratios overlay."""
    count = 15
    ks = np.arange(1, count + 1)
    fib = np.array([models.phi_fibonacci(int(k)) for k in ks])
    fig, (ax, side) = _two_figure()
    ax.semilogy(ks, models.phi_powers(count), "o-", color=BLUE, label=r"$\Phi^n$")
    ax.semilogy(ks, fib, "s--", color=ORANGE, label="$F(n+1)/F(n)$")
    ax.set_xlabel("n")
    ax.set_ylabel("value (log scale)")
    ax.set_title("Fractal-constant growth: Φ powers with Fibonacci ratios")
    ax.legend()
    _corner_note(ax, "the Fibonacci ratio shadows Φⁿ within a factor of two")
    # Secondary panel: relative convergence error of the Fibonacci ratio to Φ.
    error = np.abs(fib - models.PHI) / models.PHI
    side.semilogy(ks, error, "s-", color=ORANGE)
    side.set_xlabel("n")
    side.set_ylabel(r"relative error $|\varphi_{fib}(n) - \Phi| / \Phi$")
    side.set_title("Fibonacci-ratio convergence error", fontsize=10)
    _corner_note(side, f"target Φ = {models.PHI:.6f}")
    return save_figure(fig, output_dir, "part_I_fractal-constant")


def plot_prime_parity_numberline(output_dir: Path) -> Path:
    """part_I_prime-parity — primes on a number line, sole-even anchor vs odd classes."""
    partition = models.prime_parity_partition(100)
    odd = np.asarray(partition["odd"], dtype=float)
    fig, (ax, side) = _two_figure(width=7.2, height=3.2, width_ratios=(2.6, 1.0))
    ax.axhline(0.0, color=GRAY, linewidth=0.8)
    ax.scatter(odd, np.zeros(odd.shape), color=BLUE, s=28, zorder=3, label="odd primes")
    ax.scatter((2.0,), (0.0,), color=VERMILLION, marker="D", s=70, zorder=4, label="sole-even anchor (2)")
    ax.annotate(
        "sole-even anchor p = 2",
        (2.0, 0.0),
        textcoords="offset points",
        xytext=(6, 10),
        fontsize=8,
        color=VERMILLION,
    )
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.6, 0.6)
    ax.set_yticks([])
    ax.set_xlabel("number line")
    ax.set_title("Prime-parity partition below 100")
    ax.legend(loc="center right", fontsize=8)
    _corner_note(ax, "2 is the only even prime — every other prime is odd", loc="lower left")
    # Secondary panel: odd primes per decade.
    decade = np.arange(0, 100, 10)
    counts = np.array([int(((odd >= lo) & (odd < lo + 10.0)).sum()) for lo in decade], dtype=float)
    side.bar(decade + 5.0, counts, width=8.0, color=BLUE, alpha=0.85)
    side.set_xticks(decade + 5.0, labels=[str(lo) for lo in decade])
    side.set_xlabel("decade")
    side.set_ylabel("odd primes")
    side.set_title("Odd primes per decade", fontsize=10)
    return save_figure(fig, output_dir, "part_I_prime-parity")


def plot_holographic_rhyme_contours(output_dir: Path) -> Path:
    """part_I_holographic-rhyme — four-pillar interference field contour map."""
    coords = np.linspace(-3.0, 3.0, 241)
    field = models.holographic_rhyme_field(coords[:, None], coords[None, :], pillars=4, wavelength=1.0)
    fig, ax = new_figure()
    image = ax.contourf(coords, coords, field, levels=21, cmap="viridis")
    ax.contour(coords, coords, field, levels=9, colors="white", linewidths=0.4, alpha=0.5)
    fig.colorbar(image, ax=ax, label="interference amplitude")
    peak_row, peak_col = np.unravel_index(int(np.argmax(field)), field.shape)
    ax.scatter(
        (coords[peak_col],),
        (coords[peak_row],),
        color=VERMILLION,
        marker="*",
        s=60,
        zorder=4,
        label="constructive peak",
    )
    ax.set_xlabel("pillar-field x-coordinate")
    ax.set_ylabel("pillar-field y-coordinate")
    ax.set_title("Four-pillar holographic rhyme interference field")
    ax.legend(loc="upper right", fontsize=8)
    _corner_note(ax, "pillars = 4 · wavelength = 1", loc="lower left")
    return save_figure(fig, output_dir, "part_I_holographic-rhyme")


def plot_xd_yd_interference(output_dir: Path) -> Path:
    """part_I_multidimensional-rhyme — xD±yD combined interference contours."""
    coords = np.linspace(-3.0, 3.0, 241)
    grid_x, grid_y = np.meshgrid(coords, coords)
    summed = np.cos(2.0 * np.pi * (grid_x + grid_y))
    differenced = np.cos(2.0 * np.pi * (grid_x - grid_y))
    fig, ax = new_figure()
    image = ax.contourf(grid_x, grid_y, summed + differenced, levels=21, cmap="viridis")
    fig.colorbar(image, ax=ax, label="combined amplitude")
    ax.contour(grid_x, grid_y, summed, levels=7, colors=(ORANGE,), linewidths=0.8)
    ax.contour(grid_x, grid_y, differenced, levels=7, colors=(VERMILLION,), linewidths=0.8, linestyles="dashed")
    ax.set_xlabel("xD coordinate")
    ax.set_ylabel("yD coordinate")
    ax.set_title("xD±yD combined interference contours (solid: x+y, dashed: x−y)")
    from matplotlib.lines import Line2D

    ax.legend(
        handles=(
            Line2D((0,), (0,), color=ORANGE, label="sum branch: cos 2π(x + y)"),
            Line2D((0,), (0,), color=VERMILLION, linestyle="--", label="difference branch: cos 2π(x − y)"),
        ),
        loc="upper right",
        fontsize=8,
    )
    return save_figure(fig, output_dir, "part_I_multidimensional-rhyme")


def plot_void_potential_well(output_dir: Path) -> Path:
    """part_I_topology-void — zero-as-equilibrium potential well with restoring arrows."""
    x = np.linspace(-3.0, 3.0, 241)
    sample = np.array((-2.5, -1.5, -0.75, 0.75, 1.5, 2.5))
    fig, ax = new_figure()
    ax.plot(x, 0.5 * x**2, color=BLUE, linewidth=2.0, label=r"$V(x) = x^2/2$")
    ax.quiver(
        sample,
        0.5 * sample**2,
        -0.5 * sample,
        np.zeros(sample.shape),
        angles="xy",
        scale_units="xy",
        scale=1.0,
        color=ORANGE,
        width=0.008,
        label="restoring drift",
    )
    ax.axhline(0.0, color=GRAY, linewidth=0.6)
    ax.scatter((0.0,), (0.0,), color=VERMILLION, s=45, zorder=5, label="equilibrium (zero)")
    ax.set_xlabel("displacement x from zero")
    ax.set_ylabel("potential V(x)")
    ax.set_title("Topology of the void: zero as equilibrium")
    ax.legend()
    _corner_note(ax, "restoring drift ∝ −x returns every perturbation to zero", loc="lower right")
    return save_figure(fig, output_dir, "part_I_topology-void")


def plot_higgs_gate_curves(output_dir: Path) -> Path:
    """part_I_higgs-awareness — mass-slowing gate curve (transduction_brake family)."""
    t = np.linspace(0.0, 5.0, 200)
    fig, ax = new_figure()
    for color, k in zip(SERIES, (0.5, 1.0, 2.0)):
        ax.plot(t, models.transduction_brake(t, v0=1.0, k=k), color=color, label=f"k = {k}")
        ax.scatter((models.half_life(k),), (0.5,), color=color, marker="|", s=70, zorder=3)
    ax.set_xlabel("elapsed time t")
    ax.set_ylabel(r"velocity $v(t)$")
    ax.set_title("Mass-slowing gate: transduction-brake curve family")
    ax.legend()
    _corner_note(ax, "tick marks: half-life t½ = ln 2 / k (velocity 0.5)")
    return save_figure(fig, output_dir, "part_I_higgs-awareness")


def plot_phi_duality_mirror(output_dir: Path) -> Path:
    """part_II_proton-theater — Φ duality: x·Φ vs x/Φ symmetric mirror branches."""
    x = np.linspace(0.2, 5.0, 200)
    fig, ax = new_figure()
    ax.plot(x, x * models.PHI, color=BLUE, label=r"$x\Phi$")
    ax.plot(x, x / models.PHI, color=ORANGE, label=r"$x/\Phi$")
    ax.plot(x, x, color=GRAY, linestyle="--", linewidth=0.9, label="geometric mean")
    ax.scatter((1.0, 1.0), (models.PHI, 1.0 / models.PHI), color=(BLUE, ORANGE), s=36, zorder=4)
    ax.annotate("x = 1", (1.0, models.PHI), textcoords="offset points", xytext=(6, -2), fontsize=8, color=GRAY)
    ax.set_xlabel("x")
    ax.set_ylabel("dual branch")
    ax.set_title("Φ duality: symmetric x·Φ and x/Φ mirror branches")
    ax.legend()
    _corner_note(ax, f"Φ = {models.PHI:.6f} · the mirror multiplies back: xΦ · x/Φ = x²", loc="lower right")
    return save_figure(fig, output_dir, "part_II_proton-theater")


def plot_viscous_damping_family(output_dir: Path) -> Path:
    """part_II_viscosity-light — viscous damping curve family over drag coefficients."""
    t = np.linspace(0.0, 6.0, 240)
    fig, ax = new_figure()
    for color, k in zip(SERIES, (0.3, 0.6, 1.0, 1.6)):
        ax.plot(t, models.transduction_brake(t, v0=1.0, k=k), color=color, label=f"drag k = {k}")
        ax.scatter((1.0 / k,), (np.exp(-1.0),), color=color, s=22, zorder=3)
    ax.axhline(np.exp(-1.0), color=GRAY, linestyle=":", linewidth=0.8)
    ax.set_xlabel("elapsed time t")
    ax.set_ylabel(r"velocity $v(t)$")
    ax.set_title("Viscosity of light: damping curves over drag coefficients")
    ax.legend()
    _corner_note(ax, "dots: 1/e velocity at t = 1/k")
    return save_figure(fig, output_dir, "part_II_viscosity-light")


def plot_eddy_brake_inset(output_dir: Path) -> Path:
    """part_II_eddy-current-mirror — eddy brake v(t) = v0·e^(−kt) with drag-force inset."""
    t = np.linspace(0.0, 5.0, 200)
    velocity = models.transduction_brake(t, v0=1.0, k=1.0)
    fig, ax = new_figure()
    ax.plot(t, velocity, color=BLUE, label=r"$v(t) = v_0\,e^{-t}$")
    stop = float(t[int(np.argmax(velocity < 0.05))])
    ax.axvline(stop, color=GRAY, linestyle=":", linewidth=0.9)
    ax.annotate(f"v < 0.05 at t ≈ {stop:.2f}", (stop, 0.05), textcoords="offset points", xytext=(6, 8), fontsize=8, color=GRAY)
    ax.set_xlabel("elapsed time t")
    ax.set_ylabel("velocity v(t)")
    ax.set_title("Eddy-current mirror: transduction drag with drag-force inset")
    ax.legend(loc="center left")
    _corner_note(ax, "brake work = ∫ drag dt", loc="lower left")
    inset = ax.inset_axes((0.52, 0.52, 0.42, 0.4))
    inset.plot(t, velocity**2, color=ORANGE, linewidth=1.4)
    inset.fill_between(t, velocity**2, color=ORANGE, alpha=0.2)
    inset.set_title("drag force ∝ v²(t)", fontsize=8)
    inset.tick_params(labelsize=7)
    inset.grid(True, linestyle=":", linewidth=0.5, color=GRAY, alpha=0.5)
    inset.spines["top"].set_visible(False)
    inset.spines["right"].set_visible(False)
    return save_figure(fig, output_dir, "part_II_eddy-current-mirror")


def plot_speed_distance_isolines(output_dir: Path) -> Path:
    """part_II_crystalline-field — speed–distance iso-lines (c = d/t lattice)."""
    t = np.linspace(0.5, 10.0, 200)
    samples = np.arange(1.0, 5.0)
    fig, ax = new_figure()
    for color, c in zip(SERIES, (1.0, 2.0, 3.0, 4.0)):
        ax.plot(t, c * t, color=color, label=f"c = {c:g}")
        ax.scatter(samples, c * samples, color=color, s=12, zorder=3)
    ax.set_xlabel("time t")
    ax.set_ylabel("distance d = c·t")
    ax.set_title("Crystalline unified field: speed–distance iso-lines")
    ax.legend()
    _corner_note(ax, "dots: unit-time lattice samples · slope = c", loc="upper left")
    return save_figure(fig, output_dir, "part_II_crystalline-field")


def plot_metrological_overlap_heatmap(output_dir: Path) -> Path:
    """part_II_metrological-overlap — pairwise metrological-overlap heatmap."""
    bands = [frozenset({i + 1, i + 2, i + 3}) for i in range(8)]
    matrix = np.array([[models.metrological_overlap(a, b) for b in bands] for a in bands])
    fig, ax = _heatmap_figure(
        matrix,
        title="Pairwise metrological overlap of octave-band registers (self-overlap outlined)",
        xlabel="band register j",
        ylabel="band register i",
        cmap="Blues",
        vmin=0.0,
        vmax=1.0,
        colorbar_label="min-normalized overlap",
    )
    ax.set_xticks(np.arange(8), labels=[str(i + 1) for i in range(8)])
    ax.set_yticks(np.arange(8), labels=[str(i + 1) for i in range(8)])
    diag = np.arange(8)
    ax.scatter(diag, diag, marker="s", s=14, facecolors="none", edgecolors=VERMILLION, linewidths=0.7)
    _corner_note(ax, "self-overlap = 1 · pairs sharing a neighbour = 0.5 · disjoint = 0", loc="lower right")
    return save_figure(fig, output_dir, "part_II_metrological-overlap")


def plot_densification_curve(output_dir: Path) -> Path:
    """part_II_metamorphic-octaves — densification curve 1 + ln(1 + exposure)."""
    exposure = np.linspace(0.0, 8.0, 200)
    density = models.densification(exposure, density0=1.0, rate=1.0)
    fig, (ax, side) = _two_figure()
    ax.plot(exposure, density, color=BLUE, label="d = 1 + ln(1 + exposure)")
    marked = float(models.densification(np.array((4.0,)))[0])
    ax.scatter((4.0,), (marked,), color=ORANGE, s=36, zorder=3, label=f"exposure 4 → {marked:.4f}")
    ax.set_xlabel("exposure")
    ax.set_ylabel("density d")
    ax.set_title("Metamorphic octaves: logarithmic densification")
    ax.legend()
    _corner_note(ax, "densification never saturates — it only slows", loc="lower right")
    # Secondary panel: the marginal gain decays as 1 / (1 + exposure).
    marginal = 1.0 / (1.0 + exposure)
    side.plot(exposure, marginal, color=GREEN, linewidth=1.6)
    side.fill_between(exposure, marginal, color=GREEN, alpha=0.15)
    side.set_xlabel("exposure")
    side.set_ylabel("marginal gain")
    side.set_title("Marginal gain 1 / (1 + exposure)", fontsize=10)
    return save_figure(fig, output_dir, "part_II_metamorphic-octaves")


def plot_goldilocks_band_trace(output_dir: Path) -> Path:
    """part_II_planetary-core — goldilocks band shading over a value trace."""
    t = np.linspace(0.0, 10.0, 400)
    values = 1.0 + 0.5 * np.sin(1.3 * t) + 0.25 * np.sin(0.7 * t)
    lo, hi = 0.9, 1.15
    in_band = models.goldilocks_band(values, lo, hi)
    fig, ax = new_figure()
    ax.axhspan(lo, hi, color=GREEN, alpha=0.15, label="goldilocks band")
    ax.axhline(lo, color=GREEN, linestyle="--", linewidth=0.7)
    ax.axhline(hi, color=GREEN, linestyle="--", linewidth=0.7)
    ax.plot(t, values, color=GRAY, linewidth=1.0)
    ax.scatter(t[in_band], values[in_band], color=GREEN, s=6, zorder=3, label="in band")
    ax.set_xlabel("t")
    ax.set_ylabel("value")
    ax.set_title("Planetary core: goldilocks band shading over a value trace")
    ax.legend(loc="upper right", fontsize=8)
    _corner_note(ax, f"in-band fraction = {float(in_band.mean()):.2f} · band [{lo}, {hi}]", loc="lower left")
    return save_figure(fig, output_dir, "part_II_planetary-core")


def plot_net_zero_balance_bars(output_dir: Path) -> Path:
    """part_II_singularity-crystal — net-zero inflow/outflow balance bars, zero residual."""
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch

    inflows = {"source a": 4.0, "source b": 2.5, "source c": 3.5}
    outflows = {"sink a": 5.0, "sink b": 5.0}
    residual = models.net_zero_balance(inflows, outflows)
    names = tuple(inflows) + tuple(outflows)
    values = tuple(inflows.values()) + tuple(outflows.values())
    colors = (BLUE,) * len(inflows) + (ORANGE,) * len(outflows)
    fig, ax = new_figure()
    ax.bar(names, values, color=colors, width=0.6)
    ax.set_ylim(-0.8, 6.0)  # headroom below zero so the residual line is a visible reference
    ax.axhline(0.0, color=GRAY, linewidth=1.0, linestyle="--", label="zero residual line")
    ax.legend(
        handles=(
            Patch(color=BLUE, label="inflow"),
            Patch(color=ORANGE, label="outflow"),
            Line2D((0,), (0,), color=GRAY, linestyle="--", label="zero residual line"),
        ),
        loc="upper right",
        fontsize=8,
    )
    ax.set_xlabel("ledger entry")
    _corner_note(ax, f"residual = {residual:.1f} — the ledger closes")
    ax.set_ylabel("flow")
    ax.set_title("Singularity crystal: net-zero inflow/outflow balance")
    return save_figure(fig, output_dir, "part_II_singularity-crystal")


def plot_shelf_tier_stacked_bars(output_dir: Path) -> Path:
    """part_III_cmos-protonic — octaves-per-substrate stacked bars (silicon shelf tiers)."""
    substrates = ("silicon shelf", "protonic shelf")
    tiers = ("tier 1", "tier 2", "tier 3")
    octaves_per_tier = (33, 33, 33)  # 3 × 33 = the 99-octave map
    fig, ax = new_figure()
    bottoms = np.zeros(len(substrates))
    for tier, count, color in zip(tiers, octaves_per_tier, SERIES):
        ax.bar(substrates, (count, count), bottom=bottoms, color=color, width=0.5, label=tier)
        ax.text(0.0, bottoms[0] + count / 2.0, f"{tier}: {count}", ha="center", va="center", fontsize=8, color="white")
        bottoms = bottoms + count
    _corner_note(ax, "3 tiers × 33 = the 99-octave map on either shelf")
    ax.set_ylabel("octave bands")
    ax.set_ylim(0, 110)
    ax.set_title("Octaves per substrate shelf tier (schematic)")
    ax.legend(loc="center right")
    return save_figure(fig, output_dir, "part_III_cmos-protonic")


def plot_prime_container_growth(output_dir: Path) -> Path:
    """part_III_protein-folding — prime-container capacity: unique_address growth sequence."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    ks = np.arange(1, len(primes) + 1)
    addresses = [models.unique_address(primes[: int(k)], [1] * int(k)) for k in ks]
    fig, (ax, side) = _two_figure()
    ax.semilogy(ks, addresses, "o-", color=BLUE, label="unique_address(primes, 1)")
    ax.annotate(
        f"{addresses[-1]:,}",
        (ks[-1], addresses[-1]),
        textcoords="offset points",
        xytext=(-4, 8),
        ha="right",
        fontsize=8,
    )
    ax.set_xlabel("prime channels folded")
    ax.set_ylabel("container address (log scale)")
    ax.set_title("Prime-container capacity: unique_address growth sequence")
    ax.legend(loc="lower right", fontsize=8)
    _corner_note(ax, "each new prime channel multiplies the address space", loc="upper left")
    # Secondary panel: the decimal digit span of the container address.
    side.plot(ks, np.log10(np.asarray(addresses, dtype=float)), "o-", color=ORANGE)
    side.set_xlabel("prime channels folded")
    side.set_ylabel("decimal digits (log10 address)")
    side.set_title("Address digit span", fontsize=10)
    return save_figure(fig, output_dir, "part_III_protein-folding")


def plot_prime_power_lattice(output_dir: Path) -> Path:
    """part_III_volumetric-storage — prime-indexed address scatter (p^k lattice)."""
    ks = np.arange(1, 7)
    fig, ax = new_figure()
    for color, p in zip(SERIES, (2, 3, 5, 7, 11)):
        ax.plot(ks, [p**int(k) for k in ks], "o--", color=color, label=f"p = {p}")
    ax.set_yscale("log")
    ax.set_xlabel("exponent k")
    ax.set_ylabel("address p^k (log scale)")
    ax.set_title("Prime-indexed volumetric storage: the p^k address lattice")
    ax.legend(fontsize=8)
    _corner_note(ax, "each prime base spans its own exponential shelf", loc="upper left")
    return save_figure(fig, output_dir, "part_III_volumetric-storage")


def plot_round_robin_recycling(output_dir: Path) -> Path:
    """part_III_kinematic-recycling — round-robin set-recycling cycle over discrete time."""
    assignment = {}
    for set_index, subset in enumerate(models.round_robin(list(range(12)), 3)):
        for item in subset:
            assignment[item] = set_index
    time = np.arange(24)
    cycle = np.array([assignment[int(t) % 12] for t in time], dtype=float) + 1.0
    fig, ax = new_figure()
    for set_index, color in enumerate((BLUE, ORANGE, GREEN)):
        ax.axhspan(set_index + 0.55, set_index + 1.45, color=color, alpha=0.08)
    ax.step(time, cycle, where="mid", color=GRAY, linewidth=1.0)
    for set_index, color in enumerate((BLUE, ORANGE, GREEN)):
        mask = cycle == set_index + 1.0
        ax.scatter(time[mask], cycle[mask], color=color, s=26, zorder=3, label=f"set {set_index + 1}")
    ax.set_yticks((1, 2, 3))
    ax.set_xlabel("discrete time step")
    ax.set_ylabel("recycling set")
    ax.set_title("Kinematic set-recycling: round-robin cycle over discrete time")
    ax.legend(loc="center right", fontsize=8)
    _corner_note(ax, "12 items · 3 sets · period 12", loc="lower left")
    return save_figure(fig, output_dir, "part_III_kinematic-recycling")


def plot_stack_layers_step(output_dir: Path) -> Path:
    """part_III_moving-up-stack — stack layers step plot (model → lattice → agent)."""
    milestones = np.arange(0, 4)
    layers = np.array((0.0, 0.0, 1.0, 2.0))
    fig, ax = new_figure()
    ax.step(milestones, layers, where="post", color=BLUE, linewidth=2.0)
    for y, label in enumerate(("model layer", "lattice layer", "agent layer")):
        ax.text(2.9, y + 0.06, label, fontsize=9, color=GRAY, ha="right")
    for base in (0.0, 1.0):
        ax.annotate(
            "",
            xy=(1.55, base + 0.85),
            xytext=(1.55, base + 0.15),
            arrowprops=dict(arrowstyle="->", color=ORANGE, linewidth=1.2),
        )
    ax.set_xticks(milestones)
    ax.set_yticks((0, 1, 2), labels=("model", "lattice", "agent"))
    ax.set_xlabel("capability milestone")
    ax.set_ylabel("stack layer")
    ax.set_title("Moving up the stack: model → lattice → agent layers")
    ax.set_xlim(-0.1, 3.1)
    _corner_note(ax, "each layer rides on the one below", loc="lower left")
    return save_figure(fig, output_dir, "part_III_moving-up-stack")


def plot_bridge_throughput_radial(output_dir: Path) -> Path:
    """part_III_reality-bridge — bridge/router throughput radial plot."""
    import matplotlib.pyplot as plt

    theta = np.linspace(0.0, 2.0 * np.pi, 241)
    throughput = 1.0 + 0.5 * np.cos(2.0 * theta)
    fig, ax = plt.subplots(figsize=(6.0, 6.0), subplot_kw={"projection": "polar"})
    ax.plot(theta, throughput, color=BLUE, linewidth=1.8)
    ax.fill(theta, throughput, color=BLUE, alpha=0.2)
    ax.scatter((0.0, np.pi), (1.5, 1.5), color=VERMILLION, s=36, zorder=5)
    ax.annotate("peaks at θ = 0, π", xy=(0.30, 1.72), fontsize=8, color=VERMILLION)
    ax.set_rlabel_position(90)
    ax.grid(True, linestyle=":", linewidth=0.6, color=GRAY, alpha=0.6)
    ax.set_title("Reality bridge: radial throughput profile", va="bottom", pad=16)
    _corner_note(ax, "throughput = 1 + 0.5·cos 2θ · peaks at θ = 0, π", loc="lower left")
    return save_figure(fig, output_dir, "part_III_reality-bridge")


def plot_digit_drawer_bands(output_dir: Path) -> Path:
    """part_III_y-chromosome — digit-4 drawer manifestation: sub-band bar chart."""
    drawers = np.arange(1, 10)
    bands = np.full(drawers.shape, 11)  # 9 drawers × 11 bands = the 99-octave map
    fig, ax = new_figure()
    ax.bar(drawers, bands, color=tuple(VERMILLION if d == 4 else BLUE for d in drawers), width=0.7)
    ax.axhline(11.0, color=GRAY, linestyle=":", linewidth=0.8)
    ax.annotate(
        "digit 4",
        (4, 11),
        textcoords="offset points",
        xytext=(0, 4),
        ha="center",
        fontsize=9,
        color=VERMILLION,
    )
    ax.set_xticks(drawers)
    ax.set_xlabel("digit drawer")
    ax.set_ylabel("octave bands per drawer")
    ax.set_ylim(0, 13)
    ax.set_title("Digit-4 drawer manifestation: 9 drawers × 11 sub-bands = 99")
    from matplotlib.patches import Patch

    ax.legend(
        handles=(
            Patch(color=BLUE, label="drawers 1–3, 5–9"),
            Patch(color=VERMILLION, label="digit 4"),
        ),
        loc="upper right",
        fontsize=8,
    )
    _corner_note(ax, "every drawer carries exactly 11 bands — 99 in total", loc="upper left")
    return save_figure(fig, output_dir, "part_III_y-chromosome")


def plot_lattice_linear_ramp(output_dir: Path) -> Path:
    """part_III_pdvsa-gateway — lattice-linear flow ramp (lattice_linear_profile)."""
    steps = np.arange(1, 13)
    flow = models.lattice_linear_profile(12, rate=1.0)
    fig, ax = new_figure()
    ax.step(steps, flow, where="post", color=BLUE, linewidth=1.8, label="lattice-linear ramp")
    ax.scatter(steps, flow, color=ORANGE, s=24, zorder=3)
    ax.set_xticks(steps)
    ax.set_xlabel("gateway step")
    ax.set_ylabel("flow")
    ax.set_title("PDVSA gateway ops: lattice-linear flow ramp")
    ax.legend(loc="upper left", fontsize=8)
    _corner_note(ax, "slope = rate = 1 flow unit per gateway step", loc="lower right")
    return save_figure(fig, output_dir, "part_III_pdvsa-gateway")


def plot_work_engine_curve(output_dir: Path) -> Path:
    """part_III_macro-protein — macro-protein work-engine output curve."""
    load = np.linspace(0.0, 10.0, 200)
    half_saturation = 3.0
    fig, ax = new_figure()
    ax.plot(
        load,
        models.saturating_response(load, maximum=1.0, half_saturation=half_saturation, hill=2.0),
        color=BLUE,
        label="work output (hill n = 2)",
    )
    ax.axvline(half_saturation, color=ORANGE, linestyle="--", linewidth=0.9, label="half saturation = 3.0")
    ax.scatter((half_saturation,), (0.5,), color=ORANGE, s=36, zorder=3)
    ax.set_xlabel("applied load")
    ax.set_ylabel("work output")
    ax.set_title("Macro-protein work engine: saturating output curve")
    ax.legend(loc="lower right", fontsize=8)
    _corner_note(ax, "hill n = 2 · half the maximum at load 3", loc="upper left")
    return save_figure(fig, output_dir, "part_III_macro-protein")


def plot_visibility_frontier(output_dir: Path) -> Path:
    """part_III_invisible-frontier — visibility threshold frontier curve."""
    t = np.linspace(0.0, 10.0, 400)
    visibility = models.logistic_growth(t, r=1.0, carrying_capacity=1.0, initial=0.02)
    crossing = float(t[int(np.argmax(visibility >= 0.5))])
    fig, ax = new_figure()
    ax.plot(t, visibility, color=BLUE, label="visibility")
    ax.axhline(0.5, color=ORANGE, linestyle="--", linewidth=0.9, label="threshold = 0.5")
    ax.axvspan(0.0, crossing, color=GRAY, alpha=0.10)
    ax.text(crossing / 2.0, 0.07, "latent phase", ha="center", fontsize=8, color=GRAY)
    ax.scatter((crossing,), (0.5,), color=VERMILLION, s=36, zorder=3)
    ax.annotate(f"frontier t ≈ {crossing:.2f}", (crossing, 0.5), textcoords="offset points", xytext=(6, -12), fontsize=8)
    ax.set_xlabel("t")
    ax.set_ylabel("visibility")
    ax.set_title("Invisible frontier: visibility threshold crossing")
    ax.legend(loc="center right", fontsize=8)
    return save_figure(fig, output_dir, "part_III_invisible-frontier")


def plot_frontiers_quadrant_map(output_dir: Path) -> Path:
    """part_III_frontiers — open-problems quadrant map (value × effort)."""
    problems = np.array(
        (
            (0.15, 0.85),
            (0.30, 0.70),
            (0.20, 0.40),
            (0.40, 0.20),
            (0.70, 0.90),
            (0.85, 0.75),
            (0.75, 0.45),
            (0.90, 0.25),
        )
    )
    fig, ax = new_figure()
    ax.axvline(0.5, color=GRAY, linewidth=0.8)
    ax.axhline(0.5, color=GRAY, linewidth=0.8)
    # Do-first quadrant: high value, low effort — shaded and labelled honestly.
    ax.axvspan(0.0, 0.5, ymin=0.5, ymax=1.0, color=GREEN, alpha=0.12)
    ax.scatter(problems[:, 0], problems[:, 1], color=PURPLE, s=40, zorder=3)
    quadrants = (
        (0.25, 0.25, "low value\nlow effort", False),
        (0.75, 0.25, "low value\nhigh effort", False),
        (0.25, 0.75, "high value\nlow effort\ndo first", True),
        (0.75, 0.75, "high value\nhigh effort", False),
    )
    for x, y, label, do_first in quadrants:
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=8,
            color=GREEN if do_first else GRAY,
            weight="bold" if do_first else "normal",
        )
    from matplotlib.patches import Patch

    ax.legend(
        handles=(Patch(facecolor=GREEN, alpha=0.15, edgecolor=GREEN, label="do-first quadrant"),),
        loc="center",
        fontsize=8,
        framealpha=0.9,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("effort")
    ax.set_ylabel("value")
    ax.set_title("Frontiers: open-problems quadrant map")
    return save_figure(fig, output_dir, "part_III_frontiers")

# ---------------------------------------------------------------------------
# Unit-intro part-overview maps
#
# One deterministic overview figure per part, named ``<part_id>_unit-intro.png``
# (the manuscript embeds these at each unit opening). Like the chapter
# builders they consume no randomness, so every rendered PNG is byte-stable
# for a fixed matplotlib version.
# ---------------------------------------------------------------------------


def plot_part_0_unit_intro(output_dir: Path) -> Path:
    """part_0 unit-intro — reading map: ship/catalog → methods → five-chapter tour."""
    stations = (
        (0.0, "ship &\ncatalog", PURPLE),
        (1.0, "methods", PURPLE),
        (2.0, "orientation", BLUE),
        (3.0, "living-pem", BLUE),
        (4.0, "tensor-\ndecoupling", BLUE),
        (5.0, "master-\nsynthesis", BLUE),
        (6.0, "octave-map", BLUE),
    )
    fig, ax = new_figure(width=7.2, height=2.8)
    ax.axhline(0.0, color=GRAY, linewidth=1.0, zorder=1)
    for x, label, color in stations:
        above = x < 2.0
        ax.scatter((x,), (0.0,), s=110, color=color, zorder=3)
        ax.annotate(
            label,
            (x, 0.0),
            textcoords="offset points",
            xytext=(0, 12 if above else -12),
            ha="center",
            va="bottom" if above else "top",
            fontsize=8,
        )
    for x0 in np.arange(0.35, 6.0, 1.0):
        ax.annotate(
            "",
            (x0 + 0.3, 0.0),
            xytext=(x0, 0.0),
            arrowprops=dict(arrowstyle="->", color=GRAY, linewidth=1.0),
        )
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-1.0, 1.0)
    ax.set_yticks([])
    ax.set_xticks([s[0] for s in stations], labels=[str(i + 1) for i in range(len(stations))])
    ax.set_xlabel("reading order")
    ax.set_title("Part 0 — reading map: ship & catalog → methods → five-chapter tour")
    _corner_note(ax, "purple: how to read · blue: the five-chapter tour", loc="lower left")
    return save_figure(fig, output_dir, "part_0_unit-intro")


def plot_part_I_unit_intro(output_dir: Path) -> Path:
    """part_I unit-intro — foundations map: five stations along the Φ spine."""
    count = 10
    ks = np.arange(1, count + 1)
    spine = models.phi_powers(count)
    stages = (
        (1, "fractal constant\nΦ"),
        (3, "prime-parity\nscaffold"),
        (5, "rhyme\nfields"),
        (7, "void\ntopology"),
        (9, "Higgs\ngate"),
    )
    fig, ax = new_figure()
    ax.semilogy(ks, spine, color=BLUE, linewidth=1.8, label=r"$\Phi^n$ spine")
    for k, label in stages:
        x = float(k)
        y = float(spine[k - 1])
        ax.scatter((x,), (y,), color=VERMILLION, s=45, zorder=3)
        ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=8)
    ax.set_xticks(ks)
    ax.set_xlabel("reading order n")
    ax.set_ylabel(r"$\Phi^n$ (log scale)")
    ax.set_title("Part I — foundations map: five stations on the Φ spine")
    ax.legend(loc="lower right", fontsize=8)
    _corner_note(ax, f"spine value Φⁿ · Φ = {models.PHI:.6f}", loc="upper left")
    return save_figure(fig, output_dir, "part_I_unit-intro")


def plot_part_II_unit_intro(output_dir: Path) -> Path:
    """part_II unit-intro — eight subsystem chapters orbiting their shared constants."""
    chapters = (
        "proton-theater",
        "viscosity-light",
        "eddy-current-mirror",
        "crystalline-field",
        "metrological-overlap",
        "metamorphic-octaves",
        "planetary-core",
        "singularity-crystal",
    )
    angles = np.linspace(0.0, 2.0 * np.pi, len(chapters), endpoint=False)
    radius = 1.0
    fig, ax = new_figure(width=6.4, height=5.4)
    ax.axhline(0.0, color=GRAY, linewidth=0.8, zorder=1)
    for i, (angle, name) in enumerate(zip(angles, chapters)):
        x = radius * float(np.cos(angle))
        y = radius * float(np.sin(angle))
        ax.plot((0.38 * x, x), (0.38 * y, y), color=GRAY, linewidth=0.7, zorder=1)
        ax.scatter((x,), (y,), s=70, color=SERIES[i % len(SERIES)], zorder=3)
        above = float(np.sin(angle)) >= 0.0
        ax.annotate(
            name,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10 if above else -14),
            ha="center",
            va="bottom" if above else "top",
            fontsize=8,
        )
    ax.scatter((0.0,), (0.0,), s=200, color=GREEN, zorder=4)
    ax.annotate(
        (
            "shared constants\n"
            f"Φ ≈ {models.PHI:.3f}\n"
            "c = 299 792 458 m/s\n"
            f"register: 9 × 99 = {models.catalog_size(99, 9)} bins"
        ),
        (0.0, 0.0),
        textcoords="offset points",
        xytext=(0, -20),
        ha="center",
        va="top",
        fontsize=8,
    )
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    ax.set_title("Part II — engine-shelf systems map: eight chapters, shared constants")
    return save_figure(fig, output_dir, "part_II_unit-intro")


def plot_part_III_unit_intro(output_dir: Path) -> Path:
    """part_III unit-intro — implementations → companions → the open-problem quadrant program."""
    fig, (ax, side) = _two_figure(width=7.6, height=3.6, width_ratios=(1.7, 1.0))
    stages = (
        (0.0, "implementations\n8 chapter builds"),
        (1.0, "companions\nbridge & recycling notes"),
        (2.0, "open-problem\nquadrant program"),
    )
    ax.axhline(0.5, color=GRAY, linewidth=1.0, zorder=1)
    for x, label in stages:
        ax.scatter((x,), (0.5,), s=130, color=PURPLE, zorder=3)
        ax.annotate(
            label,
            (x, 0.5),
            textcoords="offset points",
            xytext=(0, 14),
            ha="center",
            fontsize=8,
        )
    for x0 in (0.18, 1.18):
        ax.annotate(
            "",
            (x0 + 0.64, 0.5),
            xytext=(x0, 0.5),
            arrowprops=dict(arrowstyle="->", color=GRAY, linewidth=1.2),
        )
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0.0, 1.0)
    ax.set_yticks([])
    ax.set_xticks((0.0, 1.0, 2.0), labels=("builds", "companions", "program"))
    ax.set_title("Part III pipeline", fontsize=10)
    # Secondary panel: the open-problem quadrant the unit converges on.
    problems = np.array(
        (
            (0.18, 0.82),
            (0.34, 0.60),
            (0.62, 0.86),
            (0.80, 0.66),
            (0.86, 0.16),
        )
    )
    side.axvline(0.5, color=GRAY, linewidth=0.8)
    side.axhline(0.5, color=GRAY, linewidth=0.8)
    side.axvspan(0.0, 0.5, ymin=0.5, ymax=1.0, color=GREEN, alpha=0.12)
    side.scatter(problems[:, 0], problems[:, 1], color=PURPLE, s=26, zorder=3)
    for x, y, label in (
        (0.25, 0.75, "do first"),
        (0.75, 0.75, "high value,\nhigh effort"),
        (0.25, 0.25, "low value,\nlow effort"),
        (0.75, 0.25, "low value,\nhigh effort"),
    ):
        side.text(x, y, label, ha="center", va="center", fontsize=7, color=GRAY)
    side.set_xlim(0, 1)
    side.set_ylim(0, 1)
    side.set_xlabel("effort")
    side.set_ylabel("value")
    side.set_title("Open-problem quadrant program", fontsize=10)
    return save_figure(fig, output_dir, "part_III_unit-intro")


UNIT_INTRO_BUILDERS: dict[str, Any] = {
    "part_0": plot_part_0_unit_intro,
    "part_I": plot_part_I_unit_intro,
    "part_II": plot_part_II_unit_intro,
    "part_III": plot_part_III_unit_intro,
}


def generate_intro_figures(output_dir: Path, config: dict[str, Any] | None = None) -> list[Path]:
    """Generate the four unit-intro part-overview maps.

    Filenames are fixed by the manuscript's unit-opening embeds
    (``<part_id>_unit-intro.png``), so builders dispatch directly by part id;
    ``config`` is accepted for signature symmetry with
    :func:`generate_chapter_figures` and intentionally unused.
    """
    del config
    paths = [builder(output_dir) for builder in UNIT_INTRO_BUILDERS.values()]
    logger.info("generated %d unit-intro figures in %s", len(paths), output_dir)
    return paths


CHAPTER_BUILDERS: dict[tuple[str, str], Any] = {
    ("part_0", "orientation"): plot_engine_shelf_timeline,
    ("part_0", "living-pem"): plot_living_pem_ladder,
    ("part_0", "tensor-decoupling"): plot_register_bins_heatmap,
    ("part_0", "master-synthesis"): plot_crosslink_adjacency_heatmap,
    ("part_0", "octave-map"): plot_octave_ladder,
    ("part_I", "fractal-constant"): plot_phi_growth_fibonacci,
    ("part_I", "prime-parity"): plot_prime_parity_numberline,
    ("part_I", "holographic-rhyme"): plot_holographic_rhyme_contours,
    ("part_I", "multidimensional-rhyme"): plot_xd_yd_interference,
    ("part_I", "topology-void"): plot_void_potential_well,
    ("part_I", "higgs-awareness"): plot_higgs_gate_curves,
    ("part_II", "proton-theater"): plot_phi_duality_mirror,
    ("part_II", "viscosity-light"): plot_viscous_damping_family,
    ("part_II", "eddy-current-mirror"): plot_eddy_brake_inset,
    ("part_II", "crystalline-field"): plot_speed_distance_isolines,
    ("part_II", "metrological-overlap"): plot_metrological_overlap_heatmap,
    ("part_II", "metamorphic-octaves"): plot_densification_curve,
    ("part_II", "planetary-core"): plot_goldilocks_band_trace,
    ("part_II", "singularity-crystal"): plot_net_zero_balance_bars,
    ("part_III", "cmos-protonic"): plot_shelf_tier_stacked_bars,
    ("part_III", "protein-folding"): plot_prime_container_growth,
    ("part_III", "volumetric-storage"): plot_prime_power_lattice,
    ("part_III", "kinematic-recycling"): plot_round_robin_recycling,
    ("part_III", "moving-up-stack"): plot_stack_layers_step,
    ("part_III", "reality-bridge"): plot_bridge_throughput_radial,
    ("part_III", "y-chromosome"): plot_digit_drawer_bands,
    ("part_III", "pdvsa-gateway"): plot_lattice_linear_ramp,
    ("part_III", "macro-protein"): plot_work_engine_curve,
    ("part_III", "invisible-frontier"): plot_visibility_frontier,
    ("part_III", "frontiers"): plot_frontiers_quadrant_map,
}


def omnilattice_cover(
    output_dir: Path,
    *,
    title: str = "The Infinite Octaves Omni-Lattice Textbook",
    subtitle: str = "A Modular Synthesis of the SynthOBS Engine Papers",
) -> Path:
    """Render the deterministic Omni-Lattice cover art.

    Motif per ``book.cover`` in ``docs/manuscript/config.yaml``: a lattice of
    ninety-nine octave bands keyed by the golden-ratio constant, nine digit
    drawers, and the zero-octave node at the lattice origin. The composition
    adds a framed lattice, a band-index rail, drawer separators after every
    third drawer, and a Φ key strip so the golden-ratio encoding is legible.
    Deterministic, so the cover is byte-stable. Saved as
    ``omnilattice_cover.png``.
    """
    import matplotlib.pyplot as plt
    from matplotlib import colormaps
    from matplotlib.patches import Rectangle

    drawers, bands_per_drawer = 9, 11
    fig, ax = plt.subplots(figsize=(6.4, 8.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 13.5)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    cell_w, cell_h = 0.9, 0.62
    x0, y0 = 0.9, 2.4  # lattice origin — the zero-octave node
    lattice_w = drawers * cell_w
    lattice_h = bands_per_drawer * cell_h
    powers = models.phi_powers(drawers * bands_per_drawer)
    keys = np.log(powers) / np.log(powers[-1])
    colormap = colormaps["viridis"]
    for drawer in range(drawers):
        for band in range(bands_per_drawer):
            key = keys[drawer * bands_per_drawer + band]
            ax.add_patch(
                Rectangle(
                    (x0 + drawer * cell_w, y0 + band * cell_h),
                    cell_w * 0.92,
                    cell_h * 0.82,
                    facecolor=colormap(key),
                    edgecolor="white",
                    linewidth=0.4,
                )
            )
    # Frame around the lattice plus a band-index rail on its left edge.
    ax.add_patch(
        Rectangle(
            (x0 - 0.09, y0 - 0.09),
            lattice_w + 0.18,
            lattice_h + 0.18,
            facecolor="none",
            edgecolor=GRAY,
            linewidth=0.8,
        )
    )
    for band in range(bands_per_drawer):
        ax.text(
            x0 - 0.2,
            y0 + band * cell_h + cell_h / 2,
            str(band + 1),
            ha="right",
            va="center",
            fontsize=6,
            color=GRAY,
        )
    # Drawer separators after every third drawer — three tiers of three drawers.
    for drawer in (3, 6):
        ax.plot(
            (x0 + drawer * cell_w - 0.04,) * 2,
            (y0 - 0.09, y0 + lattice_h + 0.09),
            color=GRAY,
            linewidth=0.8,
        )
    for drawer in range(drawers):
        ax.text(
            x0 + drawer * cell_w + cell_w * 0.46,
            y0 - 0.26,
            str(drawer + 1),
            ha="center",
            va="top",
            fontsize=8,
            color=GRAY,
        )
    ax.text(
        x0,
        y0 - 0.85,
        "digit drawers 1–9 · 11 octave bands each = 99",
        fontsize=8,
        color=GRAY,
        ha="left",
    )
    # Φ key strip: the golden-ratio encoding running up the right edge.
    strip_x = x0 + lattice_w + 0.45
    strip_w, strip_steps = 0.24, 64
    for step in range(strip_steps):
        ax.add_patch(
            Rectangle(
                (strip_x, y0 + step / strip_steps * lattice_h),
                strip_w,
                lattice_h / strip_steps,
                facecolor=colormap(step / (strip_steps - 1)),
                edgecolor="none",
            )
        )
    ax.add_patch(
        Rectangle((strip_x, y0), strip_w, lattice_h, facecolor="none", edgecolor=GRAY, linewidth=0.8)
    )
    ax.text(
        strip_x + strip_w + 0.18,
        y0 + lattice_h / 2,
        "Φ key\n$\\ln \\Phi^{n}$",
        rotation=90,
        ha="center",
        va="center",
        fontsize=7,
        color=GRAY,
    )
    ax.scatter(
        (x0,),
        (y0,),
        s=90,
        color=VERMILLION,
        zorder=5,
        edgecolors="white",
        linewidths=1.2,
    )
    ax.annotate(
        "zero-octave node (k = 0)",
        (x0, y0),
        textcoords="offset points",
        xytext=(-2, -26),
        fontsize=8,
        color=VERMILLION,
    )
    ax.text(5, 12.4, title, ha="center", va="center", fontsize=15, weight="bold", wrap=True)
    if subtitle:
        ax.text(5, 11.5, subtitle, ha="center", va="center", fontsize=10, color=GRAY, wrap=True)
    ax.text(
        5,
        1.0,
        "99 octaves · 9 digits · one golden-ratio key",
        ha="center",
        va="center",
        fontsize=10,
        style="italic",
        color=GRAY,
    )
    return save_figure(fig, output_dir, "omnilattice_cover")


def generate_worked_figures(output_dir: Path) -> list[Path]:
    """Generate the worked-model figures."""
    return [
        plot_logistic_growth(output_dir),
        plot_saturating_response(output_dir),
        plot_exponential_decay(output_dir),
        plot_linear_fit(output_dir),
    ]


def generate_chapter_figures(output_dir: Path, config: dict[str, Any] | None = None) -> list[Path]:
    """Generate the canonical bespoke figure for every enabled chapter.

    One figure per chapter named ``<part_id>_<stem>.png`` (the manuscript's
    ``\\includegraphics`` contract). Chapters in the canonical figure plan
    dispatch to their shared parametrized builder via :data:`CHAPTER_BUILDERS`;
    the template's source-bound case study keeps its dedicated renderer, and
    any chapter without a bespoke builder falls back to a neutral placeholder
    so cross-references always resolve.
    """
    cfg = config if config is not None else load_config()
    paths: list[Path] = []
    for chapter in iter_chapters(cfg):
        builder = CHAPTER_BUILDERS.get((chapter.part_id, chapter.stem))
        if builder is None:
            paths.append(placeholder_overview(chapter.title, output_dir, f"{chapter.part_id}_{chapter.stem}.png"))
        else:
            paths.append(builder(output_dir))
    return paths


def generate_chapter_placeholders(output_dir: Path, config: dict[str, Any] | None = None) -> list[Path]:
    """Backward-compatible alias for the chapter-figure generation contract."""
    return generate_chapter_figures(output_dir, config)


def generate_all_figures(output_dir: Path, config: dict[str, Any] | None = None) -> list[Path]:
    """Generate every figure the manuscript references — worked models, unit-intro maps, and chapter figures."""
    paths = generate_worked_figures(output_dir)
    paths.extend(generate_intro_figures(output_dir, config))
    paths.extend(generate_chapter_figures(output_dir, config))
    logger.info("generated %d figures in %s", len(paths), output_dir)
    return paths


__all__ = [
    "CHAPTER_BUILDERS",
    "UNIT_INTRO_BUILDERS",
    "cover_art",
    "generate_all_figures",
    "generate_chapter_figures",
    "generate_chapter_placeholders",
    "generate_intro_figures",
    "generate_worked_figures",
    "omnilattice_cover",
    "placeholder_overview",
    "plot_bridge_throughput_radial",
    "plot_crosslink_adjacency_heatmap",
    "plot_digit_drawer_bands",
    "plot_densification_curve",
    "plot_eddy_brake_inset",
    "plot_engine_shelf_timeline",
    "plot_exponential_decay",
    "plot_frontiers_quadrant_map",
    "plot_goldilocks_band_trace",
    "plot_higgs_gate_curves",
    "plot_holographic_rhyme_contours",
    "plot_lattice_linear_ramp",
    "plot_living_pem_ladder",
    "plot_linear_fit",
    "plot_logistic_growth",
    "plot_metrological_overlap_heatmap",
    "plot_net_zero_balance_bars",
    "plot_octave_ladder",
    "plot_part_0_unit_intro",
    "plot_part_I_unit_intro",
    "plot_part_II_unit_intro",
    "plot_part_III_unit_intro",
    "plot_phi_duality_mirror",
    "plot_phi_growth_fibonacci",
    "plot_prime_container_growth",
    "plot_prime_parity_numberline",
    "plot_prime_power_lattice",
    "plot_register_bins_heatmap",
    "plot_round_robin_recycling",
    "plot_saturating_response",
    "plot_shelf_tier_stacked_bars",
    "plot_speed_distance_isolines",
    "plot_stack_layers_step",
    "plot_viscous_damping_family",
    "plot_visibility_frontier",
    "plot_void_potential_well",
    "plot_work_engine_curve",
    "plot_xd_yd_interference",
]
