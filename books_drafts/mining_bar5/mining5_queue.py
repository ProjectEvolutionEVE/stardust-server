"""Queueing theory for shovels and trucks: arrivals, service, waiting, fleet size, simulation and dispatch."""
CODE = 'mining5_queue'
BOOK = {
    'title': 'Queueing Theory for Shovels and Trucks',
    'subtitle': 'Why trucks wait at the shovel, and how to plan so they wait less',
    "chapters": [
        ('Lines form', 'Trucks arrive at a shovel to be loaded. A queue forms when they arrive faster than they can be served.'),
        ('Arrivals and service', 'Arrivals are how often trucks come to the shovel. Service time is how long one loading takes.'),
        ('Waiting time', 'When a queue forms, trucks wait. Waiting time grows quickly as the shovel gets busier.'),
        ('Fleet size', 'Queueing theory helps choose how many trucks to run, so the shovel stays busy without long waits. Too few trucks leave the shovel idle, and too many add to the queue.'),
        ('Simulation', 'Computer simulation checks many mixes of trucks and shovels before any equipment is bought. A simulation shows the likely waiting time for each mix before any money is spent.'),
        ('Dispatch', 'Dispatch systems send each truck to the shovel with the shortest queue. This cuts waiting time.'),
    ],
    "test": [
        ('When do queues form at a shovel?', [('a', 'When the shovel is painted'), ('b', 'When trucks arrive faster than they can be served'), ('c', 'When the shift starts'), ('d', 'When the sun comes up')], 'b'),
        ('What is service time?', [('a', 'The hours spent on paperwork'), ('b', 'The time to drive to the office'), ('c', 'The length of a lunch break'), ('d', 'How long one loading takes')], 'd'),
        ('How does waiting time change as the shovel gets busier?', [('a', 'It falls'), ('b', 'It stays exactly the same'), ('c', 'It grows quickly'), ('d', 'It disappears')], 'c'),
        ('What can dispatch systems do?', [('a', 'Send trucks to the shortest queue'), ('b', 'Shorten the shift'), ('c', 'Paint the trucks'), ('d', 'Switch off the radios')], 'a'),
        ('What can simulation check before equipment is bought?', [('a', 'Many mixes of trucks and shovels'), ('b', 'The colour of each tyre'), ('c', 'The name of the mine'), ('d', 'The weather next year')], 'a'),
    ],
}
