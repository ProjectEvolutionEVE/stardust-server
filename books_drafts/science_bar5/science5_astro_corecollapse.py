"""Core-Collapse Supernova Mechanisms: how a massive star's iron core collapses and what turns that collapse into a bright explosion."""
CODE = 'science5_astro_corecollapse'
BOOK = {
    "title": 'Core-Collapse Supernova Mechanisms',
    "subtitle": 'How a massive star ends in a bright explosion',
    "chapters": [
        ('The iron core',
         'A massive star builds layers of heavier elements in its core, one shell at a time. Eventually the core is mostly iron. Fusing iron takes energy instead of releasing it, so the support for the core starts to fail.'),
        ('The collapse',
         'Without support, the iron core collapses in a fraction of a second. It shrinks to a dense ball of nuclear matter. The outer layers fall inward and bounce off this dense core.'),
        ('Neutrinos',
         'The newborn core releases a huge flood of neutrinos, which are nearly massless particles. Some neutrinos are absorbed by the material behind the shock wave. This heating helps push the star apart.'),
        ('Shock revival',
         'The shock wave can stall as it loses energy. If the heating is strong enough, the shock is revived and pushes outward. This revival is central to explaining how the star explodes.'),
        ('Asymmetry',
         'Many explosions are lopsided. Turbulent gas and rotation can make the blast stronger in some directions than others. Explosion asymmetry helps explain why neutron stars can get a kick.'),
        ('Types of supernova',
         'Core collapse makes Type II supernovae from massive stars that keep their hydrogen envelope. Other types come from stars that have lost much of their outer layers. Matching the types to models is a major goal.'),
    ],
    "test": [
        ('Why does an iron core lose its support?',
         [('a', 'Iron fusion releases energy, so the core swells'), ('b', 'Iron fusion absorbs energy, so the core collapses'), ('c', 'Iron is too light to hold a star'), ('d', 'Iron turns the core into ice')], 'b'),
        ('What role do neutrinos often play in these explosions?',
         [('a', 'They help push energy into the stalled shock'), ('b', 'They make the star invisible'), ('c', 'They turn the core to gold'), ('d', 'They stop all nuclear reactions')], 'a'),
        ('What is shock revival?',
         [('a', 'The shock wave is switched off'), ('b', 'The star is cooled to ice'), ('c', 'The shock wave is re-energised and pushes outward'), ('d', 'The star starts to shrink to a point')], 'c'),
        ('Which supernova type comes from a massive star that keeps its hydrogen envelope?',
         [('a', 'Type Ia'), ('b', 'A nova'), ('c', 'A comet'), ('d', 'Type II')], 'd'),
        ('Why are core-collapse explosions hard to simulate?',
         [('a', 'Many physical details interact and are hard to model fully'), ('b', 'The stars are too close to see'), ('c', 'Computers cannot store numbers'), ('d', 'The explosion is always perfectly round')], 'a'),
    ],
}
