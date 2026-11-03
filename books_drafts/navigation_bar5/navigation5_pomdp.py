"""Planning Under Uncertainty: Making good decisions when you cannot see the whole picture."""
CODE = 'navigation5_pomdp'
BOOK = {
    'title': 'Planning Under Uncertainty',
    'subtitle': 'Making good decisions when you cannot see the whole picture',
    'chapters': [
        ('Not knowing for sure', 'Many real problems involve uncertainty. A partially observable Markov decision process, or POMDP, is a way to plan when the true state is hidden.'),
        ('Belief spaces', 'Instead of one known state, the planner keeps a belief, which gives a probability for each possible state. Beliefs update as new observations arrive.'),
        ('Actions', 'The planner chooses actions that change the state and the belief. Each action may lead to different observations.'),
        ('Expected cost', 'The planner aims for the lowest expected cost over the future. This means weighing each outcome by its probability.'),
        ('Approximations', 'Exact solutions are often too costly for large problems. Approximate methods keep the planning fast enough to be useful.'),
        ('Uses and solvers', 'POMDPs are used in robotics, navigation and healthcare planning. Solvers are software tools that compute good policies.'),
    ],
    'test': [
        ('What does a POMDP plan for?', [('a', 'Making bread'), ('b', 'Painting ships'), ('c', 'Writing songs'), ('d', 'Problems where the true state is hidden')], 'd'),
        ('What is a belief in a POMDP?', [('a', 'A probability for each possible state'), ('b', 'A religious view'), ('c', 'A rope'), ('d', 'A sail')], 'a'),
        ('What does the planner aim for?', [('a', 'The highest noise'), ('b', 'The most fish'), ('c', 'The lowest expected cost over the future'), ('d', 'The slowest ship')], 'c'),
        ('Why use approximations?', [('a', 'Approximations make maps blank'), ('b', 'Approximations stop all planning'), ('c', 'Exact solutions are always free'), ('d', 'Exact solutions are often too costly for large problems')], 'd'),
        ('What is a solver?', [('a', 'A software tool that computes good policies'), ('b', 'A kind of paint'), ('c', 'A type of ship'), ('d', 'A recipe card')], 'a'),
    ],
}
