"""Instrument Procedure Design: Drawing the safe paths that guide aircraft down to land."""
CODE = 'navigation5_instrument_procedure_design'
BOOK = {
    'title': 'Instrument Procedure Design',
    'subtitle': 'Drawing the safe paths that guide aircraft down to land',
    'chapters': [
        ('Procedures on paper', 'An instrument procedure is a published path for aircraft flying without visual reference. Designers build these paths to keep aircraft safe near airports.'),
        ('Obstacle clearance', 'Every segment must clear terrain and obstacles by a set margin. Designers measure the ground and buildings and allow for error.'),
        ('Protected areas', 'Each segment has a protected area around its path. Designers make sure that no hazards lie within it.'),
        ('Segments', 'A typical approach has initial, intermediate, final and missed approach segments. Each one has its own rules for height, speed and turns.'),
        ('Minimums', 'The lowest height at which a pilot may descend is the minimum. It depends on the obstacles and the equipment available.'),
        ('Checks', 'Procedures are checked by flight tests and reviews before publication. Checks confirm that the design meets the criteria and that the aircraft can fly it.'),
    ],
    'test': [
        ('What is an instrument procedure?', [('a', 'A cooking recipe'), ('b', 'A type of paint'), ('c', 'A published path for aircraft flying without visual reference'), ('d', 'A sea chart symbol')], 'c'),
        ('What must each segment do?', [('a', 'Clear obstacles by a set margin'), ('b', 'Pass through buildings'), ('c', 'Cross mountains without checks'), ('d', 'Hide from radar')], 'a'),
        ('Which is NOT a typical approach segment?', [('a', 'Ocean'), ('b', 'Final'), ('c', 'Intermediate'), ('d', 'Missed approach')], 'a'),
        ('What is the minimum?', [('a', 'The shortest name'), ('b', 'The smallest wing'), ('c', 'The lowest price for tickets'), ('d', 'The lowest height at which a pilot may descend')], 'd'),
        ('What do checks confirm?', [('a', 'The menu is tasty'), ('b', 'The design meets the criteria and the aircraft can fly it'), ('c', 'The paint is dry'), ('d', 'The clock is right')], 'b'),
    ],
}
