"""Vessel Traffic Services: Shore teams that help ships in busy waters."""
CODE = 'navigation5_vts'
BOOK = {
    'title': 'Vessel Traffic Services',
    'subtitle': 'Shore teams that help ships in busy waters',
    'chapters': [
        ('Traffic in busy waters', 'Vessel Traffic Services watch ships in busy or narrow waters. They help keep traffic moving safely.'),
        ('Reporting', 'Ships send position reports to the VTS centre at set points. These reports keep the picture of traffic up to date.'),
        ('Radar', 'VTS centres use radar and other sensors to see ships in their area. Operators watch the screens constantly.'),
        ('Pilot advice', "The VTS gives information and advice to ships. The ship's master and pilot remain responsible for their own decisions."),
        ('Regulations', 'Each port or waterway has its own rules for its VTS. These rules describe reporting points, speed limits and mandatory actions.'),
        ('Operation', 'Operators are trained to understand traffic patterns and to communicate clearly. Good operation helps prevent crowding and collisions.'),
    ],
    'test': [
        ('What do VTS centres do?', [('a', 'Bake bread'), ('b', 'Build ships'), ('c', 'Sell fish'), ('d', 'Watch ships in busy or narrow waters')], 'd'),
        ('What do ships send to a VTS?', [('a', 'Position reports at set points'), ('b', 'Recipes'), ('c', 'Music requests'), ('d', 'Holiday photos')], 'a'),
        ("Who remains responsible for a ship's decisions?", [('a', "The ship's master and pilot"), ('b', 'The VTS always'), ('c', 'The weather'), ('d', 'Nobody')], 'a'),
        ('What do VTS operators give?', [('a', 'Fuel'), ('b', 'Cargo'), ('c', 'Information and advice to ships'), ('d', 'Hot meals')], 'c'),
        ('What do local rules describe?', [('a', 'Flavours of ice cream'), ('b', 'Reporting points, speed limits and mandatory actions'), ('c', 'Sea colours'), ('d', 'Bird songs')], 'b'),
    ],
}
