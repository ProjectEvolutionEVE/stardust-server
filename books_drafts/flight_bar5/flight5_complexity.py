"""Complexity and Accidents: why tightly linked, complicated systems fail in ways nobody planned for."""
CODE = 'flight5_complexity'
BOOK = {
    'title': 'Complexity and Accidents',
    'subtitle': 'Why some systems are bound to surprise us',
    'chapters': [
        ('A surprising kind of failure', 'Some accidents happen because several small things go wrong at once, in a way no one imagined. The sociologist Charles Perrow studied these events and called them normal accidents.'),
        ("Perrow's book", "Perrow's book Normal Accidents, published in 1984, argued that some high-risk systems are so complex and tightly linked that accidents are almost certain over time. The fault is in the design, not only in the people."),
        ('Tight coupling', 'A system is tightly coupled when one part affects the next quickly, with little slack. Things happen fast, and there is little room to recover. Loose coupling leaves time and space for a fix.'),
        ('Interactive complexity', 'A system is interactively complex when its parts interact in unexpected ways, and when the operators cannot see all of them at once. Warning signs can look like normal behaviour.'),
        ('Examples', 'Nuclear plant accidents and chemical plant disasters are often cited as examples. In each case, a chain of small and separate faults combined in a way the designers had not expected.'),
        ('Design responses and critics', 'Designers can add slack, clear displays and simple controls. Some critics argue that Perrow was too pessimistic, and that good training and safety culture can reduce the risk a great deal. Both views teach a useful lesson.'),
    ],
    'test': [
        ('What did Charles Perrow call accidents that come from complex systems?', [('a', 'Lucky accidents'), ('b', 'Normal accidents'), ('c', 'Small accidents'), ('d', 'Silent accidents')], 'b'),
        ('In which year was Normal Accidents published?', [('a', '1972'), ('b', '1999'), ('c', '2008'), ('d', '1984')], 'd'),
        ('What does tight coupling mean?', [('a', 'Parts are wrapped in cloth'), ('b', 'Every part works alone'), ('c', 'One part affects the next quickly, with little room to recover'), ('d', 'The system never changes')], 'c'),
        ('What makes a system interactively complex?', [('a', 'Its parts can interact in unexpected ways that are hard to see all at once'), ('b', 'It has only one part'), ('c', 'It is always painted in bright colours'), ('d', 'It is never used')], 'a'),
        ('What is a sensible design response to complexity?', [('a', 'Remove every warning light'), ('b', 'Make every link faster and tighter'), ('c', 'Hide the system from the crew'), ('d', 'Add slack, clear displays and simple controls')], 'd'),
    ],
}
