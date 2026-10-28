"""Thermoelectric Materials: materials that turn a temperature difference straight into electricity, and their limits."""
CODE = 'mining4_thermoelectric'
BOOK = {
    "title": 'Thermoelectric Materials',
    "subtitle": 'Turning a temperature difference straight into electricity',
    "chapters": [
        ('The Seebeck effect',
         'When two ends of a material are at different temperatures, charge carriers (electrons in n-type material) move from the hot end to the cold end. This makes a voltage. The effect is called the Seebeck effect, and it turns heat directly into electricity.'),
        ('Figure of merit',
         'Engineers judge a thermoelectric material by a figure of merit, usually written ZT. A good material conducts electricity well but conducts heat poorly, so the hot and cold ends stay apart. Raising ZT is the central challenge.'),
        ('Bismuth telluride',
         'Bismuth telluride is the best-known material for use near room temperature. It is used in small coolers and in some sensors. Its efficiency falls off at higher temperatures.'),
        ('Waste heat recovery',
         'Engines, furnaces and exhaust pipes throw away large amounts of heat. Thermoelectric modules can turn part of that waste heat back into electricity. The gain is usually modest, but it adds up.'),
        ('Heat-to-power in space',
         'Spacecraft with no sunlight often use radioactive heat sources with thermoelectric generators. The heat from the decaying material is turned into steady electric power for many years. Efficiency is low, but the reliability is high.'),
        ('Limits of efficiency',
         'Every heat engine is limited by the temperatures it works between. Thermoelectric devices follow the same rule, so the gap between hot and cold must be large to get useful power.'),
    ],
    "test": [
        ('What does the Seebeck effect produce?',
         [('a', 'A flash of light'), ('b', 'A cloud of gas'), ('c', 'A voltage from a temperature difference'), ('d', 'A solid block of ice')], 'c'),
        ('What makes a good thermoelectric material?',
         [('a', 'Conducts electricity well but conducts heat poorly'), ('b', 'Conducts heat well and electricity poorly'), ('c', 'Conducts neither heat nor electricity'), ('d', 'Melts at room temperature')], 'a'),
        ('Which material is best known for use near room temperature?',
         [('a', 'Pure sand'), ('b', 'Liquid mercury'), ('c', 'Clear window glass'), ('d', 'Bismuth telluride')], 'd'),
        ('What is waste heat recovery?',
         [('a', 'Throwing heat out of a window'), ('b', 'Turning waste heat from engines or furnaces back into electricity'), ('c', 'Cooling a room with a fan'), ('d', 'Burning rubbish')], 'b'),
        ("What limits any thermoelectric device's efficiency?",
         [('a', 'The colour of the device'), ('b', 'The number of screws'), ('c', 'The temperatures it works between'), ('d', 'The price of paint')], 'c'),
    ],
}
