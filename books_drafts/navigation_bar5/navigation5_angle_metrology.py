"""Angle Metrology: the circle, autocollimators, polygons, calibration, standards and errors."""
CODE = 'navigation5_angle_metrology'
BOOK = {
    "title": 'Angle Metrology',
    "subtitle": 'Measuring angles precisely, from the circle to the smallest tilt',
    "chapters": [
        ('The circle',
         'A full circle is divided into 360 degrees, a system inherited from ancient times. Every angle measurement in navigation and surveying rests on this division of the circle.'),
        ('Autocollimators',
         'An autocollimator measures very small angles by reflecting light from a mirror and reading where it returns. It is a precise tool for checking straightness, levelness and small rotations.'),
        ('Polygons',
         'A precisely made polygon, with a known number of equal sides, divides the circle into known angles. Polygons serve as angle standards against which instruments can be checked.'),
        ('Calibration',
         'Calibration checks an instrument against a known standard and records any difference. The correction is then applied to later measurements, so the instrument can be trusted.'),
        ('Standards',
         'Angle standards are kept in a traceable chain, so that a measurement in one place can be compared with one made anywhere else. Standards must be checked and stored with care.'),
        ('Errors',
         'Angle measurements are affected by misalignment, temperature change, wear and the operator\'s technique. Identify each error source, reduce it where possible, and state the uncertainty that remains.'),
    ],
    "test": [
        ('How many degrees are in a full circle?',
         [('a', '100'), ('b', '180'), ('c', '90'), ('d', '360')], 'd'),
        ('What does an autocollimator measure?',
         [('a', 'Weight'), ('b', 'Temperature'), ('c', 'Very small angles, using reflected light'), ('d', 'Sound')], 'c'),
        ('What is a polygon used for in angle metrology?',
         [('a', 'Dividing a circle into known angles'), ('b', 'Making paper'), ('c', 'Measuring rainfall'), ('d', 'Painting walls')], 'a'),
        ('Why do we calibrate angle instruments?',
         [('a', 'To make them heavier'), ('b', 'To check they read correctly against a standard'), ('c', 'To hide errors'), ('d', 'To change their colour')], 'b'),
        ('What is a common source of error in angle measurement?',
         [('a', 'The weather on the day'), ('b', 'The colour of the case'), ('c', 'The price of the instrument'), ('d', 'Misalignment and temperature change')], 'd'),
    ],
}
