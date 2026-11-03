"""Mass Spectrometry Methods in Depth: ionisation, mass analysers, fragmentation, isotope patterns and quantitative work."""
CODE = "science5_chem_mass_spec"
BOOK = {
    "title": "Mass Spectrometry Methods in Depth",
    "subtitle": "Ionisation, mass analysers, fragmentation and isotope patterns",
    "chapters": [
        ("Weighing molecules", "Mass spectrometry measures the mass-to-charge ratio of ions. It can identify a compound and reveal its structure. Samples are first turned into charged particles."),
        ("Ionisation methods", "Electron ionisation knocks electrons off molecules, often at 70 electronvolts in standard instruments. Softer methods such as electrospray keep large molecules more intact. The choice of method depends on the sample."),
        ("Mass analysers", "A mass analyser separates ions by their mass-to-charge ratio. Quadrupoles, time-of-flight tubes and magnetic sectors are common types. High-resolution analysers can give very precise masses."),
        ("Fragmentation patterns", "Ions often break into smaller pieces, and the pattern of pieces is characteristic of the molecule. Chemists read these patterns like a fingerprint. Careful analysis of the fragments helps identify unknown compounds."),
        ("Isotope patterns", "Elements such as chlorine and bromine have isotopes in known ratios. Chlorine gives a peak about one third the height of its partner two mass units higher. Bromine gives two peaks of nearly equal height. These patterns show whether these elements are present."),
        ("Tandem methods and quantification", "Tandem mass spectrometry selects one ion, breaks it and analyses the pieces. It is very sensitive and selective. Quantitative work needs calibration with known standards."),
    ],
    "test": [
        ("What does a mass spectrometer measure?",
         [("a", "The colour of a liquid"), ("b", "The mass-to-charge ratio of ions"), ("c", "The temperature of a flame"), ("d", "The loudness of a sound")], "b"),
        ("What energy is standard for electron ionisation?",
         [("a", "About 7 kilograms"), ("b", "About 700 metres"), ("c", "About 0.07 seconds"), ("d", "About 70 electronvolts")], "d"),
        ("What ratio do the chlorine isotope peaks show?",
         [("a", "About one to one hundred"), ("b", "Always equal"), ("c", "About twenty to one"), ("d", "About three to one")], "d"),
        ("What is tandem mass spectrometry?",
         [("a", "Selecting an ion, breaking it, and analysing the pieces"), ("b", "Two machines stuck together with tape"), ("c", "A method that does not use ions"), ("d", "A method for measuring sound")], "a"),
        ("Why is calibration needed in quantitative work?",
         [("a", "To paint the instrument"), ("b", "To stop the ions from forming"), ("c", "To relate the signal to known amounts"), ("d", "To change the mass of the sample")], "c"),
    ],
}
