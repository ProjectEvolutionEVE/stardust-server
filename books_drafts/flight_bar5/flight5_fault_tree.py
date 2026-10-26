"""Fault Trees: a picture of how an unwanted event can come about, and which combinations are the most dangerous."""
CODE = 'flight5_fault_tree'
BOOK = {
    'title': 'Fault Trees',
    'subtitle': 'Drawing the routes to an unwanted event',
    'chapters': [
        ('A picture of failure', 'A fault tree is a diagram that starts with one unwanted event at the top. Under it, the causes are drawn as branches. It shows at a glance how the event could come about.'),
        ('The gates', 'An AND gate means every input must fail for the output to happen. An OR gate means any one input failing is enough. Most trees use only these two gates.'),
        ('Origin', 'Fault trees were developed at Bell Labs in the early 1960s for the Minuteman missile. The method spread to aerospace and to nuclear and chemical industries.'),
        ('Probabilities', 'If the chance of each basic fault is known, the chance of the top event can be worked out through the gates. This needs care: the faults must be independent, or the answer will be wrong.'),
        ('Minimal cut sets', 'A minimal cut set is the smallest group of basic faults that together cause the top event. The smallest cut sets are the weak points. Fixing them gives the greatest gain for the effort.'),
        ('Limits', 'A tree is only as complete as the person who draws it. It can miss faults nobody thought of. Use it with other methods, and update it when the design changes.'),
    ],
    'test': [
        ('What does an AND gate in a fault tree mean?', [('a', 'Any one input failing is enough'), ('b', 'The gate is always closed'), ('c', 'Every input must fail for the output to happen'), ('d', 'The gate is only a decoration')], 'c'),
        ('Where were fault trees developed?', [('a', 'At Bell Labs in the early 1960s'), ('b', 'In a school in the 1900s'), ('c', 'In a fishing port in 1980'), ('d', 'In a jewellery shop')], 'a'),
        ('What missile was fault tree analysis first used for?', [('a', 'A paper rocket'), ('b', 'A cannon from a museum'), ('c', 'A fireworks display'), ('d', 'The Minuteman missile')], 'd'),
        ('What is a minimal cut set?', [('a', 'The largest possible list of faults'), ('b', 'The smallest group of basic faults that together cause the top event'), ('c', 'A kind of saw'), ('d', 'The total cost of a project')], 'b'),
        ('Why are the smallest cut sets important?', [('a', 'They show the weak points, and fixing them gives the greatest gain'), ('b', 'They are always the least likely'), ('c', 'They can be ignored'), ('d', 'They only matter after an accident')], 'a'),
    ],
}
