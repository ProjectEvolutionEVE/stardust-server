"""Radio Interferometry and Aperture Synthesis: how linking telescopes far apart can build an image as sharp as a single dish many kilometres across."""
CODE = 'science5_astro_interferometry'
BOOK = {
    "title": 'Radio Interferometry and Aperture Synthesis',
    "subtitle": 'Many telescopes acting as one',
    "chapters": [
        ('Working as a team',
         'An interferometer links several radio telescopes so they act together. The combined instrument can see far more sharply than any one dish. The trick works because the signals are combined carefully.'),
        ('Baselines',
         'A baseline is the distance between two telescopes in the array. Longer baselines reveal finer detail in the sky. Each pair of telescopes gives one baseline.'),
        ('Visibilities',
         'A visibility is a measured value from one pair of telescopes. It records part of the interference pattern of the incoming waves. Each visibility carries information about the sky.'),
        ('Fourier imaging',
         'The visibilities are related to the image through the Fourier transform. Computers turn many visibilities into an image of the sky. Filling in more of this mathematical map gives a cleaner picture.'),
        ('Array design',
         'The layout of an array decides which baselines it can measure. Designers spread telescopes out so that many baselines are covered. A good layout gives a sharper and more complete image.'),
        ('Very-long-baseline interferometry',
         'Very-long-baseline interferometry links telescopes across continents, or even across the globe. The sharpness it gives is extreme. The Event Horizon Telescope used this method to image a black hole\'s shadow in 2019.'),
    ],
    "test": [
        ('What is a baseline in interferometry?',
         [('a', 'The height of a building'), ('b', 'The colour of a star'), ('c', 'A starting line in a race'), ('d', 'The distance between two telescopes in the array')], 'd'),
        ('What is a visibility?',
         [('a', 'A type of cloud'), ('b', 'A measured value from one pair of telescopes that carries information about the sky'), ('c', 'The brightness of the Moon'), ('d', 'A way of seeing with bare eyes')], 'b'),
        ('What does Fourier imaging do?',
         [('a', 'It cooks food'), ('b', 'It paints a map'), ('c', 'It turns many measured visibilities into an image of the sky'), ('d', 'It counts stars')], 'c'),
        ('Why are many baselines useful?',
         [('a', 'They fill in more of the mathematical map, giving a sharper image'), ('b', 'They make the sky darker'), ('c', 'They slow down the Earth'), ('d', 'They replace the need for calibration')], 'a'),
        ('What is very-long-baseline interferometry?',
         [('a', 'Radio jokes'), ('b', 'A type of train'), ('c', 'Linking telescopes across continents or the globe to make a very sharp image'), ('d', 'A single telescope on a hill')], 'c'),
    ],
}
