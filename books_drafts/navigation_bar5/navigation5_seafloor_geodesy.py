"""Seafloor Geodesy: Measuring the seabed's position and its slow movement."""
CODE = 'navigation5_seafloor_geodesy'
BOOK = {
    'title': 'Seafloor Geodesy',
    'subtitle': "Measuring the seabed's position and its slow movement",
    'chapters': [
        ('Where is the seafloor?', 'Seafloor geodesy measures where the seabed is and how it moves. Sea water blocks radio signals, so satellites cannot see the seafloor and sound is used instead.'),
        ('Transponders on the bottom', 'Seafloor transponders are fixed devices placed on the seabed. A ship sends a sound pulse, and the transponder answers, letting the ship measure the distance.'),
        ('Acoustic ranging', 'Sound travels through water at a speed that changes with temperature, salt and depth. Measuring the travel time and correcting for that speed gives the distance to each transponder.'),
        ("Knowing the ship's place", 'A satellite system on the ship gives its position at the surface. Combining that with the acoustic ranges fixes the seabed points in the same frame as the satellites.'),
        ('Slow drift and plate motion', 'Over months and years the seabed moves. Tectonic plates drift by a few centimetres each year, and repeated surveys can detect that motion.'),
        ('Accuracy', 'In good surveys the positions can be accurate to about a decimetre or better. Errors come from sound speed, ship motion and timing, so each survey is checked with care.'),
    ],
    'test': [
        ("Why can't satellites see the seafloor directly?", [('a', 'Sea water blocks radio signals'), ('b', 'The seabed is too bright'), ('c', 'Satellites only look at land'), ('d', 'The seafloor is always moving')], 'a'),
        ('What is a seafloor transponder?', [('a', "A ship's engine"), ('b', 'A type of fish'), ('c', 'A fixed device on the seabed that answers sound pulses'), ('d', 'A chart symbol')], 'c'),
        ('What does the speed of sound in water affect?', [('a', 'The colour of the seabed'), ('b', "The ship's paint"), ('c', 'How accurately distance is calculated'), ('d', 'The number of fish')], 'c'),
        ('Roughly how fast do tectonic plates move?', [('a', 'A few centimetres a year'), ('b', 'Hundreds of metres a day'), ('c', 'Many kilometres an hour'), ('d', 'Not at all')], 'a'),
        ('Which is a main source of error a survey must correct?', [('a', "The ship's name"), ('b', 'The colour of the sky'), ('c', 'The shape of the chart'), ('d', 'Sound speed, ship motion and timing')], 'd'),
    ],
}
