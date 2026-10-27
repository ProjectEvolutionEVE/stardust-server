"""Parameterised Complexity: a second input dimension, fixed-parameter tractability, kernelisation and the W-hierarchy."""
CODE = 'computing5_parameterised_complexity'
BOOK = {'title': 'Parameterised Complexity',
 'subtitle': 'When a small hidden number makes a hard problem workable',
 'chapters': [('A second dimension',
               'Parameterised complexity measures running time against the input size and also against a small parameter. The parameter is a number that is often small in '
               'practice, such as the number of errors allowed. Some hard problems become workable when the parameter is small.'),
              ('Fixed-parameter tractability',
               'A problem is fixed-parameter tractable if it can be solved in time f(k) times a polynomial in the input size, where k is the parameter. The function f may grow '
               'fast, but the input size enters only polynomially. Such problems stay manageable when k is small.'),
              ('Kernelisation',
               'A kernel is a smaller instance that keeps the answer of the original. Kernelisation shrinks an input to a size depending only on the parameter. After the '
               'reduction, any slow method runs on a small problem.'),
              ('The W-hierarchy',
               'The W-hierarchy is a family of classes that are believed not to be fixed-parameter tractable. Problems complete for these classes are considered unlikely to have '
               'such methods. It plays a role similar to NP in classical complexity.'),
              ('Vertex cover',
               'In vertex cover, we seek a small set of vertices that touches every edge. With a parameter k for the size of the cover, a simple branching method runs in time '
               'about 2 to the power k times a polynomial. Kernels can shrink the graph first.'),
              ('Practical solvers',
               'Practical solvers combine kernelisation, bounded search and strong heuristics. They are tuned to the parameters that occur in real data. Choosing the right '
               'parameter is often the most important design decision.')],
 'test': [('What does parameterised complexity add to the input size?',
           [('a', 'A second copy of the input'), ('b', 'A colour for each vertex'), ('c', 'A password'), ('d', 'A small parameter measured separately')],
           'd'),
          ('What is fixed-parameter tractability?',
           [('a', 'Solvable in one step always'),
            ('b', 'Solvable in time f(k) times a polynomial in the input size'),
            ('c', 'Impossible to solve'),
            ('d', 'Solvable only on paper')],
           'b'),
          ('What does kernelisation produce?',
           [('a', 'A smaller instance that keeps the answer of the original'), ('b', 'A bigger graph'), ('c', 'A random number'), ('d', 'A new programming language')],
           'a'),
          ('What is vertex cover?',
           [('a', 'Painting every vertex red'),
            ('b', 'Counting the edges in a picture'),
            ('c', 'Finding a small set of vertices that touches every edge'),
            ('d', 'Sorting names alphabetically')],
           'c'),
          ('What do solvers in practice combine?',
           [('a', 'Only printing'), ('b', 'Kernelisation, bounded search and heuristics'), ('c', 'Only random guesses'), ('d', 'Only paper forms')],
           'b')]}
