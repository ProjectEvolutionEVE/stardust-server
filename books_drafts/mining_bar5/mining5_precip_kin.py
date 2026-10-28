"""Precipitation Kinetics and the Avrami Equation: how fast a new phase grows inside an alloy, and how to predict it."""
CODE = 'mining5_precip_kin'
BOOK = {
    "title": 'Precipitation Kinetics and the Avrami Equation',
    "subtitle": 'How fast a new phase grows inside an alloy, and how to predict it',
    "chapters": [
        ('A new phase forms', 'In some alloys, a second phase forms as small particles inside the first. These particles can make the alloy much stronger. How fast they form is a question of kinetics.'),
        ('Nucleation and growth', 'The particles first nucleate, then grow. Both steps depend on temperature and on how far the alloy has been pushed out of balance. Fast nucleation with slow growth gives many small particles.'),
        ('Time-temperature curves', 'Engineers plot time and temperature to show how far the change has gone. These curves look like an S. Each curve is measured for a given alloy and treatment.'),
        ('Transformed fraction', 'The transformed fraction is the share of the alloy that has changed into the new phase. It rises from nothing to one over time. The Avrami equation describes that rise in a simple form.'),
        ('Models and measurements', 'The Avrami equation uses a rate constant and an exponent that depends on how the particles form. Both are found by fitting measurements. Good data make the model useful.'),
        ('Alloy design', 'Designers use kinetics to pick heat treatments that give the right particle size. Too much time or heat can coarsen the particles and reduce strength. The right schedule is found by testing.'),
    ],
    "test": [
        ('What forms inside some alloys to make them stronger?', [('a', 'Bubbles of air'), ('b', 'Pieces of paper'), ('c', 'Small particles of a second phase'), ('d', 'Drops of water')], 'c'),
        ('What are the two steps in precipitation?', [('a', 'Cooking and cutting'), ('b', 'Painting and drying'), ('c', 'Reading and writing'), ('d', 'Nucleation and growth')], 'd'),
        ('What does the transformed fraction measure?', [('a', 'The share of the alloy that has changed to the new phase'), ('b', 'The price of the alloy'), ('c', 'The length of the bar'), ('d', 'The number of workers')], 'a'),
        ('What does the Avrami equation describe?', [('a', 'The colour of a tomato'), ('b', 'The rise of the transformed fraction over time'), ('c', 'The speed of a bicycle'), ('d', 'The taste of tea')], 'b'),
        ('What happens if an alloy is heated too long?', [('a', 'The alloy turns into sugar'), ('b', 'The alloy becomes lighter air'), ('c', 'Particles coarsen and strength can drop'), ('d', 'Nothing changes ever')], 'c'),
    ],
}
