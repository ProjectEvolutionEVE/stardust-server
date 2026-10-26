"""Air Drag on Satellites: how thin air slowly pulls a craft down, and why solar activity matters."""
CODE = 'flight5_a_atmosphere_drag'
BOOK = {
    "title": 'Air Drag on Satellites',
    "subtitle": 'How thin air slowly pulls a craft down',
    "chapters": [
        ('Thin, but not empty',
         'The air at the height of a low satellite is very thin, but it is not nothing. Each time the craft passes through, the air pushes back against it. Over days and weeks, that small push adds up to a real loss of height.'),
        ('Density matters',
         "Drag depends strongly on the air density at the craft's height. Density falls steeply as height rises. A small change in height can therefore make a big difference to how fast the craft loses speed."),
        ('The ballistic coefficient',
         "A craft's mass compared with its area and its shape is called its ballistic coefficient. A dense, compact craft falls through the air more easily than a light, wide one. Designers consider this number when they plan a satellite's life."),
        ('Solar activity',
         'The Sun heats the upper air, and the air swells when solar activity is high. This makes the air denser at satellite heights and increases drag. A satellite can therefore fall faster during a period of high solar activity.'),
        ('Estimating lifetime',
         'Engineers estimate how long a satellite will last by combining the density model, the ballistic coefficient and the expected solar activity. The estimate is never exact, but it helps plan orbit changes and fuel.'),
        ('Examples',
         'Some satellites in very low orbits have lifetimes of only a few years without boosts. Higher satellites can stay for decades. The height at which a craft flies sets much of its life.'),
    ],
    "test": [
        ('What does air drag do to a low satellite over time?',
         [('a', 'It makes the satellite faster and faster for ever'), ('b', 'It lowers the satellite slowly'), ('c', 'It paints the satellite'), ('d', 'It turns the satellite into a moon')], 'b'),
        ('How does air density change as the height goes up?',
         [('a', 'It rises steeply'), ('b', 'It stays the same at every height'), ('c', 'It falls steeply'), ('d', 'It is zero at every height')], 'c'),
        ("What does a satellite's ballistic coefficient compare?",
         [('a', 'Its colour with its speed'), ('b', 'Its crew with its fuel'), ('c', 'Its radio with its power'), ('d', 'Its mass with its area and shape')], 'd'),
        ('What happens to the upper air when solar activity is high?',
         [('a', 'It swells and becomes denser at satellite heights'), ('b', 'It disappears'), ('c', 'It freezes solid'), ('d', 'It moves to the Moon')], 'a'),
        ('Why do higher satellites usually last longer?',
         [('a', 'Because the air there is much thinner'), ('b', 'Because they are closer to the Sun'), ('c', 'Because they carry more batteries'), ('d', 'Because they have no mass')], 'a'),
    ],
}
