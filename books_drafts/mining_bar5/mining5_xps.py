"""X-ray Photoelectron Spectroscopy: reading the chemistry at the surface of a material."""
CODE = 'mining5_xps'
BOOK = {
    "title": 'X-ray Photoelectron Spectroscopy',
    "subtitle": "Reading the chemistry at a material's surface",
    "chapters": [
        ('Binding energies', "In XPS, X-rays knock electrons out of a sample. Each electron's energy tells scientists how strongly it was held, called its binding energy. Each element has its own set of binding energies, so the spectrum identifies what is present."),
        ('Surface chemistry', 'XPS is surface sensitive, because electrons from deep inside a solid cannot escape to reach the detector. It typically samples only the top few nanometres. This makes it ideal for studying coatings, corrosion and catalysts.'),
        ('Depth', 'By tilting the sample or changing the X-ray energy, scientists can look at slightly different depths. Comparing the signals shows how a layer changes from the surface inward. This gives a rough depth profile.'),
        ('Oxidation states', 'The binding energy shifts slightly when an atom gains or loses electrons. These chemical shifts reveal oxidation states, such as whether iron is in one form or another. This is one of the most useful features of the method.'),
        ('Calibration', 'Because instruments drift, scientists calibrate the energy scale against a known reference. A common reference is the carbon peak from surface contamination, set to about 284.8 electron volts. A careful calibration makes results comparable between labs.'),
        ('Interpretation', 'Reading an XPS spectrum takes care, since peaks can overlap and background signals must be removed. Good analysts compare with reference spectra from known samples. Honest reporting includes how sure the fit is.'),
    ],
    "test": [
        ('What do binding energies in XPS help identify?', [('a', 'Which elements are present'), ('b', 'The taste of the sample'), ('c', 'The sound of the X-ray tube'), ('d', 'The price of the sample')], 'a'),
        ('Why is XPS called surface sensitive?', [('a', 'It only works on liquids'), ('b', 'It burns the surface away'), ('c', 'Electrons from deep inside cannot escape to the detector'), ('d', 'It measures only the air')], 'c'),
        ('What do chemical shifts reveal?', [('a', 'The size of the detector'), ('b', 'The age of the building'), ('c', 'How loud the instrument is'), ('d', 'Oxidation states of the atoms')], 'd'),
        ('What is a common reference used to calibrate the energy scale?', [('a', 'The temperature of the lab'), ('b', 'The carbon peak from surface contamination, near 284.8 electron volts'), ('c', 'The weight of the sample tray'), ('d', 'The number of people in the room')], 'b'),
        ('Why do careful analysts compare spectra with reference spectra?', [('a', 'To make the peaks taller on purpose'), ('b', 'To remove the need for X-rays'), ('c', 'To interpret overlapping peaks from known samples'), ('d', "To change the element's name")], 'c'),
    ],
}
