"""Voronoi Diagrams and Delaunay Triangulation: nearest-site regions, the duality of the two diagrams and their use in terrain meshes."""
CODE = 'computing5_voronoi_delaunay'
BOOK = {'title': 'Voronoi Diagrams and Delaunay Triangulation',
 'subtitle': 'Nearest-site regions and the triangles that pair with them',
 'chapters': [('Nearest-site regions',
               'Given a set of sites, a Voronoi diagram splits the plane into regions. Each region holds the points closer to one site than to any other. Shops, fire stations and '
               'towers are often placed with this kind of map in mind.'),
              ('Duality',
               'The Delaunay triangulation joins sites whose Voronoi regions touch. The two diagrams are dual: one can be read from the other. Knowing one gives the other with a '
               'simple construction.'),
              ('Incremental construction',
               'A Delaunay triangulation can be built by adding one site at a time. Each new site removes the triangles whose circles contain it, then reconnects the hole. '
               'Careful bookkeeping keeps the expected work per insertion small (about constant for random insertion order), so the whole build takes about n log n.'),
              ('Triangulation quality',
               'A Delaunay triangulation avoids skinny triangles where possible, because no site lies inside the circle of any triangle. Good triangle shape makes simulations and '
               'interpolation more accurate. This is why meshes often use Delaunay methods.'),
              ('Terrain meshes',
               'Terrain and landscape models often turn scattered height measurements into triangles. The Delaunay triangulation gives a sensible surface from those points. Game '
               'engines and mapping software use it for this purpose.'),
              ('Sweep algorithms',
               'A sweep algorithm moves an imaginary line across the plane and updates the structure as it passes each site. It builds Voronoi diagrams and Delaunay '
               'triangulations in about n log n time. The idea is common in computational geometry.')],
 'test': [('What does each region of a Voronoi diagram contain?',
           [('a', 'Random points'), ('b', 'Only the edges of the plane'), ('c', 'The points closer to one site than to any other'), ('d', 'Text labels')],
           'c'),
          ('What is the relationship between Voronoi and Delaunay diagrams?',
           [('a', 'They are dual, so one can be read from the other'),
            ('b', 'They are unrelated'),
            ('c', 'They are the same drawing in colour'),
            ('d', 'They cannot be built together')],
           'a'),
          ('What does a Delaunay triangulation avoid where possible?', [('a', 'Triangles of any size'), ('b', 'Sites'), ('c', 'Lines of text'), ('d', 'Skinny triangles')], 'd'),
          ('Where are Delaunay triangulations often used?',
           [('a', 'Only for printing receipts'), ('b', 'Terrain meshes built from height measurements'), ('c', 'Only for sorting email'), ('d', 'Only for weather in cities')],
           'b'),
          ('What does a sweep algorithm do?',
           [('a', 'Moves an imaginary line across the plane and updates the structure'),
            ('b', 'Deletes all the sites'),
            ('c', 'Shuffles the plane'),
            ('d', 'Prints a map in one colour')],
           'a')]}
