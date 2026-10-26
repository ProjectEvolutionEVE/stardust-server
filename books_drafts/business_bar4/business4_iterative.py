"""Working in Short Cycles: waterfall against iteration, the Agile manifesto, sprints, feedback, small batches, and where each approach fits."""
CODE = 'business4_iterative'
BOOK = {
    "title": 'Working in Short Cycles',
    "subtitle": 'Why many teams now build in small steps with frequent feedback',
    "chapters": [
        ('Waterfall against iteration',
         'The waterfall approach moves through fixed stages, from requirements to design to build to testing, with each stage finished before the next begins. Iterative work instead builds the product in rounds, each one adding something usable and checking it with real users.'),
        ('The Agile manifesto',
         'In 2001 a group of software developers wrote the Agile Manifesto. It valued individuals and interactions, working software, customer collaboration and responding to change, above more rigid processes and documents. The ideas spread beyond software to many other fields.'),
        ('Sprints',
         'A sprint is a short, fixed period of work, often two to four weeks. At its start the team picks a set of tasks, and at its end it shows a working result. Regular sprints create a steady rhythm and a clear point to review progress.'),
        ('Feedback',
         'Short cycles bring feedback sooner, from users, testers and colleagues. Problems found early are cheaper to fix than those found at the end of a long project. Each round also tells the team what to change in the next one.'),
        ('Small batches',
         'Working in small batches means handling less work at once. Smaller batches move through the system faster, reveal problems sooner and reduce the cost of changing course. The idea is closely linked to lean thinking.'),
        ('Where it fits',
         'Short cycles suit work where needs change, or where the end result is hard to specify in advance. Fixed stages can suit projects with firm rules, known designs and little room for change, such as building a bridge to a set plan. Many teams mix the two.'),
    ],
    "test": [
        ('What does the waterfall approach do?',
         [('a', 'Builds in very small rounds with no plan'), ('b', 'Avoids all testing'), ('c', 'Uses no written requirements'), ('d', 'Moves through fixed stages, each finished before the next begins')], 'd'),
        ('In what year was the Agile Manifesto written?',
         [('a', '2001'), ('b', '1971'), ('c', '1991'), ('d', '2011')], 'a'),
        ('What is a sprint?',
         [('a', 'A race between two companies'), ('b', 'A short, fixed period of work that ends with a working result'), ('c', 'A yearly budget review'), ('d', 'A type of bank loan')], 'b'),
        ('Why does early feedback help?',
         [('a', 'It removes the need for any users'), ('b', 'It makes all work finish on one day'), ('c', 'Problems found early are usually cheaper to fix'), ('d', 'It stops change requests')], 'c'),
        ('What do small batches reveal?',
         [('a', 'That no work is ever done'), ('b', 'That the team should stop working'), ('c', 'That deadlines are never needed'), ('d', 'Problems sooner and with less cost to change course')], 'd'),
    ],
}
