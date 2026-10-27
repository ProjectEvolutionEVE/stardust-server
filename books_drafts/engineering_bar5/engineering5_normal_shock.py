"""Normal Shock Waves and Rankine-Hugoniot: shock jump conditions, entropy rise, total pressure loss, and supersonic inlet design."""
CODE = 'engineering5_normal_shock'
BOOK = {'title': 'Normal Shock Waves and Rankine-Hugoniot',
 'subtitle': 'Jump conditions, entropy rise, and what a shock costs an inlet',
 'chapters': [('A sudden wall of compression',
               'A normal shock is a thin wave, perpendicular to the flow, where gas that is moving faster '
               'than sound drops to slower-than-sound speed in a tiny distance. Across the wave the '
               'pressure, density and temperature all jump up at once. The wave is so thin that engineers '
               'treat it as a single surface.'),
              ('The jump conditions',
               'The Rankine-Hugoniot equations tie the gas before the shock to the gas after it. They come '
               'from the conservation of mass, momentum and energy across the wave. Knowing the speed before '
               'the shock gives you every property after it.'),
              ('Entropy rises',
               'The second law of thermodynamics says entropy cannot fall in an isolated process, and a '
               'shock is a real irreversible process. Entropy rises across the wave, and the flow loses '
               'useful energy as heat. The gas gets hotter while the usable part of its energy shrinks.'),
              ('Total pressure loss',
               'Total pressure is the pressure the gas would reach if it were brought to rest without '
               'losses. The total pressure falls across a normal shock, and the fall grows quickly as the '
               'flow gets faster. This loss is the main price of a shock in an engine.'),
              ('Designing a supersonic inlet',
               'A supersonic inlet slows air down before it reaches the engine. A normal shock at the front '
               'is simple but wastes total pressure, so designers try to slow the air with weaker waves '
               'first. The engineering target is to keep the total pressure as high as the mission allows.'),
              ('Why it matters to the whole craft',
               'A poorly placed shock can push the inlet into an unstable mode, where the flow pulses in and '
               'out. A good design keeps the shock where it belongs for every flight speed. The shock is a '
               'cost to manage, not a flaw to hide.')],
 'test': [('What is a normal shock?',
           [('a', 'A wave parallel to the flow'),
            ('b', 'A thin wave perpendicular to the flow'),
            ('c', 'A slow breeze'),
            ('d', 'A cooling fan')],
           'b'),
          ('Which three laws of conservation are used in the jump conditions?',
           [('a', 'Colour, weight and time'),
            ('b', 'Speed, sound and light'),
            ('c', 'Charge, voltage and current only'),
            ('d', 'Mass, momentum and energy')],
           'd'),
          ('What happens to entropy across a normal shock?',
           [('a', 'It falls to zero'),
            ('b', 'It stays exactly the same always'),
            ('c', 'It rises, since the process is irreversible'),
            ('d', 'It turns into electricity')],
           'c'),
          ('What happens to total pressure across a normal shock?',
           [('a', 'It falls'),
            ('b', 'It rises sharply'),
            ('c', 'It becomes exactly zero'),
            ('d', 'It never changes')],
           'a'),
          ('Why do supersonic inlet designers try to avoid a single strong normal shock at the front?',
           [('a', 'It makes the craft lighter'),
            ('b', 'It stops the engine from burning fuel'),
            ('c', 'It wastes total pressure'),
            ('d', 'It makes the air colder')],
           'c')]}
