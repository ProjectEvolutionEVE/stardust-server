"""Eclipses and Orbits: how shadows fall on a craft, and what that means for power and heat."""
CODE = 'flight5_a_eclipse'
BOOK = {
    "title": 'Eclipses and Orbits',
    "subtitle": 'Shadows, power and heat for craft in orbit',
    "chapters": [
        ('The shadow of the Earth',
         'The Earth casts a long shadow into space, on the side away from the Sun. A craft that passes through this shadow loses sunlight, and its solar panels stop making power. Most low orbits pass through the shadow once on each circuit.'),
        ('Shadow geometry',
         'The length and width of the shadow depend on the height of the orbit and the angle of the Sun. A craft high above the Earth can spend a long time in shadow. Low orbits spend less time in shadow, and some orbits never enter it at all.'),
        ('Eclipse seasons',
         'As the Earth goes round the Sun, the angle of the orbit to the Sun changes through the year. There are times when every orbit passes through shadow, and times when none does. Planners check these seasons when they choose how big the batteries must be.'),
        ('Power and heat',
         'In sunlight, panels make power and the craft warms. In shadow, the batteries carry the load and the craft cools. Temperature swings of this kind are one of the main tests for any part that flies in orbit.'),
        ('The Moon can cast a shadow too',
         'The Moon also casts a shadow, and a lunar eclipse of the Sun can be seen from places on the Earth. A craft near the Moon can pass in and out of that shadow, too. These events are predictable, so they can be planned around.'),
        ('Planning for the dark',
         'Good mission planning counts the time in shadow, the battery size, and the temperature changes. A small change in the orbit can move a craft into or out of shadow. Designers choose orbits with the dark time in mind.'),
    ],
    "test": [
        ('What happens to a craft that passes through the shadow of the Earth?',
         [('a', 'It turns into a comet'), ('b', 'It gains extra fuel'), ('c', 'It loses sunlight and its solar panels stop making power'), ('d', 'It stops moving forward')], 'c'),
        ('What sets the length and width of an orbit shadow?',
         [('a', 'The colour of the craft'), ('b', 'The number of crew aboard'), ('c', 'The speed of the radio'), ('d', 'The height of the orbit and the angle of the Sun')], 'd'),
        ('What do planners check when they choose how big the batteries must be?',
         [('a', 'The length of the eclipse seasons'), ('b', 'The price of paint'), ('c', 'The size of the crew bunks'), ('d', 'The weather on the Moon')], 'a'),
        ('What happens to a craft when it is in shadow?',
         [('a', 'It runs on batteries and cools down'), ('b', 'It makes the most power of the orbit'), ('c', 'It heats up at once'), ('d', 'It stops all its systems')], 'a'),
        ('Why do designers choose orbits with the dark time in mind?',
         [('a', 'Dark time helps the radio work better'), ('b', 'Dark time changes the battery and temperature needs'), ('c', 'Dark time is the only time the craft can rest'), ('d', 'Dark time makes the craft lighter')], 'b'),
    ],
}
