"""AC and DC: why most power travels as alternating current, and what direct current is still good for."""
CODE = 'engineering3b_ac_dc'
BOOK = {
    "title": 'AC and DC: Why the Grid Alternates',
    "subtitle": 'Current that flows one way, and current that keeps swinging back and forth, and why most power travels as AC',
    "chapters": [
        ('Direct and alternating',
         'Direct current, DC, flows steadily in one direction, as from a battery. Alternating current, AC, reverses direction again and again, many times a second. Mains power is AC, and most electronics convert it to DC inside.'),
        ('Frequency',
         'The rate of reversal is the frequency, measured in hertz, which means cycles per second. Mains power runs at 50 hertz in most of the world and at 60 hertz in much of the Americas. The grid must keep its frequency steady, because clocks and motors depend on it.'),
        ('Voltage in RMS',
         'AC voltage keeps rising and falling, so engineers quote a steady equivalent called the RMS voltage. Household supplies quoted as 230 volts in Europe or 120 volts in North America are RMS values. An RMS value gives the same heating as a DC supply of that same voltage.'),
        ('Why the grid is AC',
         'Power stations generate AC naturally, because a spinning magnet inside a coil makes an alternating voltage. AC can be stepped up and down easily with transformers, which steady DC cannot do. That is the main reason power grids were built on AC.'),
        ('The long-distance argument',
         'Sending power over long distances at high voltage means less current for the same power, so less energy is lost as heat in the cables. Those losses rise with the square of the current. Stepping the voltage up at the power station, and down near the users, is the economical choice.'),
        ('DC still has its place',
         'Batteries, solar panels and most electronics run on DC, and high-voltage DC lines carry power over very long distances, including under the sea. Choose AC or DC by the job, the distance and the equipment. A rectifier turns AC into DC wherever electronics need it.'),
    ],
    "test": [
        ('What does DC stand for?',
         [('a', 'Double current'), ('b', 'Direct current'), ('c', 'Distant cable'), ('d', 'Dual cell')], 'b'),
        ('What is the unit of frequency in AC power?',
         [('a', 'Watts'), ('b', 'Metres'), ('c', 'Amps'), ('d', 'Hertz')], 'd'),
        ('What is an RMS voltage?',
         [('a', 'A steady equivalent that gives the same heating as DC'), ('b', 'The highest peak the voltage ever reaches'), ('c', 'A voltage that never changes'), ('d', 'The voltage printed on a battery')], 'a'),
        ('Why are power grids built on AC?',
         [('a', 'AC never changes its voltage'), ('b', 'AC cannot be used in homes'), ('c', 'AC can be stepped up and down with transformers'), ('d', 'DC is too heavy to carry')], 'c'),
        ('Why is high voltage used for long-distance power lines?',
         [('a', 'It makes the copper heavier'), ('b', 'It adds current to the cable'), ('c', 'It stops the electricity from flowing'), ('d', 'It means less current for the same power, so less energy is lost as heat')], 'd'),
    ],
}
