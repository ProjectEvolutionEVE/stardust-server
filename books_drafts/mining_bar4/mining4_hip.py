"""Hot Isostatic Pressing: high gas pressure and high heat that close hidden pores inside a part."""
CODE = 'mining4_hip'
BOOK = {
    "title": 'Hot Isostatic Pressing',
    "subtitle": 'Gas pressure and heat that close the pores inside a part',
    "chapters": [
        ('Pressure from every side',
         'Hot isostatic pressing, often called HIP, puts a part in a sealed vessel. Inert gas, usually argon, is pushed in at high pressure and the part is heated at the same time. The pressure is the same from every direction.'),
        ('Closing hidden pores',
         'Under heat and pressure the metal inside the part softens and flows. Internal pores shrink and bond shut. Because the pressure is even, the part keeps its shape.'),
        ('Repairing castings',
         'Castings often have hidden shrinkage pores. HIP can close them and raise the strength and fatigue life of the part. This is a common reason to use it on cast turbine parts.'),
        ('Turbine and aerospace parts',
         'Parts for jet engines and other demanding uses are often given HIP treatment. A smaller number of pores means more reliable parts that can take higher loads for longer.'),
        ('Equipment and cost',
         'HIP needs a large and expensive pressure vessel and careful gas handling. The cycle takes many hours. The cost is justified when a part is expensive or when its failure would be serious.'),
        ('Quality control',
         'Makers check HIP parts by measuring density, testing samples and using X-ray or other inspection. Process records of pressure, temperature and time are kept for every batch.'),
    ],
    "test": [
        ('What does HIP stand for in metalwork?',
         [('a', 'High iron processing'), ('b', 'Heated industrial paint'), ('c', 'Hot isostatic pressing'), ('d', 'Hard ingot polishing')], 'c'),
        ('What does HIP do to internal pores?',
         [('a', 'Closes them so the part is denser'), ('b', 'Makes them larger'), ('c', 'Moves them to the surface'), ('d', 'Fills them with water')], 'a'),
        ('Which gas is commonly used inside the HIP vessel?',
         [('a', 'Chlorine'), ('b', 'Hydrogen sulfide'), ('c', 'Steam'), ('d', 'Argon')], 'd'),
        ('Why is HIP often used on castings?',
         [('a', 'Castings are always too light'), ('b', 'Castings often hide shrinkage pores that HIP can close'), ('c', 'Castings cannot be heated'), ('d', 'Castings never break')], 'b'),
        ('Why is the cost of HIP usually justified?',
         [('a', 'Because it is cheap to run'), ('b', 'Because it removes the need for inspection'), ('c', 'Because the part is expensive or its failure would be serious'), ('d', 'Because it paints the part')], 'c'),
    ],
}
