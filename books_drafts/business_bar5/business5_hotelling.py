"""Hotelling's Rule for Resources: digging now or later, price rising at the interest rate, scarcity rent, reserves and discoveries, the real record and recycling."""
CODE = 'business5_hotelling'
BOOK = {
    "title": "Hotelling's Rule for Resources",
    "subtitle": 'When to dig up a resource, and why its price may not simply climb',
    "chapters": [
        ('Dig now or later',
         'An owner of a mine or oil field must decide how much to take out today and how much to leave for later. Taking it now brings money sooner, but leaving it may bring a higher price later. Harold Hotelling studied this choice in a famous 1931 paper.'),
        ('Price rising at the interest rate',
         'Hotelling argued that, in an efficient market, the price of an exhaustible resource net of extraction cost should rise at the rate of interest. If it rose more slowly, owners would dig it all out now and invest the money. If it rose faster, owners would leave it in the ground.'),
        ('Scarcity rent',
         'The extra value above extraction cost is called scarcity rent. It rewards owners for leaving a resource in the ground. The rent reflects how little of the resource is left, and it grows over time in Hotelling\'s model.'),
        ('Reserves and discoveries',
         'In practice, new discoveries and better technology keep adding to reserves. Reserves are not a fixed stock, because they depend on prices and techniques. Hotelling\'s simple model does not include these changes, which is one reason real prices behave differently.'),
        ('The real record',
         'Over long periods, the real prices of many natural resources have fallen rather than risen. Better technology and new finds have pushed the supply curve out. Hotelling\'s rule is a useful guide, but the record shows that the story is complicated.'),
        ('Recycling',
         'Recycling can stretch the life of a resource, by returning metals and materials to use. Higher prices make recycling more worthwhile. Together with new finds and substitutes, recycling helps explain why scarcity has not always led to a steady price rise.'),
    ],
    "test": [
        ('In what year did Harold Hotelling publish his famous paper?',
         [('a', '1776'), ('b', '1999'), ('c', '1848'), ('d', '1931')], 'd'),
        ("What does Hotelling's rule say the net price should do in an efficient market?",
         [('a', 'Rise at the rate of interest'), ('b', 'Fall to zero at once'), ('c', 'Stay exactly the same for ever'), ('d', 'Double every day')], 'a'),
        ('What is scarcity rent?',
         [('a', 'The rent of a shop in a city'), ('b', 'The extra value above extraction cost, which rewards leaving a resource in the ground'), ('c', 'A tax on bread'), ('d', 'A fee for owning a bird')], 'b'),
        ('What do new discoveries and better technology do to reserves?',
         [('a', 'Always empty them at once'), ('b', 'Make them vanish'), ('c', 'Keep adding to them'), ('d', 'Turn them into paper')], 'c'),
        ('What does the real record show about the long-run prices of many resources?',
         [('a', 'They always double every decade'), ('b', 'They have never changed'), ('c', 'They are set by the weather only'), ('d', 'They have often fallen rather than risen')], 'd'),
    ],
}
