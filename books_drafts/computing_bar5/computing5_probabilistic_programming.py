"""Probabilistic programming: models as programs, inference engines, Monte Carlo methods, variational inference and model debugging."""
CODE = 'computing5_probabilistic_programming'
BOOK = {
    "title": 'Probabilistic Programming',
    "subtitle": 'Writing a model as a program, and letting an engine work out the uncertainty',
    "chapters": [
        ('Models as programs',
         'In probabilistic programming, a model is written as code that draws random values for unknown quantities. The programmer describes how the data could have been produced.'),
        ('Inference engines',
         'An inference engine works backward from the observed data to the likely values of the unknowns. Tools such as Stan, PyMC and Pyro are common examples.'),
        ('Monte Carlo methods',
         'Monte Carlo methods estimate answers by drawing many random samples. Markov chain Monte Carlo builds a chain of samples that settles on the right spread of values.'),
        ('Variational inference',
         'Variational inference chooses a simpler shape to approximate the answer, then adjusts it to fit. It is usually faster, but the approximation can miss some detail.'),
        ('Debugging models',
         'Teams check that sampling has converged, using diagnostics such as R-hat, and compare predictions with the real data. A model that cannot reproduce the data needs fixing.'),
        ('Uses',
         'Probabilistic models are used for forecasting, estimating how diseases spread, and modelling stars. They give ranges of likely answers, not just one number.'),
    ],
    "test": [
        ('What does a probabilistic program do with unknown quantities?',
         [('a', 'Draws random values for them'), ('b', 'Ignores them'), ('c', 'Prints them on paper'), ('d', 'Deletes them')], 'a'),
        ('What is an inference engine?',
         [('a', 'A car part'), ('b', 'A kind of printer'), ('c', 'A chat room'), ('d', 'A tool that works back from data to likely unknown values')], 'd'),
        ('What do Monte Carlo methods use?',
         [('a', 'One exact guess'), ('b', 'Many random samples'), ('c', 'A map of the room'), ('d', 'The office calendar')], 'b'),
        ('What is a trade-off of variational inference?',
         [('a', 'It is slower and always exact'), ('b', 'It removes all uncertainty'), ('c', 'It is faster, but may miss some detail'), ('d', 'It needs no data')], 'c'),
        ('What does R-hat help check?',
         [('a', 'Whether sampling has converged'), ('b', 'The colour of the chart'), ('c', 'The price of the server'), ('d', 'The number of staff')], 'a'),
    ],
}
