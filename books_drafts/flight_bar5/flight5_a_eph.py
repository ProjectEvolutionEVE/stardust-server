"""Planetary Ephemerides: the tables that give where planets are, and how mission planners use them."""
CODE = 'flight5_a_eph'
BOOK = {
    "title": 'Planetary Ephemerides',
    "subtitle": 'Tables of where the planets are, and how they are made',
    "chapters": [
        ('What an ephemeris is',
         'An ephemeris is a table or model that gives the position and speed of a body at each time. Planners use ephemerides to know where the Sun, planets and moons are when they plan a mission.'),
        ("JPL's models",
         'The Jet Propulsion Laboratory produces a family of planetary ephemerides, known as the DE series. These are built from many observations and fitted with a detailed model of the solar system. They are updated as new data comes in.'),
        ('Accuracy',
         'Modern ephemerides are very accurate for the inner planets and for the Moon. The outer planets are less well known, and the uncertainties are larger. Mission planners keep track of these limits.'),
        ('Voyager',
         'The missions to the outer planets relied on ephemerides to plan their flybys. Accurate positions for the planets and moons were needed to aim the craft and time the encounters. This is one of the many uses of the tables.'),
        ('Time scales',
         'Ephemerides use precise time scales, which keep track of time more carefully than everyday clocks. Mixing up time scales can shift a predicted position. Good software keeps the time scales straight.'),
        ('Using them well',
         'Planners check their path against more than one ephemeris, and they update their plans when a newer table is released. Using the best data available keeps the mission on target.'),
    ],
    "test": [
        ('What is an ephemeris?',
         [('a', 'A table or model that gives the position and speed of a body at each time'), ('b', 'A type of rocket'), ('c', "A pilot's uniform"), ('d', 'A recipe for soup')], 'a'),
        ('What is the DE series?',
         [('a', 'A list of crew names'), ('b', 'A family of planetary ephemerides from the Jet Propulsion Laboratory'), ('c', 'A line of food packs'), ('d', 'A set of paint colours')], 'b'),
        ('Which bodies are the most accurately known in these tables?',
         [('a', 'The outer planets'), ('b', 'Comets only'), ('c', 'The inner planets and the Moon'), ('d', 'Dust clouds only')], 'c'),
        ('Why do mixed-up time scales matter?',
         [('a', 'They change the colour of the planets'), ('b', 'They make rockets lighter'), ('c', 'They turn off the radio'), ('d', 'They can shift a predicted position')], 'd'),
        ('How do good planners use ephemerides?',
         [('a', 'They check against more than one table and update when newer data arrives'), ('b', 'They never check them'), ('c', 'They throw them away after launch'), ('d', 'They use them only for cooking')], 'a'),
    ],
}
