"""Robot Arms: joints, degrees of freedom, reach and the difference between repeating a move and hitting a target."""
CODE = 'engineering3c_robot_arms'
BOOK = {
    "title": 'Robot Arms: Joints and Degrees of Freedom',
    "subtitle": 'How many ways an arm can move, and why reaching a spot takes care',
    "chapters": [
        ('Links and joints',
         "A robot arm is a chain of links joined by joints. Each joint is either turning, which is called revolute, or sliding, which is called prismatic. The joints set how the arm can move, and the link lengths set how far it reaches."),
        ('Degrees of freedom',
         "A free object in space has six degrees of freedom: three ways to move in a straight line and three ways to turn. Each joint adds one degree of freedom to the arm's movement. An arm with six well-placed joints can, in general, put its tip at a chosen point and turn it to a chosen angle within reach."),
        ('Reach and workspace',
         "The workspace is the set of points the tip can reach. The link lengths and joint limits shape it, so a short arm may not reach a far shelf at all. Check the workspace against the real job before you buy."),
        ('Accuracy and repeatability',
         "Repeatability is how closely the arm returns to the same point each time. Accuracy is how close that point is to where it was meant to be. An arm can repeat very well and still miss its target, so the two must be checked separately."),
        ('Actuators and loads',
         "Each joint is driven by a motor, a hydraulic cylinder or a pneumatic piston. The heavier the load and the longer the reach, the more torque each joint must produce. Long arms bend and wobble under load, and that lowers accuracy."),
        ('Program and check',
         "A robot is taught a path, or a computer gives it one. Run a new path slowly first, and watch for joints that reach their limits or links that come close to the structure around them. Save the tested path in the records."),
    ],
    "test": [
        ('What are the two basic kinds of robot joint?',
         [('a', 'Round and square'), ('b', 'Turning (revolute) and sliding (prismatic)'), ('c', 'Hot and cold'), ('d', 'Strong and weak')], 'b'),
        ('How many degrees of freedom does a free object in space have?',
         [('a', 'Three'), ('b', 'Four'), ('c', 'Six'), ('d', 'Twelve')], 'c'),
        ('What is the workspace of a robot arm?',
         [('a', 'The set of points its tip can reach'), ('b', 'The floor under it'), ('c', 'The room it is painted'), ('d', 'Its power supply')], 'a'),
        ('What is repeatability?',
         [('a', 'How far the arm can reach'), ('b', 'How heavy the arm is'), ('c', 'How quickly the arm can paint'), ('d', 'How closely the arm returns to the same point each time')], 'd'),
        ('What happens to a long arm carrying a heavy load?',
         [('a', 'It gets more accurate'), ('b', 'It stops working'), ('c', 'It can bend and wobble, which lowers its accuracy'), ('d', 'It loses its joints')], 'c'),
    ],
}
