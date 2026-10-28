"""Thermal Management and Throttling: why processors slow themselves when they run too hot, and how to design around it."""
CODE = 'computing5_thermal_throttling'
BOOK = {'title': 'Thermal Management and Throttling',
 'subtitle': 'Heat limits, throttling, thermal design power and cooling',
 'chapters': [('Heat limits',
               'Every chip has a temperature it must not exceed. Heat comes from the electricity '
               'it uses. Keeping the temperature safe is part of every design.'),
              ('Throttling',
               'When a chip nears its heat limit, it lowers its clock speed to shed heat. This is '
               'throttling. The computer keeps working but more slowly.'),
              ('Thermal design power',
               'Thermal design power is a figure that tells cooling engineers how much heat a chip '
               'must be able to remove. It is a guide, not a precise limit. Real loads can exceed '
               'it for short periods.'),
              ('Boost behaviour',
               'Many chips run briefly faster, then settle to a lower sustained speed as heat '
               'builds up. Short tests can show a faster result than long real work. Honest '
               'benchmarks run for long enough to reach steady heat.'),
              ('Cooling choices',
               'Designers choose between fans, heat sinks, liquid loops and room airflow. Each '
               'choice has a cost in noise, size and money. The best choice depends on where the '
               'machine will live.'),
              ('Testing under heat',
               'Performance tests should run under the heat of real use, not only in a cool lab. A '
               'product that is fast cold but slow hot may disappoint users. Engineers test the '
               'whole range.')],
 'test': [('What happens when a chip nears its heat limit?',
           [('a', 'It turns into a light'),
            ('b', 'It may lower its clock speed to shed heat'),
            ('c', 'It gets faster for ever'),
            ('d', 'It stops keeping time')],
           'b'),
          ('What is throttling?',
           [('a', 'Joining two cables'),
            ('b', 'Locking a door'),
            ('c', 'Slowing down to reduce heat'),
            ('d', 'Printing a receipt')],
           'c'),
          ('What is thermal design power used for?',
           [('a', 'To set the price'),
            ('b', 'To pick the software language'),
            ('c', 'To choose the screen size'),
            ('d', 'To tell cooling engineers how much heat must be removed')],
           'd'),
          ('Why can a short test look faster than long real work?',
           [('a', 'Boost speeds may fade as heat builds up'),
            ('b', 'Short tests are always slower'),
            ('c', 'Long work cools the chip'),
            ('d', 'Tests change the weather')],
           'a'),
          ('What should a fair performance test include?',
           [('a', 'Only the first second of work'),
            ('b', 'Always a cold room only'),
            ('c', 'Running long enough to reach steady heat'),
            ('d', 'No measurements at all')],
           'c')]}
