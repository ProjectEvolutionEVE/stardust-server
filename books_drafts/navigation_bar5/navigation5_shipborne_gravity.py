"""Shipborne Gravimetry: Measuring gravity from a moving ship."""
CODE = 'navigation5_shipborne_gravity'
BOOK = {
    'title': 'Shipborne Gravimetry',
    'subtitle': 'Measuring gravity from a moving ship',
    'chapters': [
        ('Gravity at sea', 'Gravity is not quite the same everywhere on Earth. Dense rock under the sea pulls slightly harder, and a gravity survey can map those small differences.'),
        ('A gravimeter on a ship', 'A gravimeter is mounted on a ship and measures gravity as the ship sails. The instrument is very sensitive, so small changes can be recorded.'),
        ('Ship motion', 'The ship rolls, pitches, speeds up and slows down. Those movements add acceleration that looks like a change in gravity, so they must be removed.'),
        ('The Eötvös effect', "When a ship moves east, its motion along with the Earth's rotation lowers the reading. Moving west raises it. This is the Eötvös effect, and it is corrected using the ship's speed and heading."),
        ('Making sea gravity maps', 'After corrections, the readings are gridded into a map of gravity anomalies. These maps reveal ridges, trenches and buried structures under the sea.'),
        ('Noise and limits', 'Waves, weather and sensor drift add noise to the data. Good surveys use steady courses, careful filtering and repeated lines to check the results.'),
    ],
    'test': [
        ('Why does a moving ship need corrections in a gravity survey?', [('a', 'It makes the sea colder'), ('b', 'It changes the moon'), ('c', 'Its motion adds acceleration that can look like a gravity change'), ('d', 'It has no effect')], 'c'),
        ('What is the Eötvös effect?', [('a', 'A kind of fish'), ('b', 'A colour on charts'), ('c', 'A type of sonar'), ('d', "A correction for the effect of a ship's motion over the rotating Earth")], 'd'),
        ('What does a gravity anomaly show?', [('a', "The ship's speed"), ('b', 'The number of waves'), ('c', 'Dense rock or structure under the sea'), ('d', 'The age of the crew')], 'c'),
        ('Which is a source of noise in gravity data?', [('a', 'Charts'), ('b', 'A steady course'), ('c', 'Clear skies'), ('d', 'Waves, weather and sensor drift')], 'd'),
        ('What do gravity surveys produce?', [('a', 'A map of gravity anomalies'), ('b', 'A list of crew names'), ('c', 'A tide table'), ('d', 'A weather forecast')], 'a'),
    ],
}
