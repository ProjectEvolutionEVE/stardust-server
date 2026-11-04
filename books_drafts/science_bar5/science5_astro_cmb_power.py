"""CMB Anisotropy and the Power Spectrum: the faint temperature ripples in the oldest light we can see, and what their pattern tells us about the universe."""
CODE = 'science5_astro_cmb_power'
BOOK = {
    "title": 'CMB Anisotropy and the Power Spectrum',
    "subtitle": 'Ripples in the oldest light',
    "chapters": [
        ('The oldest light',
         'The cosmic microwave background is light left over from when the universe was about 380,000 years old. It now arrives as microwaves at a temperature of about 2.7 kelvin. It fills the whole sky.'),
        ('Temperature ripples',
         'The background is not perfectly smooth. Its temperature varies by about one part in 100,000 from place to place. These tiny differences are called anisotropies. They are the seeds of galaxies.'),
        ('Acoustic peaks',
         'The ripples form a pattern of peaks at particular sizes on the sky. These acoustic peaks come from sound waves in the hot early universe. Their positions tell us the shape of space.'),
        ('Polarisation',
         'Light from the background is slightly polarised, meaning its waves line up in a preferred direction. This pattern carries information about the early universe. Measuring it is a major goal of modern surveys.'),
        ('Power spectrum analysis',
         'The power spectrum shows how the strength of the ripples changes with angular size. Scientists fit this spectrum with a model of the universe. The best-fitting model gives the values of its key parameters.'),
        ('Removing foregrounds',
         'Our own galaxy and nearby sources emit signals that mix with the background. These are foregrounds. Scientists remove them carefully before reading the true background pattern.'),
    ],
    "test": [
        ('What is the cosmic microwave background?',
         [('a', 'Light from the Sun'), ('b', 'Leftover radiation from the early universe, at about 2.7 kelvin'), ('c', 'A car engine'), ('d', 'Radio from Mars')], 'b'),
        ('What are acoustic peaks?',
         [('a', 'Mountains on Earth'), ('b', 'Sound in space'), ('c', 'Peak sales'), ('d', 'Peaks in the ripple pattern made by sound waves in the early universe')], 'd'),
        ('What is polarisation in the background light?',
         [('a', 'A pattern in the direction of the light\'s waves that carries information about the early universe'), ('b', 'A type of battery'), ('c', 'A colour of the sky'), ('d', 'A rain of atoms')], 'a'),
        ('What is foreground removal?',
         [('a', 'Cleaning windows'), ('b', 'Moving the Earth'), ('c', 'Taking out signals from our own galaxy and nearby sources that mix with the background'), ('d', 'Stopping the Sun')], 'c'),
        ('What does the power spectrum show?',
         [('a', 'How the strength of temperature ripples varies with angular size'), ('b', 'The population of cities'), ('c', 'Radio stations'), ('d', 'The speed of a car')], 'a'),
    ],
}
