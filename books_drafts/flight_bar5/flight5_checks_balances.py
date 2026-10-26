"""Checks and Independent Review: why good decisions need people who are not part of the decision."""
CODE = 'flight5_checks_balances'
BOOK = {
    'title': 'Checks and Independent Review',
    'subtitle': 'Why the safety check must sit outside the decision',
    'chapters': [
        ('Why check the checker', 'The people who make a decision often cannot see its flaws. They are too close to it. A check from someone outside the decision gives a clearer view.'),
        ('Safety boards', 'Many organisations set up a safety board that reviews major decisions and can stop a launch or a flight. Its members are chosen for their skill and their independence from the schedule.'),
        ('Two-person rules', "Some critical tasks need two people, each checking the other's work. A two-person rule stops one tired or careless person from making a fatal error alone. It costs time, and it is worth the cost for the most dangerous jobs."),
        ('Independence', 'A check is only as good as its independence. If the reviewer answers to the person who made the decision, the review may bend to please. Give reviewers a line of report that runs outside the project.'),
        ('Audits', 'An audit looks back at what was done and compares it with the rules and with the plan. Audits find gaps that daily work hides. Their findings should be followed up, not filed away.'),
        ('The cost of checks', 'Checks take time and money, and they can slow a project. A good leader keeps them proportionate: heavy checks for the risks that could kill or ruin, light checks for small ones.'),
    ],
    'test': [
        ('Why should a decision be checked by someone outside it?', [('a', 'Because outsiders always know more'), ('b', 'Because checks are free'), ('c', 'Because decisions never need review'), ('d', 'Because the people who made it are often too close to see its flaws')], 'd'),
        ('What can a safety board do?', [('a', 'Hire new crew for the bar'), ('b', 'Review major decisions and stop a launch or flight if needed'), ('c', 'Set the price of fuel'), ('d', 'Choose the colour of the ship')], 'b'),
        ('What is a two-person rule for?', [('a', 'Stopping one person from making a dangerous error alone'), ('b', 'Splitting the pay in two'), ('c', 'Making every task take twice as long for no reason'), ('d', 'Keeping two bosses in the same room')], 'a'),
        ('What makes a check truly independent?', [('a', 'The reviewer answers to the person who made the decision'), ('b', 'The reviewer is chosen by the decision maker'), ('c', "The reviewer's report runs outside the project"), ('d', 'The reviewer never speaks to anyone')], 'c'),
        ('How should the cost of checks be judged?', [('a', 'The same heavy check for every task'), ('b', 'Heavy checks for risks that could kill or ruin, light checks for small ones'), ('c', 'No checks at all, to save time'), ('d', 'Only checks that cost nothing')], 'b'),
    ],
}
