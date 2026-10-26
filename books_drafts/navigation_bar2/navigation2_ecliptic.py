"""The Ecliptic and Space Coordinates: positions around the Sun, from a flat reference plane and a fixed starting direction."""
CODE = 'navigation2_ecliptic'
BOOK = {
    "title": 'The Ecliptic and Space Coordinates',
    "subtitle": 'Measuring positions around the Sun, from a flat plane and a fixed starting line',
    "chapters": [
        ('Centre on the Sun',
         'Heliocentric means centred on the Sun. A heliocentric chart puts the Sun at the middle and measures every object from there. It lets the positions of all the planets be compared directly, on one picture.'),
        ('The ecliptic plane',
         'The ecliptic is the flat plane in which the Earth travels round the Sun. Most of the planets orbit close to this same plane, so their paths look like flat rings when seen from above. A position can then be given as an angle around the plane, and a height above or below it.'),
        ('Latitude and longitude in space',
         'In space, longitude is the angle around the ecliptic plane, measured from a fixed starting direction. Latitude is the angle above or below the plane. It is the same idea as on Earth, with the ecliptic playing the part of the equator.'),
        ('The tilt of the spin axis',
         'The Earth\'s spin axis is tilted about 23.4 degrees away from the perpendicular to the ecliptic. That tilt is the reason we have seasons. A navigator has to use the right reference plane for each job, because the plane changes the numbers.'),
        ('A unit for the scale',
         'Astronomers measure distances around the Sun in astronomical units. One AU is the average distance from the Earth to the Sun. A planet\'s distance in AU, together with its angle in the plane, fixes where it sits on a flat chart.'),
        ('Stating the reference',
         'A chart of space should always say which plane and which starting direction it uses. Otherwise a height above the plane could be mistaken for a distance across it. Two charts that use different references can disagree while both being correct.'),
    ],
    "test": [
        ('What does heliocentric mean?',
         [('a', 'Centred on the Earth'), ('b', 'Centred on the Sun'), ('c', 'Centred on the Moon'), ('d', 'Centred on the Starship')], 'b'),
        ('What is the ecliptic?',
         [('a', 'The flat plane in which the Earth travels round the Sun'), ('b', 'A kind of comet'), ('c', 'A line of radar returns'), ('d', 'The path of the Moon round the Earth')], 'a'),
        ('In space, what does latitude measure?',
         [('a', 'The distance from the Earth'), ('b', 'The speed of a planet'), ('c', 'The height of a mountain'), ('d', 'The angle above or below the reference plane')], 'd'),
        ('About how far is the Earth\'s spin axis tilted from the perpendicular to the ecliptic?',
         [('a', 'About 2.3 degrees'), ('b', 'About 0 degrees'), ('c', 'About 23.4 degrees'), ('d', 'About 90 degrees')], 'c'),
        ('What is one astronomical unit?',
         [('a', 'The average distance from the Earth to the Sun'), ('b', 'The length of a day'), ('c', 'The width of Jupiter'), ('d', 'The time of one orbit')], 'a'),
    ],
}
