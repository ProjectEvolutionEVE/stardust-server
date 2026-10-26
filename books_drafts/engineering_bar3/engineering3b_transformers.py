"""Transformers: two coils on one iron core, and the trade between voltage and current that makes stepping power up or down possible."""
CODE = 'engineering3b_transformers'
BOOK = {
    "title": 'Transformers: Stepping Voltage Up and Down',
    "subtitle": 'Two coils, one iron core, and a simple trade between voltage and current',
    "chapters": [
        ('Two coils, one core',
         'A transformer has two coils of wire wound on a shared iron core. Alternating current in the first coil, the primary, sets up a changing magnetic field in the core. That field induces a voltage in the second coil, the secondary. A transformer works only with AC, because a steady DC field does not change.'),
        ('The turns ratio',
         'The voltage ratio of a transformer follows the ratio of its turns. A secondary with twice as many turns as the primary gives about twice the voltage. This ratio of turns decides whether the transformer steps the voltage up or down.'),
        ('Power in and power out',
         'A good transformer delivers nearly the same power on its output side as it takes in, less small losses. So when the voltage goes up, the current goes down in the same ratio, and when the voltage goes down, the current rises. Power is volts times amps, and that trade always holds.'),
        ('Losses and heat',
         'No transformer is perfect. Some energy is lost as heat in the copper wire and in the iron core. Large power transformers are very efficient, often above 95 per cent, but the small remaining loss still has to be carried away by oil or air.'),
        ('Isolation and safety',
         'A transformer can also separate two circuits, with no direct electrical link between the coils. This isolation protects people from a fault on the other side. Many chargers and workshop tools use an isolating transformer for that reason.'),
        ('Money in the transformer',
         'A more efficient transformer wastes less energy, which cuts its running cost over its life. Price the lower losses over the years and set them against the purchase price, as the running-cost idea in the costing book shows. A dearer, efficient unit can be the cheaper choice overall.'),
    ],
    "test": [
        ('What kind of current does a transformer need to work?',
         [('a', 'DC only'), ('b', 'None at all'), ('c', 'Alternating current, AC'), ('d', 'Static electricity')], 'c'),
        ('A secondary coil has twice the turns of the primary. Roughly what voltage does it give?',
         [('a', 'Twice the voltage'), ('b', 'Half the voltage'), ('c', 'The same voltage'), ('d', 'Zero')], 'a'),
        ('If a transformer steps the voltage up, what happens to the current?',
         [('a', 'It rises by the same amount'), ('b', 'It stays the same'), ('c', 'It doubles'), ('d', 'It falls in the same ratio')], 'd'),
        ('Where is energy lost in a transformer?',
         [('a', 'Only in its paint'), ('b', 'As heat in the copper wire and the iron core'), ('c', 'In the air above it'), ('d', 'In its label')], 'b'),
        ('What does isolation mean for a transformer?',
         [('a', 'The two circuits have no direct electrical link'), ('b', 'The coils are glued together'), ('c', 'The transformer is made of glass'), ('d', 'The output is always DC')], 'a'),
    ],
}
