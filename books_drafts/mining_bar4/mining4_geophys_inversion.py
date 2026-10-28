"""Inverting Geophysical Data in 3D: how geophysicists build a 3D model from measured data, why many models can fit, and how to test the result."""
CODE = 'mining4_geophys_inversion'
BOOK = {'title': 'Inverting Geophysical Data in 3D',
 'subtitle': 'Building 3D ground models from measured fields',
 'chapters': [('The inverse problem',
               'Geophysics measures effects at the surface, such as magnetic or electrical fields. The '
               'inverse problem asks what underground shape would cause those effects. Solving it builds a '
               'model of the ground below.'),
              ('Non-uniqueness',
               'More than one underground model can fit the same measured data. This is called '
               'non-uniqueness. A geologist must know that a single answer is never the full story.'),
              ('Model regularisation',
               'To choose a sensible model, the software adds rules that favour smooth or simple shapes. '
               'These rules are called regularisation. The rules must be chosen with care, because they '
               'shape the result.'),
              ('Constraints from drill holes',
               'Drill holes give known rock types and properties at specific points. Adding them as '
               'constraints narrows the set of possible models. A model that disagrees with the drill holes '
               'is not a good model.'),
              ('Uncertainty maps',
               'Uncertainty maps show where the model is less reliable. They are drawn so a team can see '
               'which parts of the picture are firm and which are guesses. Uncertainty is shown as clearly '
               'as the model itself.'),
              ('Checking an inversion',
               'A good inversion is checked by how well it fits the data and by how well it agrees with '
               'geology. Tests on synthetic data show whether the method can recover a known shape. Checks '
               'are done before any money is spent on drilling.')],
 'test': [('What does the inverse problem ask?',
           [('a', 'What colour the sky is'),
            ('b', 'What underground shape would cause the measured effects'),
            ('c', 'What the price of gold will be'),
            ('d', 'Who owns the land')],
           'b'),
          ('What is non-uniqueness?',
           [('a', 'A model that cannot be drawn'),
            ('b', 'A model with no data'),
            ('c', 'A model with one colour'),
            ('d', 'More than one model can fit the same data')],
           'd'),
          ('What does regularisation add to an inversion?',
           [('a', 'Rules that favour smooth or simple shapes'),
            ('b', 'Random noise'),
            ('c', 'A sound effect'),
            ('d', 'A map of the stars')],
           'a'),
          ('What do drill holes do for a 3D model?',
           [('a', 'They remove the data'),
            ('b', 'They make the model random'),
            ('c', 'They add known constraints that narrow the models'),
            ('d', 'They have no effect')],
           'c'),
          ('What do uncertainty maps show?',
           [('a', 'The weather for next week'),
            ('b', 'Where the model is firm and where it is a guess'),
            ('c', 'The route of a bus'),
            ('d', 'The age of a tree')],
           'b')]}
