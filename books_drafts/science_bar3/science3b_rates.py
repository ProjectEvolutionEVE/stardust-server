"""Reaction Rates and Activation Energy: why reactions run fast or slow, and how a catalyst changes the path. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_rates'
BOOK = {
    "title": 'Reaction Rates and Activation Energy',
    "subtitle": 'Why reactions run fast or slow, and how a catalyst changes the path',
    "chapters": [
        ('Particles must collide',
         'For a reaction to happen, particles must collide with the right orientation and with enough energy. This idea is called collision theory. More effective collisions each second means a faster reaction.'),
        ('The energy barrier',
         'Even a reaction that releases energy overall must first climb an energy barrier. The minimum energy needed to get over it is called the activation energy. Particles that arrive with too little energy simply bounce apart.'),
        ('Heat and crowding',
         'Heating a mixture makes its particles move faster, so more of them have enough energy to clear the barrier. Raising the concentration packs more particles into the same space, so there are more collisions too.'),
        ('Surface area',
         'A fine powder reacts faster than one solid lump of the same substance, because more of its surface is exposed. More surface means more places where particles can meet. The reaction itself is the same, but its rate changes.'),
        ('A catalyst lowers the barrier',
         'A catalyst gives the reaction a new path with a lower activation energy. At a given temperature, more particles then have enough energy to react. The catalyst is not used up, so a small amount can keep working again and again.'),
        ('Catalysts in life and industry',
         "Enzymes are biological catalysts that let your body run reactions at body temperature. The iron catalyst in the Haber process speeds up the making of ammonia. The platinum, palladium and rhodium in a car's catalytic converter help turn harmful exhaust into less harmful gases."),
    ],
    "test": [
        ('What must happen for a reaction to take place?',
         [('a', 'Particles must collide with enough energy and the right orientation'), ('b', 'Particles must stop moving'), ('c', 'The temperature must fall to zero'), ('d', 'The solution must turn blue')], 'a'),
        ('What is activation energy?',
         [('a', 'The energy released when a reaction ends'), ('b', 'The minimum energy needed to get over the energy barrier'), ('c', 'The energy stored in a catalyst'), ('d', 'The energy of a gas at room temperature')], 'b'),
        ('How does a catalyst change a reaction?',
         [('a', 'It raises the activation energy'), ('b', 'It stops the reaction'), ('c', 'It lowers the activation energy by offering an easier path'), ('d', 'It is used up as the reaction runs')], 'c'),
        ('Why does a fine powder often react faster than a solid lump?',
         [('a', 'Its particles are heavier'), ('b', 'It has more surface exposed for collisions'), ('c', 'It is always hotter'), ('d', 'It contains more protons')], 'b'),
        ('Which industrial process uses an iron catalyst to make ammonia?',
         [('a', 'The Haber process'), ('b', 'Electrolysis of water'), ('c', 'Titration'), ('d', 'Filtering a solution')], 'a'),
    ],
}
