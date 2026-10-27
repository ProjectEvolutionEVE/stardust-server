"""Potash flotation chemistry: sylvite and halite, amine collectors, saturated brine, salt separation, cost and control."""
CODE = 'mining5_potash'
BOOK = {
    'title': 'Potash Flotation Chemistry',
    'subtitle': 'Separating potassium salt from common salt by bubbles and chemistry',
    "chapters": [
        ('Potash', 'Potash is a potassium salt, used mainly for fertiliser. It is mined from ore that contains sylvite and halite.'),
        ('Sylvite and halite', 'Sylvite is potassium chloride. Halite is common salt, sodium chloride. The two are hard to separate by size, so flotation is used.'),
        ('Amine collectors', 'Amine collectors coat one mineral so that it sticks to bubbles and floats. The other mineral is left to sink.'),
        ('Saturated brine', 'The process runs in saturated brine. The brine keeps the salts from dissolving into the wrong stream.'),
        ('Cost and control', 'Reagent cost and changes in the feed both matter. Operators control reagent dosing and the feed to keep costs in check.'),
        ('Why it matters', 'Potash supplies potassium for crops. Efficient separation helps keep food production affordable.'),
    ],
    "test": [
        ('What is potash mainly used for?', [('a', 'Making glass'), ('b', 'Building roads'), ('c', 'Fertiliser'), ('d', 'Making paper')], 'c'),
        ('What is sylvite?', [('a', 'Common salt'), ('b', 'A type of steel'), ('c', 'A kind of coal'), ('d', 'Potassium chloride')], 'd'),
        ('What does an amine collector do?', [('a', 'Dissolves all the salt'), ('b', 'Makes one mineral stick to bubbles and float'), ('c', 'Cools the brine'), ('d', 'Turns the brine into gas')], 'b'),
        ('What solution does the process run in?', [('a', 'Saturated brine'), ('b', 'Pure distilled water'), ('c', 'Fuel oil'), ('d', 'Milk')], 'a'),
        ('What do operators control to manage cost?', [('a', 'The colour of the plant'), ('b', 'Reagent dosing and the feed'), ('c', 'The number of radios'), ('d', 'The name of the shift')], 'b'),
    ],
}
