"""Federated Learning: training a shared model on many devices without gathering all their raw data in one place."""
CODE = 'computing5_federated_learning'
BOOK = {
    "title": 'Federated Learning',
    "subtitle": 'Training together while the data stays where it is',
    "chapters": [
        ('The basic idea',
         'In federated learning, a central server sends a model to many devices. Each device trains it on its own data and sends back only the updates. The server combines the updates into an improved shared model.'),
        ('Training on devices',
         'Devices may be phones, hospitals or factory machines. They train in short rounds, often only when charging or on a fast connection. Not every device takes part in every round.'),
        ('Secure aggregation',
         'Secure aggregation lets the server learn the sum of many updates without seeing any one of them. Cryptographic methods hide the individual contributions. This protects users from having their updates read directly.'),
        ('Data that is not identical',
         "Each device's data can be very different from the others. A model averaged over unlike data can learn slowly or perform unevenly. Research focuses on methods that cope with this uneven spread."),
        ('Communication costs and privacy limits',
         'Sending updates costs bandwidth and battery, so systems compress them or send them less often. Updates can still leak some information about the data behind them. Techniques such as adding carefully scaled noise can limit this, at a cost in accuracy.'),
        ('Deployment',
         'A deployed system needs device selection, failure handling and monitoring across a huge range of hardware. Teams must check that the shared model improves for everyone, not only for the most common devices. Clear rules for updates and rollbacks are part of the design.'),
    ],
    "test": [
        ('What do the devices send back to the central server?',
         [('a', 'Their complete raw data'), ('b', 'Only model updates'), ('c', 'Photographs of the room'), ('d', "Their owners' addresses")], 'b'),
        ('What does secure aggregation let the server learn?',
         [('a', "Every device's private photographs"), ('b', 'The price of each battery'), ('c', 'The weather in each city'), ('d', 'The sum of many updates, without seeing any one of them')], 'd'),
        ('Why can non-identical data be a problem?',
         [('a', 'An average over very different data can learn slowly or unevenly'), ('b', 'Devices refuse to train on any data'), ('c', 'Identical data is always too large'), ('d', 'Servers cannot count to ten')], 'a'),
        ('What is a cost of sending updates often?',
         [('a', 'The model gets taller'), ('b', 'The screen turns off'), ('c', 'Bandwidth and battery use'), ('d', 'The training data is deleted')], 'c'),
        ('Why must a deployed system check results across many devices?',
         [('a', 'To choose a new colour for the logo'), ('b', 'To stop the model from ever updating'), ('c', "To count the number of users' pets"), ('d', 'To confirm the shared model improves for everyone, not just common devices')], 'd'),
    ],
}
