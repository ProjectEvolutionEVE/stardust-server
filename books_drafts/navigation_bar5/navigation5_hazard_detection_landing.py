"""Hazard Detection in Precision Landing: lidar hazard maps, safe site choice, the descent timeline, sensor fusion, failure modes and tests."""
CODE = 'navigation5_hazard_detection_landing'
BOOK = {
    "title": 'Hazard Detection in Precision Landing',
    "subtitle": 'Finding the rocks and slopes before a lander touches down',
    "chapters": [
        ('Mapping the hazards',
         'Before a landing, orbiting craft map the ground with cameras and with laser radar, called lidar. The map shows rocks, steep slopes and craters that could tip or trap a lander.'),
        ('Choosing a safe site',
         'Engineers choose a landing spot where the slope is gentle and rocks are few. They also leave a margin, so that a small error in the landing still leaves the lander on safe ground.'),
        ('The descent timeline',
         'Descent happens in stages, and the craft uses its sensors at each stage. It can change its plan as it comes lower. The timing matters, because each stage needs a set amount of fuel and a set speed.'),
        ('Sensor fusion',
         'A lander combines data from cameras, radar and inertial sensors. Fusing the data gives a better estimate of where the lander is and how fast it moves than any single sensor could give alone.'),
        ('Failure modes',
         'Things that can go wrong include a sensor giving a false reading, a dust cloud hiding the ground, or a sudden change in the wind. Good designs plan a response for each failure they can imagine.'),
        ('Tests',
         'Engineers test hazard detection on the ground with rigs, in computer simulations and on flights of test vehicles. Only after these tests is the system trusted with a real landing.'),
    ],
    "test": [
        ('What is lidar?',
         [('a', 'A kind of fish'), ('b', 'A cooking method'), ('c', 'Laser radar that measures distances to a surface'), ('d', 'An engine for satellites')], 'c'),
        ('What makes a site safe to land on?',
         [('a', 'A gentle slope and few rocks'), ('b', 'Very steep cliffs'), ('c', 'Thick layers of loose dust everywhere'), ('d', 'A large boulder in the middle')], 'a'),
        ('Why are several sensors combined?',
         [('a', 'To add weight to the lander'), ('b', 'To make the lander louder'), ('c', 'To paint the lander'), ('d', 'A combined estimate is better than any single sensor')], 'd'),
        ('What is a safety margin in site choice?',
         [('a', 'Spare room for small errors'), ('b', 'A kind of rock'), ('c', 'A radio signal'), ('d', 'A bill from a supplier')], 'a'),
        ('What is a failure mode?',
         [('a', 'A happy outcome'), ('b', 'A way that a system can go wrong'), ('c', 'A type of fuel'), ('d', 'A test of colour')], 'b'),
    ],
}
