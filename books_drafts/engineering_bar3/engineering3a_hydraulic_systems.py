"""Hydraulic Power: cylinders, flow, seals and pressure limits, the working side of a sealed fluid."""
CODE = 'engineering3a_hydraulic_systems'
BOOK = {
    "title": 'Hydraulic Power: Cylinders and Limits',
    "subtitle": 'How a sealed fluid multiplies force, and what sets its speed and its limit',
    "chapters": [
        ('Force from pressure',
         'A hydraulic cylinder pushes with a force equal to the pressure times the area of its piston. A bigger piston gives a bigger force at the same pressure. This is how a modest pump can lift a heavy load.'),
        ('Trading distance for force',
         'A larger piston gives more force, but it moves less for the same amount of oil. A piston with ten times the area gives ten times the force at the same pressure, and moves one tenth as far. Work in equals work out, less the losses.'),
        ('Speed is set by flow',
         'The speed of a piston equals the flow of oil divided by the area of the piston. A pump that delivers more oil each second moves the piston faster. In short, pressure sets how much force you get, and flow sets how fast it moves.'),
        ('Seals and leaks',
         'The piston and rod are sealed so that oil cannot escape and air cannot get in. A worn seal leaks, which wastes force and makes the movement jerky. Look for oil on the rod, and check the seals on a schedule.'),
        ('Limits on pressure',
         'Every hydraulic circuit has a relief valve set to the highest pressure its hoses, seals and cylinder are rated for. Hoses and fittings carry a maximum working pressure and burst well above it. Never run a circuit above its rated pressure.'),
        ('Keeping the oil clean',
         'Dirt in the oil scores valves and cylinder walls, and it wears seals quickly. Filters, clean fittings and fresh oil at the right intervals prevent most hydraulic failures. Water in the oil can also cause rust inside the system.'),
    ],
    "test": [
        ('What is the force of a hydraulic cylinder equal to?',
         [('a', 'The pressure divided by the piston area'), ('b', 'The piston area plus the pressure'), ('c', 'The weight of the oil'), ('d', 'The pressure times the piston area')], 'd'),
        ('A piston has ten times the area of another, at the same pressure and with the same oil flow. How do its force and travel compare?',
         [('a', 'One tenth the force, and ten times the travel'), ('b', 'The same force, and the same travel'), ('c', 'Ten times the force, and one tenth the travel'), ('d', 'Ten times the force, and ten times the travel')], 'c'),
        ('What sets the speed of a hydraulic piston?',
         [('a', 'The oil flow divided by the piston area'), ('b', 'The colour of the oil'), ('c', 'The temperature of the room'), ('d', 'The number of seals')], 'a'),
        ('What is a relief valve for?',
         [('a', 'To make the oil warmer'), ('b', 'To stop the pressure rising above its rated limit'), ('c', 'To add more oil to the system'), ('d', 'To paint the cylinder')], 'b'),
        ('What does dirt in hydraulic oil do?',
         [('a', 'Makes the oil thicker and better'), ('b', 'Lowers the piston area'), ('c', 'Scores valves and wears seals'), ('d', 'Stops the pump from making any noise')], 'c'),
    ],
}
