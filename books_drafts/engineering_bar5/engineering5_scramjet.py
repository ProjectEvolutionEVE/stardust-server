"""Ramjet and Scramjet Propulsion: inlet compression, supersonic combustion, thrust against drag, and the flight envelope."""
CODE = 'engineering5_scramjet'
BOOK = {'title': 'Ramjet and Scramjet Propulsion',
 'subtitle': 'Air-breathing engines, supersonic combustion, and the flight envelope',
 'chapters': [('Breathing the air',
               'A ramjet and a scramjet take their oxygen from the air they fly through, so they carry no '
               'oxidiser. The forward speed of the craft compresses the incoming air. Fuel is added and '
               'burned, and the hot gas leaves through a nozzle to push the craft forward.'),
              ('The ramjet',
               'A ramjet slows the incoming air to subsonic speed before the combustor. It works well at '
               'high supersonic speeds, but its compression falls off at very high speed. Subsonic burning '
               'is the reason a ramjet needs a slower inlet.'),
              ('The scramjet',
               'A scramjet keeps the air supersonic all the way through the combustor. Burning in supersonic '
               'flow is hard, because the fuel must mix and burn in a very short time. The gain is that the '
               'engine can work at speeds where a ramjet is no longer efficient.'),
              ('Thrust against drag',
               'Thrust must beat drag for the craft to accelerate. An air-breathing engine produces thrust '
               'only when the net force from the inlet, the combustor and the nozzle is forward. At some '
               'speed the drag and the losses rise to meet the thrust, and the margin shrinks.'),
              ('The flight envelope',
               'The flight envelope is the set of speeds and heights where the engine produces enough net '
               'thrust to work. A scramjet usually needs an extra engine to reach its starting speed, '
               'because it cannot produce useful thrust from rest. Designers plan the whole path through '
               'this envelope.'),
              ('Cost and risk',
               'Scramjet engines are tested in ground facilities and in short flight tests. The cost of the '
               'tests and the risk of failure are high, so the field advances slowly. Each step is judged by '
               'what it teaches and what it costs.')],
 'test': [('What does a ramjet or scramjet use as its oxidiser?',
           [('a', 'A tank of liquid oxygen'),
            ('b', 'Water from the sea'),
            ('c', 'Oxygen from the air it flies through'),
            ('d', 'Sunlight')],
           'c'),
          ('What does a ramjet do to incoming air before the combustor?',
           [('a', 'It slows the air to subsonic speed'),
            ('b', 'It freezes the air'),
            ('c', 'It turns the air into water'),
            ('d', 'It sends the air away')],
           'a'),
          ('What is special about a scramjet?',
           [('a', 'It works only at rest'),
            ('b', 'It uses no fuel'),
            ('c', 'It keeps the air supersonic through the combustor'),
            ('d', 'It is powered by a windmill')],
           'c'),
          ('When does an air-breathing engine give useful thrust?',
           [('a', 'When the craft is parked'),
            ('b', 'When the net force from the engine is forward'),
            ('c', 'When it is sinking'),
            ('d', 'When the lights go out')],
           'b'),
          ('What is the flight envelope?',
           [('a', 'A type of cargo bag'),
            ('b', 'A paint colour'),
            ('c', 'The shape of the cabin'),
            ('d', 'The set of speeds and heights where the engine gives enough net thrust')],
           'd')]}
