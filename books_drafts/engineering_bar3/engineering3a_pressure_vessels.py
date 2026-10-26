"""Pressure Vessels in General Terms: why round shapes carry pressure well, and how thick the wall must be."""
CODE = 'engineering3a_pressure_vessels'
BOOK = {
    "title": 'Pressure Vessels in General Terms',
    "subtitle": 'Why round shapes carry pressure well, and how thick the wall must be',
    "chapters": [
        ('A vessel holds pressure',
         'A pressure vessel is any closed container that holds a gas or a liquid at a pressure different from its surroundings. Tanks, cylinders and pipes under pressure all count. The wall must carry the force of that pressure across its whole surface.'),
        ('Hoop stress in a cylinder',
         'Pressure inside a cylinder pushes the wall outward, and the wall resists by stretching around its circumference. This is called hoop stress. For a thin wall, it equals the pressure times the radius, divided by the wall thickness.'),
        ('A sphere is stronger',
         'A sphere spreads the same pressure evenly in all directions. For the same radius and stress, a sphere needs only half the wall thickness of a cylinder. That is why many gas storage tanks are built as spheres when space allows.'),
        ('Ends and openings',
         'The ends of a cylinder carry load along its length, and they are often curved or dished so that they share it better. Openings for pipes and valves cut through the wall and weaken it. They are reinforced with extra metal around their edges.'),
        ('Test before use',
         'A new vessel is tested at a pressure above its working pressure, usually with water rather than gas. Water stores far less energy than compressed gas if the vessel fails. Each test is recorded with a date and a result, and a vessel that fails is scrapped or repaired.'),
        ('Relief and safety',
         'Every vessel needs a relief valve set below its design pressure, so it cannot build beyond its limit. Check the valve regularly, because a stuck valve offers no protection. Keep the vessel away from heat and sunlight that would raise its pressure.'),
    ],
    "test": [
        ('What is a pressure vessel?',
         [('a', 'A type of paint'), ('b', 'A closed container holding fluid at a pressure different from its surroundings'), ('c', 'A bolt with a thread'), ('d', 'A glass window with no frame')], 'b'),
        ('If the wall thickness of a thin cylinder is doubled, and the pressure and radius stay the same, what happens to the hoop stress?',
         [('a', 'It doubles'), ('b', 'It stays the same'), ('c', 'It becomes zero'), ('d', 'It halves')], 'd'),
        ("For the same radius and stress, how does a sphere's wall compare with a cylinder's?",
         [('a', 'It needs half the thickness'), ('b', 'It needs twice the thickness'), ('c', 'It needs the same thickness'), ('d', 'It needs no wall at all')], 'a'),
        ('Why is a pressure vessel often tested with water rather than gas?',
         [('a', 'Water makes the vessel bigger'), ('b', 'Gas cannot be tested at all'), ('c', 'Water stores far less energy than compressed gas if the vessel fails'), ('d', 'Water removes the need for a wall')], 'c'),
        ('What is the job of a relief valve on a vessel?',
         [('a', 'To fill the vessel with more pressure'), ('b', 'To stop the vessel building up beyond its limit'), ('c', 'To decorate the vessel'), ('d', 'To hold the vessel down on the floor')], 'b'),
    ],
}
