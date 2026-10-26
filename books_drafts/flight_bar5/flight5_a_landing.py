"""Powered Landing: how a craft slows down with its own engines and sets down on the ground."""
CODE = 'flight5_a_landing'
BOOK = {
    "title": 'Powered Landing',
    "subtitle": 'Slowing down with its own engines to set down',
    "chapters": [
        ('The descent profile',
         'A powered landing is planned as a descent profile: a path of height against time, with the speed set at each point. The engines are fired so that the craft slows as it nears the ground. The plan must work even if the craft is slightly off course.'),
        ('Throttling',
         'Engines that can be throttled let the craft change its push smoothly. Throttling lets the craft slow in stages and hover when needed. A fixed engine that can only be on or off is much harder to land with.'),
        ('Hover and hazards',
         'A craft that hovers can look for a safe spot. Hazards such as boulders, slopes or dust clouds must be seen and avoided. The Apollo lunar landings had a moment of manual control to pick a clearer place when the planned site was rough.'),
        ('Fuel cost',
         'Landing takes fuel, and the fuel needed depends on how much the craft must slow down and how long it hovers. A long hover can use a lot of propellant. Planners keep a safety margin so the craft can always reach the ground.'),
        ('Real landings',
         'Viking 1 made a powered landing on Mars in 1976. The Apollo lunar module landed on the Moon with its engine. More recently, SpaceX has landed rocket boosters back on the ground under engine power.'),
        ('Careful design',
         'Good landing design balances the descent path, the throttle range, the hazard checks and the fuel reserve. A landing that works in theory may fail in practice, so the plans are tested many times.'),
    ],
    "test": [
        ('What is a descent profile?',
         [('a', 'A photograph of the landing site'), ('b', 'A recipe for food'), ('c', 'A list of crew names'), ('d', 'A path of height against time, with the speed set at each point')], 'd'),
        ('Why is a throttleable engine helpful for landing?',
         [('a', 'It lets the craft change its push smoothly and hover'), ('b', 'It makes the craft silent'), ('c', 'It paints the craft'), ('d', 'It stops the Sun')], 'a'),
        ('Which mission landed on Mars under powered descent in 1976?',
         [('a', 'Viking 1'), ('b', 'Voyager 1'), ('c', 'Apollo 8'), ('d', 'Sputnik 1')], 'a'),
        ('What does a long hover use up?',
         [('a', 'Air'), ('b', 'Propellant'), ('c', 'Sunlight'), ('d', 'Sand')], 'b'),
        ('Why do planners keep a safety margin of fuel?',
         [('a', 'So the crew can have a party'), ('b', 'So the engines can be painted'), ('c', 'So the craft can always reach the ground'), ('d', 'So the Moon gets heavier')], 'c'),
    ],
}
