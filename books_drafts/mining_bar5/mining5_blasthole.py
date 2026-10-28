"""Blasthole drilling economics: bit life, hole diameter, drilling rates, pattern design and cost trade-offs."""
CODE = 'mining5_blasthole'
BOOK = {
    'title': 'Blasthole Drilling Economics',
    'subtitle': 'Weighing drill speed, bit life and hole size against blast quality',
    "chapters": [
        ('Why drill', 'Blastholes are drilled and loaded with explosives to break rock for loading. Drilling is one of the largest and most visible costs of a surface mine.'),
        ('Bit life', 'Drill bits wear faster in hard rock. Changing bits takes time, so bit life matters to the cost per metre.'),
        ('Hole diameter', 'Bigger holes drill more rock per hole but need bigger rigs and more explosive per hole. Smaller holes give finer control.'),
        ('Drilling rate', 'Drilling rate is measured in metres per hour. Faster drilling lowers the cost per metre, as long as the bits last.'),
        ('Pattern design', 'The spacing and burden of the holes set how well the rock breaks and how fine the fragments are. A good pattern saves both energy and wear.'),
        ('Trade-offs', 'Planners balance drill speed, bit life, hole size and blast quality. The aim is the lowest cost per tonne delivered to the mill.'),
    ],
    "test": [
        ('What are blastholes for?', [('a', 'Carrying water to the crew'), ('b', 'Venting the air from the shaft'), ('c', 'Breaking rock so it can be loaded'), ('d', 'Holding the rail tracks')], 'c'),
        ('Why does bit life matter to cost?', [('a', 'Bits are free to replace'), ('b', 'Changing bits takes time'), ('c', 'Bits never wear out'), ('d', 'Bits make the rock harder')], 'b'),
        ('What is drilling rate measured in?', [('a', 'Kilograms per shift'), ('b', 'Litres per day'), ('c', 'Volts per hour'), ('d', 'Metres per hour')], 'd'),
        ('What do hole spacing and burden set?', [('a', 'How well the rock breaks'), ('b', 'The price of the drill'), ('c', 'The colour of the rig'), ('d', 'The number of workers')], 'a'),
        ('What do planners balance to find the lowest cost?', [('a', 'Paint, lights and radios'), ('b', 'Crew names and shift hours'), ('c', 'Truck colours and tyre brands'), ('d', 'Drill speed, bit life, hole size and blast quality')], 'd'),
    ],
}
