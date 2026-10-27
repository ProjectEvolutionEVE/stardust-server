"""Convex Hulls: convex sets, the Graham scan and gift wrapping, orientation tests, floating-point robustness and uses in maps and collision checks."""
CODE = 'computing5_convex_hulls'
BOOK = {'title': 'Convex Hulls',
 'subtitle': 'The shape a set of points wraps around',
 'chapters': [('Convex sets',
               'A set is convex if the straight line between any two of its points stays inside the set. A disc is convex, and a crescent is not. The convex hull of a set of '
               'points is the smallest convex shape that contains all of them.'),
              ('The Graham scan',
               'The Graham scan sorts the points by angle around a starting point, then walks around them with a stack. It removes points that would make a dent in the boundary. '
               'Its running time is dominated by the sort, about n log n.'),
              ('Gift wrapping',
               'Gift wrapping starts at a point known to be on the hull and repeatedly finds the next point that turns the boundary the most in one direction. It is simple, and '
               'its cost depends on how many points lie on the hull. It is fast when the hull is small.'),
              ('Orientation tests',
               'An orientation test asks whether three points make a left turn, a right turn or a straight line. It is computed from a small determinant of coordinates. Almost '
               'every hull algorithm is built from this single test.'),
              ('Robustness with floating point',
               'Computers store coordinates with rounding error, so a nearly straight line may be tested wrongly. Robust code uses exact arithmetic or careful tolerances. A tiny '
               'error can make a hull algorithm produce a broken shape.'),
              ('Maps and collisions',
               'Convex hulls appear in map tools, in cutting out shapes for manufacturing, and in games that check whether two objects touch. A simple convex shape is much '
               'cheaper to test than a detailed one. Engineers often use the hull as a quick first check.')],
 'test': [('When is a set convex?',
           [('a', 'When it has exactly four corners'),
            ('b', 'When the straight line between any two of its points stays inside it'),
            ('c', 'When it is printed in colour'),
            ('d', 'When it has no points')],
           'b'),
          ('What is the convex hull of a set of points?',
           [('a', 'The largest square inside them'),
            ('b', 'A list of their names'),
            ('c', 'A line through their centre'),
            ('d', 'The smallest convex shape containing all of them')],
           'd'),
          ('What does the Graham scan begin by doing?',
           [('a', 'Printing each point'), ('b', 'Deleting every second point'), ('c', 'Sorting the points by angle around a starting point'), ('d', 'Drawing a spiral')],
           'c'),
          ('What does an orientation test decide?',
           [('a', 'Whether three points turn left, turn right or are in a straight line'), ('b', 'The colour of a point'), ('c', 'The name of a file'), ('d', 'The date of a map')],
           'a'),
          ('Why is floating-point rounding a risk for hull code?',
           [('a', 'Points cannot be stored at all'),
            ('b', 'Rounding makes every shape square'),
            ('c', 'Computers reject all decimals'),
            ('d', 'A nearly straight line may be tested wrongly')],
           'd')]}
