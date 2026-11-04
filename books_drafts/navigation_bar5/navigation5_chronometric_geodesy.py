"""Chronometric Geodesy: heights from clocks, the gravity potential, relativistic time, clock comparison, resolution and the outlook."""
CODE = 'navigation5_chronometric_geodesy'
BOOK = {
    "title": 'Chronometric Geodesy',
    "subtitle": 'Measuring height and the shape of gravity with clocks',
    "chapters": [
        ('Clocks and heights',
         'Clocks at different heights run at slightly different rates. A clock higher up runs a little faster than one lower down, because gravity is weaker there. Comparing clocks at two places can therefore reveal a difference in their heights.'),
        ('The gravity potential',
         'Scientists use the gravity potential, which is the energy needed to lift a mass against gravity. Surfaces of equal potential are where still water settles. A clock rate measures this potential directly, so clocks can map it.'),
        ('Relativity in the clock',
         'The general relativity of Einstein explains the effect. Time runs more slowly deeper in a gravity field. Satellite navigation already applies this correction to its clocks every day.'),
        ('Comparing clocks',
         'To compare two distant clocks, scientists can carry one between them, or link them with light in a fibre. Careful work removes the effects of motion and temperature before the results are read.'),
        ('Resolution',
         'Optical clocks can now detect a height difference of around a centimetre. That is far finer than the levelling methods that surveyors have used for generations. Clock comparisons can therefore be a very sensitive kind of measurement.'),
        ('The outlook',
         'Networks of clocks may one day map the gravity field of the Earth in detail and help define heights in a more direct way. Several countries are now building such networks and testing them.'),
    ],
    "test": [
        ('What happens to a clock that sits higher up?',
         [('a', 'It runs slower'), ('b', 'It runs slightly faster'), ('c', 'It stops'), ('d', 'It keeps exactly the same rate')], 'b'),
        ('What does a geopotential surface describe?',
         [('a', 'A surface of equal sunlight'), ('b', 'A surface of equal temperature'), ('c', 'A surface of equal gravity potential, where still water settles'), ('d', 'A surface of equal speed')], 'c'),
        ('Why does satellite navigation need relativity?',
         [('a', 'Clocks in orbit run at a different rate from clocks on the ground, and the difference must be corrected'), ('b', 'Satellites move too slowly to matter'), ('c', 'Radio waves do not bend in space'), ('d', 'Gravity is zero in orbit')], 'a'),
        ('How can scientists compare two distant clocks?',
         [('a', 'They shout across the distance'), ('b', 'They wait a century'), ('c', 'They use gold coins'), ('d', 'They link them with light, for example in a fibre, and correct for motion and temperature')], 'd'),
        ('What height difference can optical clocks detect?',
         [('a', 'About a kilometre'), ('b', 'About a centimetre'), ('c', 'About a metre'), ('d', 'Only the height of a building')], 'b'),
    ],
}
