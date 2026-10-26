"""Fatigue: how a part that is safe under one load can still crack after many repeats of it."""
CODE = 'engineering3a_fatigue'
BOOK = {
    "title": 'Fatigue: Failure from Repeated Loads',
    "subtitle": 'How a part with a safe load can still crack after many cycles',
    "chapters": [
        ('The same load, again and again',
         'Fatigue is the weakening of a material by repeated loading. A part can carry a load once with ease, yet crack after thousands or millions of cycles at a lower load. Almost any moving machine is at risk.'),
        ('Where cracks start',
         'Cracks begin at a stress concentration, such as a sharp corner, a small hole, a scratch or the edge of a weld. The stress is higher at these points than in the smooth metal around them. A tiny crack then grows a little with each cycle.'),
        ('How a fatigue break looks',
         'A fatigue fracture often shows a smooth, curved area where the crack grew slowly, and a rough area where the part finally broke. Faint rings called beach marks can show the stops and starts of growth. Looking for these marks helps find the cause of a failure.'),
        ('The S-N curve',
         'Engineers test many samples at different stress levels and count the cycles to failure. Plotting these gives an S-N curve, where higher stress means fewer cycles. Some steels have an endurance limit, a stress below which they seem to last indefinitely, while many aluminium alloys have no clear limit.'),
        ('A famous case',
         'The de Havilland Comet, an early jet airliner, suffered crashes in the early 1950s. The cause was fatigue cracking that began at the square corners of its windows, where cabin pressure was raised and lowered on every flight. The later design used rounded window corners to lower the stress.'),
        ('Designing against fatigue',
         'Round sharp corners, smooth the surface and avoid sudden changes in section. Cut down the number of load cycles where you can. Inspect parts that flex often, and replace them on a schedule before a crack can grow large.'),
    ],
    "test": [
        ('What is fatigue?',
         [('a', 'Heating a metal until it glows'), ('b', 'Painting a part to protect it'), ('c', 'Weakening caused by repeated loading'), ('d', 'A part being too heavy')], 'c'),
        ('Where do fatigue cracks most often begin?',
         [('a', 'At the centre of a smooth flat face'), ('b', 'On the inside of the paint'), ('c', 'Only in the middle of long bars'), ('d', 'At stress concentrations such as sharp corners or small holes')], 'd'),
        ('What do the beach marks on a fatigue fracture show?',
         [('a', 'The stops and starts of crack growth'), ('b', 'Where the paint was applied'), ('c', 'The serial number of the part'), ('d', 'The temperature of the air')], 'a'),
        ('What is an endurance limit?',
         [('a', 'The longest a part can be stored'), ('b', 'A stress below which some steels seem to last indefinitely'), ('c', 'The highest speed a part can turn'), ('d', 'The weight a part can carry at rest')], 'b'),
        ('What caused the early crashes of the de Havilland Comet?',
         [('a', 'Too much paint on the wings'), ('b', 'A shortage of fuel on every flight'), ('c', 'Fatigue cracks at the square corners of its windows'), ('d', 'Cold air leaking into the engines')], 'c'),
    ],
}
