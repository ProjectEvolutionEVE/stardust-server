"""Ephemerides: tables of predicted positions that let a navigator plan the future."""
CODE = 'navigation3a_ephemeris'
BOOK = {
    "title": 'Ephemerides: Tables of the Future',
    "subtitle": 'How navigators look up where a body will be',
    "chapters": [
        ('What an ephemeris is',
         'An ephemeris is a table that lists where a body will be at set times, such as every hour or every day. The word comes from the Greek for daily. Navigators use it instead of working out every orbit from scratch.'),
        ('Built from models and data',
         'Ephemerides are built by fitting a model of the solar system to real measurements. Radar echoes, spacecraft tracking and careful observations all feed in. The better the data, the smaller the error in the table.'),
        ('Modern ephemerides',
         "Large space agencies publish their own ephemerides. NASA's Jet Propulsion Laboratory makes the planetary ephemerides that most spacecraft use, and a public web service lets anyone look up a position for a chosen time."),
        ('Reading a table',
         'A table gives a position in a stated frame, at a stated time scale. Each row is a moment, and each column is a value such as right ascension, declination or distance. A position with no frame and no time is not useful.'),
        ('Predictions get worse with distance',
         'A table is only as good as its model. The further ahead you look, the more the small errors add up. Planners therefore check predictions against new tracking and update the tables when they drift.'),
        ('Money in the plan',
         'A good ephemeris saves money. A craft aimed at where a planet will be can use less fuel than one that must make a big correction later. Accurate tables are cheap compared with the cost of a missed target.'),
    ],
    "test": [
        ('What is an ephemeris?',
         [('a', 'A type of engine'), ('b', 'A table of predicted positions at set times'), ('c', 'A kind of star'), ('d', 'A map of rivers')], 'b'),
        ('What are ephemerides built from?',
         [('a', 'Guesses only'), ('b', 'Colours of the sky'), ('c', 'Weather reports'), ('d', 'A model fitted to real measurements')], 'd'),
        ('Why must a position in an ephemeris state its frame and its time scale?',
         [('a', 'It makes the table thicker'), ('b', 'So the planet can read it'), ('c', 'Without them the position cannot be placed or compared'), ('d', "It changes the planet's speed")], 'c'),
        ('What happens to the errors in a prediction as you look further ahead?',
         [('a', 'They grow as small errors add up'), ('b', 'They shrink to zero'), ('c', 'They stay the same'), ('d', 'They vanish after one year')], 'a'),
        ('Why can an accurate ephemeris save fuel?',
         [('a', 'It lets the craft fly without gravity'), ('b', 'It lets a craft aim at where the body will be, so fewer corrections are needed'), ('c', 'It paints the craft cheaper'), ('d', 'It removes the need for a crew')], 'b'),
    ],
}
