"""Non-Thermal Plasma Chemistry: how electrons with high energy can drive chemical reactions without heating the whole gas."""
CODE = 'science5_chem_plasma'
BOOK = {
    "title": 'Non-Thermal Plasma Chemistry',
    "subtitle": 'Energetic electrons that make chemistry happen in cool gas',
    "chapters": [
        ('A cool kind of plasma',
         'A plasma is a gas with enough energy to split some atoms into ions and electrons. In a non-thermal plasma, the electrons are very hot but the gas as a whole stays close to room temperature. This is a useful combination for chemistry.'),
        ('Energetic electrons',
         'Fast electrons collide with gas molecules and break them into reactive pieces, such as radicals and excited species. These pieces then react, often at low cost in heat, to make new compounds.'),
        ('Plasma reactors',
         'Common designs use electric discharges between electrodes, such as dielectric barrier discharges. The reactor shape, gas flow and voltage all control how many reactive species form.'),
        ('Surface treatment',
         'Plasma can clean, etch or change the surface of a material in a short time. It can make a plastic easier to paint or glue, because it adds chemical groups to the outer layer without changing the bulk material.'),
        ('Air treatment',
         'Plasma reactors can break down some pollutants in air, such as certain volatile organic compounds. The reactive species attack the pollutant molecules, which turn into smaller and less harmful products.'),
        ('Energy efficiency',
         'Energy efficiency is the main challenge. Much of the electrical energy can be lost as heat or to unwanted side reactions. Engineers measure the energy spent per unit of product to compare reactors fairly.'),
    ],
    "test": [
        ('What does a non-thermal plasma have that is very hot?',
         [('a', 'The walls of the room'), ('b', 'The glass tube only'), ('c', 'The air pressure'), ('d', 'The electrons')], 'd'),
        ('What do energetic electrons do to gas molecules?',
         [('a', 'Turn them into fresh water'), ('b', 'Freeze them solid'), ('c', 'Make them heavier'), ('d', 'Break them into reactive pieces')], 'd'),
        ('What is a dielectric barrier discharge?',
         [('a', 'A type of glass window'), ('b', 'A kind of car engine'), ('c', 'A type of plasma reactor based on electric discharges between electrodes'), ('d', 'A cooling fan')], 'c'),
        ('How can plasma help change a plastic surface?',
         [('a', 'It adds chemical groups to the outer layer'), ('b', 'It turns the plastic into metal'), ('c', 'It makes the plastic float'), ('d', 'It removes the plastic entirely')], 'a'),
        ('What is the main challenge for plasma chemistry?',
         [('a', 'Finding a colour for the gas'), ('b', 'Energy efficiency'), ('c', 'Making the gas heavier'), ('d', 'Stopping all electric current')], 'b'),
    ],
}
