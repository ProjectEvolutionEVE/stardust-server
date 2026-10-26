"""Gases and the Gas Laws: how the pressure, volume and temperature of a gas are linked, and the ideal gas law. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_gases'
BOOK = {
    "title": 'Gases and the Gas Laws',
    "subtitle": 'How the pressure, volume and temperature of a gas are linked',
    "chapters": [
        ('Gases fill their space',
         'A gas has no fixed shape or volume. It spreads out to fill whatever holds it. Its particles move quickly and bump into the walls, and those bumps are what we feel as pressure.'),
        ('Pressure and volume',
         "Boyle's law says that at a steady temperature, squeezing a gas into less space raises its pressure. Halve the volume and the pressure doubles. A bicycle pump works this way, and so does a diving tank full of compressed air."),
        ('Temperature and volume',
         "Charles's law says that at steady pressure, a gas grows larger when it is heated. The gas laws need temperatures in kelvin, a scale that starts at absolute zero, about −273 °C. A hot-air balloon rises because its warm air takes up more room and is less dense than the cool air outside."),
        ('The ideal gas law',
         'Put the laws together and you get the ideal gas law, PV = nRT. Pressure times volume equals the number of moles, times a constant, times the temperature. It is a simple model, and it works well for most gases under ordinary conditions.'),
        ('Gases in real life',
         'Hydrogen and oxygen are often stored as compressed gases, so their pressure and temperature must be watched. A tank that warms in the sun builds up pressure, which is why such tanks are kept cool and handled with care.'),
        ('Why the numbers need care',
         'Always convert a temperature to kelvin before you use the gas laws. Celsius gives wrong answers, because the laws are built on the absolute scale. Check your units first, just as you did when you learned to measure.'),
    ],
    "test": [
        ('What happens to the pressure of a gas when you squeeze it into less space at a steady temperature?',
         [('a', 'It falls'), ('b', 'It rises'), ('c', 'It stays exactly the same forever'), ('d', 'It turns into a liquid')], 'b'),
        ('Which temperature scale must the gas laws use?',
         [('a', 'Fahrenheit'), ('b', 'The number of protons'), ('c', 'Kelvin'), ('d', 'Celsius')], 'c'),
        ('Why does a hot-air balloon rise?',
         [('a', 'Its gas is heavier than the air around it'), ('b', 'It is pulled up by a magnet'), ('c', 'It burns up its air'), ('d', 'Its warm air is less dense than the cool air around it')], 'd'),
        ('What is the ideal gas law?',
         [('a', 'PV = nRT'), ('b', 'E = mc²'), ('c', 'pH = 7 always'), ('d', 'F = ma')], 'a'),
        ('Why must you check temperature units before you use the gas laws?',
         [('a', 'Because Celsius numbers can be negative'), ('b', 'Because kelvin is only for liquids'), ('c', 'Because the laws are built on the absolute scale, so Celsius gives wrong answers'), ('d', 'Because gases do not have temperatures')], 'c'),
    ],
}
