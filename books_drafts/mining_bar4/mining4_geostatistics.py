"""Geostatistics and Kriging: using variograms to measure spatial correlation, ordinary kriging to estimate blocks, and knowing the limits of estimates."""
CODE = 'mining4_geostatistics'
BOOK = {'title': 'Geostatistics and Kriging',
 'subtitle': 'Estimating ore grade between drill holes',
 'chapters': [('Variograms and spatial correlation',
               'A variogram measures how much two sample values differ as the distance between them grows. '
               'Close samples are usually similar, and far ones less so. The variogram describes this '
               'pattern of correlation.'),
              ('Ordinary kriging',
               'Ordinary kriging estimates the grade of an unsampled point by weighting nearby samples. The '
               'weights come from the variogram. Kriging gives the best linear estimate under clear '
               'assumptions.'),
              ('Estimating blocks',
               'Mines plan with blocks, which are small volumes of rock. Kriging estimates a grade for each '
               'block from the samples around it. The block grades form the basis of the mine plan.'),
              ('Estimation variance',
               'Kriging also gives an estimation variance, which measures how uncertain each estimate is. '
               'Blocks far from samples have high variance. A planner must look at the variance, not only '
               'the grade.'),
              ('Declustering',
               'Samples are often clustered where drilling was dense. Declustering corrects for this, so the '
               'average grade is not pulled toward the dense area. It makes the statistics fair across the '
               'whole deposit.'),
              ('Limits of estimates',
               'An estimate is only as good as its data and its assumptions. Estimates are smoothed and '
               'cannot predict exact grades in one block. The team must check estimates against new drilling '
               'and mining results.')],
 'test': [('What does a variogram measure?',
           [('a', 'The weight of a drill rig'),
            ('b', 'The height of a hill'),
            ('c', 'The speed of a truck'),
            ('d', 'How much sample values differ as distance grows')],
           'd'),
          ('How does ordinary kriging estimate a point?',
           [('a', 'By guessing from the colour of the map'),
            ('b', 'By weighting nearby samples, using the variogram'),
            ('c', 'By picking a random sample'),
            ('d', 'By averaging the whole planet')],
           'b'),
          ('What is a mine plan built from?',
           [('a', 'Pictures of birds'),
            ('b', 'Lists of recipes'),
            ('c', 'Blocks of rock with estimated grades'),
            ('d', 'Weather forecasts')],
           'c'),
          ('What does estimation variance tell a planner?',
           [('a', 'How uncertain each estimate is'),
            ('b', 'The price of the metal'),
            ('c', 'The colour of the rock'),
            ('d', 'The number of workers')],
           'a'),
          ('Why is declustering needed?',
           [('a', 'To remove all the samples'),
            ('b', 'To make drilling faster'),
            ('c', 'So dense drilling does not pull the average unfairly'),
            ('d', 'To turn rock into water')],
           'c')]}
