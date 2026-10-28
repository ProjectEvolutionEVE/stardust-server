"""Duality in Optimisation: primal and dual problems, weak and strong duality, shadow prices and certificates of optimality."""
CODE = 'computing5_lp_duality'
BOOK = {'title': 'Duality in Optimisation',
 'subtitle': 'Two problems that prove each other right',
 'chapters': [('Primal and dual',
               'Every linear program, called the primal, has a dual problem built from the same numbers. Each primal constraint gives a dual variable, and the roles of costs and '
               'limits swap. The dual is a second view of the same situation.'),
              ('Weak duality',
               'Weak duality says that any feasible dual value gives a bound on the best primal value. In a maximisation problem the dual value is never below the primal value. '
               'This bound holds without any calculation of the optimum.'),
              ('Strong duality',
               'Strong duality says that if the primal has an optimal solution, so does the dual, and their values are equal. This is why solvers can prove an answer is best. The '
               'matching values are the proof.'),
              ('Shadow prices',
               'The dual variables act as shadow prices: how much the objective would improve if a limit were relaxed by one unit. A factory manager can use them to judge whether '
               'buying more labour is worth the cost. The reading is only valid for small changes.'),
              ('Complementary slackness',
               'Complementary slackness links the two problems. If a constraint is not tight at the optimum, its dual variable is zero. If a variable is positive, its dual '
               'constraint is tight. These links help check an answer by hand.'),
              ('Certificates of optimality',
               'A certificate of optimality is a short proof that a solution is best, such as a matching dual solution. Anyone can verify it quickly. Certificates make '
               'optimisation results trustworthy without re-running the whole search.')],
 'test': [('What is the dual of a linear program built from?',
           [('a', 'Different random numbers'),
            ('b', 'The same numbers, with the roles of costs and limits swapped'),
            ('c', 'A picture of a graph'),
            ('d', 'The name of the author')],
           'b'),
          ('What does weak duality give?',
           [('a', 'The exact answer in every case'),
            ('b', 'A faster computer'),
            ('c', 'A colour for the answer'),
            ('d', 'A bound on the best primal value from any feasible dual value')],
           'd'),
          ('What do dual variables act as?',
           [('a', 'Passwords'), ('b', 'File sizes'), ('c', 'Shadow prices showing the value of relaxing a limit'), ('d', 'Network addresses')],
           'c'),
          ('What does complementary slackness say about a constraint that is not tight?',
           [('a', 'Its dual variable is zero'), ('b', 'Its dual variable is infinite'), ('c', 'It must be deleted'), ('d', 'It doubles the cost')],
           'a'),
          ('What is a certificate of optimality?',
           [('a', 'A printed award'),
            ('b', 'A password for the solver'),
            ('c', 'A list of all possible answers'),
            ('d', 'A short proof that a solution is best, which anyone can check')],
           'd')]}
