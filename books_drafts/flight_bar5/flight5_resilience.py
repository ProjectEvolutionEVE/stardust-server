"""Resilience Engineering: how systems keep working when things change, and what that looks like in practice."""
CODE = 'flight5_resilience'
BOOK = {
    'title': 'Resilience Engineering',
    'subtitle': 'Keeping things working when the world changes',
    'chapters': [
        ('Beyond stopping failures', 'Safety is often measured by counting what went wrong. Resilience engineering asks a different question: how do people keep things working when the conditions change, and the plan does not quite fit?'),
        ('Erik Hollnagel', 'The safety researcher Erik Hollnagel helped build the field of resilience engineering. He argued that people in systems constantly adjust their work to keep it safe and effective.'),
        ('What goes right', 'Most days, nothing goes wrong, and that is no accident. Skilled crews notice small problems, adjust, and recover before they grow. Studying those everyday adjustments teaches as much as studying failure.'),
        ('Margins', 'A resilient system keeps spare capacity, such as extra fuel, extra time or a second route. These margins let it absorb a surprise. Cutting them to save cost makes the system brittle.'),
        ('Drills and practice', 'Regular drills let crews practise recovery before they need it. Good drills include surprises and differ from the scripted version. Afterwards, the crew talks about what it learned.'),
        ('Examples and limits', 'Hospital teams, air crews and ship crews often show resilience in hard moments. Resilience has limits, though. It cannot make up for poor design, poor training or too little time.'),
    ],
    'test': [
        ('What does resilience engineering ask?', [('a', 'How many faults can be counted'), ('b', 'Who can be blamed for a fault'), ('c', 'How people keep things working when conditions change'), ('d', 'How to remove all people from the system')], 'c'),
        ('Who helped build the field of resilience engineering?', [('a', 'Erik Hollnagel'), ('b', 'Isaac Newton'), ('c', 'Jane Austen'), ('d', 'Ernest Rutherford')], 'a'),
        ('What is a margin in a resilient system?', [('a', 'A line drawn on a chart'), ('b', 'A fine for late work'), ('c', 'A type of colour paint'), ('d', 'Spare capacity, such as extra fuel or time, that lets it absorb a surprise')], 'd'),
        ('What do good drills include?', [('a', 'Only scripted steps that never change'), ('b', 'Surprises, and a talk afterwards about what was learned'), ('c', 'No practice at all'), ('d', 'Only the easiest tasks')], 'b'),
        ('What is a limit of resilience?', [('a', 'It cannot make up for poor design, poor training or too little time'), ('b', 'It is always enough on its own'), ('c', 'It means nothing can go wrong'), ('d', 'It removes the need for any plan')], 'a'),
    ],
}
