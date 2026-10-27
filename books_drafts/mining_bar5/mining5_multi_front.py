"""Sequencing multiple stope fronts: spacing, stress shadows, ventilation, access, schedules and optimisation."""
CODE = 'mining5_multi_front'
BOOK = {
    'title': 'Sequencing Multiple Stope Fronts',
    'subtitle': "Running several faces at once without them getting in each other's way",
    "chapters": [
        ('Many faces at once', 'A mine often works several stope fronts at the same time, each with its own crew and equipment. The plan has to keep them all moving safely.'),
        ('Spacing', 'Fronts must be spaced so that work in one does not disturb another. The spacing depends on the rock and the depth.'),
        ('Stress shadows', 'Mining one area leaves a zone of reduced stress nearby, and load builds up in the neighbouring ground. Planners account for both effects.'),
        ('Ventilation and access', 'Fronts share air and tunnels. Planning keeps fresh air reaching each front and keeps the routes clear.'),
        ('Schedules', 'Schedules balance output against the spacing and access rules. A schedule that looks good on paper must still be safe to run.'),
        ('Optimisation', 'Planners use computer models to test many sequences and choose the best overall plan. The model is checked against what happens on site.'),
    ],
    "test": [
        ('Why are stope fronts spaced apart?', [('a', 'So the trucks have more room to park'), ('b', 'So work in one does not disturb another'), ('c', 'So the lights use less power'), ('d', 'So the market price stays high')], 'b'),
        ('What is a zone of reduced stress near mined ground?', [('a', 'A hazard register'), ('b', 'A type of shaft lining'), ('c', 'A stress shadow'), ('d', 'A grade model')], 'c'),
        ('What must planners make sure of for ventilation?', [('a', 'That the fronts are painted the same colour'), ('b', 'That there is no air at all'), ('c', 'That the fans stop at lunch'), ('d', 'That fresh air reaches each front')], 'd'),
        ('What do computer models help planners do?', [('a', 'Test many sequences and choose the best plan'), ('b', 'Sell the ore faster'), ('c', 'Replace the shift crew'), ('d', 'Remove the need for safety rules')], 'a'),
        ('What do schedules balance?', [('a', 'Paint against lighting'), ('b', 'Output against the spacing and access rules'), ('c', 'Wages against the weather'), ('d', 'Trucks against the colour of the shift')], 'b'),
    ],
}
