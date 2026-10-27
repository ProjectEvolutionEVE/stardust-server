"""Time-series compression: delta and delta-of-delta encoding, Gorilla-style XOR compression, downsampling and retention."""
CODE = 'computing5_timeseries_compression'
BOOK = {
    "title": 'Time-Series Compression',
    "subtitle": 'Packing sensor readings tightly, since neighbouring readings are usually alike',
    "chapters": [
        ('Readings over time',
         'Sensors record a value at regular times, such as a temperature every minute. Millions of readings build up quickly.'),
        ('Delta encoding',
         'Delta encoding stores the change from one reading to the next instead of the full value. Small changes need fewer bits.'),
        ('Delta-of-delta',
         'Timestamps that arrive at steady intervals change by the same amount each time. Storing the change in the change, delta-of-delta, leaves very little to store.'),
        ('Gorilla-style compression',
         'A 2015 system called Gorilla, described by Facebook for monitoring data, stored each float value as an XOR with the one before. Neighbouring numbers share many bits, so the output is small.'),
        ('Downsampling and retention',
         'Old data is often summarised, for example one average per hour instead of every second. Retention rules then delete or roll up data after a set time.'),
        ('Costs and trade-offs',
         'Compression saves storage and speeds up reads, but it costs some processing time. Some methods are lossy, so teams decide whether small losses are acceptable.'),
    ],
    "test": [
        ('What does delta encoding store?',
         [('a', 'The change from one reading to the next'), ('b', 'The full value every time'), ('c', "The user's name"), ('d', 'A picture')], 'a'),
        ('When is delta-of-delta very effective?',
         [('a', 'When there are no timestamps'), ('b', 'When data is random noise'), ('c', 'When timestamps arrive at steady intervals'), ('d', 'When the sensor is off')], 'c'),
        ('What does downsampling do?',
         [('a', 'Adds more copies'), ('b', 'Summarises old data into fewer points'), ('c', 'Turns data into music'), ('d', 'Stops sensors')], 'b'),
        ('What is a lossy method?',
         [('a', 'One that loses the power supply'), ('b', 'One that prints fewer pages'), ('c', 'One that drops the network'), ('d', 'One that gives up some detail to save space')], 'd'),
        ('What is a trade-off of compression?',
         [('a', 'It saves storage but costs processing time'), ('b', 'It makes storage bigger'), ('c', 'It removes the need for time'), ('d', 'It stops all reads')], 'a'),
    ],
}
