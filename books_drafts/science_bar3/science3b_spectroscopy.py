"""Spectroscopy: Reading Light From a Sample: measuring the light a sample absorbs, and using it to find out what is there. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_spectroscopy'
BOOK = {
    "title": 'Spectroscopy: Reading Light From a Sample',
    "subtitle": 'Measuring the light a sample absorbs, and using it to find out what is there',
    "chapters": [
        ('Each substance takes in its own light',
         'Many substances absorb some wavelengths of light and let others pass. The pattern of absorbed light is a kind of fingerprint for that substance. Spectroscopy is the study of those patterns.'),
        ('Absorbance and concentration',
         'Absorbance measures how much light a sample takes in. For a dissolved substance, a more concentrated sample usually absorbs more. Over a useful range the link is close to a straight line, which is the idea behind the Beer-Lambert law.'),
        ('A calibration line',
         'To find an unknown, first measure the absorbance of several standard solutions with known concentrations. Plot them to make a calibration line. Then measure the unknown and read its concentration from that line.'),
        ('Infrared and bonds',
         'Infrared spectroscopy shows which bonds a molecule has, because each kind of bond vibrates at its own frequency. An O-H bond and a C-H bond absorb at different places. The spectrum tells you which groups are present.'),
        ('Mass spectrometry',
         'A mass spectrometer turns a sample into ions and sorts them by their mass to charge ratio. The pattern of peaks shows the masses of the pieces, which helps identify an unknown compound.'),
        ('Keeping the measurement honest',
         'Clean the sample cell, use a blank of pure solvent, and check that the instrument reads zero on it. Small errors add up when you work from a calibration line. Write down every setting you used.'),
    ],
    "test": [
        ("What does a substance's absorption pattern act like?",
         [('a', 'A fingerprint for the substance'), ('b', 'A recipe for its price'), ('c', 'A measure of its mass only'), ('d', 'Its colour name')], 'a'),
        ('For a dissolved substance, what usually happens to absorbance as concentration rises?',
         [('a', 'It drops to zero'), ('b', 'It stays the same'), ('c', 'It flips sign'), ('d', 'It usually rises, roughly in a straight line over a useful range')], 'd'),
        ('Why measure several standard solutions first?',
         [('a', 'To make a calibration line for reading an unknown'), ('b', 'To use up the instrument'), ('c', 'To change the colour of the sample'), ('d', 'To find the density of water')], 'a'),
        ('What does infrared spectroscopy mainly reveal?',
         [('a', 'The price of a sample'), ('b', 'The smell of a sample'), ('c', 'The bonds present in a molecule'), ('d', 'The number of protons in one atom only')], 'c'),
        ('What does a mass spectrometer sort ions by?',
         [('a', 'Colour'), ('b', 'Temperature'), ('c', 'Taste'), ('d', 'Mass to charge ratio')], 'd'),
    ],
}
