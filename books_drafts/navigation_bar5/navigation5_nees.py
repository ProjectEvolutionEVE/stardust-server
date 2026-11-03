"""Testing Filter Consistency: how to check whether a filter is honest about how wrong it might be."""
CODE = 'navigation5_nees'
BOOK = {
    "title": 'Testing Filter Consistency',
    "subtitle": 'Normalised errors, chi-squared tests, overconfidence, tuning, checks and reporting',
    "chapters": [
        ('Normalised errors',
         'A filter gives an estimate and also says how uncertain it is. The normalised estimation error squared, or NEES, compares the real error with that stated uncertainty. A good filter keeps its error in proportion to what it claims.'),
        ('Chi-squared tests',
         'When a filter is consistent, the NEES values follow a chi-squared distribution. The number of degrees of freedom is the size of the state being estimated. Averaging many NEES values gives a test that is easy to read.'),
        ('Overconfidence',
         'A filter is overconfident when its stated uncertainty is smaller than its real error. It then trusts its own answer too much and ignores new data that should move it. Overconfidence is the most common and most harmful problem.'),
        ('Tuning',
         'Overconfidence is often fixed by raising the process noise, which tells the filter that the world changes more than its model says. Tuning should use data that was not used to build the filter. Small changes are usually enough.'),
        ('Checks',
         'Run the consistency test on several recorded trips, not just one. Look at the NEES over time as well as its average. A problem that appears only in some parts of a trip is still a problem.'),
        ('Reporting',
         'Always report the estimate together with its uncertainty. Say how the consistency test was done and on what data. An honest report lets the users judge how far the answer can be trusted.'),
    ],
    "test": [
        ('What does NEES stand for?',
         [('a', 'Net energy estimate sum'), ('b', 'Normalised estimation error squared'), ('c', 'Non-linear error estimate size'), ('d', 'Navigation error easy scale')], 'b'),
        ('What distribution do NEES values follow when a filter is consistent?',
         [('a', 'Uniform'), ('b', 'Poisson'), ('c', 'Exponential'), ('d', 'Chi-squared')], 'd'),
        ('What does overconfidence mean for a filter?',
         [('a', 'Its stated uncertainty is smaller than its real error'), ('b', 'Its estimate is always exact'), ('c', 'It has no uncertainty at all'), ('d', 'It runs too slowly')], 'a'),
        ('What is a common fix for an overconfident filter?',
         [('a', 'Remove all sensors'), ('b', 'Shorten the time step to zero'), ('c', 'Increase the process noise'), ('d', 'Stop reporting results')], 'c'),
        ('Why should a filter report its uncertainty along with its estimate?',
         [('a', 'To make the plot prettier'), ('b', 'So users can judge how far the estimate can be trusted'), ('c', 'To avoid using a computer'), ('d', 'To hide small errors')], 'b'),
    ],
}
