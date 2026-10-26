"""Soft Capture and Hard Latch: how two craft join, from the first touch to a sealed hatch."""
CODE = 'flight3a_docking_latches'
BOOK = {
    "title": 'Soft Capture and Hard Latch',
    "subtitle": 'How two craft join, from the first touch to a sealed hatch',
    "chapters": [
        ('Two stages of joining',
         "Docking is usually done in stages. First the two craft touch gently and grip, which is called soft capture. Then strong latches pull them together and lock them, which is called hard latch. Each stage is checked before the next one starts."),
        ('Closing speed',
         "The closing speed is how fast one craft moves toward the other at the moment of contact. It is kept very low, often only a few centimetres a second, so the contact is gentle. A contact that is too fast can bounce the craft apart or damage the seals."),
        ('Alignment first',
         "Before contact, the two craft must line up in angle and in position. Even a small angle can make the parts meet off-centre. Sensors measure the offset, and thrusters correct it."),
        ('Checks at each step',
         "After soft capture, the system checks that the parts have seated before it moves on to the hard latch. If a check fails, the craft backs off and tries again. A rushed docking is the one most likely to fail."),
        ('Pressure and seals',
         "Once latched, the hatch between the two craft is opened only after the seal has been tested and the pressure is equal on both sides. Opening a hatch onto a leak or a pressure difference is a serious hazard."),
        ("A pilot's discipline",
         "Keep the closing speed in mind at every moment, and back off whenever a reading looks wrong. A slow, checked docking is always better than a fast, unchecked one."),
    ],
    "test": [
        ('What are the two stages of joining described here?',
         [('a', 'Soft capture, then hard latch'), ('b', 'Launch, then landing'), ('c', 'Fuel, then food'), ('d', 'Sleep, then wake')], 'a'),
        ('Why is the closing speed kept very low?',
         [('a', 'So the power bar fills up'), ('b', 'So the colours match'), ('c', 'So the contact is gentle and does not bounce the craft apart'), ('d', 'So the hold cannot be seen')], 'c'),
        ('Why must the craft line up before contact?',
         [('a', 'Because the Sun must be behind them'), ('b', 'Because a small angle can make the parts meet off-centre'), ('c', 'Because the hatch needs paint'), ('d', 'Because the crew must sing')], 'b'),
        ('What should happen if a check fails after soft capture?',
         [('a', 'Open the hatch at once'), ('b', 'Turn off the sensors'), ('c', "Stop the crew's sleep"), ('d', 'Back off and try again')], 'd'),
        ('When is it safe to open the hatch between two docked craft?',
         [('a', 'When the seal is tested and the pressure is equal on both sides'), ('b', 'As soon as the latch is touched'), ('c', 'When the Sun rises'), ('d', 'When the crew asks')], 'a'),
    ],
}
