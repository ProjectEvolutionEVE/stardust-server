"""Light and the Spectrum: how astronomers learn what stars are made of, and how fast they move, from their light. Science career, bar 2 (Scientist)."""
CODE = 'science2_spectrum'
BOOK = {
    "title": 'Light and the Spectrum',
    "subtitle": 'How astronomers learn what stars are made of from their light',
    "chapters": [
        ('Light is a wave',
         'Visible light is a small band of electromagnetic waves, with wavelengths from about 380 to 750 nanometres. Red has the longest visible wavelength and violet the shortest. Beyond the red lie infrared and radio waves, and beyond the violet lie ultraviolet, X-rays and gamma rays.'),
        ('Splitting white light',
         'White light is a mix of all the visible colours. A prism or a raindrop splits it into a rainbow, called a spectrum, because each colour bends by a slightly different amount. The spectrum shows exactly which colours a light source contains.'),
        ('Atoms leave fingerprints',
         'Each chemical element absorbs or gives off light only at specific wavelengths. Hot gas glows in bright lines at those wavelengths. Cooler gas in front of a hot source leaves dark lines at the same wavelengths. Those lines are a kind of fingerprint.'),
        ('Reading a star',
         'Astronomers spread a star\'s light into a spectrum and look for the dark lines. Each set of lines matches a known element, so the lines show which elements are in the star\'s outer layers. Hydrogen is the most common, and it leaves strong lines in many stars.'),
        ('Helium, found in the Sun first',
         'In 1868, astronomers saw a bright yellow line in the Sun\'s spectrum that matched no known element on Earth. They named the element helium, after the Greek word for the Sun. It was found on Earth only in 1895.'),
        ('Moving light tells speed',
         'When a light source moves away from us, its light is stretched toward red. When it moves toward us, the light is squeezed toward blue. This is the Doppler shift, and astronomers use it to measure how fast stars and galaxies move.'),
    ],
    "test": [
        ('What do chemical elements do to light?',
         [('a', 'They bend all colours equally'), ('b', 'They make all light white'), ('c', 'They stop all light'), ('d', 'They absorb or give off light at specific wavelengths')], 'd'),
        ('Which visible colour has the longest wavelength?',
         [('a', 'Violet'), ('b', 'Green'), ('c', 'Red'), ('d', 'Blue')], 'c'),
        ('What can astronomers learn from a star\'s spectrum?',
         [('a', 'Which elements are in its outer layers'), ('b', 'How many planets orbit it'), ('c', 'Whether it has a name'), ('d', 'The exact day it will die')], 'a'),
        ('What is the shift that shows whether a light source is moving away or toward us?',
         [('a', 'Refraction'), ('b', 'The Doppler shift'), ('c', 'Diffraction'), ('d', 'Reflection')], 'b'),
        ('Which element was spotted in the Sun\'s spectrum before anyone found it on Earth?',
         [('a', 'Gold'), ('b', 'Helium'), ('c', 'Carbon'), ('d', 'Neon')], 'b'),
    ],
}
