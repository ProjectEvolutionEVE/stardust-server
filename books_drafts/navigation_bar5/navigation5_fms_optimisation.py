"""Flight Management Optimisation: Choosing the best speed and height for each flight."""
CODE = 'navigation5_fms_optimisation'
BOOK = {
    'title': 'Flight Management Optimisation',
    'subtitle': 'Choosing the best speed and height for each flight',
    'chapters': [
        ('The flight management system', 'The flight management system plans the route, height and speed of a flight. It works out fuel use and timing from the start of the flight to the end.'),
        ('The cost index', 'The cost index weighs the cost of time against the cost of fuel. A low cost index favours saving fuel, while a high one favours speed and punctuality.'),
        ('Vertical profiles', "The climb, cruise and descent heights form the vertical profile. A good profile saves fuel and time, depending on the aircraft's weight and the air around it."),
        ('Winds', 'Winds at height can help or slow an aircraft. Flying at a level with a helpful wind can save a significant amount of fuel on a long flight.'),
        ('Finding the optimum', 'The best choice depends on the trade-off between time, fuel and safety limits. The system searches for the combination with the lowest total cost for the chosen cost index.'),
        ('Energy and decisions', 'Careful choices reduce energy use and emissions. Crews may still change the plan when weather, traffic or instructions require it.'),
    ],
    'test': [
        ('What does the cost index compare?', [('a', 'The cost of paint and tyres'), ('b', 'The price of tickets and food'), ('c', 'The cost of time against the cost of fuel'), ('d', "The cost of pilots' coffee")], 'c'),
        ('What does a low cost index favour?', [('a', 'Fuel saving'), ('b', 'Maximum speed at any cost'), ('c', 'No flights'), ('d', 'Painting the aircraft')], 'a'),
        ('What is a vertical profile?', [('a', 'The climb, cruise and descent heights of a flight'), ('b', 'A type of window'), ('c', 'A tyre pattern'), ('d', 'A chart colour')], 'a'),
        ('Why do winds matter?', [('a', 'Winds never affect flight'), ('b', 'Winds only change the paint'), ('c', 'Winds stop engines'), ('d', 'A helpful wind at some height can save fuel')], 'd'),
        ('What is the optimum?', [('a', 'The highest possible fuel burn'), ('b', 'A random speed'), ('c', 'The lowest total cost for the chosen cost index'), ('d', 'A guess')], 'c'),
    ],
}
