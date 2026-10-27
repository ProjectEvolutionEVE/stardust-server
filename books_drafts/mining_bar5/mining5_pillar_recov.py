"""Pillar recovery sequencing: pillar removal, stress transfer, collapse risk, monitoring and recovery rate."""
CODE = 'mining5_pillar_recov'
BOOK = {
    'title': 'Pillar Recovery Sequencing',
    'subtitle': 'Taking out roof-holding pillars in a safe, planned order',
    "chapters": [
        ('Why leave pillars', 'Pillars are left in place during mining to hold up the roof. They also hold ore that could be recovered later.'),
        ('Pillar removal', 'Recovering pillars means removing them in a planned order, once the mine has finished with that area. Each step is planned, not improvised.'),
        ('Stress transfer', 'When a pillar is removed, its load moves to the rock around it. Those neighbouring pillars can then carry more stress.'),
        ('Collapse risk', 'If stress moves too far, the roof can collapse. Planners check this risk before every step.'),
        ('Sequencing and monitoring', 'The order of removal is planned in advance, and movement is monitored as each pillar comes out. The plan changes if the readings change.'),
        ('Recovery rate', 'Recovery rate is the share of pillar ore brought out. It is weighed against the safety and cost of each step.'),
    ],
    "test": [
        ('Why are pillars left in a mine?', [('a', 'To store the explosives'), ('b', 'To mark the shift changes'), ('c', 'To hold up the roof'), ('d', 'To hide the ore from the market')], 'c'),
        ("Where does a removed pillar's load go?", [('a', 'Straight into the air'), ('b', 'To the rock around it'), ('c', 'Into the cage'), ('d', 'Onto the market')], 'b'),
        ('What is the danger when stress moves too far?', [('a', 'The lights go brighter'), ('b', 'The trucks run faster'), ('c', 'The rota gets shorter'), ('d', 'The roof can collapse')], 'd'),
        ('What is pillar recovery rate?', [('a', 'The share of pillar ore brought out'), ('b', 'The speed of the pillar drill'), ('c', 'The number of pillars in a level'), ('d', 'The depth of the mine floor')], 'a'),
        ('What is planned before each pillar step?', [('a', 'The colour of the helmets'), ('b', 'The price of the diesel'), ('c', 'The menu in the canteen'), ('d', 'The order of removal and the collapse risk')], 'd'),
    ],
}
