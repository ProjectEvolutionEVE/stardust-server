"""The Toyota Production System: Taiichi Ohno, just in time, the seven wastes, kanban, stopping the line, and why copying it is hard."""
CODE = 'business4_toyota'
BOOK = {
    "title": 'The Toyota Production System',
    "subtitle": 'Making only what is needed, when it is needed, and stopping to fix problems at once',
    "chapters": [
        ('Taiichi Ohno',
         'Taiichi Ohno was an engineer at Toyota who developed much of its production system after the Second World War. He taught that waste is the enemy of a firm. His ideas spread widely, and the system became known around the world as lean production.'),
        ('Just in time',
         'Just in time means making and moving parts only when they are needed, in the amounts needed. Stock sits in the factory for less time, so less cash is tied up. It needs close links with reliable suppliers, because a late part stops the line.'),
        ('The seven wastes',
         'Ohno named seven kinds of waste: making too much, waiting, moving goods, over-processing, holding stock, unnecessary motion, and defects. Finding and removing them is the everyday work of the system. Each one adds cost without adding value for the customer.'),
        ('Kanban',
         'Kanban is a signal, often a card, that tells the previous step to make more. When a part is used, its card goes back and a new one is made. Kanban keeps the flow matched to demand, and stops work piling up between steps.'),
        ('Stopping the line',
         'Any worker on a Toyota line could pull a cord to stop it when a problem appeared. Stopping felt costly, but it meant the fault was fixed at once instead of being passed down the line. The rule was that quality comes first, and the line restarts only when the cause is known.'),
        ('Why copying it is hard',
         'Many firms copied the tools, such as kanban cards, and got little benefit. The system depends on trust between workers and managers, on steady training, and on a culture that values problems as a way to learn. Those things are slow to build and hard to see from outside.'),
    ],
    "test": [
        ('Who was the Toyota engineer who developed much of the production system?',
         [('a', 'Henry Ford'), ('b', 'W. Edwards Deming'), ('c', 'Taiichi Ohno'), ('d', 'Andrew Carnegie')], 'c'),
        ('What does just in time mean?',
         [('a', 'Holding a huge stock of parts for years'), ('b', 'Working only at night'), ('c', 'Setting prices every hour'), ('d', 'Making and moving parts only when they are needed, in the amounts needed')], 'd'),
        ('How many kinds of waste did Ohno name?',
         [('a', 'Seven'), ('b', 'Three'), ('c', 'Five'), ('d', 'Twelve')], 'a'),
        ('What is kanban?',
         [('a', 'A type of Japanese tea'), ('b', 'A signal, often a card, that tells the previous step to make more'), ('c', 'A bank loan'), ('d', 'A shipping ticket for the sea')], 'b'),
        ('Why did a worker stop the line when a problem appeared?',
         [('a', 'To take a long break'), ('b', 'To end the working day'), ('c', 'So the fault was fixed at once instead of passed down the line'), ('d', 'To change the company logo')], 'c'),
    ],
}
