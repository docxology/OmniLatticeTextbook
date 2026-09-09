"""Tests for deterministic figure generation (real PNG files, no mocks)."""

from __future__ import annotations

from pathlib import Path

import pytest

from textbook.config import iter_chapters, load_config
from visualization import _scaffold, plots
from visualization.registry import FIGURE_ALT_TEXT, collect_figure_registry_entries, write_figure_registry

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _png_is_nonempty(path):
    assert path.exists()
    assert path.suffix == ".png"
    assert path.stat().st_size > 0
    # PNG magic number.
    assert path.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


@pytest.mark.parametrize(
    "fn",
    [
        plots.plot_logistic_growth,
        plots.plot_saturating_response,
        plots.plot_exponential_decay,
        plots.plot_linear_fit,
    ],
)
def test_worked_figures_write_png(tmp_path, fn):
    _png_is_nonempty(fn(tmp_path))


def test_placeholder_overview(tmp_path):
    path = plots.placeholder_overview("A Chapter", tmp_path, "demo")
    _png_is_nonempty(path)
    assert path.name == "demo.png"


def test_generate_chapter_placeholders_matches_config(tmp_path):
    config = load_config()
    paths = plots.generate_chapter_placeholders(tmp_path, config)
    # The legacy name retains one-file-per-chapter behavior while dispatching
    # filled chapters to their bespoke renderers.
    assert len(paths) == len(iter_chapters(config))
    assert "part_III_frontiers.png" in {path.name for path in paths}
    for path in paths:
        _png_is_nonempty(path)


def test_generate_chapter_figures_uses_bespoke_lattice_plots(tmp_path):
    paths = plots.generate_chapter_figures(tmp_path, load_config())

    assert len(paths) == len(iter_chapters(load_config()))
    crystal = next(path for path in paths if path.name == "part_II_singularity-crystal.png")
    _png_is_nonempty(crystal)
    placeholder = plots.placeholder_overview(
        "The Holographic Singularity Crystal", tmp_path / "control", "part_II_singularity-crystal"
    )
    assert crystal.read_bytes() != placeholder.read_bytes()



def _canonical_chapter_builders():
    """Yield (key, builder) for every enabled chapter with a bespoke builder."""
    for chapter in iter_chapters(load_config()):
        key = (chapter.part_id, chapter.stem)
        builder = plots.CHAPTER_BUILDERS.get(key)
        if builder is not None:
            yield key, builder


_CANONICAL_BUILDERS = sorted(_canonical_chapter_builders(), key=lambda item: item[0])


def test_canonical_chapter_builders_cover_the_figure_plan():
    """Every enabled chapter has a bespoke builder."""
    for chapter in iter_chapters(load_config()):
        key = (chapter.part_id, chapter.stem)
        assert key in plots.CHAPTER_BUILDERS, f"missing bespoke builder for {key}"


@pytest.mark.parametrize(
    "fn",
    [builder for _, builder in _CANONICAL_BUILDERS],
    ids=[f"{part}_{stem}" for (part, stem), _ in _CANONICAL_BUILDERS],
)
def test_canonical_chapter_figures_write_png(tmp_path, fn):
    path = fn(tmp_path)
    _png_is_nonempty(path)


def test_generate_chapter_figures_emits_canonical_names(tmp_path):
    config = load_config()
    paths = plots.generate_chapter_figures(tmp_path, config)
    expected = {f"{chapter.part_id}_{chapter.stem}.png" for chapter in iter_chapters(config)}
    assert {path.name for path in paths} == expected
    for path in paths:
        _png_is_nonempty(path)


def test_generate_chapter_figures_dispatches_bespoke_not_placeholder(tmp_path):
    paths = plots.generate_chapter_figures(tmp_path, load_config())
    octave_map = next(path for path in paths if path.name == "part_0_octave-map.png")
    control = plots.placeholder_overview(
        "Nine Digits, Ninety-Nine Octaves", tmp_path / "control", "part_0_octave-map"
    )
    assert octave_map.read_bytes() != control.read_bytes()


@pytest.mark.slow
def test_generate_all_figures(tmp_path):
    worked = plots.generate_worked_figures(tmp_path)
    paths = plots.generate_all_figures(tmp_path)
    # all figures = worked figures + one unique figure per enabled chapter.
    assert len(paths) == len(worked) + len(plots.UNIT_INTRO_BUILDERS) + len(iter_chapters(load_config()))
    names = {p.name for p in paths}
    assert "logistic_growth.png" in names  # a worked figure
    assert "part_0_orientation.png" in names  # a bespoke engine-shelf timeline
    assert "part_II_singularity-crystal.png" in names  # a bespoke lattice figure
    assert "part_0_unit-intro.png" in names  # a unit-intro part-overview map


