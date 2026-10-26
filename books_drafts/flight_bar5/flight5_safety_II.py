"""Safety-I and Safety-II: counting what goes wrong, and learning from what goes right."""
CODE = 'flight5_safety_II'
BOOK = {
    'title': 'Safety-I and Safety-II',
    'subtitle': 'Counting failures, and studying success',
    'chapters': [
        ('Two views of safety', 'Safety-I is the traditional view. It says safety means having as few things go wrong as possible. Safety-II, a term from Erik Hollnagel, says safety means having as many things go right as possible.'),
        ('Counting failures', 'Safety-I focuses on what failed and who was responsible. This is useful, and it has saved lives. Its limit is that it learns only from the rare bad days, not from the many good ones.'),
        ('Studying success', "Safety-II looks at how work is normally done well. It asks why an action that usually works sometimes fails, and why it usually does not. The answers show where the crew's real skill lies."),
        ('Variability', 'People and systems vary from day to day. Variability is not always a fault. Often it is how people cope with a changing world. Safety-II treats it as a resource to understand, not an error to remove.'),
        ('Learning from both', 'A good safety programme learns from accidents and from successful work. Use the incident reports, and also watch the daily work closely. Ask what the crew did to keep things safe, and write that down.'),
        ('Limits', 'Safety-II is not a reason to ignore failures. Serious events still need careful study. The aim is to use both views together, not to drop one for the other.'),
    ],
    'test': [
        ('What does Safety-I say safety means?', [('a', 'Having as many things go right as possible'), ('b', 'Having no rules'), ('c', 'Having no crew'), ('d', 'Having as few things go wrong as possible')], 'd'),
        ('Who gave the name Safety-II?', [('a', 'Galileo Galilei'), ('b', 'Erik Hollnagel'), ('c', 'Ada Lovelace'), ('d', 'Louis Pasteur')], 'b'),
        ('What does Safety-II study?', [('a', 'How work is normally done well, and why it sometimes fails'), ('b', 'Only the rarest accidents'), ('c', 'The colour of the hull'), ('d', 'Nothing that has gone right')], 'a'),
        ('How does Safety-II view variability?', [('a', 'As the cause of every problem'), ('b', 'As something that must be stopped at all costs'), ('c', 'As a resource to understand, not only an error to remove'), ('d', 'As a sign that the crew should leave')], 'c'),
        ('What is the sensible way to use both views?', [('a', 'Drop Safety-I completely'), ('b', 'Use both, and still study serious events carefully'), ('c', 'Ignore the daily work'), ('d', 'Stop writing reports')], 'b'),
    ],
}
