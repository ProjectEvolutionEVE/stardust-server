"""Relay Orbiters as Navigation Beacons: relay satellites around Mars and the Moon, ranging, timing, surface users, the schedule and costs."""
CODE = 'navigation5_relay_orbiters'
BOOK = {
    "title": 'Relay Orbiters as Navigation Beacons',
    "subtitle": 'Satellites that carry messages and measure distances for landers and rovers',
    "chapters": [
        ('Relay satellites',
         'Relay satellites orbit a planet and carry signals between surface users and the Earth. Mars has several of them, and some orbiters relay data from its rovers to Earth.'),
        ('Ranging',
         'A relay can also measure the distance to a surface user, by timing signals that travel back and forth. This helps find where a rover or lander is.'),
        ('Timing',
         'Signals need accurate timing, so relay satellites must keep their clocks well linked to time on Earth. Timing errors turn directly into distance errors.'),
        ('Surface users',
         'Landers and rovers on the surface are the users. They do not need to see the Earth directly, because a relay passes their messages on.'),
        ('The schedule',
         'A relay passes over a given site only at set times. Planners build the surface schedule around those windows.'),
        ('Costs',
         'Orbiters cost money to build and run, but one orbiter can serve many landers. Sharing a single relay among many missions lowers the cost for each user.'),
    ],
    "test": [
        ('What does a relay satellite do?',
         [('a', 'Stores soil samples'), ('b', 'Makes new rocks'), ('c', 'Carries signals between surface users and the Earth'), ('d', 'Paints the planet')], 'c'),
        ('How can a relay help find a rover?',
         [('a', 'By painting the rover a bright colour'), ('b', 'By reading the rover name'), ('c', 'By listening to music from the rover'), ('d', 'By timing signals sent back and forth to measure distance')], 'd'),
        ('Why must relay timing be accurate?',
         [('a', 'So the satellite can sleep'), ('b', 'Because timing errors turn into distance errors'), ('c', 'So the Sun rises on time'), ('d', 'So the colours of the planet change')], 'b'),
        ('Why do surface users not need to see the Earth directly?',
         [('a', 'Because the relay passes their messages on'), ('b', 'Because the Earth is not there'), ('c', 'Because they are blind'), ('d', 'Because they use a telescope')], 'a'),
        ('What lowers the cost for each user?',
         [('a', 'Building many rovers'), ('b', 'Sharing one relay across many missions'), ('c', 'Turning the relays off'), ('d', 'Using more paint')], 'b'),
    ],
}
