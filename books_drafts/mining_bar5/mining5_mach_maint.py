"""Machine learning for maintenance: sensor logs, failure prediction, alerts and return on investment."""
CODE = 'mining5_mach_maint'
BOOK = {
    'title': 'Machine Learning for Maintenance',
    'subtitle': 'Using sensor history to spot a machine heading for trouble',
    "chapters": [
        ('Listening to machines', 'Modern machines record sensor data, such as temperature, pressure, vibration and running hours. Each reading is a small clue about how the machine is doing.'),
        ('Predicting failure', 'A model learns patterns from the readings that came before past failures. It then flags machines whose readings look similar.'),
        ('Labels', 'A model needs labelled history: which records led to a failure and which did not. Poor labels lead to poor predictions.'),
        ('Alerts', 'Too many false alarms teach people to ignore the system, and too few miss real faults. Setting the alert level is a balance.'),
        ('Trust', 'Engineers trust a model when they can see why it raised an alert and when its past alerts proved right. Trust grows slowly and can be lost quickly.'),
        ('Return on investment', 'A prediction is worth money only if it prevents breakdowns that cost more than the system itself. Planners measure this against the real cost of downtime and repairs.'),
    ],
    "test": [
        ('What kind of data do maintenance models use?', [('a', 'Only the names of the operators'), ('b', 'Only the price of diesel'), ('c', 'Sensor readings such as temperature, pressure and vibration'), ('d', 'Only the weather forecast')], 'c'),
        ('What must a failure model learn from?', [('a', 'Labelled history of past failures and of normal running'), ('b', 'Only the colour of the machine'), ('c', 'Guesses from the market'), ('d', 'One single reading from one day')], 'a'),
        ('Why do too many false alarms cause trouble?', [('a', 'The machines run faster'), ('b', 'The alarms cost nothing to ring'), ('c', 'The model stops learning'), ('d', 'People start to ignore the alerts')], 'd'),
        ('When is a prediction worth money?', [('a', 'When it is published in a journal'), ('b', 'When it prevents breakdowns that cost more than the system'), ('c', 'When it uses the most data'), ('d', 'When it is new this year')], 'b'),
        ('What helps engineers trust a model?', [('a', 'A bright colour on the screen'), ('b', 'Seeing why an alert was raised and a record of being right'), ('c', 'Never being checked'), ('d', 'Being told it is secret')], 'b'),
    ],
}
