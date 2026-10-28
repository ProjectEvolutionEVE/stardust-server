"""Creep Mechanisms and Deformation Maps: how metals slowly stretch under steady load, and how engineers map it."""
CODE = 'mining5_creep_mech'
BOOK = {
    "title": 'Creep Mechanisms and Deformation Maps',
    "subtitle": 'How metals slowly stretch under steady load, and how engineers map it',
    "chapters": [
        ('Slow stretching', 'Creep is the slow change in shape of a material held under steady load at high temperature. It can go on for years, even when the load is below what would break the part at once. Turbines, boilers and pipes must be designed against it.'),
        ('Diffusional creep', 'At high temperature and low stress, atoms move through the crystal or along its boundaries. Nabarro-Herring creep moves atoms through the crystal, and Coble creep moves them along the boundaries. Both are controlled by diffusion.'),
        ('Power-law creep', 'At higher stress, creep speeds up with a power of the stress, and dislocations do most of the moving. This is called power-law creep. It is the main creep mode in many engineering alloys.'),
        ('Dislocation climb', 'Dislocations can climb up and over obstacles by taking in or giving out atoms. Climb needs diffusion, so temperature matters a lot. Climb helps dislocations get past barriers that would stop them otherwise.'),
        ('Deformation maps', 'A deformation map plots stress and temperature and shows which creep mode dominates in each region. Engineers use these maps to choose the safe range for a part. The maps are built from test data.'),
        ('Design and tests', 'Creep tests run for months, sometimes years. Designers add margins to allow for creep over the life of a part. Testing shows whether the margin is enough.'),
    ],
    "test": [
        ('What is creep?', [('a', 'Slow change in shape under steady load at high temperature'), ('b', 'A quick snap under sudden force'), ('c', 'A type of paint'), ('d', 'The sound of rain')], 'a'),
        ('What drives diffusional creep?', [('a', 'Light shining on the surface'), ('b', 'Atoms moving through the crystal or along its boundaries'), ('c', 'Wind blowing past'), ('d', 'Music played near the metal')], 'b'),
        ('When does power-law creep take over?', [('a', 'Only at very low stress'), ('b', 'Only in water'), ('c', 'At higher stress, with dislocations doing most of the moving'), ('d', 'Only in the dark')], 'c'),
        ('How do dislocations climb past obstacles?', [('a', 'By flying off the metal'), ('b', 'By turning into light'), ('c', 'By freezing solid'), ('d', 'By taking in or giving out atoms, which needs diffusion')], 'd'),
        ('What does a deformation map show?', [('a', 'Which creep mode dominates for each stress and temperature'), ('b', 'The price of the metal'), ('c', 'The shape of a cloud'), ('d', 'The number of rivers')], 'a'),
    ],
}
