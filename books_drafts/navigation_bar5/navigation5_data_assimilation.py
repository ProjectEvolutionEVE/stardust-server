"""Ocean Data Assimilation: Blending computer models with real measurements."""
CODE = 'navigation5_data_assimilation'
BOOK = {
    'title': 'Ocean Data Assimilation',
    'subtitle': 'Blending computer models with real measurements',
    'chapters': [
        ('A model of the ocean', 'Ocean forecasts start from a computer model that describes the current state of the sea. The model is useful, but it is never perfect.'),
        ('Observations', 'Ships, buoys, floats and satellites measure the real ocean. Each observation is compared with the model to see where the two differ.'),
        ('Nudging', 'One simple method is nudging, which gently pulls the model towards the observations over time. It avoids sudden jumps in the forecast.'),
        ('Kalman-like updates', 'Other methods weigh the model and the observations by how uncertain each one is. The more certain source gets the larger share of the correction.'),
        ('Forecast skill', 'Assimilation improves how well a forecast matches what really happens. Forecast skill is the measure of that improvement.'),
        ('Uses', 'Better ocean states help with routing ships, predicting currents and planning search and rescue. The best results come from many kinds of data working together.'),
    ],
    'test': [
        ('What is ocean data assimilation?', [('a', 'Drawing fish'), ('b', 'Painting charts'), ('c', 'Combining model states with real observations'), ('d', 'Measuring tides only')], 'c'),
        ('What does nudging do?', [('a', 'Stops the model at once'), ('b', 'Deletes all data'), ('c', "Changes the ship's name"), ('d', 'Gently pulls the model towards observations over time')], 'd'),
        ('How do Kalman-like methods weigh data?', [('a', 'By how uncertain each source is'), ('b', 'By the colour of the data'), ('c', 'By the age of the captain'), ('d', 'At random')], 'a'),
        ('What does forecast skill measure?', [('a', "The ship's speed"), ('b', 'How well a forecast matches what happens'), ('c', 'The cost of fuel'), ('d', 'The number of observers')], 'b'),
        ('Which is an example of an observation source?', [('a', 'A recipe'), ('b', 'A song'), ('c', 'A map of a city'), ('d', "A buoy's measurement")], 'd'),
    ],
}
