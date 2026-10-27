"""The Lambda Calculus: a model of computation built from functions alone, and why it underpins functional languages."""
CODE = 'computing5_lambda_calculus'
BOOK = {'title': 'The Lambda Calculus',
 'subtitle': 'Computing with functions alone',
 'chapters': [('Only functions',
               'The lambda calculus has one kind of thing: the function. A function takes a named input and gives a body, written as a lambda followed by a name and an '
               'expression. Alonzo Church and Alan Turing both studied it in the 1930s as a model of computation.'),
              ('Substitution',
               'To apply a function to an argument, replace each free copy of the input name in the body with the argument. Care is needed so that names are not captured by '
               'accident. Substitution is the core step of computing in this system.'),
              ('Beta reduction',
               'Beta reduction is the rule that turns an application of a function into its body with the argument substituted. Repeated reductions make up a calculation. Some '
               'expressions reduce forever, while others reach a normal form with no reductions left.'),
              ('Church numerals',
               'Church numerals encode a number n as a function that applies another function n times. Addition, multiplication and a test for zero can all be written as '
               'functions on these encodings. Numbers and arithmetic come from functions alone.'),
              ('Fixed points and recursion',
               'A fixed point of a function f is a value x where f applied to x gives x again. A fixed-point combinator lets a function refer to itself without naming itself. '
               'Recursion in functional languages has this same root.'),
              ('Why it matters',
               'The lambda calculus is the core of functional programming. Features such as closures and functions passed as values are direct descendants of it. It also shows '
               'that a very small system is enough for every computable function.')],
 'test': [('What is the only kind of thing in the lambda calculus?', [('a', 'A number'), ('b', 'A function'), ('c', 'A file'), ('d', 'A table')], 'b'),
          ('What does substitution do?',
           [('a', 'Deletes the function'),
            ('b', 'Prints the answer on screen'),
            ('c', 'Sends the expression over a network'),
            ('d', 'Replaces the input name in a body with the argument')],
           'd'),
          ('What is a Church numeral?',
           [('a', 'A printed digit'), ('b', 'A kind of network card'), ('c', 'A function that applies another function n times'), ('d', 'A date in the calendar')],
           'c'),
          ('What is a fixed point of a function f?',
           [('a', 'A value x where f applied to x gives x'), ('b', 'The first line of a program'), ('c', 'A function with no arguments'), ('d', 'The largest number in a list')],
           'a'),
          ('Why does the lambda calculus matter to programming?',
           [('a', 'It replaced every compiler'), ('b', 'It only works on paper'), ('c', 'It cannot compute anything'), ('d', 'It is the core of functional programming languages')],
           'd')]}
