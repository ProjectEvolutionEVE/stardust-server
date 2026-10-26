"""Acids, Bases and pH: how strong or weak a solution is, on a scale from 0 to 14. Science career, bar 2 (Scientist)."""
CODE = 'science2_acids'
BOOK = {
    "title": 'Acids, Bases and pH',
    "subtitle": 'How strong or weak a solution is, on a scale from 0 to 14',
    "chapters": [
        ('Acids and bases',
         'An acid is a substance that gives hydrogen ions, written H+, when it is dissolved in water. A base takes hydrogen ions up, and in water it gives hydroxide ions instead. Lemon juice and vinegar are acids, and baking soda and soap are bases.'),
        ('The pH scale',
         'pH measures how many hydrogen ions a solution has. The scale runs from 0 to 14. Below 7 is acidic, 7 is neutral like pure water, and above 7 is basic. Each whole step on the scale is a tenfold change.'),
        ('Why the scale is logarithmic',
         'Because each step is tenfold, a solution at pH 3 has ten times as many hydrogen ions as one at pH 4, and a hundred times as many as one at pH 5. Small numbers on the pH scale can hide very big differences.'),
        ('Neutralisation',
         'When an acid meets a base, the two cancel out each other\'s strength. They make water and a salt. Adding vinegar to baking soda fizzes, because the reaction releases carbon dioxide gas.'),
        ('Indicators',
         'Some dyes change colour with pH, so they show whether a solution is acidic or basic. Litmus turns red in acid and blue in base. Red cabbage juice works too: it is red in acid and turns green or yellow in base.'),
        ('Strong and weak',
         'A strong acid, such as hydrochloric acid, splits almost completely in water. A weak acid, such as the acetic acid in vinegar, splits only partly. Strength is about how far an acid splits, not how much of it you have. Strong acids can burn skin, so wear gloves and eye protection.'),
    ],
    "test": [
        ('What is the pH of pure water?',
         [('a', '0'), ('b', '7'), ('c', '14'), ('d', '10')], 'b'),
        ('How much more acidic is a solution at pH 3 than one at pH 5?',
         [('a', 'Twice as acidic'), ('b', 'Ten times as acidic'), ('c', 'A hundred times as acidic'), ('d', 'One step less acidic')], 'c'),
        ('What does an acid and a base make when they neutralise each other?',
         [('a', 'Only gas'), ('b', 'Pure gold'), ('c', 'Two new acids'), ('d', 'Water and a salt')], 'd'),
        ('What colour does litmus paper turn in a base?',
         [('a', 'Red'), ('b', 'Blue'), ('c', 'Green'), ('d', 'White')], 'b'),
        ('What is the real difference between a strong acid and a weak acid?',
         [('a', 'Strong acids are always more concentrated'), ('b', 'Weak acids have no hydrogen ions'), ('c', 'Strong acids split almost fully in water, weak acids only partly'), ('d', 'Strong acids are always colourless')], 'c'),
    ],
}
