"""Fundamental Constants and the Redefined SI: defining constants, the Planck constant, the Kibble balance, the fine structure constant, unit redefinition and tests of constant variation."""
CODE = 'science5_phys_constants'
BOOK = {
    "title": 'Fundamental Constants and the Redefined SI',
    "subtitle": 'How the units of measurement now rest on fixed numbers of nature',
    "chapters": [
        ('Constants of nature',
         'Some numbers appear throughout physics, such as the speed of light, the Planck constant and the elementary charge. They are called fundamental constants. Measuring them well is one of the basic jobs of metrology.'),
        ('A new kind of definition',
         'In 2019, the SI units were redefined so that seven constants have exact fixed values. The kilogram, for example, is now set by fixing the Planck constant. The units now rest on constants of nature, not on physical objects kept in a vault.'),
        ('The Planck constant',
         'The Planck constant links the energy of a photon to its frequency. Before the redefinition, its value was known only to a limited precision. Fixing it exactly lets every mass be measured in terms of it.'),
        ('The Kibble balance',
         'A Kibble balance compares mechanical power with electrical power, using quantum effects in a precise way. It links the kilogram to the Planck constant. It was the main tool used to measure the Planck constant before the redefinition.'),
        ('The fine structure constant',
         'The fine structure constant is a dimensionless number, about 1 divided by 137. It sets the strength of electromagnetic interaction. Its value is measured with very high precision, and its origin is still not explained by any accepted theory.'),
        ('Tests of constancy',
         'Scientists test whether constants change over time, by comparing light from distant quasars with laboratory atoms. So far, no clear change has been found. Each test narrows the limits on how much a constant could vary.'),
    ],
    "test": [
        ('What did the 2019 redefinition of the SI do?',
         [('a', 'It removed all units'), ('b', 'It made the metre a colour'), ('c', 'It changed the second to a day'), ('d', 'It fixed the values of seven constants exactly')], 'd'),
        ('What constant is used to define the kilogram now?',
         [('a', 'The speed of sound'), ('b', 'The Planck constant'), ('c', 'The boiling point of water'), ('d', 'The weight of a cat')], 'b'),
        ('What does a Kibble balance link to?',
         [('a', 'Bank interest rates'), ('b', 'Wind speed'), ('c', 'Mechanical power and electrical power, tied to the Planck constant'), ('d', 'Tide height')], 'c'),
        ('About how big is the fine structure constant?',
         [('a', 'About 137 times 137'), ('b', 'About 1 divided by 137'), ('c', 'About one million'), ('d', 'About zero exactly')], 'b'),
        ('How do scientists test whether constants change over time?',
         [('a', 'By weighing the Moon each year'), ('b', 'By counting the rain in a city'), ('c', 'By timing the sunrise in one town'), ('d', 'By comparing light from distant quasars with laboratory atoms')], 'd'),
    ],
}
