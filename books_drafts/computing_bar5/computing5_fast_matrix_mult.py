"""Fast Matrix Multiplication: the naive cube, Strassen's method, the matrix multiplication exponent and the practical limits."""
CODE = 'computing5_fast_matrix_mult'
BOOK = {'title': 'Fast Matrix Multiplication',
 'subtitle': 'Multiplying grids of numbers with fewer operations',
 'chapters': [('The naive cube',
               'Multiplying two n by n matrices the standard way takes about n cubed multiplications. Each entry of the result is a row times a column. For a long time this was '
               'thought to be the best possible for the task.'),
              ("Strassen's method",
               'In 1969 Volker Strassen showed how to multiply 2 by 2 blocks with seven multiplications instead of eight. Applied recursively to large matrices, this gives a '
               'method with about n to the power 2.81 operations. It was the first breakthrough below the cube.'),
              ('The matrix multiplication exponent',
               'The exponent is the smallest number omega such that matrices can be multiplied in about n to the power omega operations. Better methods have pushed the best known '
               'value down toward two. Whether two is reachable is an open question.'),
              ('Numerical stability',
               'Fast methods can lose accuracy when numbers are close in size, because they add and subtract in more complicated ways. Scientific code must check results on hard '
               'inputs. Accuracy matters as much as speed.'),
              ('Practical cutoffs',
               'Fast recursive methods carry overhead, so they only beat the standard method above a certain size. Real libraries switch to ordinary multiplication for small '
               'blocks. The cutoff depends on the hardware.'),
              ('Hardware libraries',
               'Hardware libraries use carefully tuned routines to multiply matrices, taking advantage of caches and parallel units. Graphics chips and machine learning systems '
               'depend on this work. Most programmers call these libraries rather than writing their own.')],
 'test': [('About how many multiplications does the standard method need for n by n matrices?',
           [('a', 'About n cubed'), ('b', 'About n'), ('c', 'Exactly one'), ('d', 'About the logarithm of n')],
           'a'),
          ("How many multiplications does Strassen's method use for 2 by 2 blocks?",
           [('a', 'Two'), ('b', 'Twenty'), ('c', 'Seven instead of eight'), ('d', 'Eight instead of seven')],
           'c'),
          ('What does the matrix multiplication exponent measure?',
           [('a', 'The number of rows in a table'), ('b', 'The smallest power of n needed to multiply matrices'), ('c', 'The weight of a matrix'), ('d', 'The colour of a grid')],
           'b'),
          ('Why can fast methods lose accuracy?',
           [('a', 'They use fewer digits on purpose'), ('b', 'They always round up'), ('c', 'They skip all numbers'), ('d', 'They add and subtract in more complicated ways')],
           'd'),
          ('Why do fast recursive methods switch to the standard method for small blocks?',
           [('a', 'Small blocks cannot be multiplied'),
            ('b', 'The standard method is illegal'),
            ('c', 'Their overhead makes them slower on small sizes'),
            ('d', 'Small blocks are always negative')],
           'c')]}
