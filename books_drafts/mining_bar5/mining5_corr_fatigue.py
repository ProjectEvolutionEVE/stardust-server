"""Corrosion Fatigue: how repeated loads and a wet or chemical environment together shorten a metal's life."""
CODE = 'mining5_corr_fatigue'
BOOK = {
    "title": 'Corrosion Fatigue',
    "subtitle": "How repeated loads and a harsh environment shorten a metal's life",
    "chapters": [
        ('Two attacks at once', 'Corrosion fatigue happens when a metal is under repeated loads and a corrosive environment at the same time. The combined damage is worse than either alone. Parts such as pump shafts, ships and offshore structures face it.'),
        ('Environment and cycles', 'The environment can lower the number of cycles a part can take before it fails. Even mild corrosion can have a large effect on life. The speed of the cycles and the chemistry both matter.'),
        ('Pits as starters', 'Corrosion often makes small pits in the surface. A pit can act as a notch where a crack begins. Once the crack starts, it can grow with each load cycle.'),
        ('Crack speed', 'Cracks grow faster in a corrosive environment than in dry air. The growth depends on the chemistry and on the stress range. Engineers measure this speed for each material and environment.'),
        ('Aluminium alloys', 'Some aluminium alloys are sensitive to corrosion fatigue, especially in salt water. Protective coatings and careful design help limit the damage. Choice of alloy is part of the design.'),
        ('Tests and life', 'Tests use controlled loads and chemistry to measure life. Results help estimate how long a part will last in service. Designers add margin for the harshest likely conditions.'),
    ],
    "test": [
        ('What happens in corrosion fatigue?', [('a', 'A metal is painted once'), ('b', 'Repeated loads and a corrosive environment act together'), ('c', 'A metal freezes in a day'), ('d', 'A metal is polished by sand')], 'b'),
        ('What can a corrosion pit act as?', [('a', 'A pocket of gold'), ('b', 'A window for light'), ('c', 'A notch where a crack can start'), ('d', 'A seat for a bird')], 'c'),
        ('How does a corrosive environment affect crack growth?', [('a', 'Cracks stop growing'), ('b', 'Cracks turn into metal'), ('c', 'Cracks have no effect'), ('d', 'Cracks grow faster than in dry air')], 'd'),
        ('Which kind of parts face corrosion fatigue?', [('a', 'Ships, pump shafts and offshore structures'), ('b', 'Paper cups'), ('c', 'Cotton socks'), ('d', 'Glass windows only')], 'a'),
        ('Why do designers add margin?', [('a', 'To make parts heavier for fun'), ('b', 'To allow for the harshest likely conditions'), ('c', 'To hide the test results'), ('d', 'To avoid testing at all')], 'b'),
    ],
}
