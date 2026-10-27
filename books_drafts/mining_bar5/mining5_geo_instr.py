"""Geotechnical instrumentation: piezometers, extensometers, tilt meters, alarm levels and monitoring reports."""
CODE = 'mining5_geo_instr'
BOOK = {
    'title': 'Geotechnical Instrumentation and Monitoring',
    'subtitle': 'Watching the ground move, so people are warned before a failure',
    "chapters": [
        ('Watching the ground', 'Instruments show how rock and slopes move over time. Watching them lets engineers act before a small movement becomes a failure.'),
        ('Piezometers', 'A piezometer measures water pressure in the ground. High water pressure can make a slope weaker.'),
        ('Extensometers and tilt meters', 'An extensometer measures stretch or opening in the rock. A tilt meter measures small changes in angle.'),
        ('Alarm levels', 'Each instrument has set alarm levels. When a reading passes a level, a planned response begins.'),
        ('Data loggers and reports', 'Data loggers record readings automatically, day and night. Engineers review them in regular reports.'),
        ('Why it matters', 'Monitoring gives an early warning. People can then move, stop work or add support before movement becomes dangerous.'),
    ],
    "test": [
        ('What does a piezometer measure?', [('a', 'Air speed in a tunnel'), ('b', 'Water pressure in the ground'), ('c', 'The weight of the ore'), ('d', 'The brightness of the lights')], 'b'),
        ('What does a tilt meter measure?', [('a', 'Changes in the price of copper'), ('b', 'The number of people underground'), ('c', 'The volume of water in a tank'), ('d', 'Small changes in angle')], 'd'),
        ('What are alarm levels?', [('a', 'Colours painted on the walls'), ('b', 'The times when shifts change'), ('c', 'Set readings that trigger a planned response when passed'), ('d', 'Prices that the market sets')], 'c'),
        ('What does a data logger do?', [('a', 'Records readings automatically'), ('b', 'Writes the shift rota by hand'), ('c', 'Cuts rock with a laser'), ('d', 'Sells ore to the mill')], 'a'),
        ('Why is ground monitoring used?', [('a', 'To decorate the tunnels'), ('b', 'To give early warning before movement becomes dangerous'), ('c', 'To count the trucks each day'), ('d', 'To make the ore heavier')], 'b'),
    ],
}
