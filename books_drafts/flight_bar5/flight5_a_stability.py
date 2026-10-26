"""Spin and Stability: how a spinning craft stays steady, and why energy loss can make it flip."""
CODE = 'flight5_a_stability'
BOOK = {
    "title": 'Spin and Stability',
    "subtitle": 'Keeping a craft steady, and why it can flip',
    "chapters": [
        ('Spin stabilisation',
         'A spinning body keeps its direction, much like a spinning top. Some satellites were built to spin for this reason, so that they stayed steady without needing constant control.'),
        ('Dual spin',
         'Some craft have a spinning part and a part that stays pointed. This dual spin lets a sensor point at a target while the rest of the craft spins. It combines steadiness with precise pointing.'),
        ('Explorer 1',
         'Explorer 1, the first American satellite, had a flexible antenna that flexed and wasted energy as it spun. Its energy loss moved the spin onto a short axis, a tumble known as a flat spin. It is a classic lesson in stability.'),
        ('Gravity gradient',
         'A long craft can be steadied by the difference in gravity along its length. Its near end is pulled a little more than its far end, and the craft tends to line up with the Earth. This is gravity gradient stabilisation.'),
        ('Energy loss',
         'A spinning craft that wastes energy, for example in flexing parts, can change to a spin about another axis. Designers prevent this by damping the flex. Good design keeps energy losses low.'),
        ('Examples and lessons',
         'Spin, dual spin and gravity gradient each have their uses. Each choice trades complexity against steadiness and control. Engineers choose the method that fits the mission.'),
    ],
    "test": [
        ('What does a spinning body tend to keep?',
         [('a', 'Its colour'), ('b', 'Its crew'), ('c', 'Its fuel'), ('d', 'Its direction')], 'd'),
        ('What is dual spin?',
         [('a', 'A spinning part and a pointed part, so a sensor can aim while the rest spins'), ('b', 'Two spins at once with no control'), ('c', 'A type of radio'), ('d', 'A landing method')], 'a'),
        ('What happened with Explorer 1?',
         [('a', 'Its flexible antenna wasted energy, and its spin flipped to a flat spin'), ('b', 'It landed on the Moon'), ('c', 'It sank in the sea'), ('d', 'It was painted white')], 'a'),
        ('How does gravity gradient stabilisation work?',
         [('a', 'A craft is held by a magnet'), ('b', 'A long craft lines up with the Earth because gravity pulls its near end more'), ('c', 'A craft is held by a rope'), ('d', 'A craft is held by air')], 'b'),
        ('What can make a spinning craft change its spin axis?',
         [('a', 'Music from the crew'), ('b', 'Sunny weather'), ('c', 'Energy losses, such as flexing parts'), ('d', 'Painted stripes')], 'c'),
    ],
}
