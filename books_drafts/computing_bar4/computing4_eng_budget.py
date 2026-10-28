"""Budgeting an Engineering Team: planning people, tools and projects, and reviewing spending each quarter."""
CODE = 'computing4_eng_budget'
BOOK = {
    "title": 'Budgeting an Engineering Team',
    "subtitle": 'Planning people, tools and projects, and reviewing spending each quarter',
    "chapters": [
        ('Headcount and tools',
         'The two largest parts of an engineering budget are people and tools. Headcount is the number of people paid, including their pay, benefits and equipment. Tools include licences, cloud services and test systems. Both need a plan.'),
        ('Project and run costs',
         'Project costs build something new and end when it is finished. Run costs keep existing systems working, and continue every month. Mixing them hides the true cost of keeping things alive, so keep them separate.'),
        ('Contingency',
         'Plans always change. A contingency is money set aside for unplanned work, such as an urgent fix or a new regulation. A common approach is to hold a modest share back, and to explain how it is used.'),
        ('Quarterly review',
         'Review spending every quarter against the plan. Ask what was delivered, what changed and what the next quarter needs. Quarterly reviews catch overspend early, while there is still time to adjust.'),
        ('Cost per feature',
         'Dividing spending by the number of features delivered can show how efficient the team is. The number is rough, because features differ in size. Use it to ask questions, not to set targets that encourage small, trivial features.'),
        ('Communicating budgets',
         'Explain the budget in plain terms that the business understands. Show what each amount buys, and what would happen if it were cut. A clear story builds support and avoids surprise cuts.'),
    ],
    "test": [
        ('What are the two largest parts of an engineering budget?',
         [('a', 'Office snacks and posters'), ('b', 'People and tools'), ('c', 'Travel and parking'), ('d', 'Paper and pens')], 'b'),
        ('What is a run cost?',
         [('a', 'A fee for a marathon'), ('b', 'A bonus for speed'), ('c', 'A cost paid once at launch only'), ('d', 'A cost that keeps existing systems working each month')], 'd'),
        ('What is contingency money for?',
         [('a', 'Unplanned work, such as an urgent fix'), ('b', 'Buying new chairs for the boss'), ('c', 'Paying for holidays in advance'), ('d', 'Printing the annual report')], 'a'),
        ('Why review spending every quarter?',
         [('a', 'To avoid all planning'), ('b', 'To change the company name'), ('c', 'To catch overspend early while there is time to adjust'), ('d', 'To stop the team working')], 'c'),
        ('Why is cost per feature only a rough measure?',
         [('a', 'It is always exact'), ('b', 'It cannot be calculated'), ('c', 'Features are never delivered'), ('d', 'Features differ greatly in size')], 'd'),
    ],
}
