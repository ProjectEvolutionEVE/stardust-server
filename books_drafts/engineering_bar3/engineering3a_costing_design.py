"""Costing a Design: adding up what a design really costs, and what each choice does to the price."""
CODE = 'engineering3a_costing_design'
BOOK = {
    "title": 'Costing a Design',
    "subtitle": 'How to add up what a design really costs, and what each choice does to the price',
    "chapters": [
        ('Start with a cost list',
         'Costing a design starts with a list. Write down each material, its mass, its price per kilogram, each hour of machining or assembly, and the cost of testing. Add lines for the drawings and the prototype. A list with every line visible is easier to check than a single total.'),
        ('Mass drives material cost',
         'For a material bought by weight, its cost is the mass multiplied by the price per kilogram. A lighter part costs less to make from the same material. A lighter material may cost more per kilogram, though, so compare the full cost of each option.'),
        ('Time is money too',
         'Labour counts even when no credits change hands. Estimate the hours for each step, including setting up tools, fitting and any rework. A design that needs careful hand work costs more in time than one built from standard parts.'),
        ('Trade-offs',
         'Every design balances cost, weight, strength and time. A stronger alloy may let you cut weight, but it may cost more to buy and to machine. Write each trade-off down, with the figure it changes, so the choice can be checked later.'),
        ('Running cost',
         'A cheap motor that wastes more power can cost more over its life than a dearer, efficient one. Estimate the energy each unit uses over its working life and add it to the purchase price. Count upkeep and replacement parts as well, as the costing book for a build explains.'),
        ('Allow for surprises',
         'Real builds run over, because a part fails a test or a price rises. Many planners add a contingency, a sum set aside for the unexpected. Keep the contingency visible on the list, and report what was spent against it.'),
    ],
    "test": [
        ('What is the material cost of a part bought by weight?',
         [('a', 'Its mass divided by its colour'), ('b', 'Its mass multiplied by its price per kilogram'), ('c', 'Its length plus its height'), ('d', 'Its price per tooth')], 'b'),
        ('Why compare the total cost of each option, not just the price per kilogram?',
         [('a', 'Because prices per kilogram never change'), ('b', 'Because kilograms are not a unit of mass'), ('c', 'Because only the heaviest option can be bought'), ('d', 'Because a material dearer per kilogram can still be cheaper overall, if less of it is needed')], 'd'),
        ("When does labour count toward a design's cost?",
         [('a', 'Only on weekends'), ('b', 'Only when a loan is taken'), ('c', 'Even when no credits change hands'), ('d', 'Never')], 'c'),
        ('A cheap motor wastes more power than a dearer one. Why might it cost more over its life?',
         [('a', 'Its energy use over the years adds to its true cost'), ('b', 'It cannot be fitted to a frame'), ('c', 'It has fewer wires'), ('d', 'It is always the lightest choice')], 'a'),
        ('What is a contingency in a cost list?',
         [('a', 'The name of a material'), ('b', 'A sum set aside for the unexpected'), ('c', 'A type of gear'), ('d', 'The final price of a finished part')], 'b'),
    ],
}
