"""Transit Photometry and Planet Characterisation: how a dip in a star's light reveals the size, orbit and other secrets of a planet passing in front of it."""
CODE = 'science5_astro_transit_phot'
BOOK = {
    "title": 'Transit Photometry and Planet Characterisation',
    "subtitle": 'Reading a planet from a dip in starlight',
    "chapters": [
        ('The transit',
         'When a planet passes in front of its star, the star dims for a short time. This event is called a transit. The dip is small, often well under one percent of the light.'),
        ('Transit depth',
         'The depth of the dip is roughly the planet\'s radius squared divided by the star\'s radius squared. A bigger planet blocks more light. Depth gives a first estimate of the planet\'s size.'),
        ('Limb darkening',
         'Stars are brighter at the centre than at the edge, so the light dims in a curved way during a transit. This limb darkening changes the shape of the light curve. Models must include it to get accurate sizes.'),
        ('Transit timing variations',
         'Transit timing variations are small shifts in when transits happen. They can reveal another planet pulling on the one that transits. Timing is often more sensitive than depth.'),
        ('Phase curves',
         'A phase curve tracks how a planet\'s brightness changes over one full orbit. It shows the light the planet reflects or emits from different sides. Phase curves give clues about the planet\'s atmosphere.'),
        ('Photometric noise',
         'Noise from the star, the instrument and the sky limits how well a transit can be measured. Long observations and careful corrections reduce the noise. Clean data is needed for reliable planet sizes.'),
    ],
    "test": [
        ('What is transit depth?',
         [('a', 'The fraction of starlight blocked by the planet, roughly the planet radius squared over the star radius squared'), ('b', 'The depth of an ocean'), ('c', 'A kind of tunnel'), ('d', 'Snow on a hill')], 'a'),
        ('What does limb darkening change in a transit?',
         [('a', 'The colour of the planet'), ('b', 'The size of the Moon'), ('c', 'The shape of the light curve during the transit'), ('d', 'The date of the Moon landing')], 'c'),
        ('What are transit timing variations?',
         [('a', 'Changes in the price of a clock'), ('b', 'Speeches of astronomers'), ('c', 'Weather forecasts'), ('d', 'Small shifts in when transits happen, which can reveal other planets')], 'd'),
        ('What is a phase curve?',
         [('a', 'A bent road'), ('b', 'The change in a planet\'s brightness over one orbit'), ('c', 'A kind of ruler'), ('d', 'A type of coin')], 'b'),
        ('What limits how precisely a transit can be measured?',
         [('a', 'The colour of a pencil'), ('b', 'The price of coffee'), ('c', 'The number of moons of Saturn'), ('d', 'Photometric noise from the star, the instrument and the sky')], 'd'),
    ],
}
