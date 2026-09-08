from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path

_IMAGE_LABEL_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+\.png)\)\{#(fig:[-A-Za-z0-9_.:]+)(?:\s[^}]*)?\}")
_SKIPPED_DOCS = frozenset({"AGENTS.md", "README.md", "SYNTAX.md"})

FIGURE_ALT_TEXT: dict[str, str] = {
    "fig:gallery_line": "Three sinusoidal curves share one time axis, with progressively higher oscillation frequency.",
    "fig:gallery_scatter_fit": "A scatter of points with a fitted straight line summarizing the trend.",
    "fig:gallery_bar": "A vertical bar chart compares several labeled categories, with bar height encoding each category's value.",
    "fig:gallery_grouped_bar": "Grouped vertical bars compare two series across several labeled categories.",
    "fig:gallery_hbar": "A horizontal bar chart ranks categories by the length of each bar.",
    "fig:gallery_histogram": "A histogram bins many samples, with bar heights encoding per-bin counts.",
    "fig:gallery_box": "A box plot summarizes each category's spread with quartile boxes and whiskers.",
    "fig:gallery_violin": "A violin plot shows each category's distribution as a mirrored density shape.",
    "fig:gallery_heatmap": "A rectangular heatmap uses a light-to-dark color scale to encode values across rows and columns.",
    "fig:gallery_media": "A rectangular heatmap uses a light-to-dark color scale to encode values across rows and columns.",
    "fig:gallery_quiver": "A vector field of arrows shows direction and magnitude across a grid.",
    "fig:gallery_step": "A step plot changes value at discrete thresholds, drawn as connected horizontal and vertical segments.",
    "fig:gallery_stacked_area": "A stacked area chart accumulates several series into layered bands over one axis.",
    "fig:gallery_errorbar": "Six condition means rise from left to right; every point has a vertical standard-error interval.",
    "fig:gallery_loglog": "A log-log plot shows a power law as a straight descending line.",
    "fig:gallery_pie": "A circular chart is divided into labeled slices whose angles encode category proportions.",
    "fig:gallery_annotated": "An annotated curve highlights specific points with callout labels.",
    "fig:gallery_multipanel": "A two-by-two composite contains a line chart, scatter plot, bar chart, and histogram.",
    "fig:part_0_orientation": "A timeline of the engine shelf places each corpus paper at its shelf position from the CMOS/protonic bridge to the frontier notes.",
    "fig:part_0_living-pem": "A staged ladder plot walks the Living PEM engineering lifecycle from filing to pinning.",
    "fig:part_0_tensor-decoupling": "A digit-by-octave heatmap shows the nine drawer rows and ninety-nine band columns of the master register.",
    "fig:part_0_master-synthesis": "A cross-link adjacency heatmap maps which corpus papers reference one another.",
    "fig:part_0_octave-map": "The ninety-nine octave ladder rises with golden-ratio spaced band boundaries across the register.",
    "fig:part_I_fractal-constant": "Powers of Phi grow on a log scale while Fibonacci ratios oscillate toward the same constant.",
    "fig:part_I_prime-parity": "Primes sit on a number line with the sole-even anchor highlighted against odd-prime classes.",
    "fig:part_I_holographic-rhyme": "A four-pillar interference field shows constructive and destructive rhyme across the plane.",
    "fig:part_I_multidimensional-rhyme": "Contour bands show the xD plus-or-minus yD combination of two interference fields.",
    "fig:part_I_topology-void": "A potential well bottoms out at zero with restoring arrows pointing back to equilibrium.",
    "fig:part_I_higgs-awareness": "A family of slowing curves shows mass-weighted gating toward a shared Now.",
    "fig:part_II_proton-theater": "A symmetric mirror plot contrasts x times Phi against x divided by Phi.",
    "fig:part_II_viscosity-light": "A family of viscous damping curves decays at different drag coefficients.",
    "fig:part_II_eddy-current-mirror": "An eddy brake curve decays exponentially with an inset showing the drag force.",
    "fig:part_II_crystalline-field": "Iso-lines of constant travel time lattice the speed-distance plane.",
    "fig:part_II_metrological-overlap": "A pairwise heatmap scores metrological overlap between unit families.",
    "fig:part_II_metamorphic-octaves": "The densification curve rises logarithmically with exposure.",
    "fig:part_II_planetary-core": "A value trace crosses shaded goldilocks bands marking the viable region.",
    "fig:part_II_singularity-crystal": "Inflow and outflow balance bars cancel to a zero residual at the crystal node.",
    "fig:part_III_cmos-protonic": "Stacked bars allocate octave bands across silicon shelf tiers.",
    "fig:part_III_protein-folding": "Prime-container capacity grows through unique prime-indexed addresses.",
    "fig:part_III_volumetric-storage": "A scatter lattice shows prime-indexed addresses filling volumetric space.",
    "fig:part_III_kinematic-recycling": "A round-robin cycle moves active sets through parked and recycled states over time.",
    "fig:part_III_moving-up-stack": "A step plot climbs the stack from model layer to lattice layer to agent layer.",
    "fig:part_III_reality-bridge": "A radial plot sweeps bridge and router throughput across orientations.",
    "fig:part_III_y-chromosome": "A bar chart manifests digit four's sub-bands within the register.",
    "fig:part_III_pdvsa-gateway": "A lattice-linear flow ramps linearly through the gateway stages.",
    "fig:part_III_macro-protein": "The macro-protein work engine's output curve rises with each work cycle.",
    "fig:part_III_invisible-frontier": "A visibility threshold curve separates the visible frontier from the invisible one.",
    "fig:part_III_frontiers": "A quadrant map places open problems by value and effort for the research program.",
}


@dataclass(frozen=True)
class FigureRegistryEntry:
    """One figure cross-referenced from manuscript prose to its generated file.

    Captures the label used in `{#fig:...}` markdown attributes, the figure's
    filename relative to `output/figures/`, its caption text, the manuscript
    file that references it, and the script responsible for generating it —
    the row shape written into `figure_registry.json`.
    """

    label: str
    filename: str
    caption: str
    alt: str
    source_markdown: str
    generated_by: str


def collect_figure_registry_entries(manuscript_dir: Path, figures_dir: Path) -> tuple[FigureRegistryEntry, ...]:
    """Collect figure registry entries from a directory."""
    entries: dict[str, FigureRegistryEntry] = {}
    filename_owners: dict[str, str] = {}
    figures_root = figures_dir.resolve()
    for markdown_file in sorted(manuscript_dir.rglob("*.md")):
        if markdown_file.name in _SKIPPED_DOCS:
            continue
        text = markdown_file.read_text(encoding="utf-8")
        for caption, image_path, label in _IMAGE_LABEL_RE.findall(text):
            resolved = (markdown_file.parent / image_path).resolve()
            filename = _figure_filename(image_path, resolved, figures_root)
            existing_owner = filename_owners.get(filename)
            if existing_owner is not None and existing_owner != label:
                raise ValueError(
                    f"Figure filename {filename!r} is claimed by multiple labels: {existing_owner}, {label}"
                )
            filename_owners[filename] = label
            try:
                alt = FIGURE_ALT_TEXT[label]
            except KeyError as exc:
                raise ValueError(f"Missing explicit alt-text specification for manuscript figure: {label}") from exc
            entries.setdefault(
                label,
                FigureRegistryEntry(
                    label=label,
                    filename=filename,
                    caption=caption,
                    alt=alt,
                    source_markdown=markdown_file.relative_to(manuscript_dir).as_posix(),
                    generated_by="scripts/generate_figures.py",
                ),
            )
    return tuple(entries[label] for label in sorted(entries))


def _figure_filename(image_path: str, resolved: Path, figures_root: Path) -> str:
    try:
        return resolved.relative_to(figures_root).as_posix()
    except ValueError:
        parts = Path(image_path).parts
        for index in range(len(parts) - 1):
            if parts[index : index + 2] == ("output", "figures"):
                return Path(*parts[index + 2 :]).as_posix()
        return Path(image_path).name


def write_figure_registry(manuscript_dir: Path, figures_dir: Path) -> Path:
    """Write the figure registry to a JSON file."""
    figures_dir.mkdir(parents=True, exist_ok=True)
    path = figures_dir / "figure_registry.json"
    payload = {
        "schema_version": "template-textbook-figure-registry-v1",
        "figures": [asdict(entry) for entry in collect_figure_registry_entries(manuscript_dir, figures_dir)],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


__all__ = [
    "FIGURE_ALT_TEXT",
    "FigureRegistryEntry",
    "collect_figure_registry_entries",
    "write_figure_registry",
]
