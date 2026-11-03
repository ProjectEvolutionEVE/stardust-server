"""Gauss-Markov Error Models: describing errors that drift and linger instead of jumping around at random."""
CODE = 'navigation5_gauss_markov'
BOOK = {
    "title": 'Gauss-Markov Error Models',
    "subtitle": 'Correlated noise, time constants, random walks, bias, fitting and uses',
    "chapters": [
        ('Correlated noise',
         'Some sensor errors do not change from one moment to the next at random. Today\'s error is close to yesterday\'s error. A Gauss-Markov model describes this kind of error, where each value depends on the one before it.'),
        ('Time constants',
         'The time constant tells how long an error takes to fade. A short time constant means the error forgets quickly. A long one means the error hangs around for a while before it fades.'),
        ('Random walks',
         'A random walk is an error that moves by small random steps. The steps add up over time, so the error can wander far away. It is a useful model when there is no pull back toward zero.'),
        ('Bias',
         'A bias is a steady offset in a sensor. It may stay the same for a long time, or it may slowly change. A filter can estimate the bias along with the position.'),
        ('Fitting the model',
         'To fit the model, record the sensor while it sits still or moves in a known way. Compare the readings with the truth and study how the error changes. The fitted time constant and noise level then go into the filter.'),
        ('Uses',
         'Gauss-Markov models are used in inertial navigation, clocks and many other sensors. They give the filter a realistic picture of how errors behave. Better models usually lead to more accurate and more honest answers.'),
    ],
    "test": [
        ('What is a Gauss-Markov error model used for?',
         [('a', 'Washing clothes'), ('b', 'Painting maps'), ('c', 'Naming satellites'), ('d', 'Describing errors that are correlated over time')], 'd'),
        ('What does a time constant describe?',
         [('a', 'How long a battery lasts'), ('b', 'How quickly a correlated error fades'), ('c', 'The length of a road'), ('d', 'How many sensors you have')], 'b'),
        ('What is a random walk?',
         [('a', 'A path that never changes'), ('b', 'A planned route'), ('c', 'An error that changes by small random steps which add up over time'), ('d', 'A type of camera')], 'c'),
        ('What does a bias term model?',
         [('a', 'A steady offset in an error'), ('b', 'The colour of light'), ('c', 'The number of users'), ('d', 'The distance to the Moon')], 'a'),
        ('Why fit a model to recorded errors?',
         [('a', 'So the filter can predict and remove part of the error'), ('b', 'So the sensor stops working'), ('c', 'So the map is smaller'), ('d', 'So the data is hidden')], 'a'),
    ],
}
