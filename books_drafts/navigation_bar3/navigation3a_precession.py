"""Precession: why the frame we measure from slowly turns, and how navigators keep up with it."""
CODE = 'navigation3a_precession'
BOOK = {
    "title": 'Precession: The Frame That Drifts',
    "subtitle": 'Why the reference direction creeps, and how to correct for it',
    "chapters": [
        ('A spinning top',
         'The Earth spins like a top, and its axis is tilted. The Sun and Moon pull on the bulge around its middle, so the axis slowly sweeps round a cone. This slow turn is called precession.'),
        ('The cycle',
         'One full sweep of the axis takes about 26,000 years. The equinoxes, the two points where the Sun crosses the celestial equator, creep steadily west along the ecliptic as a result. A star chart drawn a few centuries ago is noticeably out of line today.'),
        ('Why the rate is small',
         'The equinoxes move about 50 arcseconds a year. An arcsecond is one 3,600th of a degree, so this is slow. Over a human life it is hard to see, but over decades it moves whole star positions far enough to matter for a precise fix.'),
        ('Frames that are fixed on purpose',
         'To keep positions meaningful, astronomers choose an epoch, such as the year 2000 at noon, and state their positions for that date. Modern work uses the International Celestial Reference Frame, tied to very distant quasars that barely move in the sky.'),
        ('Converting between dates',
         'To compare a position from one epoch with another, a navigator applies precession, and a smaller correction called nutation, which is a short wobble on top of the slow turn. Both corrections are standard formulas, and planning software does them automatically.'),
        ('Keeping the frame in mind',
         'A position without its epoch and its frame can be wrong by a noticeable angle. Like the time scale, the frame belongs with every number. Write it down before you trust the number.'),
    ],
    "test": [
        ('What is precession?',
         [('a', "The slow sweep of the Earth's axis round a cone"), ('b', 'A sudden jump of the Earth'), ('c', 'The change of the seasons in one day'), ('d', 'The melting of polar ice')], 'a'),
        ('About how long does one full precession cycle take?',
         [('a', 'About one year'), ('b', 'About 88 days'), ('c', 'About 26,000 years'), ('d', 'About 11.9 years')], 'c'),
        ('Roughly how far do the equinoxes move each year?',
         [('a', 'About 50 degrees'), ('b', 'About 50 arcseconds'), ('c', 'About 5 kilometres'), ('d', 'Not at all')], 'b'),
        ('What does a standard epoch such as the year 2000 give a navigator?',
         [('a', 'A new colour for the stars'), ('b', 'A way to stop the Earth turning'), ('c', 'A cheaper engine'), ('d', 'A fixed starting point to state positions against')], 'd'),
        ('What is nutation?',
         [('a', 'A short wobble added on top of the slow precession'), ('b', 'A type of planet'), ('c', 'A fuel tank'), ('d', 'A name for the Milky Way')], 'a'),
    ],
}
