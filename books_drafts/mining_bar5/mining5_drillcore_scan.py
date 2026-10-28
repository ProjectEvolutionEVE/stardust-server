"""Core Scanning and Digital Logs: fast machines that scan drill core and turn what they see into digital logs linked to depth."""
CODE = "mining5_drillcore_scan"
BOOK = {
    "title": "Core Scanning and Digital Logs",
    "subtitle": "Scanner types, spectra, automated logs, photographs and integration",
    "chapters": [
        ("Scanning the core",
         "Drill core is a long cylinder of rock, and it holds the best record of what lies below. A core scanner measures it along its length, so every reading is tied to a depth. Scanning is quicker and more consistent than hand logging alone."),
        ("Scanner types",
         "Different scanners measure different things. Some read X-ray fluorescence, which shows elements. Others read magnetic susceptibility or colour. A mine may use several types on the same core."),
        ("Spectra",
         "Spectral scanners record light reflected from the core at many wavelengths. Each mineral has a pattern, so the spectrum helps name it. Spectral data can then be compared with lab results."),
        ("Automated logs",
         "The scanner's readings are turned into an automated log, a table of values by depth. Software can flag changes in rock type or alteration. A geologist still checks and corrects the log."),
        ("Photographs",
         "High-resolution photographs of each core tray are taken with a scale and a label. The photos are kept with the data. Anyone can later look at the rock without handling the core."),
        ("Integration and speed",
         "Scanner data are loaded into the same database as drill logs, assays and surveys. This makes it possible to view everything together. Fast scanning frees geologists to spend more time on interpretation."),
    ],
    "test": [
        ("What does a core scanner tie each reading to?",
         [("a", "The depth along the core"), ("b", "The colour of the lunch box"), ("c", "The name of the driver"), ("d", "The price of diesel")], "a"),
        ("What does an X-ray fluorescence scanner show?",
         [("a", "The elements in the rock"), ("b", "The number of cars in the car park"), ("c", "The noise of the drill"), ("d", "The taste of the water")], "a"),
        ("What do spectral scanners record?",
         [("a", "Sound from the drill"), ("b", "The smell of the rock"), ("c", "Light reflected from the core at many wavelengths"), ("d", "The weight of the crew")], "c"),
        ("Who checks the automated log?",
         [("a", "Nobody, the machine is always right"), ("b", "The drill operator alone"), ("c", "The caterer"), ("d", "A geologist, who corrects it where needed")], "d"),
        ("Why are core photographs kept with the data?",
         [("a", "So the core can be eaten"), ("b", "So anyone can look at the rock without handling the core"), ("c", "So the photos can be sold as posters"), ("d", "So the scanner can be switched off")], "b"),
    ],
}
