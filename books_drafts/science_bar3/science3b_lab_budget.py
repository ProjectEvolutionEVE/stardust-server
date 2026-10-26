"""Budgeting a Chemistry Lab: costing reagents by the mole, planning for waste, and buying wisely. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_lab_budget'
BOOK = {
    "title": 'Budgeting a Chemistry Lab',
    "subtitle": 'Costing reagents by the mole, planning for waste, and buying wisely',
    "chapters": [
        ('Price per mole, not per bottle',
         'Two bottles of the same chemical can cost very different amounts for the same work. Compare them by the price per mole, found by dividing the price by the number of moles in the bottle. A cheap bottle of the wrong grade can cost more in the end.'),
        ('Purity grades',
         'Chemicals come in grades of purity. A higher grade costs more, but it may be needed for accurate work, while a cheaper grade may do for teaching. Choose the grade the experiment truly needs, and no more.'),
        ('Buy in bulk, with care',
         'Buying a large amount lowers the price per gram, but only if you will use it before it goes off. Some chemicals absorb water from the air or lose strength over time. Check the shelf life before you buy.'),
        ('Price the whole experiment',
         'Add up the reagents, the glassware that may break, the power, the waste disposal and the analysis. Disposal is often forgotten, and it can be a large part of the cost. A full budget covers every line.'),
        ('Saving for equipment',
         'A new instrument can cost far more than any one experiment. Set aside a small amount each month in a savings fund. If you borrow instead, compare the interest with the time the instrument saves, and pay the loan back on schedule.'),
        ('Track and adjust',
         'Write down what each project spends, compare it with the plan each month, and adjust. A lab that tracks its costs can say early when a budget is off track, and that leaves time to act.'),
    ],
    "test": [
        ('How should you compare two bottles of the same chemical?',
         [('a', 'By the colour of the label'), ('b', 'By the price per mole'), ('c', 'By the size of the box'), ('d', 'By the first letter of the name')], 'b'),
        ('When is a higher purity grade worth paying for?',
         [('a', 'Always, for every job'), ('b', 'Never, because it is always worse'), ('c', 'When the experiment truly needs it for accurate work'), ('d', 'Only when the chemical is a gas')], 'c'),
        ('Why is buying in bulk not always a saving?',
         [('a', 'Bulk is always more expensive'), ('b', 'Bulk bottles are illegal'), ('c', 'It makes the room too cold'), ('d', 'Chemicals can lose strength or go off before you use them')], 'd'),
        ('What is often forgotten in a lab budget?',
         [('a', 'Waste disposal'), ('b', 'The name of the experiment'), ('c', 'The colour of the notebook'), ('d', 'The date on the wall')], 'a'),
        ('How can a lab keep its budget on track?',
         [('a', 'Spend first and check at the end of the year'), ('b', 'Track each project against its plan every month and adjust'), ('c', 'Ignore the plan when experiments run late'), ('d', 'Borrow money every week')], 'b'),
    ],
}
