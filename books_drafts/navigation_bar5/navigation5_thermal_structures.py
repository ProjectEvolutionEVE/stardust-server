"""Thermal Effects on Long Structures: how heat changes the length and shape of bridges, rails and towers, and how engineers allow for it."""
CODE = 'navigation5_thermal_structures'
BOOK = {
    "title": 'Thermal Effects on Long Structures',
    "subtitle": 'Expansion, daily cycles, sensors, models, corrections and design',
    "chapters": [
        ('Materials grow when warm',
         'Most materials expand when they get warmer and shrink when they cool. The change in length is small for each degree, but a long steel bridge can change by many centimetres between a cold night and a hot afternoon.'),
        ('Daily and seasonal cycles',
         'Structures move every day as the sun heats one side and the night cools it. They also move with the seasons. The motion repeats, so the same points return to similar positions over time.'),
        ('Sensors that watch the motion',
         'Engineers fit thermometers, strain gauges and GNSS receivers to long structures. Together they show how the temperature and the movement change over the day and the year.'),
        ('Models of the response',
         'A model links the temperature to the expected movement. Comparing the model with the sensor data shows whether the structure behaves as designed. A difference can be an early sign of a problem.'),
        ('Corrections',
         'Measurements of a structure must be corrected for temperature before they are compared. Otherwise a normal daily change could look like real damage or real movement.'),
        ('Design for expansion',
         'Engineers allow for expansion with expansion joints, sliding bearings and gaps in railway track. The aim is to let the structure move freely, so that heat does not build up stresses that crack or bend it.'),
    ],
    "test": [
        ('What usually happens to a material when it gets warmer?',
         [('a', 'It expands'), ('b', 'It turns into a liquid at once'), ('c', 'It becomes heavier'), ('d', 'It stops conducting heat')], 'a'),
        ('Why must temperature be corrected for in measurements of a structure?',
         [('a', 'Because temperature makes the structure grow in the dark'), ('b', 'Because thermometers are always wrong'), ('c', 'So a normal daily change is not mistaken for damage'), ('d', 'Because heat has no effect at all')], 'c'),
        ('What do engineers use to allow a bridge to expand?',
         [('a', 'Extra paint'), ('b', 'Expansion joints and sliding bearings'), ('c', 'Solid concrete blocks with no gaps'), ('d', 'Glass windows')], 'b'),
        ('What does a model of thermal response link?',
         [('a', 'Colour and taste'), ('b', 'Wind and music'), ('c', 'Salt and sugar'), ('d', 'Temperature and the expected movement')], 'd'),
        ('Why do gaps in railway track matter in hot weather?',
         [('a', 'They make trains quieter'), ('b', 'They keep the track dry'), ('c', 'They let the track expand without building up damaging stress'), ('d', 'They stop the sun from shining')], 'c'),
    ],
}
