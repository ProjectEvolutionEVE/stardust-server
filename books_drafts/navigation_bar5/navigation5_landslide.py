"""Landslide Monitoring with Positioning: sliding masses, GNSS monitors, rates, triggers, warnings and models."""
CODE = 'navigation5_landslide'
BOOK = {
    "title": 'Landslide Monitoring with Positioning',
    "subtitle": 'Using precise positioning to see slopes move before they fail',
    "chapters": [
        ('Sliding masses',
         'A landslide is a mass of soil or rock that slides down a slope. Many slopes move slowly for a long time before a sudden failure. Monitoring is how that slow movement is seen.'),
        ('GNSS monitors',
         'GNSS monitors are satellite positioning receivers fixed to the ground. They record the position of each point many times a day, and they show slow movement that the eye cannot see.'),
        ('Rates',
         'The rate of movement is how fast the ground is sliding. A steady rate may be safe, while a rising rate can signal growing danger. Track the rate over time, not only the total movement.'),
        ('Triggers',
         'A trigger is an event or a condition that can set a landslide moving, such as heavy rain, rapid melting or a sudden change in the rate. Knowing the triggers helps decide when to look more closely.'),
        ('Warnings',
         'Warnings are issued when the data or the triggers pass an agreed level. A warning gives people time to move, to protect property and to close roads. Warnings must be clear and timely.'),
        ('Models',
         'Models use the monitoring data and the ground conditions to predict how a slope may behave. A model is only as good as its data, so check it against what the monitors record.'),
    ],
    "test": [
        ('What is a GNSS monitor used for on a slope?',
         [('a', 'Cooking food'), ('b', 'Painting the ground'), ('c', 'Playing music'), ('d', 'Tracking the slow movement of the ground')], 'd'),
        ('What is a rate in landslide monitoring?',
         [('a', 'How fast the ground moves'), ('b', 'The price of land'), ('c', 'The colour of the soil'), ('d', 'The name of a village')], 'a'),
        ('What is a trigger for a landslide warning?',
         [('a', 'A sunny day'), ('b', 'Something such as heavy rain or fast movement that calls for a warning'), ('c', 'A new bridge'), ('d', 'A holiday')], 'b'),
        ('What are landslide models used for?',
         [('a', 'Painting'), ('b', 'Decorating'), ('c', 'Predicting how a slope may behave'), ('d', 'Playing games')], 'c'),
        ('Why issue landslide warnings?',
         [('a', 'To cause panic'), ('b', 'To hide the risk'), ('c', 'To stop all monitoring'), ('d', 'To give people time to act to protect life and property')], 'd'),
    ],
}
