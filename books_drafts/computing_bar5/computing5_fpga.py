"""FPGA Design: reconfigurable chips that become the circuit you describe, and what they cost to build for."""
CODE = 'computing5_fpga'
BOOK = {'title': 'FPGA Design',
 'subtitle': 'Lookup tables, place and route, timing closure and when FPGAs win',
 'chapters': [('Reconfigurable logic',
               'A field-programmable gate array is a chip full of logic blocks and wiring that can '
               'be set up again and again. A design is loaded into it like a program, and a new '
               'design can replace the old one.'),
              ('Lookup tables',
               'Most FPGA logic is built from small memories called lookup tables. Each table '
               'stores the answer for every input combination, so one table can act as any small '
               'logic function. Many of them together form a large circuit.'),
              ('Place and route',
               'The tools decide where each block sits and how the wires join them. This step is '
               'called place and route. A large design can take hours of computer time to finish.'),
              ('Timing closure',
               'Every signal must arrive before the next clock beat. Timing closure is the work of '
               'making all paths fast enough. A design that misses its timing will not run '
               'reliably, however correct its logic is.'),
              ('When FPGAs win',
               'FPGAs shine when a task needs many parallel steps, very low delay, or a special '
               'protocol that no ready-made chip handles. They are often used for prototypes and '
               'for systems that must work at the same speed every time.'),
              ('Development cost',
               'FPGA work needs skilled engineers and long tests. Per chip, an FPGA costs more '
               'than a mass-produced processor, so it pays off mainly for lower volumes or special '
               'needs.')],
 'test': [('What is an FPGA?',
           [('a', 'A type of printer'),
            ('b', 'A reconfigurable chip of logic blocks and wiring'),
            ('c', 'A sort of battery'),
            ('d', 'A kind of fabric')],
           'b'),
          ('What is a lookup table?',
           [('a', 'A table of visitors'),
            ('b', 'A dining table'),
            ('c', 'A small memory holding the answer for each input'),
            ('d', 'A spreadsheet of weather')],
           'c'),
          ('What is place and route?',
           [('a', 'Driving a car to the shop'),
            ('b', 'Moving the chip to a new room'),
            ('c', 'Writing a letter'),
            ('d', 'Deciding where blocks sit and how the wires join them')],
           'd'),
          ('What is timing closure?',
           [('a', 'Making every signal arrive before the next clock beat'),
            ('b', 'Shutting the chip down at night'),
            ('c', 'Closing a factory door'),
            ('d', 'Stopping all data')],
           'a'),
          ('When do FPGAs often make sense?',
           [('a', 'For writing letters'),
            ('b', 'For cheap mass-market phones only'),
            ('c', 'For special parallel tasks with very low delay'),
            ('d', 'For storing photos')],
           'c')]}
