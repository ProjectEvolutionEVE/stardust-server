"""Membrane Separation and Desalination Chemistry: how thin barriers separate salt from water, and what limits them."""
CODE = 'science5_chem_membranes'
BOOK = {
    "title": 'Membrane Separation and Desalination Chemistry',
    "subtitle": 'Thin barriers that let water through and hold salt back',
    "chapters": [
        ('What a membrane does',
         'A membrane is a thin barrier that lets some molecules pass and holds others back. Some membranes are based on size, and others on how well a molecule dissolves into the material. Desalination membranes mostly separate water from dissolved salt.'),
        ('Reverse osmosis',
         'Normally water moves across a membrane from fresh to salty water. Reverse osmosis pushes salty water against the membrane with pressure greater than the natural osmotic pressure, so pure water is forced through and the salt stays behind.'),
        ('Selectivity',
         'A good membrane lets water pass easily while holding back ions such as sodium and chloride. Selectivity depends on the chemistry of the polymer and the size of its pores. A membrane that is too open lets salt through, while one that is too tight needs more pressure.'),
        ('Fouling',
         'Over time, particles, bacteria and minerals build up on the surface. This is called fouling, and it blocks flow and can damage the membrane. Plants reduce fouling with pre-treatment, cleaning and careful control of flow.'),
        ('Energy use',
         'Pushing water through a membrane costs energy, mostly as pressure. Modern plants recover much of the energy from the outgoing brine stream. Lower-energy membranes are a major research goal, because energy is often the largest running cost.'),
        ('Testing a membrane',
         'Engineers test a membrane by measuring water flow, salt rejection and how the performance changes over days or months. Honest testing uses real feed water, not only clean lab solutions, because real water can behave very differently.'),
    ],
    "test": [
        ('What does a membrane do?',
         [('a', 'It lets some molecules pass and holds others back'), ('b', 'It makes salt from water'), ('c', 'It heats the water to boiling'), ('d', 'It stores electricity')], 'a'),
        ('What does reverse osmosis push water against?',
         [('a', 'The open air'), ('b', 'A hot metal plate'), ('c', 'A bag of sugar'), ('d', 'A membrane, with pressure greater than natural osmotic pressure')], 'd'),
        ('What does selectivity describe?',
         [('a', 'How well a membrane lets water pass while holding back ions'), ('b', 'How loud the pump sounds'), ('c', 'How many people use the plant'), ('d', 'How bright the membrane looks')], 'a'),
        ('What is fouling?',
         [('a', 'A type of salt'), ('b', 'A pump that runs too fast'), ('c', 'A build-up on the membrane that blocks flow'), ('d', 'A clean rinse of the membrane')], 'c'),
        ('Why is energy use important in desalination?',
         [('a', 'Because membranes cannot hold water at all'), ('b', 'Because salt needs to be heated to be removed'), ('c', 'Because energy is never needed'), ('d', 'Because pressure costs energy and energy is often the largest running cost')], 'd'),
    ],
}
