"""The Mole: Counting by the Batch: why chemists count atoms in moles, and how to turn grams into moles. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_mole'
BOOK = {
    "title": 'The Mole: Counting by the Batch',
    "subtitle": 'Why chemists count atoms by the batch, and how to turn grams into moles',
    "chapters": [
        ('Atoms are too small to count',
         'A single atom is far too small to weigh or count by hand. So chemists count in batches. The batch they use is the mole, which is a fixed number of particles, just as a dozen is always twelve.'),
        ("Avogadro's number",
         "One mole holds about 6.022 × 10²³ particles. That number is called Avogadro's number. It is so large that no one could count it one by one, so chemists measure out a mole by weighing it instead."),
        ('Molar mass',
         'Each element has a molar mass: the mass of one mole of its atoms, in grams. Carbon is about 12 grams per mole, and oxygen about 16. A compound adds up its parts, so water, H2O, is about 18 grams per mole.'),
        ('Grams to moles',
         'To turn grams into moles, divide by the molar mass. So 36 grams of water is 2 moles, because each mole weighs about 18 grams. To go the other way, multiply the moles by the molar mass to get grams.'),
        ('Counting in the minerals',
         'Every mineral in the game has a formula, and the formula gives its molar mass. So the amount of each element in a sample can be worked out in moles or in grams. Rule 27 uses the same arithmetic when it says how much metal a pure ore gives.'),
        ('Why this matters for buying',
         'A recipe written in moles tells you how much of each substance to buy. If you know the molar mass and the price, you can work out what a mole costs. This is one of the most useful habits in any chemistry lab.'),
    ],
    "test": [
        ('What is a mole?',
         [('a', 'A kind of mineral'), ('b', 'A fixed number of particles, about 6.022 × 10²³'), ('c', 'A unit of temperature'), ('d', 'A type of atom')], 'b'),
        ('What is the molar mass of an element?',
         [('a', 'Its mass in one atom'), ('b', 'Its volume at room temperature'), ('c', 'Its charge'), ('d', 'The mass of one mole of its atoms, in grams')], 'd'),
        ('About how many grams is one mole of water, H2O?',
         [('a', 'About 18'), ('b', 'About 2'), ('c', 'About 16'), ('d', 'About 36')], 'a'),
        ('How do you turn grams into moles?',
         [('a', 'Multiply by the molar mass'), ('b', 'Divide by the molar mass'), ('c', 'Add the number of protons'), ('d', 'Take the square root')], 'b'),
        ('Why do chemists count atoms in moles instead of one by one?',
         [('a', 'Atoms cannot be weighed'), ('b', 'Moles are the only unit the game allows'), ('c', 'Atoms are too small and too many to count one at a time'), ('d', 'Atoms only come in batches of two')], 'c'),
    ],
}
