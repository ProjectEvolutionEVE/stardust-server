"""Pneumatics: compressed air as a working fluid, and why air feels springy where oil feels firm."""
CODE = 'engineering3c_pneumatics'
BOOK = {
    "title": 'Pneumatics: Air Under Pressure',
    "subtitle": 'Compressed air for tools, grippers and valves, and why it feels springy',
    "chapters": [
        ('Air as a working fluid',
         "Compressed air can push machines much as oil does, but it is far more springy. Air squeezes when you push on it, so a pneumatic cylinder gives a little under load and cannot hold a position as firmly as a hydraulic one. That springiness is useful for gentle grip and safe pushing."),
        ('Making the air',
         "A compressor draws in ordinary air and squeezes it into a tank. Squeezing air heats it, so the air is cooled and its moisture removed before use. Water left in the lines causes rust and wears valves."),
        ('Cylinders and valves',
         "A pneumatic cylinder is pushed by air acting on a piston, and a valve directs the air to each side in turn. Force equals pressure times piston area, so a bigger piston gives more force at the same pressure. Speed depends on how quickly air can flow in and out."),
        ('Leaks cost money',
         "Compressed air leaks quietly, from hose joints, fittings and worn seals. A small hiss can waste a large share of what the compressor makes. Since so much energy goes into making the air, finding and fixing leaks is one of the cheapest ways to save power."),
        ('Stored air is stored energy',
         "A tank of compressed air holds a lot of energy, and a burst line can whip about and injure someone. Relief valves, pressure gauges and regular checks keep it safe. Never point an air jet at a person."),
        ('Pneumatics or hydraulics',
         "Use air where speed, cleanliness and gentle force matter. Use oil where you need firm, strong holding. Air is cheap and clean to vent, but it is less stiff. Choose from the job, and write the reason down."),
    ],
    "test": [
        ('Why does a pneumatic cylinder feel springy?',
         [('a', 'Air compresses, so the cylinder gives a little under load'), ('b', 'The piston is made of rubber'), ('c', 'The air is hot'), ('d', 'The valve is loose')], 'a'),
        ('How is the force of a pneumatic cylinder worked out?',
         [('a', 'Pressure divided by piston area'), ('b', 'Piston area plus pressure'), ('c', 'Air temperature times the length of the stroke'), ('d', 'Pressure times piston area')], 'd'),
        ('Why is water removed from compressed air?',
         [('a', 'Water makes the air lighter'), ('b', 'It helps the air expand'), ('c', 'Water in the lines causes rust and wears valves'), ('d', 'Water makes the tank colder')], 'c'),
        ('What does a leak in compressed-air lines usually cost?',
         [('a', 'Nothing, since the air is free'), ('b', 'Power, because the compressor works harder to replace the lost air'), ('c', 'Only paint'), ('d', 'A faster cylinder')], 'b'),
        ('Which is the better choice for firm, strong holding of a heavy load?',
         [('a', 'Air, because it is cheap'), ('b', 'Air, because it is springy'), ('c', 'Air, because it vents easily'), ('d', 'Hydraulic oil, which is stiffer')], 'd'),
    ],
}
