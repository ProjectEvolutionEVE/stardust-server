"""Internal Cost Allocation: sharing the cost of common platforms between teams fairly, and tracking who uses what."""
CODE = 'computing4_internal_chargeback'
BOOK = {
    "title": 'Internal Cost Allocation',
    "subtitle": 'Sharing the cost of common platforms between teams fairly',
    "chapters": [
        ('Shared platform costs',
         'Many teams use the same servers, networks and tools. The bill for these shared platforms belongs to the whole company. Without a method, the cost ends up in one central budget, and nobody sees who drives it.'),
        ('Allocation keys',
         'An allocation key is the rule used to split a shared cost, such as by number of users, by storage used or by share of compute. A good key tracks what people really consume. Keys should be simple enough to explain and check.'),
        ('Showback versus chargeback',
         'Showback shows each team what it uses, without moving money. Chargeback moves the cost into each team’s budget. Showback is a gentle start that builds awareness. Chargeback changes behaviour more strongly, so it needs trust first.'),
        ('Fairness between teams',
         'Fair allocation avoids penalising a team for a cost it cannot control. Discuss the method openly before using it. A rule that seems fair on paper can feel unfair in practice, so review it with the teams affected.'),
        ('Tagging resources',
         'Tagging means labelling each server, storage item or service with its owner and purpose. Good tags make allocation possible. Untagged resources become a shared mystery, and they are often the first thing to cut.'),
        ('Governance',
         'Name an owner for the allocation method, and review it each year. Record each decision and why it was made. Clear governance keeps the method stable, so teams can plan around it.'),
    ],
    "test": [
        ('What is an allocation key?',
         [('a', 'A key to the office door'), ('b', 'A password for the printer'), ('c', 'A type of server cable'), ('d', 'The rule used to split a shared cost between teams')], 'd'),
        ('What is the difference between showback and chargeback?',
         [('a', 'Showback is paid in cash, chargeback is free'), ('b', 'Showback shows usage without moving money, chargeback moves the cost'), ('c', 'They are the same thing'), ('d', 'Showback is only for lawyers')], 'b'),
        ('Why tag resources with an owner and purpose?',
         [('a', 'So the resources can be hidden'), ('b', 'So the tags can be sold'), ('c', 'So cost can be allocated to the people who use them'), ('d', 'So the servers run faster')], 'c'),
        ('Why discuss an allocation method before using it?',
         [('a', 'Because a method that seems fair on paper may feel unfair in practice'), ('b', 'Because discussion is never useful'), ('c', 'Because methods are secret'), ('d', 'Because money cannot be allocated')], 'a'),
        ('What does good governance for allocation include?',
         [('a', 'No written records at all'), ('b', 'A named owner and a yearly review'), ('c', 'Changing the method every day'), ('d', 'Keeping all costs in secret')], 'b'),
    ],
}
