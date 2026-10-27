"""Online Algorithms and Competitive Ratio: decisions made without knowing the future, the ski rental problem and adversarial inputs."""
CODE = 'computing5_online_algorithms'
BOOK = {'title': 'Online Algorithms and Competitive Ratio',
 'subtitle': 'Deciding now without knowing what comes next',
 'chapters': [('Decisions without the future',
               'An online algorithm must act on each input as it arrives, without seeing the rest. Caching, routing and renting are everyday examples. The question is how well '
               'such an algorithm can do compared with one that knows the future.'),
              ('Competitive ratio',
               "The competitive ratio compares an online algorithm's cost with the cost of the best offline choice on the same input, taken in the worst case. A ratio of 2 means "
               'the online cost is at most twice the best possible. It measures the price of not knowing the future.'),
              ('Ski rental',
               'In ski rental, you can rent skis for one unit per day or buy them for a fixed price. You do not know how many days you will ski. Renting until the rental cost '
               'equals the purchase price, then buying, gives a competitive ratio of 2.'),
              ('Paging',
               'Paging is an online problem where a cache of limited size must choose which page to evict when a new page is needed. Without knowing future requests, a simple '
               'rule such as least recently used performs well in practice. Analysis shows it is competitive.'),
              ('Adversaries',
               "An adversary designs the input after seeing the algorithm's rules, choosing the worst case for it. Competitive analysis assumes such adversaries exist. It is a "
               'guarantee against any input, not a prediction of typical inputs.'),
              ('Randomised online choices',
               'Randomised online algorithms make random choices, which can beat deterministic ones against some adversaries. Against an adversary that cannot see the random '
               'bits, the expected cost can be much lower. The analysis depends on what the adversary knows.')],
 'test': [('What must an online algorithm do with each input?',
           [('a', 'Act on it as it arrives, without seeing the rest'), ('b', 'Wait for the whole input first'), ('c', 'Print the input in colour'), ('d', 'Ignore the input')],
           'a'),
          ('What does the competitive ratio compare?',
           [('a', 'Two printers'), ('b', 'The price of two cars'), ('c', 'The online cost with the best offline cost, in the worst case'), ('d', 'The speed of two screens')],
           'c'),
          ('In ski rental, what is a common strategy with ratio 2?',
           [('a', 'Always buy on day one'), ('b', 'Rent until the rental cost equals the purchase price, then buy'), ('c', 'Never ski'), ('d', 'Rent forever')],
           'b'),
          ('What is an adversary in this field?',
           [('a', 'A friendly user'), ('b', 'A type of printer'), ('c', 'A network cable'), ('d', 'An input designed to be worst for the algorithm')],
           'd'),
          ('What can randomised online choices do against some adversaries?',
           [('a', 'Make every cost infinite'),
            ('b', 'Remove the need for memory'),
            ('c', 'Lower the expected cost compared with deterministic ones'),
            ('d', 'Predict the adversary exactly')],
           'c')]}
