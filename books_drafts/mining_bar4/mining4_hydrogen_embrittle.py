"""Hydrogen Embrittlement: how hydrogen atoms weaken steel, and how engineers prevent cracks that grow over time."""
CODE = 'mining4_hydrogen_embrittle'
BOOK = {
    "title": 'Hydrogen Embrittlement',
    "subtitle": 'How hydrogen weakens steel, and how it is prevented',
    "chapters": [
        ('Hydrogen atoms in steel',
         'Hydrogen atoms are very small, so they can enter the crystal of steel. They can come from water, rust, acid cleaning or welding. Once inside, they can move through the metal.'),
        ('Traps',
         'Hydrogen gathers at defects in the steel, such as grain boundaries, inclusions and voids. These spots are called traps, and hydrogen held there can build up to harmful levels.'),
        ('Delayed cracking',
         'Under sustained stress, hydrogen can help cracks grow slowly, sometimes hours or days after loading. The part can fail without warning, which is why this damage is hard to spot.'),
        ('Pipeline and tank steels',
         'Pipelines, high-pressure tanks and high-strength bolts can all be at risk. Their steel must be chosen and processed with hydrogen in mind, especially where hydrogen is present in service.'),
        ('Prevention',
         'Engineers reduce the hydrogen source, limit the hardness of high-strength steel, and use barrier coatings. After plating, parts are often baked at a low temperature to drive hydrogen out.'),
        ('Testing',
         'Tests load a specimen slowly in a hydrogen environment and watch for cracks. A notched sample shows how easily cracks start. The results help set safe limits for each steel.'),
    ],
    "test": [
        ('Why can hydrogen atoms enter steel?',
         [('a', 'They are as large as bricks'), ('b', 'They are made of glass'), ('c', 'They are very small'), ('d', 'They are always frozen')], 'c'),
        ('What are traps in steel?',
         [('a', 'Defects such as grain boundaries where hydrogen gathers'), ('b', 'Metal boxes for storage'), ('c', 'Fishing nets'), ('d', 'Holes made on purpose for bolts')], 'a'),
        ('What is delayed cracking?',
         [('a', 'Cracks that are painted over at once'), ('b', 'Cracks that close by themselves at once'), ('c', 'A type of weld'), ('d', 'Cracks that grow slowly under sustained stress, sometimes long after loading')], 'd'),
        ('Which steel parts are at risk from hydrogen?',
         [('a', 'Paper clips only'), ('b', 'Pipelines, high-pressure tanks and high-strength bolts'), ('c', 'Ceramic cups'), ('d', 'Glass windows')], 'b'),
        ('What is a common way to prevent hydrogen damage?',
         [('a', 'Soaking parts in sugar water'), ('b', 'Leaving parts in direct sun'), ('c', 'Baking parts after plating to drive hydrogen out'), ('d', 'Hammering parts flat')], 'c'),
    ],
}
