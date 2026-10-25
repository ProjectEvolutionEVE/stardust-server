"""Orbits in Plain Words: why planets keep going round the Sun, Kepler's three laws, and real orbital times."""
CODE = 'flight1_orbits'
BOOK = {
    "title": 'Orbits in Plain Words',
    "subtitle": 'Why things keep going round the Sun, and how long it takes',
    "chapters": [
        ('Falling round the Sun',
         "An orbit is a fall that keeps missing. The Sun's gravity pulls on everything in the solar system, but each object moves sideways fast enough that it keeps falling round the Sun instead of into it. Gravity bends the path, and speed keeps it going."),
        ("Kepler's first law: an oval",
         'In the early 1600s, Johannes Kepler worked out that planets move in ovals called ellipses. The Sun sits near one end of the oval rather than at its centre. Most planets are close to circles, but the shape is still an ellipse.'),
        ("Kepler's second law: faster up close",
         'A line from the Sun to a planet sweeps out equal areas in equal times. So a planet moves fastest when it is closest to the Sun and slowest when it is farthest away. Speed rises and falls all the way round the orbit.'),
        ("Kepler's third law: distance sets the year",
         "The square of an orbit's time is proportional to the cube of its average distance from the Sun. Double the distance and the year becomes about 2.8 times longer. That is why the inner planets race round and the outer giants crawl."),
        ('Real years around the Sun',
         'Mercury takes about 88 days to orbit the Sun, Venus about 225 days, Earth 365 days and Mars about 687 days. Jupiter takes about 11.9 years and Saturn about 29.5 years. These times closely match the distances, as the third law says.'),
        ('What it means for flying',
         'Real craft cannot simply speed up to reach a place sooner. A change in speed bends the path, so mission planners work out every burn ahead of time using these rules. That is why a pilot plans the path as well as the speed.'),
    ],
    "test": [
        ('What keeps a planet orbiting the Sun rather than falling into it?',
         [('a', 'The Sun pushes it away'), ('b', 'Air around the Sun'), ('c', 'Magnetism'), ('d', "Its sideways speed, with the Sun's gravity bending its path")], 'd'),
        ("According to Kepler's second law, when is a planet moving fastest?",
         [('a', 'When it is farthest from the Sun'), ('b', 'When it is closest to the Sun'), ('c', 'It moves at one steady speed all the time'), ('d', 'At the midpoint of its year')], 'b'),
        ('Which planet has the shortest year?',
         [('a', 'Mars'), ('b', 'Earth'), ('c', 'Mercury'), ('d', 'Saturn')], 'c'),
        ("About how long is Jupiter's year?",
         [('a', 'About one year'), ('b', 'About 11.9 years'), ('c', 'About 88 days'), ('d', 'About 29.5 years')], 'b'),
        ("If you double a planet's average distance from the Sun, what happens to its year?",
         [('a', 'It becomes about 2.8 times longer'), ('b', 'It becomes exactly twice as long'), ('c', 'It stays the same'), ('d', 'It becomes half as long')], 'a'),
    ],
}
