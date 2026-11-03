"""Tidal Evolution of Orbits: how the pull of tides slowly reshapes orbits and spins over very long times."""
CODE = 'navigation5_tidal_evolution'
BOOK = {
    "title": 'Tidal Evolution of Orbits',
    "subtitle": 'The tidal bulge, orbital decay, spin synchronisation, moons, time scales and models',
    "chapters": [
        ('The tidal bulge',
         'A nearby body raises a bulge on a planet or moon, because it pulls harder on the near side. The bulge is never quite lined up with the pull. That mismatch is what drives the changes.'),
        ('Orbital decay',
         'Friction within the body turns some of the spin energy into heat. The orbit then changes slowly, and often shrinks. Close moons can spiral inward this way.'),
        ('Spin synchronisation',
         'Spin synchronisation is when a body\'s rotation period matches its orbit period. The same face then always points toward the other body. Many moons of the planets have reached this state.'),
        ('Moons',
         'Tides also move the orbits of moons. Some move outward and some move inward, depending on the balance of spins and orbits. The Moon of Earth is slowly moving away from us.'),
        ('Time scales',
         'Tidal changes are very slow. They can take millions or billions of years to show clearly. Planners use models to see their effects over such long spans.'),
        ('Models',
         'Tidal models describe the bulge, the friction and the spin. They are used to predict how orbits and spins change over time. The results depend on how well the body\'s properties are known.'),
    ],
    "test": [
        ('What is a tidal bulge?',
         [('a', 'A bump on a cake'), ('b', 'A raised shape of the body caused by a nearby body\'s pull'), ('c', 'A painted hill'), ('d', 'A shop')], 'b'),
        ('What is spin synchronisation?',
         [('a', 'A music term'), ('b', 'A film'), ('c', 'A motor'), ('d', 'When a body\'s rotation period matches its orbit period, so one face always points at the other body')], 'd'),
        ('What is orbital decay caused by tides?',
         [('a', 'An orbit shrinking as tidal energy is lost'), ('b', 'An orbit growing'), ('c', 'A broken moon'), ('d', 'A star')], 'a'),
        ('What do tidal models help predict?',
         [('a', 'Food'), ('b', 'Films'), ('c', 'How orbits and spins change over long times'), ('d', 'The price of paint')], 'c'),
        ('What is a typical time scale for these changes?',
         [('a', 'Millions or billions of years'), ('b', 'A time card'), ('c', 'A clock in a shop'), ('d', 'A time zone')], 'a'),
    ],
}
