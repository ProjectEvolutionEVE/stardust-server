"""Oblique Shocks and Prandtl-Meyer Expansion: shock angles, flow deflection, expansion fans, wave drag, and shaping for supersonic flight."""
CODE = 'engineering5_oblique_shock'
BOOK = {'title': 'Oblique Shocks and Prandtl-Meyer Expansion',
 'subtitle': 'Shock angles, expansion fans, and shaping a craft for supersonic flight',
 'chapters': [('A wave at an angle',
               'When supersonic air meets a sharp corner, the shock forms at an angle to the flow rather '
               'than straight across it. The angle depends on the flow speed and the turn the corner makes. '
               'A shock at a shallow angle is weaker than a normal shock at the same speed.'),
              ('Turning the flow',
               'An oblique shock turns the flow toward the wall that made it. The turn, called the '
               'deflection angle, sets how strong the shock is. A small turn gives a weak shock, and a '
               'larger turn can give a strong one that is only just attached to the corner.'),
              ('Expansion at a convex corner',
               'When supersonic air flows around a convex corner, it does not shock. It expands through a '
               'fan of Mach waves, and this is the Prandtl-Meyer expansion. The pressure falls as the flow '
               'turns away, and the flow speeds up across the fan.'),
              ('Wave drag',
               'Shock waves carry energy away from the craft, and that loss appears as wave drag. Wave drag '
               'is one of the main reasons supersonic craft need a different shape from subsonic ones. Sharp '
               'leading edges and thin wings keep the shocks weak.'),
              ('Shaping for supersonic flight',
               'Designers use a pointed nose, slim wings and carefully placed corners to control where the '
               'shocks go. Every corner is a choice: a sharp corner makes a shock, and a smooth expansion '
               'makes a fan. The aim is the least drag for the job.'),
              ('Checking the design',
               'Engineers check their shapes with theory, with wind tunnel tests and with computer '
               'simulation. Each check shows the shock angles, the pressures and the drag at each speed. A '
               'shape that works at one speed can fail at another, so the whole flight envelope must be '
               'tested.')],
 'test': [('What is the angle of an oblique shock compared with a normal shock?',
           [('a', 'It lies across the flow'),
            ('b', 'It is always vertical'),
            ('c', 'It does not exist'),
            ('d', 'It lies at an angle to the flow')],
           'd'),
          ('What is the deflection angle?',
           [('a', 'The angle the wing makes with the ground'),
            ('b', 'The angle of the landing gear'),
            ('c', 'The turn the flow makes toward the wall'),
            ('d', 'The tilt of the Sun')],
           'c'),
          ('What happens when supersonic air flows around a convex corner?',
           [('a', 'It expands through a fan of Mach waves'),
            ('b', 'It forms a normal shock'),
            ('c', 'It stops completely'),
            ('d', 'It turns into liquid')],
           'a'),
          ('What does wave drag come from?',
           [('a', 'The colour of the paint'),
            ('b', 'Heavy cargo in the hold'),
            ('c', 'Energy carried away by shock waves'),
            ('d', 'Cold fuel in the tanks')],
           'c'),
          ('How do designers keep shocks weak on a supersonic craft?',
           [('a', 'Use blunt, thick leading edges'),
            ('b', 'Use sharp leading edges and thin wings'),
            ('c', 'Make the craft as heavy as possible'),
            ('d', 'Fly only at low speed')],
           'b')]}
