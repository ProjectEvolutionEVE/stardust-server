"""Hyperspectral Core Imaging: scanning drill core with many light bands to map minerals, and why calibration and data volume matter."""
CODE = "mining5_hsi_core"
BOOK = {
    "title": "Hyperspectral Core Imaging",
    "subtitle": "Mapping minerals across drill core with many bands of light",
    "chapters": [
        ("Spectral range", "A hyperspectral camera records light across many narrow bands, often from visible to short-wave infrared. Each mineral reflects a characteristic pattern across these bands. That pattern is its spectral fingerprint."),
        ("Mineral mapping", "Scanning a drill core builds a map of the minerals along its length. Geologists identify clay, carbonate and iron minerals from their fingerprints. The map is a fast, consistent record of the core."),
        ("Scan speed", "Hyperspectral scanners can cover a core much faster than hand logging. Speed lets teams log more core in less time. Scanning must still be done carefully so the image is sharp."),
        ("Calibration", "Calibration uses reference panels and known minerals to make sure readings are accurate. Without it, colours and spectra can drift. Teams calibrate before each scan."),
        ("Interpretation", "The spectra must be interpreted by a trained geologist. Some minerals look alike, so checks against laboratory data are needed. The map is a guide, not a final answer."),
        ("Data volume", "A single core scan produces a very large data file. Storage and processing need planning from the start. Good data management keeps scans usable for years."),
    ],
    "test": [
        ("What does a hyperspectral camera record?",
         [("a", "Only sound"), ("b", "Only smell"), ("c", "Only touch"), ("d", "Light across many narrow bands")], "d"),
        ("What is a spectral fingerprint?",
         [("a", "A mark left by a finger"), ("b", "A type of stamp"), ("c", "A pattern of reflected light that is typical of a mineral"), ("d", "A kind of map")], "c"),
        ("Why is calibration done before each scan?",
         [("a", "So the core gets heavier"), ("b", "So readings stay accurate and do not drift"), ("c", "So the scanner makes a sound"), ("d", "So the core turns blue")], "b"),
        ("Why must a geologist check the spectra?",
         [("a", "Some minerals look alike, so laboratory checks are needed"), ("b", "Spectra are always perfect"), ("c", "Spectra only show the time"), ("d", "Spectra never change")], "a"),
        ("What does a hyperspectral scan produce?",
         [("a", "A tiny note on paper"), ("b", "A cake"), ("c", "A song"), ("d", "A very large data file that needs planning")], "d"),
    ],
}
