"""Wind Field Modelling for Aircraft: Mapping the winds an aircraft will fly through."""
CODE = 'navigation5_wind_fields'
BOOK = {
    'title': 'Wind Field Modelling for Aircraft',
    'subtitle': 'Mapping the winds an aircraft will fly through',
    'chapters': [
        ('Winds aloft', 'Winds at flight height can be strong and can change quickly. Forecast models give a picture of these winds across the sky.'),
        ('Jet streams', 'Jet streams are fast, narrow currents of wind high in the atmosphere. Aircraft flying with them can save fuel and time.'),
        ('Uncertainty', 'Forecast winds are not exact. Models show a range of likely winds, so planners check how much a route could change.'),
        ('Routing', 'Route planners use the wind fields to choose heights and paths. A small change of route or height can make a large difference to fuel.'),
        ('Errors', 'Models can miss small features, such as local turbulence or the exact position of a jet. Pilots compare forecasts with reports from other aircraft.'),
        ('Data', 'Wind data come from weather balloons, satellites and aircraft reports. Combining these sources makes the wind fields more reliable.'),
    ],
    'test': [
        ('What are jet streams?', [('a', 'Water pipes'), ('b', 'Shops'), ('c', 'Fast, narrow currents of wind high in the atmosphere'), ('d', 'Engine parts')], 'c'),
        ('Why do planners check a range of forecast winds?', [('a', 'Because forecast winds are not exact'), ('b', 'Because the wind is always zero'), ('c', 'Because maps are colourful'), ('d', 'Because aircraft cannot fly')], 'a'),
        ('How can flying with a jet stream help?', [('a', 'It always stops the aircraft'), ('b', 'It makes the aircraft heavier'), ('c', 'It removes the pilot'), ('d', 'It can save fuel and time')], 'd'),
        ('What can models miss?', [('a', 'The date'), ('b', 'The name of the airline'), ('c', 'The colour of the cabin'), ('d', 'Small features such as local turbulence')], 'd'),
        ('Which is a source of wind data?', [('a', 'Weather balloons, satellites and aircraft reports'), ('b', 'Ice cream vans'), ('c', 'Garden hoses'), ('d', 'Sandwich shops')], 'a'),
    ],
}
