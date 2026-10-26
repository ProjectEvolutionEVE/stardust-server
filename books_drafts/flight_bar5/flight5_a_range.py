"""Range Safety: how a launch is kept away from people, and when a rocket must be destroyed in flight."""
CODE = 'flight5_a_range'
BOOK = {
    "title": 'Range Safety',
    "subtitle": 'Keeping launches away from people',
    "chapters": [
        ('Hazard areas',
         'A launch range sets hazard areas along the path of a rocket. These are the zones where falling parts or a failed rocket could cause harm. Rockets are planned to stay inside the safe corridor the range allows.'),
        ('Flight termination',
         'If a rocket goes off course and threatens people, the range safety officer can end its flight. This is called flight termination. The rocket is destroyed in a controlled way, which keeps the debris inside the hazard area.'),
        ('A real example',
         'In 1996 the Ariane 5 rocket lost its way after an early software fault. Its range safety system destroyed it in the air. The event showed both the value and the cost of flight termination.'),
        ('Rules and planning',
         'Range safety rules limit the chance of harm from a launch. Operators must show that their rocket meets the risk limits before each flight. Planning covers the path, the timing and the fallback options.'),
        ('Debris',
         "Debris from a failure can fall over a wide area. The hazard areas are chosen to keep the chance of harm to people very low. Modern systems also track the rocket's position with great care."),
        ('Modern systems',
         "Today's launch ranges use better tracking and automated safety systems. These can react more quickly than a person could. Even so, the core rule is simple: keep people safe first."),
    ],
    "test": [
        ('What is a hazard area?',
         [('a', 'A shop for crew food'), ('b', 'A zone where falling parts or a failed rocket could cause harm'), ('c', 'A hall for training'), ('d', 'A park with benches')], 'b'),
        ('What is flight termination?',
         [('a', 'Landing a rocket on a runway'), ('b', 'Cutting the fuel for a rest'), ('c', 'Ending the flight of a rocket in a controlled way when it threatens people'), ('d', 'Changing the colour of the nose cone')], 'c'),
        ('What happened to the Ariane 5 rocket in 1996?',
         [('a', 'It landed on the Moon'), ('b', 'It sailed to Mars'), ('c', 'It was painted red'), ('d', 'It was destroyed in the air by its range safety system')], 'd'),
        ('Who decides whether a rocket in trouble should be terminated?',
         [('a', 'The range safety officer'), ('b', "The rocket's paint crew"), ('c', 'A passing aircraft pilot'), ('d', 'The local weather report')], 'a'),
        ('What is the aim of range safety rules?',
         [('a', 'To keep the chance of harm to people very low'), ('b', 'To make launches longer'), ('c', 'To stop all rockets for ever'), ('d', 'To give rockets more fuel')], 'a'),
    ],
}
