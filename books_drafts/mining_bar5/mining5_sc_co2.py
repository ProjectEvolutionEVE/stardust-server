"""Supercritical carbon dioxide in extraction: phase behaviour, solvents, metal extraction, energy, separation and limits."""
CODE = 'mining5_sc_co2'
BOOK = {
    'title': 'Supercritical CO2 in Extraction',
    'subtitle': 'A carbon dioxide state that can carry metals, with care and cost',
    "chapters": [
        ('A strange state', 'Carbon dioxide becomes supercritical above about 31 degrees Celsius and high pressure. In that state it is neither a clear liquid nor a plain gas.'),
        ('Solvents', 'Supercritical carbon dioxide dissolves some organic compounds, and it is used as a solvent in certain processes. It dissolves most metals poorly on its own.'),
        ('Metal extraction', 'To pull metals out, supercritical carbon dioxide is mixed with a chelating agent. The agent binds the metal and carries it into the fluid.'),
        ('Energy', 'Pressurising carbon dioxide takes energy. Planners weigh that energy against the gain in extraction.'),
        ('Separation', 'Lowering the pressure lets the carbon dioxide return to a gas. The dissolved material is left behind as a solid.'),
        ('Limits', 'The method is limited by the cost of pressure equipment and by which materials dissolve. It remains a specialised method.'),
    ],
    "test": [
        ('About what temperature is the critical point of carbon dioxide?', [('a', 'About 31 degrees Celsius'), ('b', 'About 100 degrees Celsius'), ('c', 'About minus 40 degrees Celsius'), ('d', 'About 500 degrees Celsius')], 'a'),
        ('What is added to supercritical carbon dioxide to pull out metals?', [('a', 'Sand'), ('b', 'A chelating agent'), ('c', 'Fresh water'), ('d', 'Diesel fuel')], 'b'),
        ('What happens when the pressure is lowered?', [('a', 'The carbon dioxide turns into metal'), ('b', 'The mixture gets heavier'), ('c', 'The carbon dioxide returns to gas and leaves the dissolved material behind'), ('d', 'Nothing changes at all')], 'c'),
        ('What is a cost of this method?', [('a', 'Paint for the vessels'), ('b', 'Payment to the local radio'), ('c', 'Rent for the canteen'), ('d', 'Energy to pressurise the carbon dioxide')], 'd'),
        ('Why is supercritical carbon dioxide called a specialised method?', [('a', 'It is used only in kitchens'), ('b', 'Pressure equipment is costly and only some materials dissolve'), ('c', 'It needs no equipment at all'), ('d', 'It works only underwater')], 'b'),
    ],
}
