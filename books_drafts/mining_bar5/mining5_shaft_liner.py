"""Shaft lining under load: concrete and steel liners, water pressure, joints, inspection and repair."""
CODE = 'mining5_shaft_liner'
BOOK = {
    'title': 'Shaft Lining Under Load',
    'subtitle': 'Keeping a deep shaft wall sound against rock and water pressure',
    "chapters": [
        ('The shaft wall', 'A shaft is lined with concrete or steel to keep loose rock from falling in and to keep water out. The lining must last as long as the shaft is used.'),
        ('Water pressure', 'Groundwater pushes on the liner from outside. In a deep shaft the pressure can be very high.'),
        ('Steel and concrete', 'Steel liners resist bending and pulling forces well. Concrete liners carry compressive loads well.'),
        ('Joints', 'The joints between liner sections must be designed to move a little without leaking. Movement from the rock is expected.'),
        ('Inspection', 'Liners are inspected with cameras and surveys to find cracks and leaks early. Records show how the liner changes over the years.'),
        ('Repair', 'Cracks are sealed, or the liner is reinforced. An early repair costs far less than a major failure.'),
    ],
    "test": [
        ('What does a shaft lining keep out?', [('a', 'Light from the surface'), ('b', 'Fresh air from the fans'), ('c', 'Falling rock and water'), ('d', 'Trucks from the yard')], 'c'),
        ('What pushes against a shaft liner from outside?', [('a', 'Wind from the surface'), ('b', 'Groundwater'), ('c', 'Heat from the sun'), ('d', 'Sound from the mill')], 'b'),
        ('What do concrete liners carry well?', [('a', 'Loads that twist the shaft'), ('b', 'Loads from the sea'), ('c', 'Loads from the market'), ('d', 'Compressive loads')], 'd'),
        ('What are the joints in a liner designed to do?', [('a', 'Move a little without leaking'), ('b', 'Stay rigid and never move'), ('c', 'Carry the cage'), ('d', 'Hold the lights')], 'a'),
        ('Why is an early repair worth it?', [('a', 'It costs less than a major failure'), ('b', 'It makes the shaft deeper'), ('c', 'It changes the ore grade'), ('d', 'It lets the trucks go faster')], 'a'),
    ],
}
