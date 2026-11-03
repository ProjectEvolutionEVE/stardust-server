"""Satellite Laser Ranging: retroreflector satellites, timed laser pulses, orbit tracking, the geocentre, gravity and the station network."""
CODE = 'navigation5_slr'
BOOK = {
    "title": 'Satellite Laser Ranging',
    "subtitle": 'Timing laser pulses that bounce off satellites to measure their orbits',
    "chapters": [
        ('Retroreflector satellites',
         'Some satellites carry arrays of corner reflectors, so that laser light returns to its source. LAGEOS is the classic example of such a satellite.'),
        ('Timed pulses',
         'A ground station fires a short laser pulse and times its return. The round trip gives the distance to the satellite, to within a few millimetres.'),
        ('Orbit tracking',
         'Repeated measurements build up a very accurate orbit. Those orbits are used to test gravity and to define reference frames.'),
        ('The geocentre',
         'The geocentre is the centre of mass of the Earth. Laser ranging helps track where it lies relative to the ground stations.'),
        ('Gravity',
         'Because the orbits are so precise, they reveal small irregularities in the gravity field of the Earth.'),
        ('The station network',
         'Stations around the world track the same satellites. Their results are combined into a single, precise picture of orbits and positions.'),
    ],
    "test": [
        ('What is a retroreflector?',
         [('a', 'A device that sends light straight back to its source'), ('b', 'A type of mirror on a car'), ('c', 'A device that makes sound'), ('d', 'A kind of battery')], 'a'),
        ('How is the distance found in satellite laser ranging?',
         [('a', 'By guessing from the orbit'), ('b', 'By counting clouds'), ('c', 'By weighing the satellite'), ('d', 'By timing the round trip of a laser pulse')], 'd'),
        ('What does the geocentre mean?',
         [('a', 'The surface of the Earth'), ('b', 'The centre of mass of the Earth'), ('c', 'The hottest point on Earth'), ('d', 'The highest mountain')], 'b'),
        ('What can precise satellite orbits reveal?',
         [('a', 'Cooking recipes'), ('b', 'The taste of rain'), ('c', 'Small irregularities in the gravity field of the Earth'), ('d', 'Music from space')], 'c'),
        ('Why do ground stations work together?',
         [('a', 'To compete for the best results'), ('b', 'To hide their results from each other'), ('c', 'To paint the satellites'), ('d', 'To track the same satellites and combine precise results')], 'd'),
    ],
}
