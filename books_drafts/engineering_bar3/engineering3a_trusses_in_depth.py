"""Trusses in Depth: working out the push or the pull in every bar, one joint at a time."""
CODE = 'engineering3a_trusses_in_depth'
BOOK = {
    "title": 'Trusses in Depth',
    "subtitle": 'Working out the push or the pull in every bar, one joint at a time',
    "chapters": [
        ('Every joint is in balance',
         'In a truss at rest, every joint is in balance: the forces on it add up to zero in every direction. That gives two equations at each joint, one sideways and one up or down. Solving joint by joint is called the method of joints.'),
        ('Start where you know the most',
         'Begin at a joint with only two unknown bars, because balance gives you two equations to solve for them. Once a bar force is known, it becomes known at the next joint too. Work outward until every bar is found.'),
        ('Pull or push',
         'A bar that pulls on its joint is in tension, and a bar that pushes on it is in compression. Mark each bar as pull or push once you have solved it. A bar in compression must also be checked for buckling, because a long, thin bar can bend sideways before it crushes.'),
        ('Counting the bars',
         'A simple flat truss can be solved by balance alone when it has twice its number of joints, minus 3, in bars. A triangle has 3 joints and 3 bars, and that fits. Too few bars and the frame can collapse, and too many means balance alone is not enough.'),
        ('Find the supports first',
         'Before solving any joint, find the forces at the supports, using the whole truss in balance. A symmetric truss under a symmetric load shares that load equally between its two supports. Skip this step and every bar in the truss will come out wrong.'),
        ('A joint is only as good as its fixing',
         'The bars of a truss meet at pins, bolts or welds, and a joint that cannot carry its share is the weak point. Check the fixing as carefully as the bar itself. A bar that is strong but poorly joined will still fail.'),
    ],
    "test": [
        ('What does it mean for a joint in a truss at rest to be in balance?',
         [('a', 'The forces on it add to zero in every direction'), ('b', 'It is painted in two colours'), ('c', 'It carries no load at all'), ('d', 'It is the heaviest point')], 'a'),
        ('How many bars does a simple flat truss with 5 joints need?',
         [('a', '5'), ('b', '3'), ('c', '7'), ('d', '10')], 'c'),
        ('Which bar is in compression?',
         [('a', 'A bar that pulls on its joint'), ('b', 'A bar that pushes on its joint'), ('c', 'A bar with no load'), ('d', 'A bar that is painted')], 'b'),
        ('Why must a long, thin bar in compression be checked for buckling?',
         [('a', 'It can bend sideways before it crushes'), ('b', 'It becomes lighter when squeezed'), ('c', 'It always snaps in two'), ('d', 'It stops conducting heat')], 'a'),
        ('What should you find before solving the joints one by one?',
         [('a', 'The colour of each bar'), ('b', 'The forces at the supports'), ('c', 'The number of bolts in the bridge'), ('d', 'The name of the builder')], 'b'),
    ],
}
