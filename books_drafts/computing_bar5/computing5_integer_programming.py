"""Integer Programming: whole-number choices, branch and bound, cutting planes, NP-hardness in general, and scheduling and routing models."""
CODE = 'computing5_integer_programming'
BOOK = {'title': 'Integer Programming',
 'subtitle': 'Whole-number choices and the search that finds them',
 'chapters': [('Whole-number choices',
               'An integer program is a linear program in which some or all variables must be whole numbers. You cannot build half a bridge or assign half a crew. Whole numbers '
               'make many real decisions possible to model, but much harder to solve.'),
              ('Branch and bound',
               'Branch and bound solves the relaxed problem, then splits the feasible region on a fractional variable. Each branch gives a bound, and branches that cannot beat '
               'the best known answer are dropped. The method is a careful search of a tree.'),
              ('Cutting planes',
               'A cutting plane is an extra linear constraint that removes fractional points without removing any whole-number solution. Adding cuts shrinks the region around the '
               'true answer. Solvers combine cuts with branching.'),
              ('NP-hardness',
               'In general, integer programming is NP-hard, so no method is known to solve all instances quickly. Some special cases are easy, and many real problems have '
               'structure that solvers exploit. Expect good performance on structured problems, not on every input.'),
              ('Scheduling and routing',
               'Integer programs model timetables, shift rosters, delivery routes and factory schedules. Yes or no choices for each task or each road are the key variables. These '
               'models are standard in airlines and logistics.'),
              ('Solver practice',
               'Good modelling matters as much as the solver. A tight formulation with strong cuts often solves far faster than a loose one with the same meaning. Engineers test '
               'models on small cases before scaling up.')],
 'test': [('What extra requirement does an integer program have?',
           [('a', 'Variables must be colours'), ('b', 'Variables must be words'), ('c', 'Some or all variables must be whole numbers'), ('d', 'Variables must be dates')],
           'c'),
          ('What does branch and bound do?',
           [('a', 'Splits the feasible region and drops branches that cannot beat the best known answer'),
            ('b', 'Prints the solution in colour'),
            ('c', 'Deletes all variables'),
            ('d', 'Replaces integers with words')],
           'a'),
          ('What is a cutting plane?',
           [('a', 'A knife for paper'),
            ('b', 'A kind of printer'),
            ('c', 'A file format'),
            ('d', 'An extra linear constraint that removes fractional points and keeps every whole-number solution')],
           'd'),
          ('In general, integer programming is what kind of problem?',
           [('a', 'Trivially easy for every input'), ('b', 'NP-hard'), ('c', 'Not a mathematical problem'), ('d', 'Solved by a single line of code')],
           'b'),
          ('Which real problem is modelled with integer programs?',
           [('a', 'Shift rosters and delivery routes'), ('b', 'Choosing a screen colour only'), ('c', 'Writing a poem'), ('d', 'Drawing a logo')],
           'a')]}
