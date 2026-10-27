"""Edge Computing Architecture: computing near users, data placement, syncing to the core, offline operation and device fleets."""
CODE = 'computing5_edge_architecture'
BOOK = {
    "title": 'Edge Computing Architecture',
    "subtitle": 'Computing near the people and machines that use it',
    "chapters": [
        ('Computing near the user',
         'Edge computing runs processing close to where data is made or used, such as a phone, a shop, a factory floor or a cell tower. It is a response to the fact that distant data centres add delay to every round trip.'),
        ('Why place matters',
         'Each trip to a far-off server takes time. Processing nearby can shorten the wait and cut the amount of data that must cross long networks. The gain is largest for tasks that need an answer right away.'),
        ('Where data lives',
         'Some data is best kept local, for reasons of speed, cost or privacy. A good design decides what stays at the edge, what is copied back to the core, and what is only summarised before it travels.'),
        ('Syncing to the core',
         'Edge sites and the central core must agree in the end. Teams choose how often to sync and what happens when two sites change the same record at the same time. Those choices shape how the whole system behaves.'),
        ('Working offline',
         'An edge site may lose its connection. It should keep working on its own, queue its changes and send them once the link returns. A system that stops whenever the network drops is badly designed for the edge.'),
        ('Managing many devices',
         'A fleet of edge devices needs remote updates, renewed security certificates, health checks and a quick way to replace failed hardware. Doing these by hand at each site does not scale.'),
    ],
    "test": [
        ('What is edge computing?',
         [('a', 'Computing only in one giant central data centre'), ('b', 'Computing placed close to where data is made or used'), ('c', 'Computing done on paper'), ('d', 'A type of computer keyboard')], 'b'),
        ('What is the main benefit of processing near the user?',
         [('a', 'Less delay and less data sent across long networks'), ('b', 'Higher electricity bills'), ('c', 'No need for any security'), ('d', 'Permanent storage of every file')], 'a'),
        ('What must a design decide about data at the edge?',
         [('a', 'The colour of the device case'), ('b', 'How many people use the site'), ('c', 'What stays local, what is copied to the core, and what is summarised'), ('d', 'Whether to remove the power supply')], 'c'),
        ('What should an edge site do when its network link is lost?',
         [('a', 'Stop working until someone visits in person'), ('b', 'Delete all of its data'), ('c', 'Keep working locally, queue its changes, and sync when the link returns'), ('d', 'Send everything by postal mail')], 'c'),
        ('Which need comes with a large fleet of edge devices?',
         [('a', 'Remote updates, certificates and health checks'), ('b', 'No need for any management'), ('c', 'Only paper manuals'), ('d', 'One shared password kept for life')], 'a'),
    ],
}
