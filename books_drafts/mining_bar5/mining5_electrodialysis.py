"""Electrodialysis for salts: ion-selective membranes, brine concentration, energy use, fouling and use."""
CODE = 'mining5_electrodialysis'
BOOK = {
    'title': 'Electrodialysis for Salts',
    'subtitle': 'Using charged membranes and an electric field to concentrate brine',
    "chapters": [
        ('Charged membranes', 'Electrodialysis uses ion-selective membranes and an electric field. The field moves salt ions through a stack of membranes.'),
        ('Concentration', 'Ions are pulled out of one stream into another. One side becomes more concentrated brine and the other becomes fresher water.'),
        ('Brine', 'Brine is salt water. Electrodialysis can concentrate it, which reduces the volume that must be treated later.'),
        ('Energy', 'The process uses electricity. Its energy cost depends on the salt concentration and the flow.'),
        ('Fouling', 'Scale and organic matter can coat the membranes and reduce their performance. Pretreatment limits fouling.'),
        ('Use', 'The process is used where its salt separation suits the feed water and the energy cost is acceptable. Clean feed water and good design make the process more reliable.'),
    ],
    "test": [
        ('What drives ions through electrodialysis membranes?', [('a', 'A strong wind'), ('b', 'An electric field'), ('c', 'A heavy weight'), ('d', 'Sunlight')], 'b'),
        ('What does electrodialysis do with brine?', [('a', 'Turns it into metal'), ('b', 'Freezes it solid'), ('c', 'Sends it into the air'), ('d', 'Concentrates it')], 'd'),
        ('What coats membranes and reduces their performance?', [('a', 'Scale and organic matter, called fouling'), ('b', 'Clean fresh water'), ('c', 'Dry sand'), ('d', 'Bright light')], 'a'),
        ('What limits fouling?', [('a', 'Turning the power off at lunch'), ('b', 'Using bigger trucks'), ('c', 'Pretreatment of the feed'), ('d', 'Painting the membranes')], 'c'),
        ('What does the energy cost of electrodialysis depend on?', [('a', 'The colour of the plant'), ('b', 'The name of the operator'), ('c', 'The day of the week'), ('d', 'Salt concentration and flow')], 'd'),
    ],
}
