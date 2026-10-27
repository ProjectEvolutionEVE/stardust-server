"""Enrichment Ratios and Mass Balance: how much ore becomes concentrate, and how to check the sums so the numbers hold."""
CODE = 'mining5_enrich'
BOOK = {
    "title": 'Enrichment Ratios and Mass Balance',
    "subtitle": 'How much ore becomes concentrate, and how to check the sums',
    "chapters": [
        ('Upgrading', 'A mill upgrades ore by removing waste and keeping the valuable mineral. The upgrading ratio is the mass of feed divided by the mass of concentrate. A higher ratio means more of the feed was thrown away.'),
        ('Grade and yield', 'Grade is how much metal the material holds, and yield is how much of the mass of the feed ends up in the concentrate (recovery is the share of the metal). A plant can raise grade, but then yield may fall. The best choice balances the two.'),
        ('Recovery', 'Recovery is the share of the metal in the feed that ends up in the concentrate. It is the key number for the money a plant makes. A small change in recovery can change the profit a lot.'),
        ('Balance equations', 'A mass balance says that what goes in must come out: the feed equals the concentrate plus the tailings. Metal balances work the same way. Checking the balance shows whether the numbers add up.'),
        ('Plant decisions', 'Operators use the balance to decide on grinding, flotation and other settings. The balance also shows where metal is being lost. Decisions are based on the numbers, not on guesses.'),
        ('Checking sampling', 'Every balance depends on good samples. Poor sampling gives false numbers that mislead the plant. Plants check their sampling and calibrate their instruments regularly.'),
    ],
    "test": [
        ('What is the upgrading ratio?', [('a', 'The colour of the ore'), ('b', 'The mass of feed divided by the mass of concentrate'), ('c', 'The price of diesel'), ('d', 'The number of workers')], 'b'),
        ('What is grade?', [('a', 'How fast the belt moves'), ('b', 'How deep the mine is'), ('c', 'How much metal the material holds'), ('d', 'How many trucks are parked')], 'c'),
        ('What is recovery?', [('a', 'The rain that falls on a mine'), ('b', 'The number of engines in a truck'), ('c', 'The shape of the mill'), ('d', 'The share of metal in the feed that ends up in the concentrate')], 'd'),
        ('What does a mass balance say?', [('a', 'What goes in must come out'), ('b', 'Metal grows in the tank'), ('c', 'Water is always lost'), ('d', 'Balances never matter')], 'a'),
        ('Why does poor sampling matter?', [('a', 'It makes the ore sweeter'), ('b', 'It gives false numbers that mislead the plant'), ('c', 'It cools the mill'), ('d', 'It stops the trucks')], 'b'),
    ],
}
