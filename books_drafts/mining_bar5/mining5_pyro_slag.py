"""Slag Fuming and Zinc Recovery: how a furnace drives zinc and lead out of slag and into a saleable oxide."""
CODE = 'mining5_pyro_slag'
BOOK = {
    "title": 'Slag Fuming and Zinc Recovery',
    "subtitle": 'Driving zinc and lead out of slag and into saleable oxide',
    "chapters": [
        ('Why slag still holds metal', 'Smelter slag can still hold zinc and lead after the main metal is taken out. These metals are valuable and worth recovering. Plants treat the slag to capture them before it is stored.'),
        ('Fuming', 'In fuming, the molten slag is blown with air and fuel, often coal. Zinc and lead are driven off as vapour and are collected as fine dust. The leftover slag is cleaner and safer to store.'),
        ('The Waelz kiln', 'A Waelz kiln is a long rotating furnace that treats slag and dust together. It turns zinc and lead into oxides that can be collected. The kiln is one of the most common tools for this job.'),
        ('Zinc oxide', 'The collected zinc oxide is a useful product, and it is sold or sent to zinc refineries. The oxide must be tested for purity and for other elements. Buyers pay for the grade they receive.'),
        ('Lead', 'Lead oxide is collected along with zinc in the same dust. It is separated and sent for its own refining. Plants treat lead with great care because it is toxic.'),
        ('Residue and economics', 'The leftover slag still has to be stored safely. Plants balance the value of the zinc and lead against the energy and fuel the process uses. Fuming pays when metal prices are high enough.'),
    ],
    "test": [
        ('Why is smelter slag treated for zinc and lead?', [('a', 'These metals can still be valuable and worth recovering'), ('b', 'Slag is a sweet food'), ('c', 'Slag is a fuel for cars'), ('d', 'Slag is made of gold only')], 'a'),
        ('What happens to zinc and lead in fuming?', [('a', 'They turn into water'), ('b', 'They are driven off as vapour and collected as dust'), ('c', 'They freeze into ice'), ('d', 'They float off into space')], 'b'),
        ('What kind of furnace is a Waelz kiln?', [('a', 'A small paper oven'), ('b', 'A pottery wheel'), ('c', 'A long rotating furnace'), ('d', 'A sealed glass jar')], 'c'),
        ('What product is collected from the Waelz kiln for zinc?', [('a', 'Sugar syrup'), ('b', 'Wood pulp'), ('c', 'Clear glass'), ('d', 'Zinc oxide')], 'd'),
        ('Why does lead need great care?', [('a', 'Lead is toxic'), ('b', 'Lead is sweet'), ('c', 'Lead is a gas at room temperature'), ('d', 'Lead is never found in slag')], 'a'),
    ],
}
