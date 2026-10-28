"""Cell-Based Architecture: splitting a service into isolated cells, so a fault stays inside one cell and does not spread everywhere."""
CODE = 'computing5_cell_architecture'
BOOK = {
    "title": 'Cell-Based Architecture',
    "subtitle": 'Isolated cells that keep a failure small',
    "chapters": [
        ('What a cell is',
         'A cell is a complete, self-contained copy of a service stack that serves a share of the users. Each cell has its own compute, storage and dependencies. Cells are designed to work without the others.'),
        ('Isolation and blast radius',
         "Blast radius is the number of users a failure can harm. When faults stay inside one cell, the blast radius is limited to that cell's users. Smaller cells mean smaller failures."),
        ('Cell routing',
         'A router decides which cell serves each user, usually by a stable identifier. Routing must be simple and reliable, because a failure in the router can affect every cell. Moving a user between cells needs a careful process.'),
        ('Capacity per cell',
         'Each cell must have enough capacity for its users, with room for peaks. Adding cells adds capacity in steps. Planning sizes the cells so that losing one can be absorbed by the rest.'),
        ('Migration',
         'Moving an existing system into cells is a large project. Teams usually start by routing a small share of traffic to the first new cell. The move is then expanded as confidence grows.'),
        ('Operations',
         "Operators need dashboards and runbooks that show each cell's health. Deployments can be staged cell by cell, so a bad release reaches only a few users first. Practice drills help teams respond when a cell fails."),
    ],
    "test": [
        ('What is a cell in cell-based architecture?',
         [('a', 'A battery for a phone'), ('b', 'A cell in a spreadsheet only'), ('c', 'A self-contained copy of a service stack serving a share of users'), ('d', 'A prison room')], 'c'),
        ('What is blast radius?',
         [('a', 'The number of users a failure can harm'), ('b', 'The size of a firework'), ('c', 'The speed of a network cable'), ('d', 'The weight of a server')], 'a'),
        ('Why must the cell router be simple and reliable?',
         [('a', 'Routers never fail'), ('b', 'Routers only print reports'), ('c', 'Routers do not handle users'), ('d', 'A failure in the router can affect every cell')], 'd'),
        ('How are deployments often staged in a cell design?',
         [('a', 'All at once to every user'), ('b', 'Cell by cell, so a bad release reaches only a few users first'), ('c', 'Only on paper'), ('d', 'Only at midnight on the moon')], 'b'),
        ("Why plan each cell's capacity with room to spare?",
         [('a', 'So cells never need to be measured'), ('b', 'So cells can hold more paper'), ('c', 'So the rest can absorb the users of a lost cell'), ('d', 'So cells are always empty')], 'c'),
    ],
}
