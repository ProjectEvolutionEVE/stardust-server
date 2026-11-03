"""Geodetic Structural Health Monitoring: building sensors, displacement, thermal effects, data fusion, alarms and standards."""
CODE = 'navigation5_structural_health'
BOOK = {
    "title": 'Geodetic Structural Health Monitoring',
    "subtitle": 'Keeping buildings and bridges under watch with positioning and sensors',
    "chapters": [
        ('Building sensors',
         'Sensors fixed to a structure measure movement, strain and other signs of change. Each sensor records a small part of the picture, and together they show how the whole structure is behaving.'),
        ('Displacement',
         'Displacement is how far a point on the structure has moved from where it was. Geodetic methods measure displacement precisely, even when the movement is only a few millimetres.'),
        ('Thermal effects',
         'Daily heating and cooling make structures expand and contract. A bridge may move every day with the sun. Thermal effects must be separated from real damage before any alarm is raised.'),
        ('Data fusion',
         'Data fusion combines readings from several sensors and methods into one clearer picture. Two independent measurements that agree give more confidence than one alone.'),
        ('Alarms',
         'An alarm is raised when a reading crosses a set limit. Alarm levels are agreed in advance, based on the design. A good alarm is clear, timely and tested before it is relied on.'),
        ('Standards',
         'Standards make results comparable and dependable, from one structure to another and from one year to the next. Follow recognised standards for sensors, data and reporting.'),
    ],
    "test": [
        ('What do building sensors measure?',
         [('a', 'Movement, strain and other signs of change in a structure'), ('b', 'Taste'), ('c', 'Music'), ('d', 'Smell')], 'a'),
        ('What causes thermal effects in a bridge?',
         [('a', 'Paint'), ('b', 'Sound'), ('c', 'Daily heating and cooling that makes the structure move'), ('d', 'Rain alone')], 'c'),
        ('What is data fusion?',
         [('a', 'Melting metal'), ('b', 'Cooking data'), ('c', 'Deleting data'), ('d', 'Combining data from several sensors to give one clearer picture')], 'd'),
        ('What is an alarm for in structural monitoring?',
         [('a', 'To be ignored'), ('b', 'To warn when a reading crosses a set limit'), ('c', 'To play music'), ('d', 'To decorate the building')], 'b'),
        ('Why are standards important in structural health monitoring?',
         [('a', 'They make sensors cheap'), ('b', 'They are not needed'), ('c', 'They make results comparable and dependable'), ('d', 'They block the data')], 'c'),
    ],
}
