"""Orbiting a Comet: very low gravity, outgassing, orbit design, the landing attempt, navigation errors and the data returned."""
CODE = 'navigation5_rosetta_orbit'
BOOK = {
    "title": 'Orbiting a Comet',
    "subtitle": 'Flying around a comet that gives off jets of gas as it nears the Sun',
    "chapters": [
        ('Very low gravity',
         'A comet has extremely weak gravity, so a spacecraft moving slowly can drift away from it. Orbits must be designed around the small pull of the comet shape and its spin.'),
        ('Outgassing',
         'As a comet nears the Sun, its ice turns to gas, and jets of gas and dust escape from the surface. These jets push on a nearby spacecraft and change its orbit.'),
        ('Orbit design',
         'Engineers plan orbits that stay safe despite the jets, the shape and the spin. The Rosetta mission used a sequence of orbits at different distances to map the comet closely.'),
        ('The landing attempt',
         'The lander Philae separated from Rosetta in 2014 and touched down on the comet. Its harpoons did not fire properly, so it bounced twice before settling in a shadowed place.'),
        ('Navigation errors',
         'Small errors in the models of the comet shape or gravity grow over time. Navigators correct them using regular images and tracking data.'),
        ('The data returned',
         'Rosetta returned images, gas measurements and surface data over more than two years. This gave a close view of a comet as its activity grew near the Sun.'),
    ],
    "test": [
        ('What is special about a comet gravity?',
         [('a', 'It is very strong'), ('b', 'It is extremely weak'), ('c', 'It is the same as the gravity of the Earth'), ('d', 'It always pushes spacecraft away')], 'b'),
        ('What is outgassing?',
         [('a', 'Gas and dust jets escape as ice turns to gas near the Sun'), ('b', 'Astronauts breathing out'), ('c', 'Painting a probe'), ('d', 'Cooling a probe with ice')], 'a'),
        ('What must an orbit designer include?',
         [('a', 'The colour of the comet'), ('b', 'Only the weather on Earth'), ('c', 'The taste of the comet dust'), ('d', 'The effects of the jets, the shape and the spin')], 'd'),
        ('What happened to the lander Philae at landing?',
         [('a', 'It flew back to Earth'), ('b', 'It became a moon of the comet'), ('c', 'Its harpoons did not fire properly, and it bounced before settling'), ('d', 'It sank into the comet')], 'c'),
        ('Why do navigation errors need correcting?',
         [('a', 'Small errors grow over time'), ('b', 'They make the comet taste better'), ('c', 'They are good for the orbit'), ('d', 'Errors never grow at all')], 'a'),
    ],
}
