"""Budgeting for a Fleet: planning the money for a set of craft, from the fixed lines to the surprises."""
CODE = 'flight5_m_budget_fleet'
BOOK = {
    'title': 'Budgeting for a Fleet',
    'subtitle': 'Planning the money for a set of craft',
    'chapters': [
        ('What a budget is', 'A budget is a plan for money coming in and going out over a set period. It turns your goals into numbers. A good budget is reviewed, not just written once.'),
        ('Fixed and variable costs', 'Fixed costs stay the same whatever you do, such as insurance or a yearly licence. Variable costs rise and fall with use, such as fuel and repairs. Keep them in separate lines so you can see which part you control.'),
        ('Per-craft costs', 'Work out what one craft costs to run for an hour or a week. Add the share of shared costs, such as the hangar. Then you can see whether a job pays for the craft that does it.'),
        ('Contingency', 'Set aside a contingency, a share of the budget kept for surprises. A common rule is to hold back a fixed share for the unknown. Spending it should need a reason written down.'),
        ('Variance', 'Variance is the gap between the budget and what really happened. Look at it each month. A small gap is normal; a steady gap shows the plan needs changing.'),
        ('A yearly review', 'Review the whole budget once a year. Ask what changed, which costs have grown, and whether the plan still fits the goals. Adjust the plan rather than hide the difference.'),
    ],
    'test': [
        ('What is a budget?', [('a', 'A list of songs'), ('b', 'A plan for money in and out over a set period'), ('c', 'A type of fuel'), ('d', 'A map of the stars')], 'b'),
        ('Which of these is a fixed cost?', [('a', 'Fuel used on a run'), ('b', 'Repairs after a hard landing'), ('c', 'Parts used in a job'), ('d', 'A yearly licence')], 'd'),
        ('What is a contingency?', [('a', 'A fee paid to a bank'), ('b', 'A bonus for the crew'), ('c', 'A share of the budget kept for surprises'), ('d', 'The first estimate ever made')], 'c'),
        ('What is variance?', [('a', 'The gap between the budget and what really happened'), ('b', 'A type of colour'), ('c', 'The number of crew'), ('d', 'The distance to a planet')], 'a'),
        ('Why keep fixed and variable costs on separate lines?', [('a', 'So the budget is longer'), ('b', 'So costs can be hidden'), ('c', 'So fixed costs never change'), ('d', 'So you can see which part you control')], 'd'),
    ],
}
