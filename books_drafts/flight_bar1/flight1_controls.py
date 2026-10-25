"""Flight Controls and Handling: the throttle, the stick and the thrusters, and the real physics of moving in space."""
CODE = 'flight1_controls'
BOOK = {
    "title": 'Flight Controls and Handling',
    "subtitle": 'Throttle, stick and thrusters, and how a craft really moves in space',
    "chapters": [
        ('Three controls',
         'Your craft has three main controls. The throttle, the arrows in the bottom right corner under WARP, sets how fast you may go. The stick works anywhere on the screen: press and hold to steer. The side thrusters at the bottom left turn the craft where it sits.'),
        ('The throttle',
         'Each tap of the up arrow adds 10%, and each tap of the down arrow takes 10% away, from 0% to 100%. Under power, the craft speeds up toward the speed the throttle sets. Turn the throttle down and it coasts down to the new speed. At 0% it stops pushing and drifts to a stop.'),
        ('Steering with the stick',
         'Press and hold anywhere away from the buttons, and the stick appears under your finger. Pull back to raise the nose, push to dip it, and move left or right to bank. Under power, the craft flies where it points.'),
        ('Turning in place',
         'The side thrusters turn the craft without moving it forward. Use them to line up on a target before you take aim with the stick. They are for turning, not for going anywhere.'),
        ("Newton's laws in space",
         "Newton's first law says a moving thing keeps moving at the same speed and in the same direction unless a force acts on it. Space has almost no air, so nothing slows a craft down: once you stop pushing, you keep going. Newton's second law says the change in speed depends on the push divided by the mass, so a heavy craft speeds up more slowly than a light one with the same engine."),
        ('Why the game keeps your speed',
         'The game is not an exact copy of empty space. Left alone, a craft would drift forever, so the game gently slows it when you are not pushing, and the throttle gives you a speed you can count on. Think of the throttle as a speed setting, not a rocket that never stops.'),
    ],
    "test": [
        ("How much does one tap of the throttle's up arrow add?",
         [('a', '10%'), ('b', '1%'), ('c', '25%'), ('d', '100%')], 'a'),
        ('What does the throttle setting control?',
         [('a', 'The colour of the craft'), ('b', 'The top speed you are allowed'), ('c', 'How many bars you have'), ('d', 'The distance to the Sun')], 'b'),
        ("What does Newton's first law say about a moving object in space?",
         [('a', 'It slows down by itself'), ('b', 'It must be pushed all the time'), ('c', 'It keeps moving at the same speed and direction unless a force acts on it'), ('d', 'It speeds up when there is no air')], 'c'),
        ('What do the side thrusters do?',
         [('a', 'Carry you forward fast'), ('b', 'Lock onto debris'), ('c', 'Open the hold'), ('d', 'Turn the craft in place')], 'd'),
        ('Why does the game gently slow the craft when you stop pushing?',
         [('a', 'So a craft never drifts forever, which keeps the game playable'), ('b', 'Space is full of air that drags on it'), ('c', 'The Starship pulls it back'), ('d', 'Gravity from the Sun stops it at once')], 'a'),
    ],
}
