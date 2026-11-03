"""Economics of Aids to Navigation: lighthouses and buoys, maintenance costs, public funding, traffic benefits, allocation and modernisation."""
CODE = 'navigation5_aids_economics'
BOOK = {
    "title": 'Economics of Aids to Navigation',
    "subtitle": 'Paying to keep the lights and buoys that guide ships safely',
    "chapters": [
        ('Lighthouses and buoys',
         'Aids to navigation mark safe water for ships. Lighthouses and buoys are the best-known examples, but there are many others. Each one has a job to do for the vessels that pass it.'),
        ('Maintenance costs',
         'Aids must be kept lit, upright and accurate. The costs of maintenance are steady and often easy to forget. Plan them every year, not only after a failure.'),
        ('Public funding',
         'Most aids are paid for from public funds. All shipping benefits from them, and it is hard to charge each ship fairly for the service it receives.'),
        ('Traffic benefits',
         'Safe marks reduce groundings, delays and accidents, and so help trade move smoothly. Count these benefits alongside the costs when you judge the value of an aid.'),
        ('Allocation',
         'Limited money must be shared among many aids. Rank them by how much traffic and risk each one serves, and direct the money where it protects the most people and cargo.'),
        ('Modernisation',
         'Newer systems can be cheaper to run and more reliable. Plan upgrades in stages, and keep the old marks in place until the new ones are proven.'),
    ],
    "test": [
        ('What do aids to navigation do?',
         [('a', 'Sell fuel to ships'), ('b', 'Carry cargo across the sea'), ('c', 'Build new ships'), ('d', 'Mark safe water for ships')], 'd'),
        ('Why is public funding common for aids to navigation?',
         [('a', 'Because they bring no benefit'), ('b', 'Because all shipping benefits and it is hard to charge each user'), ('c', 'Because they are private toys'), ('d', 'Because maintenance is free')], 'b'),
        ('What benefit do safe marks bring?',
         [('a', 'Fewer groundings, delays and accidents'), ('b', 'Higher paint costs'), ('c', 'More ships in the harbour automatically'), ('d', 'Lower sea levels')], 'a'),
        ('How should limited money be shared among aids?',
         [('a', 'Equal amounts with no thought'), ('b', 'Only to the biggest buoy'), ('c', 'Ranked by how much traffic and risk each one serves'), ('d', 'By the colour of each buoy')], 'c'),
        ('What is a good approach to modernisation?',
         [('a', 'Replace everything at once with no test'), ('b', 'Plan upgrades in stages and keep old marks until new ones are proven'), ('c', 'Stop all maintenance'), ('d', 'Sell the old lights')], 'b'),
    ],
}
