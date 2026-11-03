"""Maximum Likelihood Positioning: choosing the position that makes the measurements most likely."""
CODE = 'navigation5_ml_estimation'
BOOK = {
    "title": 'Maximum Likelihood Positioning',
    "subtitle": 'Likelihood, noise models, the optimum, comparison, computation and practice',
    "chapters": [
        ('What is likelihood',
         'Likelihood measures how probable the measurements are, for a given guess at the position. A guess that makes the readings look likely scores well. A guess that makes them look strange scores badly.'),
        ('Noise models',
         'A noise model says how the measurement errors are spread out. Many sensors are close to Gaussian, meaning small errors are common and large ones are rare. The choice of model shapes the answer.'),
        ('The optimum',
         'The maximum likelihood estimate is the position with the highest likelihood. It is the best guess under the assumed noise model. Finding it often means turning the problem into a sum that a computer can minimise.'),
        ('Comparison',
         'Maximum likelihood can be compared with simpler methods. It is usually more accurate when the noise model is right. If the model is wrong, it can be less reliable than a simple method.'),
        ('Computation',
         'For most positioning problems there is no simple formula for the answer. The computer searches for it by stepping toward a better guess. The search must start from a sensible place to succeed.'),
        ('Practice',
         'Start with a simple noise model and check it against real data. Test the method on recorded trips before using it live. Report the answer together with how sure the method is about it.'),
    ],
    "test": [
        ('What is a likelihood?',
         [('a', 'The chance a battery is full'), ('b', 'How probable the measurements are for a given set of values'), ('c', 'The price of a satellite'), ('d', 'The speed of light')], 'b'),
        ('What is a noise model?',
         [('a', 'A statement of how measurement errors are spread out'), ('b', 'A machine that makes sound'), ('c', 'A speaker'), ('d', 'The sound of wind')], 'a'),
        ('What does a maximum-likelihood estimate give?',
         [('a', 'The largest possible error'), ('b', 'A random guess'), ('c', 'The price of data'), ('d', 'The value that makes the observed data most probable')], 'd'),
        ('For Gaussian noise, what does maximum likelihood reduce to?',
         [('a', 'A sum of colours'), ('b', 'A random walk'), ('c', 'Least squares'), ('d', 'An exponential decay')], 'c'),
        ('Why compare estimators?',
         [('a', 'To find the best colour'), ('b', 'To choose a paint'), ('c', 'To remove the need for data'), ('d', 'To see which gives more accurate and reliable answers')], 'd'),
    ],
}
