"""Ground Tracks: the path a craft traces over the turning Earth, and how to design it."""
CODE = 'flight5_a_ground_tracks'
BOOK = {
    "title": 'Ground Tracks',
    "subtitle": 'The path a craft traces over the turning Earth',
    "chapters": [
        ('The path on the ground',
         'A ground track is the line that a satellite traces on the surface of the Earth. It is what you would see if you drew the point directly under the craft as it moves. Because the Earth turns, that line is not a simple repeat of the orbit.'),
        ('Why the track shifts',
         'The Earth turns once a day, while a low satellite completes an orbit in about ninety minutes. So each orbit starts a little farther west than the one before. Over a day the tracks form a neat set of lines that drift across the map.'),
        ('Repeat orbits',
         'If the orbit is timed so that after a whole number of days the craft passes over the same spot again, the track repeats. Designers use this to revisit the same places on a steady schedule. Remote sensing satellites often rely on this idea.'),
        ('Coverage',
         'How much of the planet a satellite can see depends on how close its tracks lie and how wide its sensor is. Closer tracks give better coverage of a region. A wider sensor fills more of the gap between neighbouring tracks.'),
        ('Designing the orbit',
         'The altitude and tilt of an orbit set the pattern of its track. Engineers balance how often a place is seen against how much fuel it takes to keep the orbit. The choice is always a trade.'),
        ('Examples',
         'Many Earth-observing satellites are placed so that they pass over each place at about the same local time each day. That makes pictures easier to compare from one day to the next. Other designs repeat their tracks every few days or every few weeks.'),
    ],
    "test": [
        ('Why does a satellite ground track shift from one orbit to the next?',
         [('a', 'The satellite changes colour'), ('b', 'The Earth turns beneath it between orbits'), ('c', 'Gravity grows each time'), ('d', 'The orbit gets bigger')], 'b'),
        ('What is a ground track?',
         [('a', 'A road for the ground crew'), ('b', 'A rocket trail seen in the sky'), ('c', 'The line on the surface under the craft as it moves'), ('d', 'A radio beam sent to the Earth')], 'c'),
        ('What is a repeat orbit?',
         [('a', 'An orbit that never ends'), ('b', 'An orbit inside the air'), ('c', 'A second copy of a satellite'), ('d', 'An orbit that passes over the same spot after a whole number of days')], 'd'),
        ('What makes coverage of a region better?',
         [('a', 'Tracks that lie closer together'), ('b', 'Tracks that lie farther apart'), ('c', 'A narrower sensor with wider gaps'), ('d', 'A slower Earth')], 'a'),
        ('What does the choice of altitude and tilt decide?',
         [('a', 'The pattern of the ground track'), ('b', 'The name of the mission'), ('c', 'The colour of the solar panels'), ('d', 'The language of the crew')], 'a'),
    ],
}
