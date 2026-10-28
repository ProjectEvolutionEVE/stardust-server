"""Layer of Protection Analysis: independent layers, risk reduction factors and target frequencies."""
CODE = 'engineering5_lopa'
BOOK = {'title': 'Layer of Protection Analysis',
 'subtitle': 'Independent layers, risk reduction factors and the money side of protection',
 'chapters': [('Layers, not just one guard',
               'Layer of Protection Analysis, or LOPA, checks whether the protection in a process is enough. '
               'Instead of relying on one safeguard, it counts several layers. Each layer must stop the bad '
               'outcome on its own, so if one fails the next still works.'),
              ('What makes a layer independent',
               'An independent protection layer must be effective, auditable and independent of the cause it '
               'guards against. It must not share a failure with the layer before it. A relief valve and an '
               'alarm run by the same faulty sensor are not two independent layers.'),
              ('Risk reduction factors',
               'A layer reduces risk by a factor. If a layer fails on demand one time in a hundred, its risk '
               'reduction factor is 100. The factor is simply one divided by the probability that the layer '
               'fails when it is needed.'),
              ('Target frequency',
               'The target frequency is the rate at which the bad event is acceptable. Start with how often '
               'the initiating event happens. Divide that by the target, and the result tells you how much '
               'extra risk reduction you need from the layers.'),
              ('Keeping the layers honest',
               'A layer on paper must also work in practice. Each one needs a named owner, regular testing '
               'and records that show it was checked. A layer that is never tested may give false comfort.'),
              ('The money side',
               'Each protection layer costs money to buy, install and maintain. A good analysis shows where '
               'extra layers are needed and where they are not. Spending where the risk is real avoids '
               'waste, and it also shows the layers you can trust.')],
 'test': [('What does LOPA check?',
           [('a', 'Whether the paint colours are correct'),
            ('b', 'Whether a process has enough independent protection'),
            ('c', 'How many workers were hired last year'),
            ('d', 'The price of raw steel')],
           'b'),
          ('A layer fails on demand one time in a hundred. What is its risk reduction factor?',
           [('a', '1'), ('b', '10'), ('c', '100'), ('d', '1000')],
           'c'),
          ('Which feature must an independent protection layer have?',
           [('a', 'It must be the newest layer'),
            ('b', 'It must be operated by one person only'),
            ('c', 'It must cost more than the process'),
            ('d', 'It must be independent of the cause it guards against')],
           'd'),
          ('What does dividing the initiating event rate by the target frequency give?',
           [('a', 'The extra risk reduction the layers must provide'),
            ('b', 'The weather forecast'),
            ('c', 'The number of workers on shift'),
            ('d', 'The count of pipe joints')],
           'a'),
          ('Why must each layer be tested regularly?',
           [('a', 'So it can be sold at a higher price'),
            ('b', 'So the layer is not a false comfort'),
            ('c', 'So the owner has something to do'),
            ('d', 'So the paint does not peel')],
           'b')]}
