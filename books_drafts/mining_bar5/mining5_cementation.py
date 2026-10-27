"""Cementation on iron: displacement reactions, copper recovery from solution, scrap iron as reagent, kinetics and cement copper."""
CODE = 'mining5_cementation'
BOOK = {
    'title': 'Cementation on Iron',
    'subtitle': 'An old method that recovers copper from solution using scrap iron',
    "chapters": [
        ('An old method', 'Cementation is an old method. Iron dissolves while copper deposits from the solution onto it, because iron is more reactive than copper.'),
        ('Displacement reaction', 'Iron gives up electrons to copper ions. The copper ions turn into solid copper on the iron surface.'),
        ('Copper from solution', 'Copper is recovered from dilute solutions, such as mine water, by this method. This makes the method useful for dilute streams that carry only a little copper.'),
        ('Scrap iron', 'Cheap scrap iron can serve as the reagent. It is consumed as it reacts.'),
        ('Kinetics and quality', 'Reaction speed depends on surface area, temperature and mixing. The copper made this way is called cement copper, and its quality depends on the conditions.'),
        ('Uses and waste', 'Cement copper is smelted or sold. The spent solution and the iron must be managed as waste.'),
    ],
    "test": [
        ('Why does iron recover copper from solution?', [('a', 'Copper is more reactive than iron'), ('b', 'Iron is lighter than water'), ('c', 'Copper dissolves in air'), ('d', 'Iron is more reactive than copper')], 'd'),
        ('What is the displacement reaction here?', [('a', 'Copper gives electrons to iron and melts'), ('b', 'Iron turns into gas'), ('c', 'Iron gives electrons to copper ions, and solid copper deposits'), ('d', 'Copper turns into sand')], 'c'),
        ('What is cement copper?', [('a', 'A type of concrete'), ('b', 'The solid copper made by cementation'), ('c', 'A kind of fuel'), ('d', 'A cleaning liquid')], 'b'),
        ('What does reaction speed depend on?', [('a', 'Surface area, temperature and mixing'), ('b', 'The colour of the tank'), ('c', 'The name of the operator'), ('d', 'The day of the week')], 'a'),
        ('What must be managed as waste?', [('a', 'The copper product only'), ('b', 'The lunch leftovers only'), ('c', 'The spent solution and the iron'), ('d', 'The clean water tap')], 'c'),
    ],
}
