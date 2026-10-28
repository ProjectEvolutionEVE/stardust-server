"""Total Cost of Ownership: adding up every cost of a system over its life, not only the price on the invoice."""
CODE = 'computing4_tco'
BOOK = {
    "title": 'Total Cost of Ownership',
    "subtitle": 'Adding up every cost over the life of a system, not only the price on the invoice',
    "chapters": [
        ('Direct and hidden costs',
         'Direct costs are the bills you can see, such as licences and servers. Hidden costs include training, integration, downtime and the time staff spend on upkeep. A cheap price can hide expensive costs later.'),
        ('Time horizons',
         'Choose a time horizon, such as three or five years, and cost everything across it. A short horizon favours options with low upfront cost. A long horizon shows the true cost of maintenance and upgrades.'),
        ('Staff costs',
         'People are often the largest cost of a system. Count the hours to set up, operate, support and change it. A tool that saves money on licences but doubles the hours of a skilled engineer may cost more overall.'),
        ('Licences and support',
         'Licence fees and support contracts often rise over time. Check renewal terms, price increases and what support actually covers. Include them in every year of the horizon, not only the first.'),
        ('Comparing options fairly',
         'Compare options on the same scope, the same horizon and the same assumptions about load. Include the cost of leaving, such as migration and data export. An unfair comparison can point confidently in the wrong direction.'),
        ('Sensitivity checks',
         'Change the main assumptions, such as growth in users or the cost of staff, and see how the answer moves. If a small change flips the decision, the choice is fragile. Share the sensitivity results so that the decision is clear to everyone.'),
    ],
    "test": [
        ('What does total cost of ownership add up?',
         [('a', 'Only the first invoice'), ('b', 'The number of office chairs'), ('c', 'Only the colour of the logo'), ('d', 'Every cost of a system over its life')], 'd'),
        ('Which is a hidden cost?',
         [('a', 'The licence price printed on the invoice'), ('b', 'Downtime and the time staff spend on upkeep'), ('c', 'The rent of the building'), ('d', 'The price of a pen')], 'b'),
        ('Why does the time horizon matter?',
         [('a', 'It changes the weather'), ('b', 'It sets the name of the product'), ('c', 'It decides which costs are counted over the period'), ('d', 'It stops all upgrades')], 'c'),
        ('What is a sensitivity check?',
         [('a', 'Changing key assumptions to see whether the answer flips'), ('b', 'Testing the screen brightness'), ('c', 'Checking the password strength'), ('d', 'Counting the cups of tea')], 'a'),
        ('Why include the cost of leaving a system?',
         [('a', 'Because leaving is always free'), ('b', 'Because migration and export are real costs of the choice'), ('c', 'Because leaving never happens'), ('d', 'Because it reduces the staff cost to zero')], 'b'),
    ],
}
