"""Budgeting a Field Season: planning the crew, camp, fuel, drilling and cash for a season of exploration."""
CODE = 'mining4_field_season'
BOOK = {
    "title": 'Budgeting a Field Season',
    "subtitle": 'Crew, camp, fuel, drilling and the cash to get through a season',
    "chapters": [
        ('Crew and camp',
         'A field season needs a crew, food, shelter and transport. Each person and each camp day is a cost, and the budget starts by counting them. Remote sites often cost more than home sites.'),
        ('Fuel and aircraft',
         'Vehicles, generators and aircraft burn fuel, and aircraft hours are often the largest single cost. Prices can change during a season, so the budget allows for it.'),
        ('Drilling contracts',
         'Drilling is usually bought from a contractor by the metre or by the day. The contract should say what is included, such as moving the rig and handling core samples.'),
        ('Contingency',
         'A contingency is a reserve for things nobody can fully predict, such as bad weather or a lost part. Planners often set aside a percentage of the total budget for it.'),
        ('Cash timing',
         'Costs come before results. Crews must be paid and fuel bought long before samples are assayed. The cash plan must show when money goes out, not only the total.'),
        ('Reporting results',
         'Funders and partners expect a report of what was spent and what was found. Good records of costs and results make the next season easier to fund.'),
    ],
    "test": [
        ('What is usually the largest single cost in some field seasons?',
         [('a', 'Pencils'), ('b', 'Maps of the town'), ('c', 'Aircraft hours and fuel'), ('d', 'Flags')], 'c'),
        ('What is a contingency in a budget?',
         [('a', 'A reserve for things that cannot be fully predicted'), ('b', 'A gift to the sponsor'), ('c', 'A payment for the old office'), ('d', 'A fine for lateness')], 'a'),
        ('What does a drilling contract usually charge by?',
         [('a', 'The colour of the drill'), ('b', 'The weight of the cook'), ('c', 'The number of birds'), ('d', 'The metre or the day')], 'd'),
        ('Why does cash timing matter in a field season?',
         [('a', 'Money never leaves the bank'), ('b', 'Costs come before results, so money must be ready early'), ('c', 'Results always come first'), ('d', 'Fuel is free')], 'b'),
        ('Why report what was spent and found?',
         [('a', 'Reports are only for decoration'), ('b', 'Reports stop the rain'), ('c', 'Funders and partners expect it, and it helps the next season'), ('d', 'Reports replace the crew')], 'c'),
    ],
}
