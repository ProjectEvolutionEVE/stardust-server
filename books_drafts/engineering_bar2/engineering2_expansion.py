"""Hot and Cold Parts: expansion and fit, and how to design for a temperature swing."""
CODE = 'engineering2_expansion'
BOOK = {
    "title": 'Hot and Cold Parts: Expansion and Fit',
    "subtitle": 'How parts grow and shrink with temperature, and how to design for it',
    "chapters": [
        ('Everything moves with heat',
         "Most materials grow when heated and shrink when cooled. The change for each degree is measured by a coefficient of "
         "thermal expansion. It is small for one degree, but over a long part, or across a large temperature swing, it adds "
         "up to millimetres."),
        ('Steel, aluminium and copper',
         "Steel grows about 12 millionths of its length for each degree Celsius. Aluminium grows about 23 millionths, nearly "
         "twice as much, and copper about 17 millionths. When two of these metals are fixed together, they move by different "
         "amounts, and that difference can crack a joint."),
        ('Expansion joints and gaps',
         "Long bridges, rails and pipes have expansion joints or deliberate gaps, so they can grow without breaking. The gap is "
         "sized for the largest change in temperature the structure will see."),
        ('Bimetal strips',
         "Two metals with different expansion rates, bonded together, bend when heated, because one side grows more than the "
         "other. Bimetal strips are used in simple thermostats and switches, where the bend is the useful movement."),
        ('Shrink fits',
         "A part can be heated so it grows and slides over a shaft, then cools and grips tightly. Or the shaft can be chilled so "
         "it shrinks into a hole. The result depends on the temperature change and the materials, so measure before you "
         "assemble."),
        ('Designing for the swing',
         "Design for the hottest and coldest temperatures the part will see, not only room temperature. A surface in sunlight "
         "can grow while its shaded side stays cool. Leave room for movement, and check every clearance on paper before you "
         "build."),
    ],
    "test": [
        ("Which grows more for each degree of heating: aluminium or steel?",
         [('a', 'Aluminium, about twice as much'), ('b', 'Steel, about twice as much'), ('c', 'They grow by the same amount'), ('d', 'Neither one grows')], 'a'),
        ("Why do long bridges and rails have expansion joints?",
         [('a', 'To make them lighter'), ('b', 'To stop them ever getting hot'), ('c', 'To hold the paint on'), ('d', 'So they can grow and shrink without cracking')], 'd'),
        ("Why does a bimetal strip bend when it is heated?",
         [('a', 'One metal shrinks in the heat'), ('b', 'The two metals grow by different amounts'), ('c', 'Heat makes it magnetic'), ('d', 'The strip melts')], 'b'),
        ("How does a shrink fit grip?",
         [('a', 'By gluing the parts together'), ('b', 'By welding the parts together'), ('c', 'Heating a part so it grows over a shaft, then letting it cool and grip; or chilling the shaft to shrink into a hole'), ('d', 'By magnets')], 'c'),
        ("What temperatures should a design be checked against?",
         [('a', 'Only room temperature'), ('b', 'Only the warmest day of the year'), ('c', 'The yearly average'), ('d', 'The hottest and coldest the part will see')], 'd'),
    ],
}
