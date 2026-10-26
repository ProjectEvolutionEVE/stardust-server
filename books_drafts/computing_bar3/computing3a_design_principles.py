"""Software design principles: one job per part, parts that do not reach too far into each other, and each rule kept in one place."""
CODE = 'computing3a_design_principles'
BOOK = {
    "title": 'Design Principles',
    "subtitle": 'One job per part, parts that stay apart, and rules kept in one place',
    "chapters": [
        ('Why design matters',
         'A design is the plan for how the parts of a program fit together. Good design makes changes easy and safe. Poor design makes every small change touch many other places, and each one can break something new.'),
        ('One job per part',
         'Give each part of a program one clear job. A function that does one thing is easier to name, to test and to reuse. If you find yourself describing a part with "and" again and again, it may have more than one job.'),
        ('Keep a rule in one place',
         'If the same rule is written in several places, the copies drift apart. One gets fixed while the others stay wrong. Keep each rule in one place and let the rest call it. The game\'s store module works this way: every change to what a player owns goes through a few functions.'),
        ('Loose coupling',
         'Two parts are coupled when a change to one forces a change to the other. Loose coupling keeps parts apart, so each can change without breaking the rest. A clear interface between two parts is how you keep them loose.'),
        ('High cohesion',
         'Cohesion is how well the things inside one part belong together. A part with high cohesion holds related jobs. If a part holds unrelated jobs, moving some of them elsewhere makes the whole design easier to follow.'),
        ('Simple beats clever',
         'Choose the simplest design that does the job and is still easy to change. Clever tricks are hard to read later, and hard to change safely. The game\'s first principle, keep it simple and fun, works for code too.'),
    ],
    "test": [
        ('What does the one-job rule say?',
         [('a', 'Put all the code in one file'), ('b', 'Let every function do many things'), ('c', 'Use as many names as possible'), ('d', 'Give each part one clear job')], 'd'),
        ('Why keep a rule in one place?',
         [('a', 'So the rule is hidden from everyone'), ('b', 'So a copy cannot drift out of step, and a fix is made once'), ('c', 'So players can change it'), ('d', 'So the file grows larger')], 'b'),
        ('What does loose coupling mean?',
         [('a', 'Parts share every variable they have'), ('b', 'All parts are the same size'), ('c', 'Parts can change without forcing changes in the others'), ('d', 'Parts never call each other')], 'c'),
        ('What is cohesion?',
         [('a', 'How well the things inside one part belong together'), ('b', 'How many lines a part has'), ('c', 'How fast a part runs'), ('d', 'How many parts a program has')], 'a'),
        ('When is a clever trick the wrong choice?',
         [('a', 'When it is short'), ('b', 'When it is hard to read and to change later'), ('c', 'When it uses a single name'), ('d', 'Never')], 'b'),
    ],
}
