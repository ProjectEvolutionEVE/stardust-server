"""Multilateration Surveillance: Finding aircraft by timing their replies."""
CODE = 'navigation5_multilateration'
BOOK = {
    'title': 'Multilateration Surveillance',
    'subtitle': 'Finding aircraft by timing their replies',
    'chapters': [
        ('A different way to see aircraft', 'Multilateration finds an aircraft by timing its signal as it reaches several receivers. No single radar dish is needed.'),
        ('Time differences', "The signal reaches each receiver at a slightly different moment. The time differences between receivers give the aircraft's position."),
        ('Receivers', 'Several receivers are set up around an area, often an airport. More receivers and good spacing give better results.'),
        ('Accuracy and geometry', 'The shape of the receivers around the aircraft matters. Good geometry gives sharp fixes, while poor geometry gives weaker ones.'),
        ('Airports', 'Airports use multilateration to track aircraft on the ground and in the air nearby. It helps controllers see movement in busy areas.'),
        ('Cost', 'Receivers can be cheaper and quicker to install than a radar, though each site needs power and data links. Planners weigh these costs against the benefits.'),
    ],
    'test': [
        ('What does multilateration use to locate an aircraft?', [('a', 'A paint colour'), ('b', "The aircraft's name"), ('c', 'Time differences between receivers'), ('d', 'A paper map')], 'c'),
        ('What makes multilateration work?', [('a', 'Several receivers set up around an area'), ('b', 'One single dish only'), ('c', 'Smoke signals'), ('d', 'Sea currents')], 'a'),
        ('What does good receiver geometry give?', [('a', 'Blurred paint'), ('b', 'Fewer runways'), ('c', 'Lower tides'), ('d', 'Sharp position fixes')], 'd'),
        ('Where is multilateration often used?', [('a', 'At airports, for ground and nearby air movement'), ('b', 'Under the sea only'), ('c', 'In deep forests only'), ('d', 'On planets')], 'a'),
        ('What is a factor in choosing multilateration?', [('a', 'Cost, power and data links at each site'), ('b', 'The colour of the sky'), ('c', 'The number of fish'), ('d', 'The age of the moon')], 'a'),
    ],
}
