"""Launch Windows and Cheaper Routes: choosing the right day to leave saves fuel, time and money."""
CODE = 'navigation3a_launch_windows'
BOOK = {
    "title": 'Launch Windows and Cheaper Routes',
    "subtitle": 'Leaving at the right time, and planning routes that save fuel and money',
    "chapters": [
        ('The right day to leave',
         'A planet keeps moving, so a route that is cheap on one day can be expensive a few weeks later. A launch window is the short span of dates when the planets line up well for a route. Miss it, and the trip can need much more fuel.'),
        ('Synodic periods',
         'The time between two good alignments of Earth and another planet is called the synodic period. For Mars, the synodic period is about 780 days, so good windows come roughly every 26 months. Planners plan years ahead around these dates.'),
        ('Shorter trips, more fuel',
         'A faster trip usually needs more fuel, and a slower one usually needs less. A Hohmann transfer to Mars takes about 260 days. A planner weighs the extra fuel and the lost time against each other before choosing the route.'),
        ('Cheaper routes with a longer trip',
         'A bi-elliptic transfer goes out to a far point before coming back in. For very large changes of orbit it can need less fuel than a Hohmann transfer, but it takes much longer. The saving is real only when the change is very large.'),
        ('Money on the route',
         'In the game, flying a craft costs 50 credits an hour, or a weekly lease of 500 credits, paid to the WSC. A longer flight therefore costs more, so a route that saves an hour of flight saves real credits. Planning the route is a way of planning the budget.'),
        ('Plan the whole trip',
         'The cheapest trip is the one planned with the window, the route, the fuel and the schedule together. Check each choice against the others. A plan that saves fuel but misses the window can cost more in the end.'),
    ],
    "test": [
        ('What is a launch window?',
         [('a', 'A short span of dates when the planets line up well for a route'), ('b', 'A glass panel on a ship'), ('c', 'A type of engine'), ('d', 'A daily timetable for crew')], 'a'),
        ('About how long is the synodic period for Mars?',
         [('a', 'About 88 days'), ('b', 'About 11.9 years'), ('c', 'About 780 days'), ('d', 'About 24 hours')], 'c'),
        ('What usually happens to fuel needs when a trip is faster?',
         [('a', 'They always fall'), ('b', 'They usually rise'), ('c', 'They stay the same'), ('d', 'They vanish')], 'b'),
        ('When can a bi-elliptic transfer save fuel compared with a Hohmann transfer?',
         [('a', 'For a trip between two nearby moons'), ('b', 'Whenever the trip is short'), ('c', 'Never'), ('d', 'For very large changes of orbit, though it takes much longer')], 'd'),
        ('In the game, what does flying a craft cost by the hour?',
         [('a', '50 credits an hour'), ('b', '5 credits an hour'), ('c', '500 credits an hour'), ('d', 'Nothing, the WSC pays')], 'a'),
    ],
}
