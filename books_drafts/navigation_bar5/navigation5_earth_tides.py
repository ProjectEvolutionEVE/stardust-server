"""Solid Earth Tides: the rise and fall of the crust, Sun and Moon forcing, amplitude, corrections to station positions, standard models and their effects."""
CODE = 'navigation5_earth_tides'
BOOK = {
    "title": 'Solid Earth Tides',
    "subtitle": 'The ground itself rises and falls, and precise positions must allow for it',
    "chapters": [
        ('The crust moves',
         'The solid Earth rises and falls twice a day, a little like the sea does, but much less. The rock flexes under the pull of the Moon and the Sun.'),
        ('Sun and Moon forcing',
         'The Sun pulls harder on the Earth overall, but the Moon raises the larger tidal force because it is much closer; the tidal effect of the Sun is about half that of the Moon. Their combined pull creates the tidal bulge that moves the ground.'),
        ('Amplitude',
         'The total rise and fall of the ground can reach tens of centimetres. A change of that size matters for precise positions.'),
        ('Corrections to positions',
         'Precise station positions must be corrected for the solid Earth tide. Without the correction, the results would show false motion of the ground.'),
        ('Models',
         'Standard tide models are published, and mission and survey teams apply them. The models are shared as part of agreed conventions.'),
        ('Effects',
         'Ignoring the tides causes errors in heights, in baselines and in the timing of signals. Applying the corrections keeps many results consistent with each other.'),
    ],
    "test": [
        ('How does the solid Earth move each day?',
         [('a', 'It stays perfectly still'), ('b', 'It spins in a circle'), ('c', 'It rises and falls twice a day, a little like the sea'), ('d', 'It shrinks steadily')], 'c'),
        ('What causes the solid Earth tide?',
         [('a', 'The pull of the Moon and the Sun'), ('b', 'Wind blowing on the mountains'), ('c', 'Heat from volcanic fires'), ('d', 'Ice floating on rivers')], 'a'),
        ('What is the amplitude of the solid Earth tide?',
         [('a', 'The colour of the crust'), ('b', 'The size of the rise and fall, reaching tens of centimetres'), ('c', 'The number of rocks in a field'), ('d', 'The depth of the sea')], 'b'),
        ('Why are station positions corrected for tides?',
         [('a', 'To change the orbit of the Moon'), ('b', 'To hide the rock from view'), ('c', 'To lower the sea level'), ('d', 'Without it, results show false motion')], 'd'),
        ('What helps teams apply the correction consistently?',
         [('a', 'Guessing at each station'), ('b', 'Published standard tide models'), ('c', 'Painting the maps'), ('d', 'Ignoring the Moon')], 'b'),
    ],
}
