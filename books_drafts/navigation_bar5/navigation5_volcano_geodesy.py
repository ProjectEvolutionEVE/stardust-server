"""Volcano Monitoring by Geodesy: inflation, GNSS, InSAR, magma movement, warnings and models."""
CODE = 'navigation5_volcano_geodesy'
BOOK = {
    "title": 'Volcano Monitoring by Geodesy',
    "subtitle": 'Reading the shape of a volcano to hear the magma beneath it',
    "chapters": [
        ('Inflation',
         'Before some eruptions, a volcano swells as magma gathers below the surface. This inflation changes the shape of the ground. Measuring that shape is one of the best early signs of unrest.'),
        ('GNSS',
         'GNSS receivers on the flanks of a volcano measure the position of each point, often every day. Their records show how the ground is rising, falling or leaning over time.'),
        ('InSAR',
         'InSAR compares satellite radar images to map ground movement across a wide area. It shows the whole pattern of swelling, which GNSS points alone may miss between stations.'),
        ('Magma movement',
         'Magma moves underground, and its movement can change the ground above it. Geodetic data helps estimate where the magma is, how much there is, and whether it is moving toward the surface.'),
        ('Warnings',
         'Warnings are issued when measurements pass levels agreed in advance. A warning gives officials and the public time to prepare. The clearer the trend, the better the warning.'),
        ('Models',
         'Models turn the measurements into an estimate of the magma source and its likely behaviour. Models help interpret the data, but they must be checked against other evidence before they are trusted.'),
    ],
    "test": [
        ('What does inflation of a volcano mean?',
         [('a', 'The volcano getting smaller'), ('b', 'The volcano being painted'), ('c', 'The ground swelling as magma gathers below'), ('d', 'A type of sound')], 'c'),
        ('What tools measure volcano ground movement?',
         [('a', 'Rulers'), ('b', 'Clocks'), ('c', 'Cameras only'), ('d', 'GNSS and InSAR')], 'd'),
        ('What is magma movement?',
         [('a', 'Water flowing down a river'), ('b', 'Molten rock moving underground'), ('c', 'Traffic on a road'), ('d', 'Snow melting')], 'b'),
        ('What do volcano warnings do?',
         [('a', 'Give time to act to protect people'), ('b', 'Cause harm'), ('c', 'Stop monitoring'), ('d', 'Hide the data')], 'a'),
        ('Why are models used in volcano monitoring?',
         [('a', 'To fill time'), ('b', 'To help interpret measurements and judge what may happen next'), ('c', 'To paint maps'), ('d', 'To count tourists')], 'b'),
    ],
}
