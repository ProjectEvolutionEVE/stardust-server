"""Bounded Clock Uncertainty and TrueTime: using clock error bounds to order events across the world."""
CODE = 'computing5_truetime'
BOOK = {
    "title": 'Bounded Clock Uncertainty and TrueTime',
    "subtitle": 'Using clock error bounds to order events across the world',
    "chapters": [
        ('Clocks that disagree', 'Clocks on different machines drift apart, and no two are exactly right. Instead of pretending they agree, a system can record how wrong a clock might be. That gives a time interval, not a single time.'),
        ('Clock uncertainty intervals', 'An interval is a range that the true time must fall inside. If two intervals do not overlap, the order of the events is known for sure. If they overlap, the system must wait or be careful.'),
        ('Commit wait', 'Google Spanner waits out the uncertainty before making a transaction visible. This commit wait ensures that later transactions really see later times. The wait is short because the uncertainty is kept small.'),
        ("Spanner's approach", 'Spanner uses TrueTime, an interface that returns an interval for the current time, to give external consistency. External consistency means the order seen from outside matches the true order of commits. Google described the system publicly in 2012.'),
        ('Hardware clocks', 'TrueTime relies on atomic clocks and GPS receivers in data centres to keep the uncertainty small. Machines also check each other for drift. Together these parts give a tight, known bound on error.'),
        ('Alternatives', 'Other systems use logical clocks or hybrid clocks, which avoid needing special hardware. They give a weaker order, or need more careful reasoning. Each approach trades hardware cost against precision of ordering.'),
    ],
    "test": [
        ('What does a clock uncertainty interval give?',
         [('a', 'A paint colour'), ('b', 'A memory bank'), ('c', 'A cable length'), ('d', 'A range the true time must fall inside')], 'd'),
        ('Why does commit wait happen?',
         [('a', 'To heat the machine'), ('b', 'To ensure later transactions see later times'), ('c', 'To print a receipt'), ('d', 'To close the building')], 'b'),
        ('What does external consistency mean?',
         [('a', 'Machines are the same colour'), ('b', 'Data is not stored'), ('c', 'Users must wait for a week'), ('d', 'The outside order matches the true order of commits')], 'd'),
        ('What do TrueTime systems use to keep uncertainty small?',
         [('a', 'Atomic clocks and GPS receivers'), ('b', 'Paper calendars'), ('c', 'Coloured pencils'), ('d', 'Carrier pigeons')], 'a'),
        ('What is a benefit of logical or hybrid clocks?',
         [('a', 'They avoid needing special clock hardware'), ('b', 'They are the most precise'), ('c', 'They remove all network delay'), ('d', 'They need atomic clocks')], 'a'),
    ],
}
