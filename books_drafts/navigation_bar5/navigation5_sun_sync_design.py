"""Designing Sun-Synchronous Orbits: using Earth's bulge to keep an orbit's plane turning with the Sun."""
CODE = 'navigation5_sun_sync_design'
BOOK = {
    "title": 'Designing Sun-Synchronous Orbits',
    "subtitle": 'Nodal regression from Earth\'s bulge, choosing inclination, local time, imaging revisit, design examples and drift',
    "chapters": [
        ('Nodal regression',
         'Earth is slightly bulged at the equator, and that bulge tugs on a satellite\'s orbit. The orbit\'s plane slowly turns, an effect called nodal regression. The turning rate depends on the orbit\'s size and tilt.'),
        ('Choosing the inclination',
         'A sun-synchronous orbit is chosen so that the turning matches the Sun\'s yearly motion. For low orbits this needs a tilt of about ninety-eight degrees. The inclination is the main design choice.'),
        ('Local time',
         'Because the orbit keeps pace with the Sun, the satellite passes a given place at the same local time each day. This lets it take pictures under similar light. Designers pick the local time to suit the mission.'),
        ('Imaging revisit',
         'Revisit is how often a satellite passes over the same place. The orbit height, the sensor width and the number of satellites all affect it. Designers balance these to meet the need.'),
        ('Design examples',
         'Earth-watching satellites are common examples. They are placed in these orbits to get steady light and regular coverage. Each design starts with a target local time and a revisit goal.'),
        ('Drift',
         'The orbit still drifts from small forces, such as drag and the Sun\'s pull. Corrections keep the local time steady. Without them, the orbit slowly moves out of its planned design.'),
    ],
    "test": [
        ('What causes nodal regression?',
         [('a', 'Wind'), ('b', 'Earth\'s equatorial bulge pulling on the orbit'), ('c', 'The Moon\'s paint'), ('d', 'Rain')], 'b'),
        ('Why is a specific inclination chosen?',
         [('a', 'For the colour'), ('b', 'For music'), ('c', 'To match the orbit\'s turning to the Sun\'s yearly motion'), ('d', 'For shop hours')], 'c'),
        ('What is the local time of a sun-synchronous orbit?',
         [('a', 'The time at which the satellite crosses the equator going north, which stays fixed'), ('b', 'A time zone'), ('c', 'The time of a shop'), ('d', 'A clock on the ship')], 'a'),
        ('What does revisit mean?',
         [('a', 'Food'), ('b', 'Paint'), ('c', 'Speed'), ('d', 'How often a satellite passes over the same place')], 'd'),
        ('What is drift in this context?',
         [('a', 'A boat\'s speed'), ('b', 'The lens'), ('c', 'The film'), ('d', 'A slow change in an orbit caused by small forces, which must be corrected')], 'd'),
    ],
}
