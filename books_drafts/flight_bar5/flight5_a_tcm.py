"""Trajectory Correction Manoeuvres: the small burns that keep a long trip on target."""
CODE = 'flight5_a_tcm'
BOOK = {
    "title": 'Trajectory Correction Manoeuvres',
    "subtitle": 'Small burns that keep a long trip on target',
    "chapters": [
        ('Why they are needed',
         'No launch is perfect, and the craft is never pushed exactly as planned. Tiny differences in speed and direction grow over long distances. Trajectory correction manoeuvres, or TCMs, are small burns that bring the path back on target.'),
        ('Planning the burns',
         'The team plans the burns before launch, with a schedule and a rough size for each one. They are placed where they do the most good for the least fuel. The plan is updated as real data comes in.'),
        ('Tracking',
         "Ground stations measure the craft's position and speed by radio, often every day. These measurements show how far the path has drifted. Only accurate tracking makes a good correction possible."),
        ('How big a burn is',
         'Most correction burns are small, sometimes only a few metres per second, and sometimes much less. Even a small burn can change where the craft will arrive by a large distance. Careful sizing saves fuel.'),
        ('Navigation error',
         'The navigation error is the uncertainty in where the craft really is. It is reduced as more tracking data comes in. Each correction is chosen to fit the current error, not to chase an old one.'),
        ('Arrivals at Mars',
         'Missions to Mars have relied on correction burns to arrive at the right place. A miss by even a few kilometres can change the landing site a great deal. Many successful arrivals were the result of steady correction work.'),
    ],
    "test": [
        ('What are trajectory correction manoeuvres?',
         [('a', 'Large turns of the Sun'), ('b', 'Radio songs sent to Earth'), ('c', 'Paint jobs on the craft'), ('d', 'Small burns that bring a path back on target')], 'd'),
        ('Why do missions use ground stations to track the craft?',
         [('a', 'To measure its position and speed so the path can be corrected'), ('b', 'To count the stars'), ('c', 'To change the weather'), ('d', 'To cool the craft')], 'a'),
        ('What is navigation error?',
         [('a', 'The uncertainty about where the craft really is'), ('b', 'A mistake in the menu'), ('c', 'A broken window'), ('d', 'A fault in the crew bunks')], 'a'),
        ('How big are most correction burns?',
         [('a', 'Usually very large, like a planet'), ('b', 'Often small, sometimes only a few metres per second'), ('c', 'Always bigger than the launch'), ('d', 'Always zero')], 'b'),
        ('Why do Mars missions rely on correction burns?',
         [('a', 'To make Mars move'), ('b', "To shorten the crew's holiday"), ('c', 'To arrive at the right place, since small errors grow over distance'), ('d', 'To change the colour of the sky')], 'c'),
    ],
}
