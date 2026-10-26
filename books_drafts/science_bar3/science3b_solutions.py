"""Solutions and Concentration: how much solute is dissolved in a solvent, how to measure it, and how to dilute it. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_solutions'
BOOK = {
    "title": 'Solutions and Concentration',
    "subtitle": 'How much solute is dissolved in a solvent, and how to measure it',
    "chapters": [
        ('Solute and solvent',
         'A solution forms when a solute dissolves in a solvent. Salt is the solute in salt water, and water is the solvent. The result is one clear mixture, with the solute spread evenly through the solvent.'),
        ('Concentration',
         'Concentration tells you how much solute is in a set amount of solution. Chemists often use molarity, which is moles of solute per litre of solution. A one-molar solution holds one mole of solute in every litre.'),
        ('Making a solution',
         'To make a solution of a set concentration, weigh the right number of moles of solute and dissolve it. Then add water up to the mark on the flask, so the final volume is right. Measuring the water alone gives the wrong answer.'),
        ('Saturation',
         'A solvent can hold only so much solute at a given temperature. When no more will dissolve, the solution is saturated. For most solids, warming the solvent lets more dissolve. For gases it is the opposite: warm water holds less dissolved gas.'),
        ('Dilution',
         'To make a weaker solution, add more solvent. The rule C1 × V1 = C2 × V2 says the amount of solute stays the same while the volume grows. So one litre of 1-molar solution, diluted to two litres, becomes 0.5 molar.'),
        ('Labels that matter',
         'Always write the concentration on the bottle. A label that says only "salt water" tells you nothing about how strong it is. A wrong guess can ruin an experiment, or a whole batch of product.'),
    ],
    "test": [
        ('In salt water, which substance is the solvent?',
         [('a', 'Salt'), ('b', 'Water'), ('c', 'Both are solvents'), ('d', 'Neither')], 'b'),
        ('What does molarity measure?',
         [('a', 'Moles of solute per litre of solution'), ('b', 'Grams of solvent per gram of solute'), ('c', 'The temperature at which a solution boils'), ('d', 'The number of protons in a solute')], 'a'),
        ('A solution holds as much solute as it can at a given temperature. What is it called?',
         [('a', 'Diluted'), ('b', 'Neutral'), ('c', 'Saturated'), ('d', 'Ionised')], 'c'),
        ('Warm water holds more of most solids, but less of which kind of substance?',
         [('a', 'Liquids'), ('b', 'Gases'), ('c', 'Metals'), ('d', 'Crystals')], 'b'),
        ('You have 1 litre of 1-molar solution and dilute it to 2 litres. What is the new concentration?',
         [('a', '0.5 molar'), ('b', '2 molar'), ('c', '1 molar'), ('d', '4 molar')], 'a'),
    ],
}
