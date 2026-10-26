"""A Short History of Finding Your Way: the stars, the compass, the sextant, and the long hunt for a clock that keeps time at sea."""
CODE = 'navigation2_history'
BOOK = {
    "title": 'A Short History of Finding Your Way',
    "subtitle": 'Stars, compass, sextant, and the hunt for a clock that keeps time at sea',
    "chapters": [
        ('Before instruments',
         'For most of history, people found their way by the Sun and the stars. Sailors who stayed in sight of the coast steered by landmarks. Those who went out of sight of land watched the sky, because a star that rises and sets in the same place each night gives a direction you can trust.'),
        ('The compass',
         'A magnetic compass has a needle that lines up roughly north and south. Sailors in China, and later in Europe, used magnetized needles to steer on cloudy days and at night. The needle points to magnetic north, which is not quite true north, and the gap between them changes from place to place.'),
        ('The sextant',
         'A sextant measures the angle between a star, or the Sun, and the horizon. Two men, John Hadley in England and Thomas Godfrey in America, each devised one in the early 1730s. With a sextant and a table of star positions, a navigator could find latitude with real accuracy.'),
        ('The longitude problem',
         'Latitude could be found from the sky, but longitude could not, because the Earth turns. To know how far east or west you are, you must compare your local time with the time at a known place. In 1714 Britain passed a law offering a large prize for a practical way to find longitude at sea.'),
        ("Harrison's sea clock",
         'The Earth turns through 15 degrees every hour, so one hour of time difference equals 15 degrees of longitude. A clockmaker, John Harrison, built sea clocks that kept time far better than anything before them. His fourth clock, H4, lost only about five seconds on a voyage of 81 days in 1761.'),
        ('From clocks to satellites',
         'Navigators carried good clocks for generations after Harrison. Today the clock is in orbit: satellites carry atomic clocks, and a receiver on the ground works out its position from their signals. The old questions of stars, clocks and distance still sit under every modern fix.'),
    ],
    "test": [
        ('Why was longitude harder to find at sea than latitude?',
         [('a', 'The Earth turns, so a navigator must compare local time with the time at a known place'), ('b', 'Latitude needs no sky at all'), ('c', 'Longitude is measured in metres'), ('d', 'Longitude changes with the seasons')], 'a'),
        ('Which instrument measures the angle between a star, or the Sun, and the horizon?',
         [('a', 'A magnetic compass'), ('b', 'A chronometer'), ('c', 'A sextant'), ('d', 'A log line')], 'c'),
        ('How many degrees does the Earth turn in one hour?',
         [('a', '1 degree'), ('b', '15 degrees'), ('c', '24 degrees'), ('d', '360 degrees')], 'b'),
        ('About how long was the 1761 voyage on which H4 lost only about five seconds?',
         [('a', 'About 8 days'), ('b', 'About 5 hours'), ('c', 'About 81 years'), ('d', 'About 81 days')], 'd'),
        ('Why does a magnetic compass not always point to true north?',
         [('a', 'Magnetic north differs from true north, and the gap varies from place to place'), ('b', 'The needle is too heavy'), ('c', 'Metal ships pull the needle toward the Sun'), ('d', 'Compasses only work at night')], 'a'),
    ],
}
