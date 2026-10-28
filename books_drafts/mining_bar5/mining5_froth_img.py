"""Froth imaging and control in flotation: cameras, bubble size, froth stability, control loops, reagent dosing and gains."""
CODE = 'mining5_froth_img'
BOOK = {
    'title': 'Froth Imaging and Control',
    'subtitle': 'Using cameras and control loops to keep flotation running at target',
    "chapters": [
        ('Watching the froth', 'Cameras above flotation cells record the surface of the froth. Software reads its look to judge how the cell is running.'),
        ('Bubble size', 'Smaller bubbles usually give more contact with particles. Image analysis measures the size of the bubbles.'),
        ('Froth stability', 'A stable froth holds its shape. A froth that is too unstable or too stiff can lower recovery.'),
        ('Control loops', 'A control loop adjusts a setting, such as reagent dosing, to keep the froth at a target. The loop repeats many times a minute.'),
        ('Reagent dosing', 'Reagents are added in small steps, and the effect is watched on the camera. Small steps prevent overshoot.'),
        ('Gains', 'The gain sets how strongly the controller reacts. A gain that is too high causes swings, and one that is too low is slow.'),
    ],
    "test": [
        ('What do cameras above a flotation cell record?', [('a', 'The surface of the froth'), ('b', 'The depth of the mine'), ('c', 'The number of trucks'), ('d', 'The weather on the surface')], 'a'),
        ('What usually happens with smaller bubbles?', [('a', 'Less contact with particles'), ('b', 'More contact with particles'), ('c', 'Faster trucks'), ('d', 'Louder pumps')], 'b'),
        ('What does a control loop adjust?', [('a', 'The colour of the cab'), ('b', 'The shift start times'), ('c', 'The price of the ore'), ('d', 'A setting, such as reagent dosing, to keep a target')], 'd'),
        ('What is the gain of a controller?', [('a', 'The number of cameras'), ('b', 'The colour of the screen'), ('c', 'How strongly it reacts'), ('d', 'The length of the cable')], 'c'),
        ('What happens if the gain is too high?', [('a', 'The system stops for good'), ('b', 'The froth turns to metal'), ('c', 'The system swings back and forth'), ('d', 'The screen goes dark')], 'c'),
    ],
}
