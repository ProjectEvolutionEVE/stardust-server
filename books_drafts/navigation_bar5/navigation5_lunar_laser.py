"""Lunar Laser Ranging: corner reflectors left on the Moon, the round trip of a laser pulse, the Earth-Moon distance, lunar orientation, tests of gravity and precision."""
CODE = 'navigation5_lunar_laser'
BOOK = {
    "title": 'Lunar Laser Ranging',
    "subtitle": 'Bouncing laser light off mirrors on the Moon to measure the Earth-Moon distance',
    "chapters": [
        ('Corner reflectors',
         'Astronauts placed retroreflectors on the Moon during the Apollo missions. A corner reflector sends light straight back toward the place it came from, so a laser aimed from Earth returns to Earth.'),
        ('The round trip',
         'A ground station fires a short laser pulse toward the Moon. The light travels there and back, taking about two and a half seconds. The time of that trip gives the distance.'),
        ('The Earth-Moon distance',
         'The Moon is about 384,000 kilometres away, and laser ranging measures that distance to within a few millimetres in good conditions. Long series of measurements reveal the true motion of the Moon.'),
        ('Lunar orientation',
         'Repeated measurements show how the Moon rotates and how its orientation changes. These details give scientists clues about the inside of the Moon, including whether it has a fluid core.'),
        ('Tests of gravity',
         'The orbit of the Moon is tested against gravity theories. Lunar laser ranging gives one of the strongest checks of the equivalence principle, which says that all bodies fall with the same acceleration in a gravity field.'),
        ('Precision',
         'The Moon is slowly moving away from the Earth, by about 3.8 centimetres a year. Laser ranging measures this drift, which is caused by the tides that the Moon raises on the Earth.'),
    ],
    "test": [
        ('What do corner reflectors do?',
         [('a', 'Send light straight back toward its source'), ('b', 'Make light change colour'), ('c', 'Make a sound'), ('d', 'Store electricity')], 'a'),
        ('About how long does the laser light take to make the round trip to the Moon?',
         [('a', 'About an hour'), ('b', 'About two and a half seconds'), ('c', 'About a year'), ('d', 'About a millisecond')], 'b'),
        ('Roughly how far away is the Moon?',
         [('a', 'About 384 kilometres'), ('b', 'About 38 million kilometres'), ('c', 'About 3,840 kilometres'), ('d', 'About 384,000 kilometres')], 'd'),
        ('What does the Moon yearly drift tell scientists?',
         [('a', 'The Moon is getting smaller'), ('b', 'The Sun is cooling down'), ('c', 'Tidal forces are slowly moving the Moon away from the Earth'), ('d', 'The Earth has stopped turning')], 'c'),
        ('What does lunar laser ranging test?',
         [('a', 'The taste of lunar rock'), ('b', 'The orbit of the Moon and gravity theories'), ('c', 'The temperature of the Sun'), ('d', 'How fast fish swim')], 'b'),
    ],
}
