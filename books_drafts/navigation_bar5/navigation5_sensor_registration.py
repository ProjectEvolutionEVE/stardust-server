"""Online Sensor Bias Estimation: letting a navigation system learn its own sensor errors while it runs."""
CODE = 'navigation5_sensor_registration'
BOOK = {
    "title": 'Online Sensor Bias Estimation',
    "subtitle": 'Bias states, online calibration, observability, estimation, drift and results',
    "chapters": [
        ('Bias states',
         'A bias state is a steady offset in a sensor, added to the filter as one more value to estimate. The filter then works out the position and the bias together. Ignoring the bias would leave a steady error in every answer.'),
        ('Online calibration',
         'Online calibration estimates sensor errors while the system is running. It does not need a special test in a workshop. The system improves as it goes.'),
        ('Observability',
         'A bias can only be estimated if the data reveals it. The filter must be able to tell the bias apart from other errors. If it cannot, the estimate stays uncertain.'),
        ('Estimation',
         'Enough motion or a variety of viewpoints makes the bias observable. A vehicle that never turns or changes speed may not reveal some biases at all. Good planning of the motion helps the estimate settle.'),
        ('Drift',
         'Some biases change slowly over time. The filter must follow the change without forgetting the rest of the data. Models of drift tell the filter how fast a bias may move.'),
        ('Results',
         'Online estimates usually give a clear improvement in accuracy. They should be checked against a reference when one is available. A bias that is still uncertain should be reported as uncertain.'),
    ],
    "test": [
        ('What is a bias state?',
         [('a', 'A steady offset in a sensor that the filter estimates along with position'), ('b', 'A bias in a voting poll'), ('c', 'The colour of a sensor'), ('d', 'A map label')], 'a'),
        ('What is online calibration?',
         [('a', 'Calibrating in a factory once only'), ('b', 'Estimating sensor errors while the system runs'), ('c', 'Painting the sensor'), ('d', 'Turning the sensor off')], 'b'),
        ('What does observability mean here?',
         [('a', 'The sensor can be seen'), ('b', 'The sensor has a light'), ('c', 'The sensor is cheap'), ('d', 'The filter can tell the bias apart from other errors')], 'd'),
        ('What helps a bias become observable?',
         [('a', 'Standing still forever'), ('b', 'Turning off the power'), ('c', 'Enough motion or varied viewpoints'), ('d', 'Using a smaller map')], 'c'),
        ('Why does sensor drift matter?',
         [('a', 'It changes the bias over time, so the estimate must follow it'), ('b', 'It makes sensors cheaper'), ('c', 'It stops the clock'), ('d', 'It sets the map scale')], 'a'),
    ],
}