def test_figure_registry_entries_match_manuscript_labels(tmp_path):
    plots.generate_all_figures(tmp_path)
    entries = collect_figure_registry_entries(PROJECT_ROOT / "docs" / "manuscript", tmp_path)
    labels = {entry.label for entry in entries}
    assert "fig:part_0_orientation" in labels
    assert "fig:gallery_line" in labels
    assert "fig:part_III_frontiers" in labels
    assert labels <= set(FIGURE_ALT_TEXT)
    assert all(entry.alt.strip() for entry in entries)


def test_figure_registry_rejects_missing_explicit_alt_text(tmp_path):
    manuscript = tmp_path / "manuscript"
    figures = tmp_path / "figures"
    manuscript.mkdir()
    figures.mkdir()
    (manuscript / "chapter.md").write_text(
        "![A caption is not an alt-text substitute.](../figures/unknown.png){#fig:unknown}\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Missing explicit alt-text specification.*fig:unknown"):
        collect_figure_registry_entries(manuscript, figures)


@pytest.mark.slow
def test_figure_registry_validates_manuscript_references(tmp_path):
    paths = plots.generate_all_figures(tmp_path)
    from visualization.gallery import generate_gallery_figures

    paths.extend(generate_gallery_figures(tmp_path / "gallery"))
    manuscript_dir = PROJECT_ROOT / "docs" / "manuscript"
    registry = write_figure_registry(manuscript_dir, tmp_path)
    entries = collect_figure_registry_entries(manuscript_dir, tmp_path)

    missing = [entry.filename for entry in entries if not (tmp_path / entry.filename).exists()]
    blank_alt = [entry.label for entry in entries if not entry.alt.strip()]

    assert registry.exists()
    assert paths
    assert missing == [], missing
    assert blank_alt == [], blank_alt


