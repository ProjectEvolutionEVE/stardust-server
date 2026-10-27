"""Nuclear Thermal Propulsion Concepts: reactor heating of propellant, specific impulse, shielding needs, and engineering limits in general terms."""
CODE = 'engineering5_nuclear_thermal'
BOOK = {'title': 'Nuclear Thermal Propulsion Concepts',
 'subtitle': 'Heating propellant with a reactor, and why shielding and limits matter',
 'chapters': [('Heat, not burning',
               'A nuclear thermal rocket uses a reactor to heat a propellant, usually hydrogen, rather than '
               'burning it. The hot gas leaves through a nozzle and pushes the craft. The heat source is the '
               'reactor, not a chemical flame.'),
              ('Specific impulse',
               'Specific impulse is a measure of how much thrust an engine gets from each unit of '
               'propellant. Light hydrogen leaves at a high speed when heated, so nuclear thermal designs '
               'can reach a specific impulse roughly double that of common chemical rockets. That is the '
               'main reason the concept is studied.'),
              ('Shielding',
               'A reactor gives off radiation, so the crew and sensitive equipment need shielding. The '
               'shield adds mass, and mass costs thrust and fuel. Engineers place the reactor far from the '
               'crew and balance the shield against the mission length.'),
              ('Engineering limits',
               'The reactor must run at very high temperature for a long time, and the materials must not '
               'fail. The hydrogen must be handled and kept cold until it is used. Each limit shapes the '
               'size and cost of the design.'),
              ('Cost and safety rules',
               'Any nuclear system must meet strict safety and licensing rules. The cost of building and '
               'proving the reactor is high, and public trust must be earned. Designers keep the concept in '
               'a clear, open review process.'),
              ('A concept, not yet a craft',
               'Nuclear thermal propulsion has been tested on the ground in the past, but no operational '
               'craft uses it today. The concept shows promise for long trips. Its real value depends on the '
               'cost and safety work still to come.')],
 'test': [('How does a nuclear thermal rocket make its thrust?',
           [('a', 'It burns wood'),
            ('b', 'It spins a propeller'),
            ('c', 'It uses wheels on the ground'),
            ('d', 'A reactor heats a propellant that leaves through a nozzle')],
           'd'),
          ('What does specific impulse measure?',
           [('a', 'The number of seats on the craft'),
            ('b', 'The length of the hold'),
            ('c', 'How much thrust an engine gets from each unit of propellant'),
            ('d', 'The price of the paint')],
           'c'),
          ('Why is shielding needed around a reactor?',
           [('a', 'Because the reactor gives off radiation'),
            ('b', 'To keep the craft from floating'),
            ('c', 'To make the paint dry faster'),
            ('d', 'To stop the lights')],
           'a'),
          ('What is the downside of heavy shielding?',
           [('a', 'It makes the craft lighter'),
            ('b', 'It removes all radiation from the crew'),
            ('c', 'It adds mass, which costs thrust and fuel'),
            ('d', 'It cools the reactor for free')],
           'c'),
          ('Has an operational nuclear thermal craft flown today?',
           [('a', 'Yes, many thousands fly every day'),
            ('b', 'No, the concept has been studied and tested on the ground but not flown'),
            ('c', 'Yes, it powers the cabin lights'),
            ('d', 'It flies only in the sea')],
           'b')]}
