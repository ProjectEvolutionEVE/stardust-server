"""Fault Trees: working backward from one bad event to the chain of causes that could lead to it."""
CODE = 'engineering3c_fault_trees'
BOOK = {
    "title": 'Fault Trees: Working Backward From a Failure',
    "subtitle": 'Drawing the chain of causes that leads to one bad event',
    "chapters": [
        ('Start at the bad event',
         "A fault tree starts from one unwanted event at the top, such as a loss of power. Ask what could cause it, and write each cause beneath. The tree grows downward until it reaches basic causes that need no further breaking down."),
        ('The AND gate',
         "An AND gate means the event above happens only if all the causes below happen together. Two things that must both fail at once make the top event less likely. Read it as this and that."),
        ('The OR gate',
         "An OR gate means the event above happens if any one of the causes below happens. Each extra OR cause makes the top event more likely. Read it as this or that."),
        ('Chances through the gates',
         "For independent causes, the chance of an AND is the product of the chances, so it becomes small very quickly. The chance of an OR is roughly the sum of the small chances, so it grows as causes are added. These rules let you estimate which causes matter most."),
        ('Finding the weak spots',
         "A cut set is a group of basic causes that together bring down the top event. The smallest cut sets show where a single failure is enough to cause the disaster. Those are the places to protect first."),
        ('Using the tree',
         "Draw the tree before you build, and update it whenever a part changes. Use it to plan tests and inspections at the weak points. A fault tree is a plan for what to watch, not only a report of what went wrong."),
    ],
    "test": [
        ('Where does a fault tree start?',
         [('a', 'At the smallest part'), ('b', 'At one unwanted event at the top'), ('c', 'At the market'), ('d', 'At the hold')], 'b'),
        ('What does an AND gate mean?',
         [('a', 'The event happens if any one cause happens'), ('b', 'The event never happens'), ('c', 'The event happens at random'), ('d', 'The event happens only if all the causes below happen together')], 'd'),
        ('What does an OR gate mean?',
         [('a', 'The event happens if any one of the causes below happens'), ('b', 'The event needs every cause to happen'), ('c', 'The event is planned'), ('d', 'The event is harmless')], 'a'),
        ('For independent causes joined by an AND gate, what happens to the chance of the top event?',
         [('a', 'It rises'), ('b', 'It equals the sum of the causes'), ('c', 'It becomes small quickly, since it is a product of chances'), ('d', 'It doubles')], 'c'),
        ('What is a cut set?',
         [('a', 'A part that has been cut'), ('b', 'A group of basic causes that together bring down the top event'), ('c', 'A saw for metal'), ('d', 'A way to fold a drawing')], 'b'),
    ],
}
