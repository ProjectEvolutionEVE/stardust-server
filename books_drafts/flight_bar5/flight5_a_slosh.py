"""Sloshing and Control: how liquids inside a tank move and push back on the craft that carries them."""
CODE = 'flight5_a_slosh'
BOOK = {
    "title": 'Sloshing and Control',
    "subtitle": 'How liquids inside a tank move and push back',
    "chapters": [
        ('Liquids move',
         'A tank of liquid fuel does not stay still when a craft turns or accelerates. The liquid sloshes from side to side, and its motion pushes back on the tank and the craft. This is called sloshing.'),
        ('Modelled as pendulums',
         'Engineers often model the slosh as a set of pendulums or springs attached to the tank. Each one has a natural rate of swinging. The model predicts how the liquid will push on the craft during a burn or a turn.'),
        ('Baffles',
         'Baffles are plates or ribs inside a tank that damp the slosh. They break up the movement of the liquid so that it settles faster and pushes less hard on the walls. Designers add baffles where the slosh could cause trouble.'),
        ('Control interactions',
         'The sloshing liquid can feed back into the control system. If the controller reacts to the slosh, it can make the craft shake more. Careful design and filtering keep the controller from chasing the wobble.'),
        ('Examples',
         'Many rockets and satellites carry large amounts of liquid, so sloshing is a common concern. Engineers test the slosh models on the ground and check them against flight data. A good model is one that predicts the real motion well.'),
        ('Why it matters',
         "A small slosh can grow into a large problem when it lines up with the craft's own motion. Planners model it early and test the controller against it. Tanks, baffles and controllers must work together."),
    ],
    "test": [
        ('What is sloshing?',
         [('a', 'Liquid moving inside a tank when a craft turns or accelerates'), ('b', 'A type of soup'), ('c', 'A paint for the hull'), ('d', 'A radio mode')], 'a'),
        ('How is slosh often modelled?',
         [('a', 'As pendulums or springs attached to the tank'), ('b', 'As a bird in flight'), ('c', 'As a book on a shelf'), ('d', 'As a painted line')], 'a'),
        ('What do baffles do?',
         [('a', 'They make the liquid colder'), ('b', 'They damp the slosh so the liquid settles faster'), ('c', 'They let the liquid escape'), ('d', 'They make the tank bigger')], 'b'),
        ('How can slosh affect the control system?',
         [('a', 'It turns the controller into a lamp'), ('b', 'It stops the radio'), ('c', 'It can feed back into the controller and make the craft shake more'), ('d', 'It makes the crew sleepy')], 'c'),
        ('Why do engineers test slosh models against flight data?',
         [('a', 'To change the colour of the tank'), ('b', 'To make the rocket heavier'), ('c', 'To remove the fuel'), ('d', 'To check that the model predicts the real motion well')], 'd'),
    ],
}
