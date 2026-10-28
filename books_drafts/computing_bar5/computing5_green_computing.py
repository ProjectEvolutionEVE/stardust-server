"""Energy-Efficient Computing: how much power a computer uses for each task, and the choices that save energy."""
CODE = 'computing5_green_computing'
BOOK = {'title': 'Energy-Efficient Computing',
 'subtitle': 'Power per task, idle states, voltage scaling and carbon',
 'chapters': [('Power per task',
               'Energy efficiency asks how much energy a task takes, not only how fast the '
               'computer is. A faster machine that finishes sooner can sometimes use less energy '
               'in total. Measuring the work done per watt makes the choice clear.'),
              ('Idle states',
               'When a processor has nothing to do, it can drop into low-power states. Keeping '
               'work bunched together lets the machine sleep for longer. Wasted wake-ups use '
               'energy for nothing.'),
              ('Voltage and frequency scaling',
               'Dynamic voltage and frequency scaling lowers the clock and voltage when full speed '
               'is not needed. Lower voltage saves a lot of power. The trade-off is slower work at '
               'those times.'),
              ('Data-centre efficiency',
               'Large data centres measure how much of their power reaches the computers, using a '
               'ratio called power usage effectiveness. Better cooling and power design raise this '
               'share. Small gains add up across many machines.'),
              ('Carbon accounting',
               'Carbon accounting turns energy use into emissions, which depend on how the '
               'electricity was made. The same job can have very different carbon costs at '
               'different times and places. Honest reporting names the method used.'),
              ('Software choices',
               'Software can save energy by doing less work, caching results, and avoiding '
               'needless polling. Choices like these often save more than new hardware. Developers '
               'can measure the effect with simple tools.')],
 'test': [('Why measure energy per task?',
           [('a', 'Because it sets the computer colour'),
            ('b', 'Because it shows the real cost of the work done'),
            ('c', 'Because it is the same as the price'),
            ('d', 'Because it stops the clock')],
           'b'),
          ('What does dynamic voltage and frequency scaling do?',
           [('a', 'Raises the voltage for ever'),
            ('b', 'Turns the screen blue'),
            ('c', 'Lowers voltage and clock speed when full speed is not needed'),
            ('d', 'Deletes files')],
           'c'),
          ('What does power usage effectiveness measure?',
           [('a', 'The number of staff'),
            ('b', 'The height of the building'),
            ('c', 'The number of windows'),
            ('d', 'How much of a data centre power reaches the computers')],
           'd'),
          ('What does carbon accounting depend on besides energy used?',
           [('a', 'How the electricity was made'),
            ('b', 'The colour of the rack'),
            ('c', 'The name of the engineer'),
            ('d', 'The day of the week only')],
           'a'),
          ('Which kind of software choice often saves energy?',
           [('a', 'Adding more loops that run forever'),
            ('b', 'Repeating the same calculation many times for fun'),
            ('c', 'Doing less work and avoiding needless polling'),
            ('d', 'Turning on every device at once')],
           'c')]}
