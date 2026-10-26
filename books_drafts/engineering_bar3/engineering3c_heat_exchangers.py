"""Heat Exchangers: passing heat from one fluid to another without mixing them."""
CODE = 'engineering3c_heat_exchangers'
BOOK = {
    "title": 'Heat Exchangers: Passing Heat Between Fluids',
    "subtitle": 'Moving heat from one fluid to another without letting them mix',
    "chapters": [
        ('Heat without mixing',
         "A heat exchanger moves heat from a hot fluid to a cold one while keeping the two fluids apart. A wall between them is the path the heat crosses. Car radiators and refrigerators both rely on heat exchangers."),
        ('Two common designs',
         "A shell-and-tube exchanger runs one fluid through a bundle of tubes inside a larger shell, with the other fluid flowing around the outside. A plate exchanger stacks thin, ridged plates with channels between them. Plates give a great deal of surface in a small space."),
        ('Flow direction',
         "In a counterflow exchanger the two fluids run in opposite directions. The cold fluid can leave warmer than the hot fluid leaves, which lets it pull out more heat. In parallel flow both fluids run the same way, and the best they can reach is one shared temperature, so less heat moves."),
        ('How much heat moves',
         "The heat moved depends on the area of the wall, how well the wall conducts heat, and the average temperature difference between the fluids. Double the area and, other things equal, you roughly double the heat moved. Fouling, a layer of scale or dirt on the surface, slows the transfer and must be cleaned off."),
        ('Saving energy',
         "An exchanger can take heat that would be thrown away and give it to something useful, such as warming incoming water. That recovered heat is energy you do not have to buy. The savings pay back the exchanger's cost over time, so work out the payback before you decide."),
        ('Keeping it clean',
         "Dirt in an exchanger raises the pressure drop across it and cuts the flow. Measure that pressure drop regularly, clean the surfaces on a schedule, and write the readings in the records. A clean exchanger does its job for less power."),
    ],
    "test": [
        ('What is the wall in a heat exchanger for?',
         [('a', 'To mix the two fluids'), ('b', 'To stop all heat from moving'), ('c', 'To keep the fluids apart while heat crosses'), ('d', 'To store the heat')], 'c'),
        ('In a counterflow exchanger, what do the two fluids do?',
         [('a', 'Run the same way'), ('b', 'Run in opposite directions'), ('c', 'Stop at the middle'), ('d', 'Swap places every minute')], 'b'),
        ('What does dirt on an exchanger surface do?',
         [('a', 'Slows the heat transfer, so the exchanger must be cleaned'), ('b', 'Speeds up the heat transfer'), ('c', 'Has no effect at all'), ('d', 'Turns the fluid into a solid')], 'a'),
        ('What can an exchanger do with heat that would otherwise be wasted?',
         [('a', 'Throw it into space'), ('b', 'Double it'), ('c', 'Store it in the hull'), ('d', 'Give it to something useful, such as warming incoming water')], 'd'),
        ('Which design gives a lot of heat-transfer area in a small space?',
         [('a', 'A shell with no tubes'), ('b', 'A stack of thin plates'), ('c', 'A single straight pipe'), ('d', 'A solid block with no channels')], 'b'),
    ],
}
