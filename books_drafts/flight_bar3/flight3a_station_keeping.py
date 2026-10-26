"""Station Keeping: why orbits drift, and the small burns that hold a craft in its place."""
CODE = 'flight3a_station_keeping'
BOOK = {
    "title": 'Station Keeping',
    "subtitle": 'Why orbits drift, and the small burns that hold a craft in place',
    "chapters": [
        ('Nothing stays exactly put',
         "Even a well-set orbit does not stay exactly the same forever. Small pulls from the Sun, the Moon and the uneven shape of the planet nudge it off course. A craft that must stay in place has to keep correcting."),
        ('Air drag in low orbit',
         "Close to a planet, a thin trace of air still drags on a craft. The drag takes away speed, so the orbit slowly sinks. In the lowest orbits the sinking can be quick, and crews need regular boosts to climb back up."),
        ('Small regular burns',
         "Station keeping is a series of small, regular burns that hold the orbit inside its planned band. Many small burns usually cost less than one big correction, and they are easier to get right. The pilot plans them on a fixed schedule."),
        ('The geostationary ring',
         "Satellites that must hover over one spot on the ground sit in a special ring about 36,000 km above the equator. Even there, the Sun and the Moon pull them off position, so they need station keeping too. Each burn uses fuel, and the fuel left sets how long the satellite can work."),
        ('Fuel is the clock',
         "When the fuel is spent, the craft can no longer hold its place and must be moved or retired. The fuel left is the true measure of how long a station can be held. Pilots watch that number as closely as they watch the orbit."),
        ("The pilot's habit",
         "Check the orbit against the plan on every flight. Note any drift early, when a small burn is cheap. Waiting until the drift is large means a bigger burn and more fuel, and so a bigger bill."),
    ],
    "test": [
        ('What is station keeping?',
         [('a', 'Holding a craft in a planned band with small, regular burns'), ('b', 'Parking the craft on the ground'), ('c', 'Storing food for the crew'), ('d', 'Painting the hull')], 'a'),
        ('Why does the orbit of a low craft slowly sink?',
         [('a', 'The engines leak'), ('b', 'Thin air drags on it and takes away speed'), ('c', 'The Sun pushes it upward'), ('d', 'It is too heavy to stay up')], 'b'),
        ('Why are many small burns often better than one big correction?',
         [('a', 'They make the craft spin'), ('b', 'They empty the hold'), ('c', 'They usually cost less overall and are easier to get right'), ('d', 'They are faster')], 'c'),
        ('About how far above the equator is the geostationary ring?',
         [('a', 'About 36 km'), ('b', 'About 360 km'), ('c', 'About 3,600,000 km'), ('d', 'About 36,000 km')], 'd'),
        ('Why should a pilot correct a small drift early?',
         [('a', 'A small burn is cheap, and a late large one uses more fuel'), ('b', 'Drift is always fatal'), ('c', 'The Moon grows angry'), ('d', 'It does not matter when it is corrected')], 'a'),
    ],
}
