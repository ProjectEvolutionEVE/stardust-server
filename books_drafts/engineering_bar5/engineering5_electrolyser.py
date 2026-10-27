"""Electrolyser Design and Efficiency: electrode reactions, cell voltage losses, membranes, efficiency curves, and the money side of cost per kilogram of hydrogen."""
CODE = 'engineering5_electrolyser'
BOOK = {'title': 'Electrolyser Design and Efficiency',
 'subtitle': 'Electrode reactions, voltage losses, membranes, and the cost of hydrogen',
 'chapters': [('Splitting water with power',
               'An electrolyser passes electric current through water to split it into hydrogen and oxygen. '
               'Hydrogen forms at the cathode and oxygen at the anode. The process needs electricity, so the '
               'power price is the biggest part of the running cost.'),
              ('The electrode reactions',
               'At the anode, water loses electrons to make oxygen and hydrogen ions. At the cathode, those '
               'ions gain electrons to make hydrogen gas. The two reactions must be balanced in charge, and '
               'each one needs a catalyst to run at a useful speed.'),
              ('Cell voltage losses',
               'The ideal voltage to split water is about 1.23 volts at standard conditions. A real cell '
               'needs more, because of the energy lost to the reactions, to the resistance of the cell, and '
               'to the transport of gas and ions. These losses set the efficiency.'),
              ('Membranes',
               'A membrane separates the hydrogen from the oxygen while letting the ions pass. Proton '
               'exchange membranes and alkaline separators are the two main kinds. Each has its own '
               'strengths in cost, purity and working range.'),
              ('Efficiency curves',
               'An electrolyser is most efficient at a certain current density, and the efficiency falls as '
               'the current rises. Engineers plot an efficiency curve to choose the operating point. Running '
               'at the best point saves power, but a lower output costs more per kilogram.'),
              ('The money side',
               'The cost per kilogram of hydrogen depends on the electricity price, the hours of running, '
               'the capital cost of the plant and the maintenance. A plant that runs most hours spreads its '
               'capital cost over more hydrogen. Engineers judge every design by the total cost over its '
               'life.')],
 'test': [('What does an electrolyser do?',
           [('a', 'Splits water into hydrogen and oxygen using electric current'),
            ('b', 'Makes water from hydrogen and oxygen in a burner'),
            ('c', 'Turns paint into metal'),
            ('d', 'Stores sunlight in a tank')],
           'a'),
          ('About what voltage is the ideal minimum to split water?',
           [('a', 'About 1 million volts'),
            ('b', 'Exactly zero volts'),
            ('c', 'About 1.23 volts at standard conditions'),
            ('d', 'About 230 volts in every case')],
           'c'),
          ('What is the job of a membrane in an electrolyser?',
           [('a', 'To hold the paint'),
            ('b', 'To separate hydrogen from oxygen while letting ions pass'),
            ('c', 'To store the cabin air'),
            ('d', 'To make the cell colder')],
           'b'),
          ('What is the largest part of the running cost of an electrolyser?',
           [('a', 'The paint'), ('b', 'The cabin lights'), ('c', 'The seats'), ('d', 'The electricity')],
           'd'),
          ('Why does running at the best point on an efficiency curve matter?',
           [('a', 'It makes the cell louder'),
            ('b', 'It removes the need for water'),
            ('c', 'It saves power for each kilogram of hydrogen made'),
            ('d', 'It turns the oxygen into paint')],
           'c')]}
