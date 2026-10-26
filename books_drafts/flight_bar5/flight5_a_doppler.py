"""Doppler Tracking: measuring a craft's speed from the shift in its radio signal."""
CODE = 'flight5_a_doppler'
BOOK = {
    "title": 'Doppler Tracking',
    "subtitle": 'Measuring speed from the shift in a radio signal',
    "chapters": [
        ('The Doppler shift',
         'When a source of waves moves toward you, the waves bunch up and arrive at a higher pitch. When it moves away, they spread out and arrive lower. The same effect happens with radio signals from a spacecraft, and it is called the Doppler shift.'),
        ('Range rate',
         'The size of the shift tells the team how fast the craft is moving toward or away from the station. This speed along the line of sight is called the range rate. Measured over time, it reveals a great deal about the path.'),
        ('Fitting the path',
         'The team collects many Doppler measurements and fits a model of the orbit or trajectory to them. The best fit is the path that matches all the measurements most closely. Small changes in the model show up clearly.'),
        ('Accuracy',
         "Doppler tracking can be very precise, especially over a long pass. Its accuracy depends on the stability of the transmitter, the station, and the models of the Earth's ionosphere and the troposphere. Careful modelling keeps errors low."),
        ('Apollo and beyond',
         'Doppler tracking helped guide the Apollo missions through the Earth and the Moon. Its use has continued on many later missions, from planetary probes to Earth satellites.'),
        ('Modern use',
         'Modern deep-space navigation still uses Doppler data as one of its main tools. It is often combined with ranging, which measures distance, and with other methods. Together they give the team a full picture of the craft.'),
    ],
    "test": [
        ('What is the Doppler shift?',
         [('a', 'A change in the pitch or frequency of waves from a moving source'), ('b', 'A change in the colour of a planet'), ('c', 'A dent in a fuel tank'), ('d', 'A new kind of rocket')], 'a'),
        ('What does range rate describe?',
         [('a', 'The size of the crew'), ('b', 'The speed along the line of sight toward or away from the station'), ('c', 'The cost of the mission'), ('d', 'The number of solar panels')], 'b'),
        ('What do teams do with many Doppler measurements?',
         [('a', 'They throw them away'), ('b', 'They print them on paper'), ('c', 'They fit a model of the path to them'), ('d', 'They use them to cook food')], 'c'),
        ('What helped guide the Apollo missions?',
         [('a', 'Smoke signals'), ('b', 'Paper maps'), ('c', 'Kites'), ('d', 'Doppler tracking')], 'd'),
        ('Which kind of measurement is often combined with Doppler data?',
         [('a', 'Ranging, which measures distance'), ('b', 'Taste tests'), ('c', 'Photographs of food'), ('d', 'Sound recordings of the crew')], 'a'),
    ],
}
