"""Nanofiltration of lithium brines: pore sizes, divalent rejection, magnesium and lithium separation, pretreatment, scale and economics."""
CODE = 'mining5_nanofilt'
BOOK = {
    'title': 'Nanofiltration of Lithium Brines',
    'subtitle': 'Separating lithium from the other salts in natural brine',
    "chapters": [
        ('Brine from salt flats', 'Lithium is found in some natural brines. Nanofiltration can help separate it from the other salts in the brine.'),
        ('Pore sizes', 'Nanofiltration membranes have pores around a nanometre across. They let some ions pass and hold others back.'),
        ('Divalent rejection', 'Membranes reject ions with two charges, such as magnesium, more strongly than ions with one charge, such as lithium. This helps separate them.'),
        ('Pretreatment', 'Brines are cleaned first to remove solids and compounds that would foul the membranes. Skipping this step shortens the life of the membranes.'),
        ('Scale and economics', 'Good results at scale need the membrane system to handle large flows at a reasonable cost. Every extra membrane stage adds to the cost of the plant.'),
        ('Limits', 'Separation is never perfect. Later steps are still needed to reach pure lithium.'),
    ],
    "test": [
        ('About how large are nanofiltration pores?', [('a', 'About a metre'), ('b', 'About a centimetre'), ('c', 'About a kilometre'), ('d', 'About a nanometre')], 'd'),
        ('Which ions does nanofiltration reject more strongly?', [('a', 'Single-charged ions such as lithium'), ('b', 'Divalent ions such as magnesium'), ('c', 'Gases such as oxygen'), ('d', 'Solid grains of sand')], 'b'),
        ('What is pretreatment for?', [('a', 'Removing solids and compounds that would foul the membranes'), ('b', 'Adding colour to the brine'), ('c', 'Cooling the brine to ice'), ('d', 'Making the brine louder')], 'a'),
        ('Why are later steps still needed after nanofiltration?', [('a', 'Membranes are always perfect'), ('b', 'Lithium is never present'), ('c', 'Separation is never perfect'), ('d', 'The brine is pure from the start')], 'c'),
        ('What must a membrane system cover at scale?', [('a', 'Only a single bucket of brine'), ('b', 'The office lighting'), ('c', 'Large flows at a reasonable cost'), ('d', 'The canteen menu')], 'c'),
    ],
}
