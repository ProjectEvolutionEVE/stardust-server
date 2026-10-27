"""Shovel and truck economics: bucket fill, cycle times, fleet matching, productivity, costs and sizing."""
CODE = 'mining5_shovel_econ'
BOOK = {
    'title': 'Shovel and Truck Economics',
    'subtitle': 'Matching loaders and haulers so neither sits idle',
    "chapters": [
        ('The loading team', 'Shovels load trucks, and the two must be matched so that neither waits for long. Most of the cost is in keeping this team busy.'),
        ('Bucket fill', 'The bucket fill factor describes how full each bucket is. A fuller bucket means fewer passes to fill a truck.'),
        ('Cycle times', 'A truck cycle is the time to load, haul, dump and return. Shorter cycles mean more tonnes per hour.'),
        ('Matching', 'Too many trucks mean queues at the shovel. Too few mean the shovel sits idle. Good matching balances the two.'),
        ('Costs', 'Operating cost per tonne falls when productivity rises. Bigger machines cost more to buy and run, so size matters.'),
        ('Sizing', 'Equipment is sized for the haul distance, the ore and the target output. A fleet built for the wrong job wastes money every shift.'),
    ],
    "test": [
        ('What does bucket fill factor describe?', [('a', 'How many buckets the shovel owns'), ('b', 'How often the bucket is painted'), ('c', 'How full each bucket is'), ('d', 'How long the bucket takes to cool')], 'c'),
        ('What is a truck cycle?', [('a', 'Only the drive back to the workshop'), ('b', 'A shift change'), ('c', 'The time spent fuelling'), ('d', 'Load, haul, dump and return')], 'd'),
        ('What happens when there are too many trucks?', [('a', 'Queues form at the shovel'), ('b', 'The shovel gets faster'), ('c', 'The ore gets richer'), ('d', 'The trucks stop using fuel')], 'a'),
        ('What does operating cost per tonne do when productivity rises?', [('a', 'Rises'), ('b', 'Falls'), ('c', 'Stays exactly the same'), ('d', 'Becomes unmeasurable')], 'b'),
        ('What is equipment sized for?', [('a', 'The colour of the cab'), ('b', 'The number of radio channels'), ('c', 'The name of the operator'), ('d', 'The haul distance, the ore and the target output')], 'd'),
    ],
}
