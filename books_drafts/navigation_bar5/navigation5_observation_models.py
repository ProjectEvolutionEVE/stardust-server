"""Measurement Models and Nonlinearity: how a measurement relates to position, and why the relation bends."""
CODE = 'navigation5_observation_models'
BOOK = {
    "title": 'Measurement Models and Nonlinearity',
    "subtitle": 'Range functions, linearisation, Jacobians, error, iteration and geometry',
    "chapters": [
        ('Range functions',
         'A range measurement tells you how far a receiver is from a known point. The range function is the formula that turns a position guess into that expected distance. The estimator compares the expected distance with the measured one.'),
        ('Linearisation',
         'Most range functions curve, so they are not straight lines. Linearisation replaces the curve with a straight line near the current guess. That makes the mathematics simple enough to solve quickly.'),
        ('Jacobians',
         'A Jacobian is a table of partial derivatives. It records how each measurement changes when each part of the position changes. It is the main tool for linearising a model.'),
        ('Error from linearisation',
         'A straight line is only a close match near the point where it was drawn. Far from that point, the error grows. Keeping the guess close to the truth keeps the error small.'),
        ('Iteration',
         'Because the linear step is only approximate, the estimator repeats it. Each pass gives a better guess. Iteration stops when the changes become very small.'),
        ('Geometry',
         'The layout of the known points affects how precise the answer is. Points spread out in different directions give a sharper fix. Points bunched together in one direction give a weaker one.'),
    ],
    "test": [
        ('What is a range function?',
         [('a', 'A measure of brightness'), ('b', 'A list of fuel'), ('c', 'A map colour'), ('d', 'A formula giving the distance from a receiver to a known point')], 'd'),
        ('What is linearisation?',
         [('a', 'Drawing a straight line on a map'), ('b', 'Approximating a curved relation by a straight-line one near a point'), ('c', 'Counting lines of code'), ('d', 'Removing all noise')], 'b'),
        ('What is a Jacobian?',
         [('a', 'A matrix of partial derivatives'), ('b', 'A type of boat'), ('c', 'A camera lens'), ('d', 'A weather symbol')], 'a'),
        ('Why does the estimator iterate?',
         [('a', 'To waste time'), ('b', 'To change the colour'), ('c', 'To repeat the linear step until the estimate settles'), ('d', 'To store data')], 'c'),
        ('Why does geometry matter for range measurements?',
         [('a', 'The arrangement of the known points affects how precise the answer is'), ('b', 'The colour of the sky'), ('c', 'The time of day'), ('d', 'The price of data')], 'a'),
    ],
}
