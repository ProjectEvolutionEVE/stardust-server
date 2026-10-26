"""Geostationary Transfer: how a satellite climbs from a low start to its final slot over the equator."""
CODE = 'flight5_a_gto'
BOOK = {
    "title": 'Geostationary Transfer',
    "subtitle": 'From a low start to a slot over the equator',
    "chapters": [
        ('The problem',
         'A rocket cannot usually lift a satellite straight to its final height over the equator. Most launches reach a low, elliptical starting orbit first. The satellite then has to climb the rest of the way on its own power.'),
        ('The transfer orbit',
         "The usual path is a geostationary transfer orbit, an ellipse with a low point near the Earth and a high point at geostationary height. The climb happens in stages, using the satellite's own engine."),
        ('The apogee burn',
         'At the high point of the ellipse, the satellite fires its engine to raise the low point and round off the orbit. This is the apogee burn. It turns the long ellipse into a circle at geostationary height.'),
        ('Changing the plane',
         'A satellite launched from a site away from the equator starts at an angle to the equator. Changing that tilt costs fuel, so planners often combine the tilt change with the apogee burn to save propellant.'),
        ('Electric raising',
         'Some satellites use electric thrusters to climb slowly over weeks or months. This saves a great deal of fuel but takes much longer. Operators weigh the time saved against the fuel the satellite can carry.'),
        ('Timelines and cost',
         'A full transfer can take several days with chemical engines, or many months with electric ones. The mission plan sets the schedule and the fuel budget together. Both affect what the satellite costs and how long it can work.'),
    ],
    "test": [
        ('Why is a geostationary satellite usually not lifted straight to its final height?',
         [('a', 'Because most launches reach a low starting orbit first'), ('b', 'Because rockets cannot lift anything'), ('c', 'Because the Sun blocks the way'), ('d', 'Because the satellite is too small to climb')], 'a'),
        ('What is the shape of a geostationary transfer orbit?',
         [('a', 'An ellipse with a low point near the Earth and a high point at geostationary height'), ('b', 'A straight line'), ('c', 'A circle at the Moon'), ('d', 'A spiral inside the atmosphere')], 'a'),
        ('What is the apogee burn?',
         [('a', 'A burn at the low point to lift the satellite off the pad'), ('b', 'An engine firing at the high point that turns the ellipse into a circle'), ('c', 'A burn to cool the panels'), ('d', 'A signal sent to the ground')], 'b'),
        ('What does electric raising trade for fuel savings?',
         [('a', 'Speed for distance'), ('b', 'Power, because it makes no power'), ('c', 'Time, because the climb takes much longer'), ('d', 'Crew, because it needs none')], 'c'),
        ('Why do planners often combine a tilt change with the apogee burn?',
         [('a', 'To make the satellite lighter'), ('b', 'To make the launch louder'), ('c', 'To reach the Moon sooner'), ('d', 'To save propellant, since a tilt change costs fuel')], 'd'),
    ],
}
