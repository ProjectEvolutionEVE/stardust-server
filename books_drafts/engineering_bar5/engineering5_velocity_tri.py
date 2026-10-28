"""Velocity Triangles in Turbomachinery: absolute and relative velocities, work input, incidence and deviation angles, and blade angle choice."""
CODE = 'engineering5_velocity_tri'
BOOK = {'title': 'Velocity Triangles in Turbomachinery',
 'subtitle': 'Absolute and relative speeds, work input, and choosing blade angles',
 'chapters': [('Three speeds on one diagram',
               'A velocity triangle shows three speeds at once: the blade speed, the absolute speed of the '
               'gas as seen from outside, and the relative speed of the gas as seen from the moving blade. '
               'The three form a triangle, and the diagram makes the flow easy to read.'),
              ('Absolute and relative',
               'Absolute velocity is measured from the casing, and relative velocity is measured from the '
               'rotating blade. A blade only cares about the relative flow, because that is the flow it '
               'meets. Engineers draw both to see how the gas strikes each blade.'),
              ('Work input',
               'The work a rotor does on the gas, or takes from it, follows from the change in the swirl of '
               'the flow. Euler work equation puts this into a formula using the blade speed and the swirl '
               'velocities. A bigger change in swirl means more work through the same blade speed.'),
              ('Incidence and deviation',
               'Incidence is the angle between the incoming flow and the blade leading edge. Deflection is the angle through which the blade turns the flow. Deviation is the difference between the flow\'s exit angle and the blade\'s exit angle. Both must stay within limits, or '
               'the flow separates and losses rise sharply.'),
              ('Choosing the blade angle',
               'The blade angle is set so that the flow meets it smoothly over the full working range. '
               'Designers choose the angle to meet the expected incidence at the design speed and to give '
               'acceptable losses away from it. The choice is a trade-off between efficiency and the width '
               'of the working range.'),
              ('Why the diagram matters',
               'A velocity triangle is the first sketch of any turbomachine design. It links the speed of '
               'the rotor to the work and the losses before any detailed shape is drawn. Every later step '
               'builds on the triangle drawn at the start.')],
 'test': [('How many speeds does a velocity triangle show?',
           [('a', 'One'), ('b', 'Ten'), ('c', 'Three'), ('d', 'None')],
           'c'),
          ('From where is absolute velocity measured?',
           [('a', 'From the casing'),
            ('b', 'From the moving blade'),
            ('c', 'From the passengers'),
            ('d', 'From the Sun')],
           'a'),
          ('What does the Euler work equation relate work to?',
           [('a', 'The colour of the blades'),
            ('b', 'The length of the hold'),
            ('c', 'The change in swirl of the flow and the blade speed'),
            ('d', 'The number of pilots')],
           'c'),
          ('What is incidence?',
           [('a', 'The price of a blade'),
            ('b', 'The angle between the incoming flow and the blade leading edge'),
            ('c', 'The speed of the craft'),
            ('d', 'The weight of the fuel')],
           'b'),
          ('What is the trade-off in choosing a blade angle?',
           [('a', 'Paint colour against shaft length'),
            ('b', 'Cabin size against tyre size'),
            ('c', 'There is no trade-off'),
            ('d', 'Efficiency at the design point against the width of the working range')],
           'd')]}
