"""Nuclear Chemistry and Radiotracers: tracer principles, separation, activation analysis, decay corrections and radiation safety."""
CODE = "science5_chem_radiochem"
BOOK = {
    "title": "Nuclear Chemistry and Radiotracers",
    "subtitle": "Tracers, radiochemical separation, activation analysis and safe handling",
    "chapters": [
        ("Following an atom", "A radiotracer is a radioactive form of an element used to follow its path through a system. Because its radiation can be detected, it shows where the element goes. Tracers help answer questions that are hard to answer any other way."),
        ("Tracer principles", "A good tracer behaves the same chemically as the stable element it stands for. Its tiny amount should not change the system being studied. Its signal must be easy to detect over the background."),
        ("Radiochemical separation", "Radiochemical separation isolates a radioactive element from a mixture before it is measured. Chemists use precipitation, extraction and chromatography. Clean separation prevents false readings."),
        ("Activation analysis", "Neutron activation analysis makes stable atoms radioactive by bombarding a sample with neutrons. Each element then gives off characteristic radiation as it decays. Measuring these signals gives a sensitive analysis of trace elements."),
        ("Decay corrections", "Radioactive samples lose activity over time, and the decay follows the half-life of the isotope. Results must be corrected back to a reference time. A carbon-14 half-life of about 5730 years is a famous example in dating."),
        ("Radiation safety", "Radioactive materials need careful handling. The three main protections are time, distance and shielding. Monitoring badges and clear rules keep workers safe."),
    ],
    "test": [
        ("What is a radiotracer?",
         [("a", "A radioactive form of an element used to follow its path"), ("b", "A kind of radio set for music"), ("c", "A type of plastic bottle"), ("d", "A brand of paint")], "a"),
        ("What should a good tracer do?",
         [("a", "Change into a different element"), ("b", "Behave chemically like the stable element it stands for"), ("c", "Stop all reactions"), ("d", "Make the system heavier")], "b"),
        ("What does activation analysis do?",
         [("a", "Makes a sample colder"), ("b", "Turns a liquid into a gas"), ("c", "Paints a sample with radium"), ("d", "Makes stable atoms radioactive by neutron bombardment and measures the decay")], "d"),
        ("Why must radioactive results be decay-corrected?",
         [("a", "Because the sample gets bigger"), ("b", "Because the activity falls over time at the isotope's half-life"), ("c", "Because the sample changes colour"), ("d", "Because the sample becomes invisible")], "b"),
        ("What are the three main protections in radiation safety?",
         [("a", "Music, sleep and food"), ("b", "Heat, cold and wind"), ("c", "Paint, glue and tape"), ("d", "Time, distance and shielding")], "d"),
    ],
}
