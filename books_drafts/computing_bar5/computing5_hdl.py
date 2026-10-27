"""Hardware Description Languages: describing circuits in code and catching errors before they are built."""
CODE = 'computing5_hdl'
BOOK = {'title': 'Hardware Description Languages',
 'subtitle': 'Signals, clocks, simulation, synthesis and testbenches',
 'chapters': [('Describing circuits in code',
               'A hardware description language describes what a circuit does, using signals and '
               'rules. The description can be simulated before any chip exists. Verilog and VHDL '
               'are the two best-known examples.'),
              ('Signals and clocks',
               'Signals carry values from place to place in a circuit. Many designs step forward '
               'on a clock, a steady beat that tells each part when to update. Getting the timing '
               'of signals right is central to the design.'),
              ('Simulation versus synthesis',
               'Simulation runs the description to see what it does. Synthesis turns the same '
               'description into real logic gates. Some code simulates well but cannot be built, '
               'so designers keep to a style that does both.'),
              ('Testbenches',
               'A testbench is a program that feeds a design test inputs and checks its outputs. '
               'Good testbenches try normal use and unusual cases. They catch many mistakes before '
               'fabrication.'),
              ('Errors caught early',
               'A bug found in simulation costs minutes to fix. The same bug found in a '
               'manufactured chip can cost months and a great deal of money. This is why most '
               'effort goes into checking before the build.'),
              ('Reuse and style',
               'Engineers write reusable blocks with clear interfaces, so each block can be tested '
               'alone. Clear style makes teams faster and reduces the chance of hidden errors.')],
 'test': [('What does a hardware description language describe?',
           [('a', 'The taste of coffee'),
            ('b', 'How a circuit behaves, which can be simulated'),
            ('c', 'The weather at a factory'),
            ('d', 'Music on a radio')],
           'b'),
          ('What is a clock used for in a circuit?',
           [('a', 'To show the time on a wall'),
            ('b', 'To heat the chip'),
            ('c', 'To tell the parts when to update'),
            ('d', 'To store the password')],
           'c'),
          ('What does synthesis do?',
           [('a', 'It deletes the description'),
            ('b', 'It prints a poster'),
            ('c', 'It plays a sound'),
            ('d', 'It turns the description into real logic gates')],
           'd'),
          ('What is a testbench?',
           [('a', 'A program that feeds a design inputs and checks outputs'),
            ('b', 'A table in a kitchen'),
            ('c', 'A kind of memory chip'),
            ('d', 'A bench in a park')],
           'a'),
          ('Why do designers catch bugs in simulation?',
           [('a', 'Because simulation makes the chip bigger'),
            ('b', 'Because bugs cannot be fixed later'),
            ('c', 'Because a bug fixed before the build costs far less'),
            ('d', 'Because the clock is turned off')],
           'c')]}
