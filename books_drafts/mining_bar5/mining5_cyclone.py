"""Hydrocyclones and Classification: using spinning slurry to split fine from coarse, and keeping the split steady."""
CODE = 'mining5_cyclone'
BOOK = {
    "title": 'Hydrocyclones and Classification',
    "subtitle": 'Splitting fine from coarse with spinning slurry',
    "chapters": [
        ('A spinning sort', 'A hydrocyclone is a cone-shaped vessel. Slurry is fed in at the side and spins fast, so heavy coarse particles move outward and down. Fine particles are carried up through the centre. This is called classification.'),
        ('Cut size', 'The cut size is the particle size where half of the material goes to each side. Operators change the cut size to suit the next step in the plant. Getting the cut size right is central to good grinding.'),
        ('Underflow density', 'The underflow is the thick slurry that leaves the bottom of the cyclone. Its density affects how much fine material is carried with the coarse. Operators watch the underflow to keep the split on target.'),
        ('Efficiency and wear', 'Efficiency is how well the cyclone sends fine and coarse to the right places. Abrasive slurry wears the liner over time, which changes the split. Liners are inspected and replaced on a schedule.'),
        ('Control loops', 'Operators use pressure, density and flow to control the cyclone. Automatic controls adjust settings to hold the split steady. Steady control gives a better product and less wasted grinding.'),
        ('Circuit design', 'A cyclone works best as part of a circuit, with grinding mills and screens around it. Coarse material is sent back for regrinding. The circuit is designed as a whole, not as one part alone.'),
    ],
    "test": [
        ('How does a hydrocyclone separate particles?', [('a', 'It melts the particles'), ('b', 'It freezes the slurry'), ('c', 'It paints the particles'), ('d', 'Heavy coarse particles move outward and down while fine ones rise through the centre')], 'd'),
        ('What is cut size?', [('a', 'The particle size where half the material goes to each side'), ('b', 'The length of the pipe'), ('c', 'The colour of the cone'), ('d', 'The weight of the workers')], 'a'),
        ('What is the underflow?', [('a', 'The water leaving the top'), ('b', 'The thick slurry leaving the bottom of the cyclone'), ('c', 'The air inside the pump'), ('d', 'The fuel for the mill')], 'b'),
        ('What does abrasive slurry do over time?', [('a', 'It polishes the cone to a mirror'), ('b', 'It makes the cone lighter'), ('c', 'It wears the liner and changes the split'), ('d', 'It has no effect at all')], 'c'),
        ('Why is a cyclone part of a circuit?', [('a', 'Cyclones only work alone'), ('b', 'Circuits are for painting walls'), ('c', 'Coarse material is never reused'), ('d', 'Coarse material is sent back for regrinding, so the circuit works as a whole')], 'd'),
    ],
}
