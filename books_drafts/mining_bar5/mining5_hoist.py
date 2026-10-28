"""Mine hoists: drum and friction types, rope design, speed profiles, safety, maintenance and capacity."""
CODE = 'mining5_hoist'
BOOK = {
    'title': 'Hoists, Cages and Winders',
    'subtitle': 'How people, rock and equipment travel up and down a mine shaft',
    "chapters": [
        ('Lifting in a mine', 'A hoist lifts people, rock and equipment up and down a shaft. The cage or skip rides on steel rope driven by a winder.'),
        ('Drum and friction hoists', 'A drum hoist winds rope onto a drum. A friction hoist grips the rope by friction over a driving sheave. Both types are used in mines.'),
        ('Rope design', 'Hoist rope is made of steel wires and must be designed for the load, for bending and for wear. It is inspected often.'),
        ('Speed profiles', 'A hoist speeds up and slows down along a set profile. Gentle changes protect the rope and the load.'),
        ('Safety and maintenance', 'Hoists have brakes, overwind controls and regular checks. Safety rules set how they are maintained and tested.'),
        ('Capacity', "A hoist's capacity depends on the load, the speed and the depth of the shaft. Engineers size it for the whole job, not just one lift."),
    ],
    "test": [
        ('What does a hoist move?', [('a', 'People, rock and equipment up and down a shaft'), ('b', 'Water through a pipe'), ('c', 'Air through a fan'), ('d', 'Electricity along a cable only')], 'a'),
        ('How does a friction hoist grip its rope?', [('a', 'With a hook at the top of the shaft'), ('b', 'By friction over a driving sheave'), ('c', 'With glue poured on the rope'), ('d', 'With a magnet on the cage')], 'b'),
        ('What must hoist rope be designed for?', [('a', 'The colour of the cage'), ('b', 'The name of the shaft'), ('c', 'The load, bending and wear'), ('d', 'The price of the shift')], 'c'),
        ('Why does a hoist follow a speed profile?', [('a', 'To make the cage noisier'), ('b', 'To save time on paperwork'), ('c', 'To lift more water'), ('d', 'To protect the rope and the load')], 'd'),
        ('What does hoist capacity depend on?', [('a', 'The number of lights in the shaft'), ('b', 'The load, the speed and the shaft depth'), ('c', 'The colour of the headframe'), ('d', 'The day of the week')], 'b'),
    ],
}
