"""Turbulence Avoidance Routing: Choosing a smoother way through the sky."""
CODE = 'navigation5_turbulence_routing'
BOOK = {
    'title': 'Turbulence Avoidance Routing',
    'subtitle': 'Choosing a smoother way through the sky',
    'chapters': [
        ('Bumpy air', 'Turbulence is rough, unsteady air that shakes an aircraft. Most turbulence is brief, but strong bumps can injure people who are not belted in.'),
        ('Forecast turbulence', 'Forecasts give the chance and strength of turbulence at different heights. They are updated regularly as the weather changes.'),
        ('Turbulence indices', "Indices give a number for how rough the air is expected to be. A common measure is the eddy dissipation rate, which describes the energy of the air's motion."),
        ('Choosing altitude', 'Flying higher or lower can avoid the worst air. A different height may cost a little fuel but save a lot of discomfort.'),
        ('Cost', 'Each change of route or height has a cost in time and fuel. Planners weigh that cost against the comfort and safety gained.'),
        ('Decisions', 'Crews and dispatchers decide together. Passenger safety, seat-belt signs and clear communication guide the final choice.'),
    ],
    'test': [
        ('What is turbulence?', [('a', 'A type of cake'), ('b', 'Calm water'), ('c', 'A radio station'), ('d', 'Rough, unsteady air that shakes an aircraft')], 'd'),
        ('What do turbulence indices give?', [('a', 'A number for how rough the air is expected to be'), ('b', 'The price of fuel'), ('c', 'The name of the captain'), ('d', 'The colour of clouds')], 'a'),
        ('What does the eddy dissipation rate describe?', [('a', 'The weight of the crew'), ('b', 'The size of the seats'), ('c', "The energy of the air's motion"), ('d', 'The taste of coffee')], 'c'),
        ('What can changing altitude do?', [('a', 'Make the air hotter'), ('b', 'Avoid the worst air'), ('c', 'Stop the engines'), ('d', 'Remove clouds')], 'b'),
        ('What guides the final choice of route?', [('a', 'Random chance'), ('b', 'Only the menu'), ('c', 'Passenger safety and clear communication'), ('d', 'Nothing')], 'c'),
    ],
}
