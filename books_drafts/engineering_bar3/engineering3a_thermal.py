"""Thermal Management: how heat travels through a part, and how designers pull it out before it does harm."""
CODE = 'engineering3a_thermal'
BOOK = {
    "title": 'Thermal Management: Moving Heat Away',
    "subtitle": 'How heat travels through a part, and how designers pull it out before it does harm',
    "chapters": [
        ('Heat from losses',
         'Almost every working machine makes heat it does not want. Motors lose power in their wires and bearings, and electronics lose power each time they switch. Thermal management is the job of getting that heat out before it harms the parts.'),
        ('Three ways heat moves',
         'Heat travels by conduction through solid material, by convection when a fluid carries it away, and by radiation as infrared energy. Most cooling designs use all three together. In vacuum only radiation works, as the book on engineering in vacuum explains.'),
        ('Conduction and the path',
         'Heat moves quickly through metal and slowly through plastic and ceramic. Copper conducts heat better than aluminium, and aluminium better than steel, but aluminium is much lighter. A short, wide, metal path from the heat source gives the best flow.'),
        ('Fins and heat sinks',
         'A heat sink is a block of metal with many fins that spread the heat over a large surface. The more surface there is, the more heat leaves for the air or coolant. A fan blowing across the fins can raise that flow a great deal.'),
        ('Gaps and paste',
         'Two flat metal faces touch at only a few points, and the gaps between them hold air, which insulates. Thermal paste or a pad fills those gaps so that heat can cross. Forgetting this step can leave a part running far hotter than designed.'),
        ('Design to a limit',
         'Each part has a highest safe temperature, and the design must keep every part below it in the hottest conditions it will meet. Measure the temperature under full load, not at rest. Then add a margin for a hot day or a blocked fin.'),
    ],
    "test": [
        ('Where does most of a motor\'s wasted power end up?',
         [('a', 'In heat in its wires and bearings'), ('b', 'In the paint'), ('c', 'In the light it gives off'), ('d', 'In the weight of the shaft')], 'a'),
        ('Which way does heat move through a solid?',
         [('a', 'Radiation'), ('b', 'Conduction'), ('c', 'Evaporation'), ('d', 'Magnetism')], 'b'),
        ('Of copper, aluminium and steel, which conducts heat best?',
         [('a', 'Steel'), ('b', 'Aluminium'), ('c', 'Copper'), ('d', 'All three conduct heat equally')], 'c'),
        ('What do the fins of a heat sink do?',
         [('a', 'They give a large surface for heat to leave'), ('b', 'They hold the heat in'), ('c', 'They make the sink heavier'), ('d', 'They block the airflow')], 'a'),
        ('Why use thermal paste between a chip and its heat sink?',
         [('a', 'It fills tiny air gaps that would insulate'), ('b', 'It makes the chip louder'), ('c', 'It stops the heat sink from being fitted'), ('d', 'It adds weight on purpose')], 'a'),
    ],
}
