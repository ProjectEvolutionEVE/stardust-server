"""Ascent to Orbit: the gravity turn, staging and the fuel a rocket spends climbing to orbit."""
CODE = 'flight5_a_launch_ascent'
BOOK = {
    "title": 'Ascent to Orbit',
    "subtitle": 'The gravity turn, staging and the fuel a rocket spends',
    "chapters": [
        ('Going up, then over',
         'A rocket leaves the pad climbing nearly straight up. It then tips gradually over, so that it is moving sideways as well as up. This sideways speed is what an orbit needs.'),
        ('The gravity turn',
         'After a while, the rocket lets gravity help turn its path, so that it follows a smooth curve rather than fighting the pull. This is the gravity turn. It saves fuel and keeps the rocket steady.'),
        ('Max-Q',
         'As the rocket speeds up, the air pressure on it rises and then falls. The point of greatest pressure, called max-Q, is one of the hardest moments of the ascent. Rockets often ease the throttle there.'),
        ('Staging',
         'A rocket is built in stages. Each stage drops away when its fuel is spent, so the rest of the rocket does not carry dead weight. Staging is one of the main ways to reach orbit with a practical rocket.'),
        ('Losses',
         'Some of the fuel is used to fight gravity and drag rather than to gain orbital speed. Designers call this the losses. Good ascent planning keeps the losses small without risking the rocket.'),
        ('A typical profile',
         'A typical ascent takes under about ten minutes to reach a low orbit. The rocket climbs, turns, and burns each stage in turn. The whole sequence is planned in great detail before launch.'),
    ],
    "test": [
        ('Why does a rocket tip over during ascent?',
         [('a', 'To give itself sideways speed, which an orbit needs'), ('b', 'Because it has lost its engine'), ('c', 'To hide from the sun'), ('d', 'Because the crew is asleep')], 'a'),
        ('What is the gravity turn?',
         [('a', 'A turn that lets gravity help bend the path and saves fuel'), ('b', 'A turn of the pad'), ('c', 'A turn of the crew seats'), ('d', 'A turn of the radio dial')], 'a'),
        ('What is max-Q?',
         [('a', 'The highest point of the orbit'), ('b', 'The point of greatest air pressure on the rocket during ascent'), ('c', 'A rocket model name'), ('d', 'The name of a crew member')], 'b'),
        ('Why is a rocket built in stages?',
         [('a', 'So the rocket can be painted in layers'), ('b', 'So the engines can be stored'), ('c', 'So that spent stages can drop away and not carry dead weight'), ('d', 'So it can float')], 'c'),
        ('What are the losses in an ascent?',
         [('a', 'Lost radio signals only'), ('b', 'Lost crew members'), ('c', 'Lost paint'), ('d', 'Fuel spent fighting gravity and drag instead of gaining orbital speed')], 'd'),
    ],
}
