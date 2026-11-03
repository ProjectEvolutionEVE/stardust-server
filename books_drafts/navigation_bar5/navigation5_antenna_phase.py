"""Antenna Phase Centre Models: the electrical centre, calibration, elevation dependence, height errors, the calibration chamber and standards."""
CODE = 'navigation5_antenna_phase'
BOOK = {
    "title": 'Antenna Phase Centre Models',
    "subtitle": 'Why an antenna does not measure from its middle, and how that is corrected',
    "chapters": [
        ('The electrical centre',
         'The phase centre of an antenna is the point where its signal seems to come from. It is not always at the physical middle of the antenna.'),
        ('Calibration',
         'Each antenna type is calibrated, so that the offset of its phase centre is known in each direction. These numbers are used in precise positioning.'),
        ('Elevation dependence',
         'The phase centre shifts depending on the angle of the incoming signal. A satellite low in the sky gives a different offset than one overhead.'),
        ('Height errors',
         'An error in the phase centre becomes an error in the measured height. Height is the hardest quantity to get right in positioning, so even a small offset matters.'),
        ('The calibration chamber',
         'Antennas are tested in a special room whose walls absorb stray reflections, called an anechoic chamber, or on a turntable that rotates them through many angles.'),
        ('Standards',
         'Agencies and standards bodies publish the antenna models, so that every user applies the same corrections and their results agree.'),
    ],
    "test": [
        ('What is the phase centre of an antenna?',
         [('a', 'The point where its signal seems to come from'), ('b', 'The colour of the antenna'), ('c', 'The weight of the antenna'), ('d', 'The price of the antenna')], 'a'),
        ('Why is each antenna type calibrated?',
         [('a', 'To paint it'), ('b', 'To give it a name'), ('c', 'To change its shape'), ('d', 'So the offset of its phase centre is known in each direction')], 'd'),
        ('What is elevation dependence?',
         [('a', 'The antenna rising in height'), ('b', 'The paint on the antenna fading'), ('c', 'The phase centre shifting with the angle of the incoming signal'), ('d', 'The price of the antenna changing')], 'c'),
        ('Why do height errors matter most?',
         [('a', 'Height is the easiest quantity to measure'), ('b', 'Height is the hardest to get right, so small offsets matter'), ('c', 'Height does not matter in positioning'), ('d', 'Height is set by the paint')], 'b'),
        ('What is an anechoic chamber used for?',
         [('a', 'Cooking meals'), ('b', 'Playing music'), ('c', 'Growing plants'), ('d', 'Testing antennas without stray reflections')], 'd'),
    ],
}
