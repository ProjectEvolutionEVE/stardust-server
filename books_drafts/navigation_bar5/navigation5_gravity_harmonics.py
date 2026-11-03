"""Spherical Harmonic Gravity Models: the expansion of gravity, degree and order, coefficients, truncation, accuracy and use."""
CODE = 'navigation5_gravity_harmonics'
BOOK = {
    "title": 'Spherical Harmonic Gravity Models',
    "subtitle": 'Describing the gravity of a whole planet as a sum of simple patterns',
    "chapters": [
        ('Expanding gravity',
         'Scientists describe the gravity of a planet as a sum of simple patterns called spherical harmonics. Each pattern describes gravity variation on a different scale.'),
        ('Degree and order',
         'The degree tells how many waves fit around the planet, and the order describes the direction of the pattern. Higher degrees capture finer detail.'),
        ('Coefficients',
         'Each term in the sum has a coefficient, a number that sets how strong that pattern is. A full model is a long list of these coefficients.'),
        ('Truncation',
         'Models stop at a chosen maximum degree. Cutting the series short, which is called truncation, means that the finest detail is lost.'),
        ('Accuracy',
         'Accuracy depends on the data and on the degree used. Very high degree models, such as EGM2008, which reaches degree 2159, give fine detail of the gravity of the Earth.'),
        ('Use',
         'Gravity models are used to compute orbits, heights and the shape of the geoid. They are essential to precise navigation and to Earth science.'),
    ],
    "test": [
        ('What are spherical harmonics?',
         [('a', 'Musical instruments'), ('b', 'Types of fruit'), ('c', 'A kind of rock'), ('d', 'Simple patterns used to add up the gravity of a planet')], 'd'),
        ('What does the degree of a harmonic tell?',
         [('a', 'Its colour'), ('b', 'How many waves fit around the planet'), ('c', 'Its price'), ('d', 'How many stars can be seen')], 'b'),
        ('What is a coefficient in a gravity model?',
         [('a', 'A number that sets how strong a pattern is'), ('b', 'The name of a place'), ('c', 'A kind of ship'), ('d', 'A calendar date')], 'a'),
        ('What is truncation?',
         [('a', 'Adding more stars to a map'), ('b', 'Painting a model'), ('c', 'Stopping the series at a chosen degree'), ('d', 'Sending a radio signal')], 'c'),
        ('What maximum degree did the model EGM2008 reach?',
         [('a', 'Degree 2'), ('b', 'Degree 20'), ('c', 'Degree 200'), ('d', 'Degree 2159')], 'd'),
    ],
}
