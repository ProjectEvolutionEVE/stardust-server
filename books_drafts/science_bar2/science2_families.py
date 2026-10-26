"""The Periodic Table's Families: why elements in the same column behave alike. Science career, bar 2 (Scientist)."""
CODE = 'science2_families'
BOOK = {
    "title": 'The Periodic Table\'s Families',
    "subtitle": 'Why elements in the same column behave alike',
    "chapters": [
        ('A table of the elements',
         'The periodic table arranges the known elements in order of atomic number, which is the number of protons in each atom\'s nucleus. Each row is called a period, and each column is called a group. Reading the table tells you a lot about how an element will behave.'),
        ('Groups share behaviour',
         'Elements in the same group have the same number of electrons in their outer shell. Because the outer electrons do the chemistry, elements in one group tend to react in similar ways. That is why the table is so useful.'),
        ('The alkali metals',
         'The first column, apart from hydrogen, holds the alkali metals: lithium, sodium and potassium. They are soft, shiny and reactive, and they react strongly with water. They are never found pure in nature, because they react with the air around them.'),
        ('The noble gases',
         'The last column holds the noble gases, such as helium, neon and argon. Their outer shells are full, so they hardly react with anything. That is why argon is used to shield hot metal in welding, and why some lamps are filled with noble gases.'),
        ('The halogens',
         'The column next to the noble gases holds the halogens: fluorine, chlorine, bromine and iodine. They are very reactive, and they combine with alkali metals to make salts. Sodium and chlorine make sodium chloride, which is ordinary table salt.'),
        ('Metals and non-metals',
         'Metals sit on the left and in the middle of the table, and non-metals sit on the right. A few elements, such as silicon, lie along the dividing line and show some of both. Carbon, sulfur and phosphorus, found in the fields, are all non-metals.'),
    ],
    "test": [
        ('What is an element\'s atomic number?',
         [('a', 'Its atomic mass, rounded'), ('b', 'The number of protons in its nucleus'), ('c', 'The number of rows it sits in'), ('d', 'How many groups it has')], 'b'),
        ('What do elements in the same group share?',
         [('a', 'The same colour'), ('b', 'The same boiling point at any pressure'), ('c', 'Similar numbers of outer electrons, so similar chemistry'), ('d', 'The same mass')], 'c'),
        ('Which family is soft and shiny, and reacts strongly with water?',
         [('a', 'The noble gases'), ('b', 'The halogens'), ('c', 'The alkali metals'), ('d', 'The non-metals on the right')], 'c'),
        ('Why are the noble gases so unreactive?',
         [('a', 'Their outer shells are full'), ('b', 'They have no electrons at all'), ('c', 'They are always frozen'), ('d', 'They are too heavy to move')], 'a'),
        ('Which pair of elements makes table salt?',
         [('a', 'Iron and sulfur'), ('b', 'Gold and oxygen'), ('c', 'Carbon and hydrogen'), ('d', 'Sodium and chlorine')], 'd'),
    ],
}
