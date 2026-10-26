"""Interplanetary Trajectory Design: choosing when to leave, how to use planets, and where to arrive."""
CODE = 'flight5_a_interplanetary'
BOOK = {
    "title": 'Interplanetary Trajectory Design',
    "subtitle": 'Launch windows, planetary assists and arrival',
    "chapters": [
        ('Launch windows',
         'Planets move around the Sun at different speeds, so the best times to launch to another planet come at intervals. These are called launch windows. Missing a window can mean waiting many months or years for the next one.'),
        ('The departure',
         'The launch sets the speed and direction of the craft as it leaves the Earth. The planners choose a path that uses as little fuel as possible while still reaching the target on time.'),
        ('Gravity assists',
         'A craft can fly past a planet and borrow a little of its motion, gaining speed without much fuel. This is a gravity assist. Voyager 2 used several of these to reach the outer planets.'),
        ('The arrival',
         'Arriving at a planet means slowing down enough to be captured, or passing close by. The arrival burn is one of the most important moments of the trip, and it must be timed carefully.'),
        ('Correction manoeuvres',
         'Small errors build up during the trip, so the craft makes correction burns along the way. These fix the path so that the arrival is on target. Planners plan for them from the start.'),
        ('Mission examples',
         'Many missions have used launch windows, gravity assists and arrival burns together. The plan is a balance of time, fuel and risk. Each mission teaches new ways to fly these paths.'),
    ],
    "test": [
        ('What is a launch window?',
         [('a', 'A window in the rocket'), ('b', 'A radio frequency'), ('c', 'A time when the planets line up well for a trip'), ('d', 'A crew hatch')], 'c'),
        ('What is a gravity assist?',
         [('a', 'Lifting a craft with a crane'), ('b', 'Turning off gravity'), ('c', "A pilot's seat"), ('d', "Using a planet's motion to gain speed without much fuel")], 'd'),
        ('Which spacecraft used several gravity assists to reach the outer planets?',
         [('a', 'Voyager 2'), ('b', 'A balloon'), ('c', 'The Hubble telescope'), ('d', 'A weather satellite')], 'a'),
        ('Why does a craft make correction burns along the way?',
         [('a', 'Because small errors build up during the trip'), ('b', 'Because it is bored'), ('c', 'Because the planets ask it to'), ('d', 'Because the paint is wet')], 'a'),
        ('What is the arrival burn?',
         [('a', 'A fire in the galley'), ('b', 'A burn to slow the craft enough to be captured or pass close by'), ('c', 'A signal to Earth'), ('d', 'A fuel leak')], 'b'),
    ],
}
