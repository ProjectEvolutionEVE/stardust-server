"""Air Data and Air Data Computers: How an aircraft knows its speed and height from air pressure."""
CODE = 'navigation5_air_data'
BOOK = {
    'title': 'Air Data and Air Data Computers',
    'subtitle': 'How an aircraft knows its speed and height from air pressure',
    'chapters': [
        ('Air pressure tells the story', 'An aircraft senses the pressure of the air around it. From those pressures, the air data computer works out speed and height.'),
        ('Pitot and static', 'A pitot tube measures total pressure, from air hitting its front opening. Static ports measure the pressure of the undisturbed air around the aircraft.'),
        ('Computing airspeed', 'The difference between total and static pressure gives the dynamic pressure. The computer uses it to calculate airspeed.'),
        ('Altitude', 'Static pressure gives pressure altitude, which the computer converts into height. Pressure settings from the weather can adjust the reading.'),
        ('Corrections', 'Position errors, air temperature and the shape of the aircraft all affect the readings. The computer applies corrections so the numbers are accurate.'),
        ('Calibration', 'Pitot and static systems are tested and calibrated regularly. Blocked or leaking lines can cause wrong readings, so checks matter.'),
    ],
    'test': [
        ('What does a pitot tube measure?', [('a', 'Sea temperature'), ('b', 'Engine noise'), ('c', 'Total pressure'), ('d', 'Wind colour')], 'c'),
        ('What do static ports measure?', [('a', 'Still air pressure around the aircraft'), ('b', 'Cabin music'), ('c', 'Ground speed only'), ('d', 'Ocean depth')], 'a'),
        ('How is airspeed worked out?', [('a', 'From the colour of the wings'), ('b', 'From the difference between total and static pressure'), ('c', 'From the number of passengers'), ('d', 'From the size of the runway')], 'b'),
        ('What does static pressure give?', [('a', 'Fuel price'), ('b', 'The name of the pilot'), ('c', 'The time of lunch'), ('d', 'Pressure altitude')], 'd'),
        ('What can cause wrong readings?', [('a', 'Blocked or leaking lines'), ('b', 'Regular calibration'), ('c', 'Clean instruments'), ('d', 'Checked systems')], 'a'),
    ],
}
