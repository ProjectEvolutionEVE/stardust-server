"""Turbocharger Matching and Boost Control: compressor maps, turbine maps, wastegates, boost response, and matching to an engine."""
CODE = 'engineering5_turbo_match'
BOOK = {'title': 'Turbocharger Matching and Boost Control',
 'subtitle': 'Compressor and turbine maps, wastegates, boost response, and matching to the engine',
 'chapters': [('What a turbocharger does',
               'A turbocharger uses the exhaust gas to spin a turbine, which drives a compressor that forces '
               'more air into the engine. More air lets the engine burn more fuel and make more power. The '
               'turbo is a clever use of waste energy.'),
              ('Compressor and turbine maps',
               'A compressor map plots pressure ratio against flow, and shows where the compressor works '
               'well. A turbine map does the same for the turbine. Engineers use both maps to pick a turbo '
               'that works in the right place for the engine.'),
              ('The wastegate',
               'A wastegate is a valve that lets some exhaust bypass the turbine. Opening it limits the '
               'boost, and closing it lets the turbine work harder. The wastegate protects the engine from '
               'too much pressure.'),
              ('Boost response',
               'Boost response is how quickly the turbo builds pressure after the driver asks for power. A '
               'small turbine spins up quickly but may run out of flow at high power. A large turbine gives '
               'more top power but responds more slowly.'),
              ('Matching to the engine',
               'The turbo must match the engine size, speed and exhaust flow. A poor match wastes energy, '
               'runs the compressor in the wrong place, or overheats the exhaust. Engineers check the match '
               'on the maps and on the test bench.'),
              ('Balance of cost and gain',
               'A bigger turbo costs more and adds weight, but it may gain power. Each step is checked '
               'against its cost, its life and the engine goals. The best match is the one that gives the '
               'needed power with the least loss.')],
 'test': [('What drives the compressor of a turbocharger?',
           [('a', 'A battery in the cabin'),
            ('b', 'A fan on the roof'),
            ('c', 'A bicycle pedal'),
            ('d', 'A turbine turned by the exhaust gas')],
           'd'),
          ('What does a compressor map show?',
           [('a', 'The seating plan'),
            ('b', 'The route to the Sun'),
            ('c', 'Pressure ratio against flow, and where the compressor works well'),
            ('d', 'The paint colours')],
           'c'),
          ('What is a wastegate?',
           [('a', 'A valve that lets some exhaust bypass the turbine'),
            ('b', 'A door to the hold'),
            ('c', 'A seat belt'),
            ('d', 'A fuel pump')],
           'a'),
          ('What does boost response mean?',
           [('a', 'How loud the horn is'),
            ('b', 'How many wheels there are'),
            ('c', 'How quickly the turbo builds pressure after power is asked for'),
            ('d', 'How heavy the cargo is')],
           'c'),
          ('What happens with a poor turbo match?',
           [('a', 'Power always rises for free'),
            ('b', 'Energy is wasted and the compressor may run in the wrong place'),
            ('c', 'Nothing changes at all'),
            ('d', 'The engine turns into paint')],
           'b')]}
