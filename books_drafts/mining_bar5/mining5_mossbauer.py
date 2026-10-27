"""Mossbauer Spectroscopy of Iron: reading iron's oxidation, magnetism and minerals from a gamma-ray spectrum."""
CODE = 'mining5_mossbauer'
BOOK = {
    "title": 'Mössbauer Spectroscopy of Iron',
    "subtitle": "Reading iron's state from recoil-free gamma rays",
    "chapters": [
        ('Recoil-free gamma rays', 'In a solid, some gamma rays are emitted and absorbed without losing energy to recoil. This is the Mössbauer effect, named after Rudolf Mössbauer, who discovered it in the 1950s. It makes the energy of the gamma ray extremely precise.'),
        ('Oxidation states', 'The tiny shifts in the gamma-ray energy depend on the electrons around the iron nucleus. From these isomer shifts, scientists can tell whether iron is in the iron two or iron three state. This is the most common use of the method.'),
        ('Magnetic hyperfine fields', 'When iron is magnetic, the nucleus feels a magnetic field from its own electrons. This splits the spectrum into a pattern of six lines in a common case. The pattern reveals magnetic order in the sample.'),
        ('Iron minerals', 'Many iron minerals can be identified by their Mössbauer patterns, including hematite, magnetite and goethite. Geologists use the method to study rocks, soils and ancient pottery. Each mineral leaves a characteristic fingerprint.'),
        ('Sample types', 'Samples can be solid powders, thin foils or crystals containing iron-57, the isotope that the method uses. Thin, evenly spread samples give the cleanest spectra. Some measurements can be made at very low temperature.'),
        ('Reading spectra', 'A Mössbauer spectrum is a graph of counts against the velocity of the source. The positions, widths and relative areas of the peaks each tell part of the story. Fitting a model to the peaks gives the answer, and the fit must make chemical sense.'),
    ],
    "test": [
        ('What is the Mössbauer effect?', [('a', 'A way to make paint dry faster'), ('b', 'A kind of steel welding'), ('c', 'Gamma rays emitted and absorbed in a solid without losing energy to recoil'), ('d', 'A rule about the price of gold')], 'c'),
        ('What do isomer shifts help scientists identify in iron?', [('a', 'Whether the iron is in the iron two or iron three state'), ('b', 'The shape of a leaf'), ('c', 'The colour of the sky'), ('d', 'The number of bolts in a bridge')], 'a'),
        ('What does a six-line pattern in a spectrum usually reveal?', [('a', 'A broken detector'), ('b', 'Magnetic order in the sample'), ('c', 'The sample is made of glass only'), ('d', 'The room is too warm')], 'b'),
        ('Which iron mineral can be identified this way?', [('a', 'Table salt'), ('b', 'Chalk'), ('c', 'Quartz sand only'), ('d', 'Hematite')], 'd'),
        ('Which isotope does the method use in iron samples?', [('a', 'Iron-57'), ('b', 'Carbon-12'), ('c', 'Oxygen-16'), ('d', 'Helium-4')], 'a'),
    ],
}