def test_figure_registry_rejects_two_labels_claiming_one_filename(tmp_path):
    manuscript = tmp_path / "manuscript"
    figures = tmp_path / "figures"
    manuscript.mkdir()
    figures.mkdir()
    (manuscript / "chapter.md").write_text(
        "\n".join(
            (
                "![Bar.](../figures/shared.png){#fig:gallery_bar}",
                "![Line.](../figures/shared.png){#fig:gallery_line}",
            )
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="claimed by multiple labels"):
        collect_figure_registry_entries(manuscript, figures)


def test_scaffold_new_figure_and_save(tmp_path):
    fig, ax = _scaffold.new_figure(width=4, height=3)
    ax.plot([0, 1], [0, 1])
    path = _scaffold.save_figure(fig, tmp_path, "noext")
    _png_is_nonempty(path)
    assert path.name == "noext.png"


def test_cover_art(tmp_path):
    path = plots.cover_art(tmp_path, subtitle="A scaffold")
    _png_is_nonempty(path)
    assert path.name == "template_textbook_cover.png"


def test_cover_art_no_subtitle(tmp_path):
    """cover_art with no subtitle must still produce a valid PNG."""
    path = plots.cover_art(tmp_path)  # subtitle="" by default
    _png_is_nonempty(path)
    assert path.name == "template_textbook_cover.png"


def test_omnilattice_cover(tmp_path):
    path = plots.omnilattice_cover(tmp_path)
    _png_is_nonempty(path)
    assert path.name == "omnilattice_cover.png"


def test_omnilattice_cover_is_deterministic(tmp_path):
    """The cover must render byte-stable across runs and directories."""
    first = plots.omnilattice_cover(tmp_path / "a")
    second = plots.omnilattice_cover(tmp_path / "b")
    assert first.read_bytes() == second.read_bytes()


def test_figures_are_deterministic(tmp_path):
    first = tmp_path / "a"
    second = tmp_path / "b"
    p1 = plots.plot_logistic_growth(first)
    p2 = plots.plot_logistic_growth(second)
    assert p1.read_bytes() == p2.read_bytes()


def test_figure_registry_fallback_filename(tmp_path):
    """_figure_filename falls back to basename when path doesn't contain output/figures/."""
    from visualization.registry import _figure_filename

    # A path that doesn't contain 'output/figures' at all — the last-resort fallback.
    image_path = "/some/completely/different/path/my_figure.png"
    resolved = Path(image_path)
    figures_root = tmp_path / "output" / "figures"
    result = _figure_filename(image_path, resolved, figures_root)
    # Fallback: just the filename.
    assert result == "my_figure.png"


def test_figure_registry_extracts_from_output_figures_path(tmp_path):
    """_figure_filename extracts relative path from 'output/figures' segment."""
    from visualization.registry import _figure_filename

    # A path that has 'output/figures' in the middle.
    image_path = "../../output/figures/gallery/gallery_bar.png"
    resolved = (tmp_path / image_path).resolve()  # won't be under figures_root
    figures_root = tmp_path / "nowhere"  # resolved won't be relative to this
    result = _figure_filename(image_path, resolved, figures_root)
    # Should extract "gallery/gallery_bar.png"
    assert result == "gallery/gallery_bar.png"


def test_chapter_builders_cover_thirty_figures():
    """The upgraded composite figure plan ships exactly 30 bespoke builders."""
    assert len(plots.CHAPTER_BUILDERS) == 30


@pytest.mark.parametrize(
    "builder",
    [
        plots.plot_eddy_brake_inset,
        plots.plot_phi_growth_fibonacci,
        plots.plot_goldilocks_band_trace,
        plots.plot_frontiers_quadrant_map,
    ],
    ids=["eddy-brake-inset", "phi-growth-fibonacci", "goldilocks-band", "frontiers-quadrant"],
)
def test_upgraded_composites_are_byte_deterministic(tmp_path, builder):
    """Representative upgraded composites render byte-stable across runs and directories."""
    first = builder(tmp_path / "a")
    second = builder(tmp_path / "b")
    _png_is_nonempty(first)
    assert first.read_bytes() == second.read_bytes()


_POLISHED_BUILDERS = (
    plots.plot_register_bins_heatmap,
    plots.plot_octave_ladder,
    plots.plot_net_zero_balance_bars,
    plots.plot_prime_parity_numberline,
    plots.plot_xd_yd_interference,
    plots.plot_digit_drawer_bands,
)


@pytest.mark.parametrize(
    "builder",
    _POLISHED_BUILDERS,
    ids=["register-bins", "octave-ladder", "net-zero-bars", "prime-parity", "xd-yd-interference", "digit-drawers"],
)
def test_polished_builders_nonempty_and_byte_deterministic(tmp_path, builder):
    """Polished annotation-heavy builders stay valid PNGs and byte-stable across runs/dirs."""
    first = builder(tmp_path / "a")
    _png_is_nonempty(first)
    second = builder(tmp_path / "b")
    _png_is_nonempty(second)
    assert first.read_bytes() == second.read_bytes()


# ---------------------------------------------------------------------------
# Unit-intro part-overview figures and the extended gallery (shared contract).
# ---------------------------------------------------------------------------

from visualization import gallery as gallery_module  # noqa: E402

_INTRO_ITEMS = sorted(plots.UNIT_INTRO_BUILDERS.items())
_NEW_GALLERY_NAMES = (
    "octave_register",
    "phi_ladder",
    "prime_line",
    "damping_family",
    "net_zero_bars",
    "overlap_matrix",
)


@pytest.mark.parametrize("part,builder", _INTRO_ITEMS, ids=[part for part, _ in _INTRO_ITEMS])
def test_unit_intro_figures_write_contract_png(tmp_path, part, builder):
    path = builder(tmp_path)
    _png_is_nonempty(path)
    assert path.name == f"{part}_unit-intro.png"


def test_generate_intro_figures_emits_four_contract_names(tmp_path):
    paths = plots.generate_intro_figures(tmp_path)
    assert [p.name for p in paths] == [
        "part_0_unit-intro.png",
        "part_I_unit-intro.png",
        "part_II_unit-intro.png",
        "part_III_unit-intro.png",
    ]
    for path in paths:
        _png_is_nonempty(path)


@pytest.mark.parametrize(
    "builder",
    [plots.plot_part_I_unit_intro, plots.plot_part_III_unit_intro],
    ids=["part-I-intro", "part-III-intro"],
)
def test_unit_intro_figures_are_byte_deterministic(tmp_path, builder):
    first = builder(tmp_path / "a")
    second = builder(tmp_path / "b")
    _png_is_nonempty(first)
    assert first.read_bytes() == second.read_bytes()


@pytest.mark.parametrize("name", _NEW_GALLERY_NAMES)
def test_new_gallery_renderers_write_contract_png(tmp_path, name):
    path = gallery_module.render_gallery_entry({"name": name, "title": name}, tmp_path)
    _png_is_nonempty(path)
    assert path.name == f"gallery_{name}.png"


def test_gallery_specs_carry_six_new_entries():
    names = [spec["name"] for spec in gallery_module.load_specs()]
    assert len(names) == 18 + 6
    for name in _NEW_GALLERY_NAMES:
        assert name in names


def test_gallery_phi_ladder_is_byte_deterministic(tmp_path):
    first = gallery_module.phi_ladder_plot(tmp_path / "a")
    second = gallery_module.phi_ladder_plot(tmp_path / "b")
    _png_is_nonempty(first)
    assert first.read_bytes() == second.read_bytes()


def test_new_figure_labels_have_alt_text():
    expected = {f"fig:{part}_unit-intro" for part in plots.UNIT_INTRO_BUILDERS} | {
        f"fig:gallery_{name}" for name in _NEW_GALLERY_NAMES
    }
    assert expected <= set(FIGURE_ALT_TEXT)
    assert all(FIGURE_ALT_TEXT[label].strip() for label in expected)
