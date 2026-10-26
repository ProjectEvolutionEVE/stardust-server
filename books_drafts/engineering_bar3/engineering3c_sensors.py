"""Sensors: how machines turn temperature, pressure, force and position into numbers they can use."""
CODE = 'engineering3c_sensors'
BOOK = {
    "title": 'Sensors: Turning the World Into Numbers',
    "subtitle": 'How machines measure temperature, pressure, force and position',
    "chapters": [
        ('What a sensor does',
         "A sensor turns a physical quantity into a signal a machine can read, such as a voltage or a count of pulses. Temperature, pressure, force and position are the common ones. A controller can only act on what its sensors report to it."),
        ('Temperature sensors',
         "A thermocouple makes a small voltage where two different metals join, and the voltage rises with temperature. A thermistor's resistance changes strongly with temperature. A resistance temperature detector uses a metal wire whose resistance rises steadily and predictably with heat."),
        ('Pressure and force',
         "A pressure transducer turns the push of a fluid into an electrical signal, often through a thin diaphragm that bends. A strain gauge is a thin wire or foil glued to a part; as the part stretches, the gauge's resistance changes. A load cell uses strain gauges to weigh what is placed on it."),
        ('Position and speed',
         "An encoder counts marks on a disc or a strip, which tells the controller how far a shaft has turned or a slide has moved. A Hall sensor reacts to a magnet passing close by, so it can detect a tooth on a wheel or the turn of a shaft."),
        ('Accuracy, range and drift',
         "A sensor has a range it can measure, a resolution (the smallest step it can show) and an accuracy (how close its reading is to the true value). Sensors drift over time. Check them against a known standard, which is called calibration."),
        ('Trusting the reading',
         "A sensor that is stuck, loose or wired wrongly can give a confident wrong answer. Compare two sensors where you can, and watch for readings that jump or never move. A reading you cannot check is a reading to question."),
    ],
    "test": [
        ('What does a sensor do?',
         [('a', 'Pushes the machine'), ('b', 'Turns a physical quantity into a signal a machine can read'), ('c', 'Stores power'), ('d', 'Paints the part')], 'b'),
        ('What does a thermocouple produce?',
         [('a', 'A change in colour'), ('b', 'A change in weight'), ('c', 'A small voltage where two different metals join, which rises with temperature'), ('d', 'A sound')], 'c'),
        ('What is a strain gauge?',
         [('a', 'A layer of paint'), ('b', 'A tiny motor'), ('c', 'A battery'), ('d', 'A thin wire or foil whose resistance changes as the part it is glued to stretches')], 'd'),
        ('What is the resolution of a sensor?',
         [('a', 'The smallest step it can show'), ('b', 'Its colour'), ('c', 'Its maximum weight'), ('d', 'How many wires it has')], 'a'),
        ('What is calibration?',
         [('a', 'Painting the sensor'), ('b', 'Turning the sensor off'), ('c', 'Checking a sensor against a known standard'), ('d', 'Replacing the wires')], 'c'),
    ],
}
