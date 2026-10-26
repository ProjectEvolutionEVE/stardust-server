"""Mechanisms and Linkages: bars joined at pivots, and how a machine turns one motion into another."""
CODE = 'engineering2_linkages'
BOOK = {
    "title": 'Mechanisms and Linkages',
    "subtitle": 'Bars joined at pivots: how a machine turns one motion into another',
    "chapters": [
        ('A mechanism changes motion',
         "A mechanism is a set of parts that moves in a planned way. It takes one kind of motion, such as a turning shaft, "
         "and gives another, such as a rocking arm or a sliding block. The rigid parts are called links, and the joints "
         "between them are pivots or sliders."),
        ('Pivots and sliders',
         "A pivot lets two links turn relative to each other. A slider lets one link slide along another. Most linkages use "
         "only these two kinds of joint, which is why they are cheap, strong and easy to repair."),
        ('The four-bar linkage',
         "Four rigid bars joined at pivots, with one bar fixed to the frame, is the simplest useful linkage. Its motion depends "
         "on the lengths of its bars. Change one length and the whole motion changes, which makes linkages easy to tune. "
         "Many windscreen wipers are four-bar linkages."),
        ('Crank and rocker',
         "Turn a short crank and it can drive a longer arm to rock back and forth. Each full turn of the crank makes the "
         "rocker swing through the same fixed arc. Engineers pick the lengths to set how far it swings and how fast."),
        ('Cams and followers',
         "A cam is a shaped wheel that turns and pushes a follower, which moves up and down or back and forth. The shape of "
         "the cam decides the motion exactly. Engines use cams to open and close the valves at the right moment in each turn."),
        ('Designing a linkage',
         "Start with the motion you need, then choose bar lengths that give it. Test with a paper drawing or a cardboard model "
         "before you build. Check for dead points, where the linkage locks or jams, and for parts that hit each other as they "
         "move. Record every length, so a builder can make it exactly."),
    ],
    "test": [
        ("What are the rigid bars of a linkage called?",
         [('a', 'Cables'), ('b', 'Links'), ('c', 'Springs'), ('d', 'Wires')], 'b'),
        ("Which two kinds of joint do most linkages use?",
         [('a', 'Welds and rivets'), ('b', 'Glue and tape'), ('c', 'Springs and cables'), ('d', 'Pivots and sliders')], 'd'),
        ("In a four-bar linkage, what most changes its motion?",
         [('a', 'The lengths of its bars'), ('b', 'The colour of the bars'), ('c', 'The number of bolts'), ('d', 'The weight of the frame')], 'a'),
        ("What does a cam do?",
         [('a', 'Stores power in a spring'), ('b', 'Melts metal'), ('c', 'Pushes a follower through a motion set by its shape'), ('d', 'Measures the temperature')], 'c'),
        ("Why do engines use cams to open and close valves?",
         [('a', 'Cams are cheaper than paint'), ('b', 'They open and close the valves at the right moment in each turn'), ('c', 'Cams cool the engine'), ('d', 'Cams stop rust')], 'b'),
    ],
}
