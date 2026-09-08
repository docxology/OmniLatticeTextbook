"""Shared structural contract for the Omni-Lattice textbook.

Everything that must agree across the manuscript, the figure generators, and the
tests lives here so there is exactly one place to change it:

* ``CITATION_KEYS``  — the keys defined in ``manuscript/references.bib``; chapter
  prose may only cite from this set (extend both together).
* ``GLOSSARY_ANCHORS`` — the ``{#gl:...}`` anchors defined in
  ``manuscript/glossary.md``; chapter prose may only link to these.
* ``REQUIRED_SECTION_HEADINGS`` / ``REQUIRED_TOKENS`` — the structural elements
  every chapter must contain. ``content.validate_chapter`` enforces them and
  ``content.scaffold_chapter`` always emits them, so a freshly scaffolded stub
  passes validation by construction.
* ``STUB_MARKERS`` — the markers authors search for to find what still needs
  writing. Counting them measures fill progress.
"""

from __future__ import annotations

# --- Bibliography -----------------------------------------------------------
# One key per source text of the Infinite Octaves Omni-Lattice corpus (author:
# Prudencio Mendez, SS Vibelandia ship blog). Keep references.bib and this
# tuple in sync (test_manuscript_integrity checks it).
CITATION_KEYS: tuple[str, ...] = (
    "mendez2026ship",
    "mendez2026livingPem",
    "mendez2026catalog",
    "mendez2026pdvsaGateway",
    "mendez2026pdvsaMockup",
    "mendez2026cmosProtonic",
    "mendez2026tensorDecoupling",
    "mendez2026masterSynthesis",
    "mendez2026digitsMaster",
    "mendez2026metamorphic",
    "mendez2026planetaryCore",
    "mendez2026yChromosome",
    "mendez2026invisibleFrontier",
    "mendez2026realityBridge",
    "mendez2026higgsGate",
    "mendez2026primeParity",
    "mendez2026stack",
    "mendez2026proteinFolding",
    "mendez2026volumetricStorage",
    "mendez2026protonTheater",
    "mendez2026topologyVoid",
    "mendez2026holographicRhyme",
    "mendez2026mdRhyme",
    "mendez2026singularityCrystal",
    "mendez2026zeroOctave",
    "mendez2026setRecycling",
    "mendez2026eddyMirror",
    "mendez2026metrologicalOverlap",
    "mendez2026viscosityLight",
    "mendez2026crystallineField",
    "mendez2026macroProtein",
)

# --- Glossary ---------------------------------------------------------------
# Anchors defined in manuscript/glossary.md. Vocabulary harvested from the
# corpus digests; every chapter may link only to these anchors.
GLOSSARY_ANCHORS: tuple[str, ...] = (
    "omni-lattice",
    "octave",
    "digit",
    "master-register",
    "catalog-architecture",
    "engine-shelf",
    "fair-exchange",
    "honesty-first",
    "narrative-empirical-operational-tiers",
    "living-pem",
    "tensor-decoupling",
    "master-synthesis",
    "fractal-constant",
    "golden-ratio",
    "prime-parity",
    "binary-dyad-anchor",
    "irreducible-minimum-set",
    "holographic-rhyme",
    "four-pillar-fractal",
    "multidimensional-rhyme",
    "topology-of-the-void",
    "higgs-gate",
    "proton-space",
    "electron-theater",
    "phi-duality",
    "viscosity-of-light",
    "eddy-current-mirror",
    "transduction-line",
    "c-bridge",
    "self-observation-drag",
    "crystalline-unified-field",
    "metrological-overlap",
    "net-zero",
    "singularity-crystal",
    "zero-octave",
    "node-k0",
    "cmos-protonic",
    "silicon-shelf",
    "prime-container",
    "volumetric-storage",
    "kinematic-set-recycling",
    "lattice-linear",
    "macro-protein",
    "reality-bridge",
)

# --- Chapter structural contract -------------------------------------------
# H2 headings every chapter must carry (Pandoc auto-numbers; no manual numbers).
REQUIRED_SECTION_HEADINGS: tuple[str, ...] = (
    "Learning Objectives",
    "Summary",
    "Key Terms",
    "Further Reading",
    "Practice",
)

# Literal tokens every chapter must contain (pandoc-crossref + pedagogy markers).
REQUIRED_TOKENS: tuple[str, ...] = (
    "{#sec:",  # section label on the H1
    "{#fig:",  # at least one cross-referencable figure
    "{#tbl:",  # at least one cross-referencable table
    "{#eq:",  # at least one cross-referencable equation
    "```mermaid",  # at least one inline diagram
    "<!-- chapter-metadata-badge -->",  # difficulty/time badge
    "<!-- curriculum-scaffold-start -->",  # study blueprint block
)

# Markers that flag unwritten content. ``content.count_stub_markers`` finds them.
STUB_MARKERS: tuple[str, ...] = ("<!-- STUB", "TODO:", "TKTK")

__all__ = [
    "CITATION_KEYS",
    "GLOSSARY_ANCHORS",
    "REQUIRED_SECTION_HEADINGS",
    "REQUIRED_TOKENS",
    "STUB_MARKERS",
]
