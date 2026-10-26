"""The Deep Space Network: the ground stations that track distant craft, measure their speed and range, and keep them in contact."""
CODE = 'navigation3a_dsn'
BOOK = {
    "title": 'The Deep Space Network',
    "subtitle": 'Three ground sites that keep in touch with craft across the solar system',
    "chapters": [
        ('Why a network',
         "A deep-space craft is far away and moves fast, so one ground dish cannot always see it. The Deep Space Network is a set of large antennas that work together. Operated by NASA's Jet Propulsion Laboratory, it has three complexes."),
        ('Three sites round the globe',
         'The complexes are at Goldstone in California, near Madrid in Spain, and near Canberra in Australia. They sit roughly 120 degrees apart in longitude. As the Earth turns, a spacecraft is always above the horizon of at least one of them.'),
        ('Big dishes, weak signals',
         'The network uses antennas up to 70 metres across. The signal from a far craft is so weak that the dish must gather it with great care. Low-noise receivers and long integration times help catch a whisper from billions of kilometres away.'),
        ('Measuring speed by Doppler',
         "A craft moving toward Earth sends radio waves that arrive at a slightly higher frequency, and a craft moving away gives a lower one. Measuring that shift tracks the craft's speed toward or away from the station very precisely."),
        ('Measuring distance by round trip',
         'The network also sends a signal and times its return from the craft. Light takes a known time to cross the distance and back, so the round trip gives the range. For a craft far beyond Neptune, such as Voyager 1, the round trip takes more than a day.'),
        ('Money in the link',
         'Tracking time costs money, so mission teams plan their passes to be as few and as useful as possible. A clear plan for each pass saves network hours, and that is money saved for the mission.'),
    ],
    "test": [
        ('What is the Deep Space Network?',
         [('a', 'A computer game'), ('b', 'A type of satellite'), ('c', 'A group of ships'), ('d', 'A set of large ground antennas that track distant craft')], 'd'),
        ('Roughly how far apart are the three DSN complexes in longitude?',
         [('a', 'About 30 degrees'), ('b', 'About 120 degrees'), ('c', 'About 60 degrees'), ('d', 'About 180 degrees')], 'b'),
        ("How does Doppler tracking measure a craft's speed?",
         [('a', 'By measuring the frequency shift of its radio signal'), ('b', 'By counting the crew'), ('c', 'By weighing the fuel'), ('d', 'By looking at the colour of the craft')], 'a'),
        ('How is distance found by round-trip ranging?',
         [('a', 'By guessing the size of the craft'), ('b', 'By reading a star catalogue'), ('c', 'By timing a signal sent out to the craft and back'), ('d', 'By using a compass')], 'c'),
        ('Why do mission teams plan tracking passes carefully?',
         [('a', 'Because antennas are painted each day'), ('b', 'Because the Sun blocks every signal'), ('c', 'Because craft cannot receive signals'), ('d', 'Because tracking time is limited, and a clear plan saves network hours and money')], 'd'),
    ],
}
