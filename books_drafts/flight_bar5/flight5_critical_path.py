"""Critical Path Method: finding the chain of tasks that sets the earliest finish, and the slack in the rest."""
CODE = 'flight5_critical_path'
BOOK = {
    'title': 'Critical Path Method',
    'subtitle': 'The chain of tasks that sets the end date',
    'chapters': [
        ('Where it came from', 'The critical path method was developed around 1957 by DuPont and Remington Rand engineers, as a way to plan plant shutdowns and maintenance. It has since spread to nearly every kind of project.'),
        ('Building a network', 'Draw each task as a box or node, and link it to the tasks that must come before it. The network shows which tasks depend on which. Accurate links are the foundation of the method.'),
        ('The critical path', 'The critical path is the longest chain of dependent tasks through the network. Its total length sets the earliest possible finish of the whole project. A delay on this path delays the project.'),
        ('Float', 'Float, or slack, is how long a task can be delayed without delaying the project. Tasks off the critical path have float. Tasks on it have none.'),
        ('Crashing a schedule', 'Crashing means adding resources to critical tasks to shorten them. It costs money, and the benefit may stop once another path becomes critical. Check the whole network each time.'),
        ('Use with care', 'The method is only as good as its estimates and links. Update it as work finishes. A plan that is never updated shows the wrong critical path.'),
    ],
    'test': [
        ('Roughly when was the critical path method developed?', [('a', 'Around 1857'), ('b', 'Around 1987'), ('c', 'Around 1900'), ('d', 'Around 1957')], 'd'),
        ('What is the critical path?', [('a', 'The shortest chain of tasks'), ('b', 'The longest chain of dependent tasks, which sets the earliest finish'), ('c', 'The path a crew walks'), ('d', 'A road on a map')], 'b'),
        ('What is float?', [('a', 'How long a task can be delayed without delaying the project'), ('b', 'The weight of a ship'), ('c', 'The cost of fuel'), ('d', 'A type of bridge')], 'a'),
        ('What is crashing a schedule?', [('a', 'Stopping the project for a year'), ('b', 'Removing all tasks'), ('c', 'Adding resources to critical tasks to shorten them'), ('d', 'Crashing a ship into a dock')], 'c'),
        ('Why must the network be kept up to date?', [('a', 'Because updates are required by the sun'), ('b', 'Because a plan that is never updated shows the wrong critical path'), ('c', 'Because old networks are always faster'), ('d', 'Because nobody reads them')], 'b'),
    ],
}
