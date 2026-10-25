"""Elements and Compounds: atoms, elements, compounds, and how to read the formula of a mineral. Science career, bar 1 (Research Assistant)."""
CODE = 'science1_elements'
BOOK = {
    "title": 'Elements and Compounds',
    "subtitle": 'Atoms, and how to read the formula of a mineral',
    "chapters": [
        ('Everything is made of atoms',
         'Every material is built from tiny particles called atoms. About 118 different elements are known, and every mineral in the fields is made from some of them. Atoms are far too small to see, but chemists count and weigh them with great care.'),
        ('Elements: one kind of atom',
         'An element is a substance made of only one kind of atom. Native gold, written Au, is an element, and so is pure carbon, which is the diamond in the fields. Iron, sulfur and copper are elements too.'),
        ('Compounds: atoms joined together',
         'A compound is two or more elements joined together by chemical bonds. Most ore minerals are compounds. Chalcopyrite, written CuFeS2, is made of copper, iron and sulfur joined into one crystal.'),
        ('Reading a formula',
         'The letters in a formula are the elements, and a small number after a letter counts its atoms. No number means one atom. So CuFeS2 has one copper atom, one iron atom and two sulfur atoms, and galena, PbS, has one lead atom for each sulfur atom.'),
        ('Share by weight',
         'Each kind of atom has a known atomic weight. Add up the weights in the formula, then one element\'s share is its weight divided by the total. For chalcopyrite, copper is about 34.6 per cent of the total weight, so 100 kg of this ore gives about 34.6 kg of copper. The rest is slag.'),
        ('What this means in the game',
         'A bigger share means more metal from each kilo of ore. Hematite, written Fe2O3, is about 70 per cent iron by weight, which is why it is such a useful iron ore. Every ore piece in the game is pure mineral, so its formula tells you its yield.'),
    ],
    "test": [
        ('What is an element?',
         [('a', 'A mixture of several minerals'), ('b', 'A mineral with water in it'), ('c', 'A crystal from a debris field'), ('d', 'A substance made of only one kind of atom')], 'd'),
        ('What is a compound?',
         [('a', 'A single atom of gold'), ('b', 'Two or more elements joined chemically'), ('c', 'Any mixture of sand and ice'), ('d', 'A rock that is only one kind of atom')], 'b'),
        ('In the formula CuFeS2, how many sulfur atoms are there?',
         [('a', 'One'), ('b', 'Three'), ('c', 'Two'), ('d', 'None')], 'c'),
        ('Native gold, written Au, is what kind of substance?',
         [('a', 'An element'), ('b', 'A compound'), ('c', 'A mixture'), ('d', 'Water')], 'a'),
        ('Hematite is Fe2O3. Roughly what share of its weight is iron?',
         [('a', 'About 30 per cent'), ('b', 'About 70 per cent'), ('c', 'About 100 per cent'), ('d', 'About 5 per cent')], 'b'),
    ],
}
