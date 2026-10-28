"""Machine Learning for Prospectivity: training models on known deposits, avoiding overfitting, validating on withheld areas, and knowing the limits."""
CODE = 'mining4_ml_prospectivity'
BOOK = {'title': 'Machine Learning for Prospectivity',
 'subtitle': 'Honest prospect maps from known deposits and careful testing',
 'chapters': [('Known deposits as training data',
               'A prospectivity model learns from places where ore is already known. The known deposits are '
               'the training data, and maps of geology, geophysics and geochemistry are the inputs. The '
               'model looks for patterns linked to those deposits.'),
              ('Weights of evidence',
               'Weights of evidence is a simple statistical method. It gives each map layer a weight based '
               'on how often ore occurs where that layer is present. The weights are then added together '
               'into a prospect map.'),
              ('Overfitting',
               'Overfitting happens when a model learns the training data too closely and fails on new '
               'ground. It can look perfect on the known deposits and still be useless. Simple models and '
               'careful checks help avoid it.'),
              ('Validation on withheld areas',
               'To test a model honestly, a team holds back some known deposits and some areas. It builds '
               'the model without them, then checks whether it finds the withheld deposits. This is the real '
               'test of a prospect map.'),
              ('Honest prospectivity maps',
               'An honest map shows its uncertainty and its test results. It does not promise ore in every '
               'shaded area. The map is a guide for where to explore next, not a guarantee of a deposit.'),
              ('Limits of models',
               'A model can only learn from the data it has. Rare deposit types may have too few examples. A '
               'geologist must always check the model against field knowledge before acting.')],
 'test': [('What is the training data for a prospectivity model?',
           [('a', 'Random numbers'),
            ('b', 'Pictures of animals'),
            ('c', 'Places where ore is already known'),
            ('d', 'Recipes')],
           'c'),
          ('What does weights of evidence do?',
           [('a', 'Gives each map layer a weight based on how often ore occurs there'),
            ('b', 'Weighs the drill rigs'),
            ('c', 'Weighs the rock in a scale'),
            ('d', 'Counts the cars on a road')],
           'a'),
          ('What is overfitting?',
           [('a', 'A model that is too small to run'),
            ('b', 'A model with no inputs'),
            ('c', 'A model that runs too fast'),
            ('d', 'A model that learns training data too closely and fails on new ground')],
           'd'),
          ('How is a model tested honestly?',
           [('a', 'By using only the training data again'),
            ('b', 'By holding back known deposits and areas and checking whether it finds them'),
            ('c', 'By asking a friend'),
            ('d', 'By guessing the result')],
           'b'),
          ('What should an honest prospect map show?',
           [('a', 'A promise of ore in every area'),
            ('b', 'Only the colour blue'),
            ('c', 'A list of recipes'),
            ('d', 'Its uncertainty and test results')],
           'd')]}
