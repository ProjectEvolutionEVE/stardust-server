"""Flight Logs and Records: what to write down on every flight, and how records help a pilot improve."""
CODE = 'flight3a_flight_logs'
BOOK = {
    "title": 'Flight Logs and Records',
    "subtitle": 'What to write down on every flight, and how records help you improve',
    "chapters": [
        ('Why keep a log',
         "A flight log is a written record of a flight: the times, the speeds, the fuel, the readings and any problems. Pilots keep logs because memory fades fast. A written record also shows patterns that nobody notices in the moment."),
        ('Flight recorders',
         "Aircraft carry a flight data recorder, often called a black box, that stores readings from the flight. After an incident, investigators use it to find out what the craft was doing. The recorder is usually painted bright orange, so that it can be found."),
        ('Telemetry',
         "Telemetry is the data a spacecraft sends down to the ground, such as its temperatures, its power and its position. Ground teams watch telemetry for trends. A gap in the telemetry is a warning to check the link and the craft."),
        ('What to note',
         "Write down the time, the start and finish positions, the fuel used, the hours flown and anything that surprised you. Short notes made at once are more useful than long ones written later. Keep the same format each time, so that you can compare flights."),
        ('Reading your own trends',
         "Read several logs side by side to spot patterns. You may find that long flights always use more fuel, or that one kind of approach tends to overshoot. These are lessons that a single flight cannot show."),
        ('Hours are money too',
         "The hours in your log are also the hours you are billed for. Keeping them accurate lets you check a bill, and compare the hourly rate with a weekly lease. A log is a budget tool as well as a safety tool."),
    ],
    "test": [
        ('What is a flight log?',
         [('a', 'A written record of times, readings, fuel and problems'), ('b', 'A map of the moons'), ('c', 'A tin of food'), ('d', 'A chart of paint colours')], 'a'),
        ('What is the common name for a flight data recorder?',
         [('a', 'A grey box'), ('b', 'A green box'), ('c', 'A silver ring'), ('d', 'A black box')], 'd'),
        ('What is telemetry?',
         [('a', 'Sound from the engines'), ('b', 'Data that a spacecraft sends down to the ground'), ('c', 'A type of hatch'), ('d', 'Fuel for the lamps')], 'b'),
        ('Why are short notes written soon after a flight useful?',
         [('a', 'They are longer than the flight itself'), ('b', 'They make the craft faster'), ('c', 'Memory fades, so notes made at once are more accurate'), ('d', 'They can replace the telemetry')], 'c'),
        ('Why does keeping accurate hours help a pilot?',
         [('a', 'It helps check a bill and compare the hourly rate with a weekly lease'), ('b', 'It makes the stars brighter'), ('c', 'It changes the colour of the craft'), ('d', 'It opens the hatch')], 'a'),
    ],
}
