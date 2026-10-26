"""Case Study: Ariane 5, 1996. A software fault that a backup could not stop."""
CODE = 'flight3a_case_ariane5'
BOOK = {
    "title": 'Case Study: Ariane 5, 1996',
    "subtitle": 'A software fault that a backup could not stop',
    "chapters": [
        ('The first flight',
         "In June 1996 the European rocket Ariane 5 made its first flight. It was a new, larger design. Parts of its flight software were reused from the earlier Ariane 4, which had flown safely for years."),
        ('Numbers that did not fit',
         "About 37 seconds after launch, a sideways speed value grew larger than the reused software had been built to handle. The software tried to store a large number in a smaller space, and the number did not fit. The computer shut down, and the error message it sent was read as flight data."),
        ('The backup failed too',
         "The rocket carried two inertial reference units, a main one and a backup. Both ran the same software, so both failed in the same way. With no good readings, the flight computer sent wild steering commands."),
        ('Self-destruct',
         "The rocket swung off course and broke apart under the strain, and its range safety system destroyed it. The loss ran into the hundreds of millions of euros, and the satellites it carried were lost too."),
        ('The lesson of a shared fault',
         "A backup helps only when it can fail in a different way. A second system that runs the same code can share the same mistake. Engineers learned to ask whether a backup is truly independent, not just a copy."),
        ('Check the limits',
         "Before reusing old code in a new craft, check each value against the new limits. Ask what happens at the edges of the range, not just in the middle. A pilot who reads the numbers carefully catches faults early."),
    ],
    "test": [
        ('Where did Ariane 5 reuse flight software from?',
         [('a', 'Its paint'), ('b', 'Its radio'), ('c', 'Its music'), ('d', 'The earlier Ariane 4')], 'd'),
        ('About how long after launch did the failure begin?',
         [('a', 'About 3 seconds'), ('b', 'About 37 seconds'), ('c', 'About 37 minutes'), ('d', 'About 3 hours')], 'b'),
        ('Why did the backup inertial unit fail too?',
         [('a', 'It was painted the same colour'), ('b', 'It was turned off on purpose'), ('c', 'Both units ran the same software and shared the same fault'), ('d', 'It never had any power')], 'c'),
        ('What is the main lesson about backups from this case?',
         [('a', 'A backup helps only when it can fail in a different way'), ('b', 'A backup should be kept in the hold'), ('c', 'Backups are always heavier'), ('d', 'Rockets never need backups')], 'a'),
        ('What is a sensible step when reusing old code in a new craft?',
         [('a', 'Trust it, because it worked before'), ('b', 'Remove all the checks'), ('c', 'Check every value against the new limits, including the edges'), ('d', 'Use only the middle of the range')], 'c'),
    ],
}
