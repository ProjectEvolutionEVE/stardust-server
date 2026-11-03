"""Automated Collision Avoidance: How a computer can plan a safe change of course."""
CODE = 'navigation5_collision_avoidance_algo'
BOOK = {
    'title': 'Automated Collision Avoidance',
    'subtitle': 'How a computer can plan a safe change of course',
    'chapters': [
        ('Searching for a safe move', 'An automated system looks at possible changes of speed and course. It picks a move that keeps the ship clear of other ships and of obstacles.'),
        ('Encoding the rules', "Rules such as those for right-of-way are written into the system's logic. The system then checks each candidate manoeuvre against them."),
        ('Constraints', 'Safety limits such as minimum distance, turning ability and water depth are constraints. A good plan respects every constraint at once.'),
        ('Speed changes', 'Changing speed can be as effective as changing course. A system may consider both kinds of move.'),
        ('Testing', 'Designers test the system in simulations with many encounters, including unusual ones. Testing shows where the logic fails.'),
        ('Approval', 'Before use at sea, the system must be approved against recognised standards. Approval means showing that it works safely in the conditions it is meant for.'),
    ],
    'test': [
        ('What does an automated system search for?', [('a', 'Lost gloves'), ('b', 'Best biscuits'), ('c', 'Fish species'), ('d', 'Possible changes of speed and course')], 'd'),
        ('What is a constraint?', [('a', 'A safety limit such as minimum distance or water depth'), ('b', 'A type of sail'), ('c', 'A kind of paint'), ('d', 'A cooking pot')], 'a'),
        ('Why are speed changes considered?', [('a', 'They are never useful'), ('b', 'They only matter in harbour'), ('c', 'They can be as effective as course changes'), ('d', 'They are banned')], 'c'),
        ('Why test with many encounters?', [('a', 'To find where the logic fails'), ('b', 'To make the ship heavier'), ('c', 'To paint the bridge'), ('d', 'To cancel the rules')], 'a'),
        ('What does approval require?', [('a', 'Buying a bigger engine'), ('b', 'Showing it works safely in the conditions it is meant for'), ('c', "Changing the ship's name"), ('d', 'Painting the hull')], 'b'),
    ],
}
