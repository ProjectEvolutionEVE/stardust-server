"""Nuclear Magnetic Resonance in Practice: how NMR spectra reveal molecular structure through chemical shift, coupling and integration."""
CODE = "science4_chem_nmr"
BOOK = {
    "title": "Nuclear Magnetic Resonance in Practice",
    "subtitle": "Reading the spectrum that shows where the atoms are",
    "chapters": [
        ("Chemical shift",
         "Chemical shift is the position of a signal in the spectrum, measured in parts per million. Nuclei in different chemical surroundings resonate at slightly different frequencies. The shift helps identify the kind of group each signal comes from."),
        ("Spin coupling",
         "Neighbouring nuclei can split a signal into several peaks, a pattern called spin coupling. The number of peaks in a multiplet is usually one more than the number of equivalent neighbours. This shows which atoms are next to each other."),
        ("Reading a spectrum",
         "To read a spectrum, look at the chemical shift, the splitting and the integration together. Each feature supports the others. A clear reading builds a picture of the molecule piece by piece."),
        ("Integration",
         "The area under each signal is proportional to the number of nuclei that give rise to it. Integration tells you the relative numbers of each kind of hydrogen. It is one of the most useful clues in a spectrum."),
        ("Structure from spectra",
         "By combining shifts, splitting and integrals, chemists propose a structure that fits all the data. The proposed structure must explain every peak. A structure that leaves a peak unexplained must be revised."),
        ("Sample preparation",
         "A good spectrum needs a clean sample dissolved in a suitable deuterated solvent. Impurities and water can add unwanted peaks. Careful preparation makes the spectrum easier to read and the structure easier to trust."),
    ],
    "test": [
        ("In what unit is chemical shift measured?",
         [("a", "Parts per million"), ("b", "Grams"), ("c", "Litres"), ("d", "Kelvin")], "a"),
        ("What does spin coupling show?",
         [("a", "The colour of the sample"), ("b", "Which atoms are next to each other"), ("c", "The temperature of the room"), ("d", "The weight of the tube")], "b"),
        ("If a signal has two equivalent neighbours, how many peaks is it usually split into?",
         [("a", "One"), ("b", "Two"), ("c", "Three"), ("d", "Four")], "c"),
        ("What does the integration of a signal tell you?",
         [("a", "The melting point of the sample"), ("b", "The relative number of nuclei that give rise to it"), ("c", "The age of the sample"), ("d", "The shape of the flask")], "b"),
        ("Why is a clean sample important?",
         [("a", "Because clean samples are heavier"), ("b", "Because dirt makes the spectrum faster"), ("c", "Because samples must be brown"), ("d", "Because impurities can add unwanted peaks")], "d"),
    ],
}
