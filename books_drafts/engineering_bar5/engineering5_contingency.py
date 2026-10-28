"""Contingency Reserves and Budget Risk: risk-based reserves, Monte Carlo cost ranges, reserve drawdown and budget governance."""
CODE = 'engineering5_contingency'
BOOK = {'title': 'Contingency Reserves and Budget Risk',
 'subtitle': 'Setting aside money for what might go wrong, and governing how it is used',
 'chapters': [('Why reserves exist',
               'Projects almost always meet surprises, such as late materials or unexpected ground '
               'conditions. A contingency reserve is money set aside for these known unknowns. Without it, a '
               'small surprise can break the budget.'),
              ('Risk-based reserves',
               'A risk-based reserve is sized from the list of risks, how likely each one is and what it '
               'would cost. The total of the expected costs guides the size of the reserve. A reserve sized '
               'on a guess is weaker than one based on the risk list.'),
              ('Monte Carlo cost ranges',
               'A Monte Carlo analysis runs the cost model many times with random values for the uncertain '
               'inputs. The results form a range of possible total costs. The range shows how likely it is '
               'that the budget will hold.'),
              ('Reserve drawdown',
               'Drawdown is the use of the reserve as risks arrive. Tracking drawdown shows whether the '
               'reserve is being used faster than the project is moving forward. A reserve used early may '
               'leave the project short later.'),
              ('Budget governance',
               'Governance sets who may release reserve money and under what rules. Clear approval steps '
               'stop the reserve being spent on things that are not risks. Records show every release and '
               'the reason for it.'),
              ('The money side of budget risk',
               'A budget with no reserve looks cheap but is risky. A large reserve ties up money that could '
               'earn a return elsewhere. The right size balances the cost of holding money against the cost '
               'of running short.')],
 'test': [('What is a contingency reserve?',
           [('a', 'Money set aside for known unknowns in a project'),
            ('b', 'A spare box of pencils'),
            ('c', 'A type of tent'),
            ('d', 'A parking space')],
           'a'),
          ('What is a Monte Carlo cost range?',
           [('a', 'A map of a casino'),
            ('b', 'A range of total costs from many random runs of the cost model'),
            ('c', 'A list of staff names'),
            ('d', 'A type of bolt')],
           'b'),
          ('What is reserve drawdown?',
           [('a', 'Adding paint to the reserve'),
            ('b', 'Selling the office'),
            ('c', 'Using the reserve as risks arrive'),
            ('d', 'Painting the budget sheet')],
           'c'),
          ('Why does budget governance matter?',
           [('a', 'It makes the reserve disappear'),
            ('b', 'It removes the need for records'),
            ('c', 'It lets anyone spend without asking'),
            ('d', 'It sets who may release reserve money and under what rules')],
           'd'),
          ('What is the risk of a budget with no reserve?',
           [('a', 'A small surprise can break the budget'),
            ('b', 'The budget always stays exact'),
            ('c', 'Surprises become impossible'),
            ('d', 'The project finishes early by default')],
           'a')]}
