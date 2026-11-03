"""Tilt Sensing and Inclinometers: bubble levels, MEMS tilt sensors, calibration, error, monitoring and uses."""
CODE = 'navigation5_tilt_sensing'
BOOK = {
    "title": 'Tilt Sensing and Inclinometers',
    "subtitle": 'Knowing exactly how far a surface or structure has leaned',
    "chapters": [
        ('Bubbles',
         'A bubble level is a sealed glass vial with a bubble inside. When the surface is level, the bubble sits in the centre. It is a simple, reliable way to show tilt by eye.'),
        ('MEMS tilt sensors',
         'MEMS tilt sensors are small electronic chips that measure tilt. They are cheap, compact and can run for long periods, which makes them useful for continuous monitoring.'),
        ('Calibration',
         'A tilt sensor must be checked against a known reference and corrected. Calibration gives the readings a stated accuracy, so that they can be trusted and compared over time.'),
        ('Error',
         'Tilt readings are affected by temperature change, mounting, vibration and drift. Allow for these in the setup, and check the sensor again after any change to its surroundings.'),
        ('Monitoring',
         'Tilt monitoring watches a structure or the ground over time. A steady change may signal a problem long before it is visible. Regular readings and clear limits make the trend easy to see.'),
        ('Uses',
         'Tilt sensors are used on dams, towers, cranes, bridges and slopes. They help engineers know when a structure is moving more than expected, and when action is needed.'),
    ],
    "test": [
        ('What is a bubble level?',
         [('a', 'A glass vial with a bubble that shows when a surface is level'), ('b', 'A toy'), ('c', 'A tap'), ('d', 'A window')], 'a'),
        ('What is a MEMS tilt sensor?',
         [('a', 'A large clock'), ('b', 'A paper chart'), ('c', 'A type of ship'), ('d', 'A small electronic chip that measures tilt')], 'd'),
        ('Why calibrate a tilt sensor?',
         [('a', 'To make it louder'), ('b', 'To hide faults'), ('c', 'To check and correct its readings against a known reference'), ('d', 'To change its colour')], 'c'),
        ('What is a common source of error in tilt sensing?',
         [('a', 'The shape of the sensor case'), ('b', 'Temperature change'), ('c', 'The name of the sensor'), ('d', 'The colour of the sensor')], 'b'),
        ('What is tilt monitoring used for?',
         [('a', 'Painting walls'), ('b', 'Making music'), ('c', 'Watching structures and ground for movement'), ('d', 'Cooking food')], 'c'),
    ],
}
