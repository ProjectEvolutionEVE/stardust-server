"""Hybrid Rocket Motors: solid fuel with liquid oxidiser, regression rate, throttling, mixture ratio, and safety."""
CODE = 'engineering5_hybrid_rocket'
BOOK = {'title': 'Hybrid Rocket Motors',
 'subtitle': 'Solid fuel, liquid oxidiser, and the safety and control they offer',
 'chapters': [('Two phases in one motor',
               'A hybrid rocket keeps its fuel in solid form and feeds its oxidiser from a separate tank. '
               'Most designs use a solid fuel such as a plastic and a liquid or gaseous oxidiser. The two '
               'meet in the chamber and burn.'),
              ('Regression rate',
               'The fuel surface burns away as the motor runs, and the rate at which it recedes is the '
               'regression rate. It depends mainly on the oxidiser flow over the fuel surface. Engineers '
               'measure it in tests to predict how much fuel is left at each moment.'),
              ('Throttling',
               'A hybrid motor is easy to throttle, because the thrust follows the oxidiser flow. Closing '
               'the oxidiser valve reduces the burn, and opening it increases the burn. This makes the motor '
               'simpler to control than a solid motor.'),
              ('Mixture ratio',
               'The mixture ratio is the balance of oxidiser to fuel in the chamber. As the fuel surface '
               'grows or shrinks, the ratio can drift. Engineers keep the ratio in a range that gives good '
               'performance and protects the hardware.'),
              ('Safety',
               'Because fuel and oxidiser are kept apart until the moment they are needed, a hybrid is less '
               'prone to an accidental explosion than many solid motors. The oxidiser tank and the valves '
               'still need careful design. Handling and testing rules protect the crew and the ground.'),
              ('The cost of simplicity',
               'Hybrids trade some performance for simplicity, control and safety. Their regression rate is '
               'often slower than designers would like, which limits thrust. Engineers weigh these '
               'trade-offs against the mission and the budget.')],
 'test': [('How is fuel stored in a hybrid rocket motor?',
           [('a', 'In solid form'),
            ('b', 'As a liquid in the cabin'),
            ('c', 'As a gas in the hold'),
            ('d', 'It is not stored')],
           'a'),
          ('What is the regression rate?',
           [('a', 'The price of the fuel'),
            ('b', 'The speed of the crew'),
            ('c', 'The rate at which the fuel surface burns away'),
            ('d', 'The colour of the chamber')],
           'c'),
          ('How is the thrust of a hybrid motor usually controlled?',
           [('a', 'By changing the colour of the nozzle'),
            ('b', 'By adjusting the oxidiser flow'),
            ('c', 'By opening the cabin doors'),
            ('d', 'By turning off the lights')],
           'b'),
          ('What is the mixture ratio?',
           [('a', 'The ratio of seats to passengers'),
            ('b', 'The ratio of paint to metal'),
            ('c', 'The ratio of day to night'),
            ('d', 'The balance of oxidiser to fuel in the chamber')],
           'd'),
          ('Why is a hybrid motor often safer than many solid motors?',
           [('a', 'It has no chamber'),
            ('b', 'It runs on sunlight'),
            ('c', 'Fuel and oxidiser are kept apart until they are needed'),
            ('d', 'It never burns')],
           'c')]}
