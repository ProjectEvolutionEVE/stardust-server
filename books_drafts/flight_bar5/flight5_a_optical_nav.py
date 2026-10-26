"""Optical Navigation: finding a craft's position by looking at the stars, moons and planets."""
CODE = 'flight5_a_optical_nav'
BOOK = {
    "title": 'Optical Navigation',
    "subtitle": 'Finding your place by looking at the stars and moons',
    "chapters": [
        ('Looking outward',
         'A camera on a craft can find its position by looking at the stars behind distant bodies. The stars act as a fixed background, and the position of a known body against them tells the team where the craft is pointing and how far away the body is.'),
        ('Moons as targets',
         'Large moons are useful targets. When a craft takes pictures of a moon against the stars, the team can work out where the craft is compared with that moon. This helps refine the path at the end of a long trip.'),
        ('Voyager and Cassini',
         'Images of planets and moons have long been used to check and refine the paths of spacecraft. Cassini, for example, used pictures of moons during its long tour of Saturn to confirm where it was.'),
        ('Autonomy',
         'Some craft now carry enough software to find their way with their own cameras, with little help from the ground. Deep Space 1 tested this kind of autonomous navigation on a flyby of a comet.'),
        ('Limits',
         'Optical navigation needs something to look at, and it works best when the target is clear and the stars are steady. It cannot tell how far away the craft is from the star background alone, so it works best alongside radio tracking.'),
        ('Why it matters',
         'Optical navigation is cheap, because it uses the camera the craft already carries. It gives a fresh, independent check on the path. Teams often combine it with radio data for the best result.'),
    ],
    "test": [
        ("What does optical navigation use to find a craft's position?",
         [('a', 'Pictures of stars and known bodies against the stars'), ('b', 'A map of the ocean'), ('c', 'Radio songs from the crew'), ('d', 'Weather reports')], 'a'),
        ('Why are large moons useful targets for navigation?',
         [('a', "They can be compared with the craft's position and help refine the path"), ('b', 'They are very bright lights'), ('c', 'They carry fuel for the craft'), ('d', 'They stop the craft from moving')], 'a'),
        ('What did Deep Space 1 test on its flyby of a comet?',
         [('a', 'A cake recipe'), ('b', 'Autonomous navigation with its own cameras'), ('c', 'Solar sails made of paper'), ('d', 'Telephone calls')], 'b'),
        ('Why is optical navigation often combined with radio tracking?',
         [('a', 'Because cameras cannot take pictures'), ('b', 'Because radio makes stars brighter'), ('c', 'Because radio data can supply the distance that star pictures alone do not'), ('d', 'Because the Moon needs radio')], 'c'),
        ('What is a main advantage of optical navigation?',
         [('a', 'It needs a new, expensive instrument'), ('b', 'It works only in daylight on Earth'), ('c', 'It stops the engines'), ('d', 'It uses a camera the craft already carries')], 'd'),
    ],
}
