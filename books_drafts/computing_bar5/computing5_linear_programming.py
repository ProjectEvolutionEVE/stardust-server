"""Linear Programming and the Simplex Method: linear objectives and constraints, feasible regions and how the simplex method finds the best vertex."""
CODE = 'computing5_linear_programming'
BOOK = {'title': 'Linear Programming and the Simplex Method',
 'subtitle': 'Best choices under straight-line limits',
 'chapters': [('Objectives and constraints',
               'A linear program maximises or minimises a linear objective, subject to linear constraints on the variables. A factory might maximise profit given limits on labour '
               'and materials. The model is a set of straight-line rules.'),
              ('The feasible region',
               'The constraints together form a feasible region: all the choices that satisfy every rule. For linear programs this region is a convex shape with flat sides. Every '
               'feasible choice lies inside it.'),
              ('Vertices',
               'If a linear program has a best answer, one of the best answers sits at a vertex, a corner of the feasible region. This is the key fact that makes the problem '
               'tractable. Searching corners is much easier than searching every point.'),
              ('The simplex method',
               'The simplex method walks from one vertex to a neighbouring vertex that improves the objective, until no neighbour is better. George Dantzig developed it in the '
               '1940s. It is fast in practice, even though some carefully built inputs make it slow.'),
              ('Duality',
               'Every linear program has a companion problem called its dual. The dual gives bounds on the original objective, and their values match when both have optimal '
               'solutions. Duality is a tool for checking answers.'),
              ('Solving allocation problems',
               'Linear programming solves allocation questions: how much of each product to make, how to route goods, how to feed animals at least cost. Real solvers handle '
               'thousands of variables. The results are used in logistics, energy and finance.')],
 'test': [('What does a linear program optimise?',
           [('a', 'A linear objective under linear constraints'), ('b', 'A colour scheme'), ('c', 'A list of names'), ('d', 'The weather')],
           'a'),
          ('What shape is the feasible region of a linear program?',
           [('a', 'A spiral'), ('b', 'A ring with holes'), ('c', 'A convex shape with flat sides'), ('d', 'A random cloud of points')],
           'c'),
          ('Where can the best answer of a linear program lie?',
           [('a', 'Always at the centre of the Earth'), ('b', 'At a vertex of the feasible region'), ('c', 'Outside every constraint'), ('d', 'In a random place')],
           'b'),
          ('Who developed the simplex method?', [('a', 'Alan Turing'), ('b', 'Ada Lovelace'), ('c', 'Grace Hopper'), ('d', 'George Dantzig')], 'd'),
          ('What is the dual of a linear program used for?',
           [('a', 'Printing reports'), ('b', 'Deleting constraints'), ('c', 'Giving bounds on the original objective and checking answers'), ('d', 'Choosing a font')],
           'c')]}
