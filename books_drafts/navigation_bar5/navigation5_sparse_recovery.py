"""Sparse Signal Recovery: how a signal with few active parts can be rebuilt from fewer measurements than usual."""
CODE = 'navigation5_sparse_recovery'
BOOK = {
    "title": 'Sparse Signal Recovery',
    "subtitle": 'Sparsity, l1 minimisation, reconstruction, measurement design and radar use',
    "chapters": [
        ('What sparse means',
         'A signal is sparse when most of its parts are zero or close to zero. Many real signals are sparse once they are written in the right form. Sparse signals can be described with few numbers.'),
        ('Recovering from fewer measurements',
         'Normally you need as many measurements as unknowns. If the signal is sparse, far fewer measurements can still give a correct answer. This saves time, power and cost.'),
        ('The l1 idea',
         'Finding the sparsest answer directly is very hard. Minimising the sum of absolute values, the l1 norm, is a practical stand-in that usually finds the right answer. It turns a hard search into a solvable problem.'),
        ('Reconstruction',
         'Reconstruction builds the full signal from the few measurements and the sparsity rule. Good methods check that the result fits the data. The output is an estimate, and its quality depends on the conditions.'),
        ('Measurement design',
         'How the measurements are taken matters. Random or carefully designed patterns make recovery more reliable. A poor design can hide the signal even when it is sparse.'),
        ('Radar use and limits',
         'Sparse methods are used in radar to sharpen images with fewer pulses. They are not a magic fix. When the signal is not sparse, or the noise is large, the recovered signal can be wrong.'),
    ],
    "test": [
        ('What does it mean for a signal to be sparse?',
         [('a', 'Most of its parts are zero or close to zero'), ('b', 'It is always very loud'), ('c', 'It has no frequency'), ('d', 'It is painted red')], 'a'),
        ('Why can sparse signals be recovered from fewer measurements?',
         [('a', 'Because measurements are not needed'), ('b', 'Because noise is always zero'), ('c', 'Because most unknowns are already known to be zero'), ('d', 'Because the signal is very large')], 'c'),
        ('What is the l1 norm?',
         [('a', 'The price of a map'), ('b', 'The number of pages'), ('c', 'The weight of a sailor'), ('d', 'The sum of absolute values')], 'd'),
        ('What does a poor measurement design do?',
         [('a', 'It makes the signal louder'), ('b', 'It can hide the signal even when it is sparse'), ('c', 'It always helps'), ('d', 'It changes the colour of the sky')], 'b'),
        ('When can sparse recovery go wrong?',
         [('a', 'When the sun is up'), ('b', 'When the team is happy'), ('c', 'When the paper is white'), ('d', 'When the signal is not sparse or the noise is large')], 'd'),
    ],
}
