"""Redundancy: backup parts that wait, share the work or vote on the answer."""
CODE = 'engineering3c_redundancy'
BOOK = {
    "title": 'Redundancy: Backups That Take Over',
    "subtitle": 'Spare parts that wait, share the work or vote on the answer',
    "chapters": [
        ('Why have a spare',
         "Redundancy means having more than one way to do a job, so one failure does not stop the whole system. A spare pump, a second power line and a backup computer are all examples. Redundancy costs money and space, so it is used where a failure would be serious."),
        ('Cold and hot standby',
         "A cold standby sits switched off until the main part fails. It stays fresh, but it takes time to start. A hot standby runs all the time and takes over at once, though it wears as well. Choose between them by how fast the switch-over must be."),
        ('Sharing the load',
         "In a load-sharing system, several parts work together. If one fails, the rest carry more of the work. Engineers must check that the survivors can cope, or the next failure follows quickly. A spare that cannot take the full load is not a real backup."),
        ('Voting',
         "Three independent units can vote on an answer, and the two that agree win. This is called two-out-of-three voting. If one unit gives a wrong answer, the other two outvote it, so the system keeps working correctly."),
        ('The common-cause problem',
         "Two backups built to the same design can fail together for one shared reason, such as the same bug, the same heat or the same flaw in a batch of parts. This is a common-cause failure, and it defeats redundancy. Use different designs, separate power feeds and separate places where you can."),
        ('Testing the backup',
         "A backup that is never tested may not work when it is needed. Switch it over on a schedule and check that it takes the load. Write each test in the records, so you know the backup is real."),
    ],
    "test": [
        ('What is redundancy?',
         [('a', 'Making a part heavier'), ('b', 'Painting spare parts red'), ('c', 'Having more than one way to do a job, so one failure does not stop the whole system'), ('d', 'Removing all backups')], 'c'),
        ('What is a cold standby?',
         [('a', 'A backup that sits switched off until the main part fails'), ('b', 'A backup that runs at full power all the time'), ('c', 'A backup kept in a freezer'), ('d', 'A backup that is never used at all')], 'a'),
        ('In a load-sharing system, what must engineers check?',
         [('a', 'The paint'), ('b', 'The colour of the spare'), ('c', 'Only the cost of the parts'), ('d', 'That the surviving parts can carry the full load')], 'd'),
        ('How does two-out-of-three voting work?',
         [('a', 'Two units vote on lunch'), ('b', 'Three independent units vote on an answer, and the two that agree win'), ('c', 'Three units vote on the price'), ('d', 'Each unit votes on its own colour')], 'b'),
        ('Why can two backups with the same design fail together?',
         [('a', 'They may share one cause, such as the same flaw or the same heat, which is a common-cause failure'), ('b', 'They are always too far apart'), ('c', 'Backups never fail'), ('d', 'Two backups are always stronger than one')], 'a'),
    ],
}
