"""Solar Sail Dynamics and Materials: radiation pressure, sail film materials, deployment mechanisms, attitude control, and area scaling."""
CODE = 'engineering5_solar_sail'
BOOK = {'title': 'Solar Sail Dynamics and Materials',
 'subtitle': 'Light pushing a thin sail, the films that work, and steering with the Sun',
 'chapters': [('Light has a push',
               'Sunlight carries momentum, and when it strikes a surface it pushes on it. This is radiation '
               'pressure. The push is tiny near Earth, only a few micronewtons on each square metre, but it '
               'never stops, so a large thin sail can gain speed over time.'),
              ('Sail film materials',
               'A solar sail is a very thin film, often a polymer such as Kapton or Mylar with a reflective '
               'coating. The film must be light, strong enough to unfold, and able to survive heat and '
               'radiation in space. Thinner films are lighter but harder to handle.'),
              ('Deployment',
               'A sail must be folded to fit the launch vehicle and then unfolded in space. Booms, spars or '
               'spinning can open it. Each deployment step is a point of risk, so designers test the folding '
               'and unfolding many times on the ground.'),
              ('Attitude control',
               'A sail is steered by changing the angle of its surface to the Sunlight. Small tilts shift '
               'the direction of the push, and reflective panels or movable vanes give the control. The sail '
               'can then turn the craft without using any fuel.'),
              ('Area scaling',
               'The push on a sail grows with its area, but the supporting structure gets heavier faster than the area grows, so the push per kilogram falls. '
               'Engineers must find the size that gives the best ratio of push to mass. '
               'Very large sails are only useful if the mass stays low.'),
              ('The money side',
               'A solar sail uses no propellant, so it saves the cost of fuel. Its cost lies in the sail, '
               'its folding and the long time it needs to build speed. Planners compare the saved fuel '
               'against the time, the cost and the risk of the sail.')],
 'test': [('What is radiation pressure?',
           [('a', 'The pressure of a tyre'),
            ('b', 'The weight of the cargo'),
            ('c', 'The push that sunlight gives to a surface it strikes'),
            ('d', 'The heat in a kettle')],
           'c'),
          ('What are solar sail films often made from?',
           [('a', 'Thin polymers such as Kapton or Mylar with a reflective coating'),
            ('b', 'Thick lead blocks'),
            ('c', 'Ice cubes'),
            ('d', 'Wet paper')],
           'a'),
          ('How is a solar sail steered?',
           [('a', 'By pulling a rope on the ground'),
            ('b', 'By blowing on it'),
            ('c', 'By changing the angle of its surface to the Sunlight'),
            ('d', 'By turning off the Sun')],
           'c'),
          ('Why is there a limit to how big a sail should be?',
           [('a', 'Sails cannot be larger than a book'),
            ('b', 'Its supporting structure gets heavier faster than its area grows, so the push per kilogram falls'),
            ('c', 'Big sails melt at once'),
            ('d', 'Light cannot reach them')],
           'b'),
          ('What does a solar sail not need?',
           [('a', 'Attitude control'), ('b', 'Deployment'), ('c', 'A sail film'), ('d', 'Propellant')],
           'd')]}
