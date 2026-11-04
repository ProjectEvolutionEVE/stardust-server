"""Dynamic Heights and Geopotential Numbers: gravity-weighted heights, geopotential numbers, the reference surface, water flow, precise levelling and uses."""
CODE = 'navigation5_dynamic_height'
BOOK = {
    "title": 'Dynamic Heights and Geopotential Numbers',
    "subtitle": 'Heights that follow the way water really flows',
    "chapters": [
        ('Heights that follow gravity',
         'Dynamic heights are heights weighted by the gravity at each point. They match the way that water really flows across a landscape.'),
        ('Geopotential numbers',
         'A geopotential number is the work needed to lift a unit mass from the reference surface up to a point. It is measured in units of energy per unit mass.'),
        ('The reference surface',
         'All heights are measured from a reference surface, often sea level or the geoid. The choice of reference surface sets the zero of the heights.'),
        ('Water flow',
         'Water flows from higher to lower geopotential. Surfaces of equal geopotential are the surfaces on which water would be level, which is why dynamic heights are useful for water.'),
        ('Levelling',
         'Precise levelling measures height differences along a line. Gravity corrections are added to turn those differences into differences in geopotential.'),
        ('Uses',
         'Engineers and scientists use these heights for water supply, flood planning and ocean studies, where the direction of flow matters.'),
    ],
    "test": [
        ('What is a dynamic height?',
         [('a', 'A height weighted by the gravity at each point'), ('b', 'The height of a kite in the wind'), ('c', 'The height of a tree'), ('d', 'The height of a cloud')], 'a'),
        ('What is a geopotential number?',
         [('a', 'A telephone number'), ('b', 'A scale on a map'), ('c', 'The work needed to lift a unit mass from the reference surface to a point'), ('d', 'A calendar date')], 'c'),
        ('What sets the zero of heights?',
         [('a', 'The colour of the sky'), ('b', 'The choice of reference surface'), ('c', 'The weather on the day'), ('d', 'The phase of the Moon')], 'b'),
        ('Why do dynamic heights suit water?',
         [('a', 'Water has no weight'), ('b', 'Water flows toward the highest point in the sky'), ('c', 'Water never moves'), ('d', 'Water flows from higher to lower geopotential')], 'd'),
        ('What is precise levelling?',
         [('a', 'Measuring height differences along a line, with gravity corrections'), ('b', 'Cutting the grass on a field'), ('c', 'Measuring the speed of the wind'), ('d', 'Mixing paint for a map')], 'a'),
    ],
}
