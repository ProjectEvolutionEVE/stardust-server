"""Thermal Insulation Materials: slowing heat through walls and pipes, and weighing the cost of insulation against the energy saved."""
CODE = 'engineering4_insulation'
BOOK = {
    "title": "Thermal Insulation Materials",
    "subtitle": "Slowing heat through walls and pipes, and weighing its cost against the energy saved",
    "chapters": [
        ("Conductivity",
         "Thermal conductivity measures how easily heat flows through a material. A low conductivity makes a good insulator."),
        ("Mineral wool",
         "Mineral wool traps still air in its fibres, which slows heat flow. It is widely used for loft and wall insulation."),
        ("Foams",
         "Foams trap gas in closed cells and resist heat flow. Foam panels and pipe covers are common examples."),
        ("Aerogel",
         "Aerogel is a very light solid, mostly air, with very low conductivity. It costs more than common insulation materials."),
        ("Multilayer insulation",
         "Thin reflective layers with gaps between them cut radiant heat. It is used in spacecraft and in some cryogenic systems."),
        ("The money side",
         "Insulation has a price, and its payback is the energy it saves over its life. A thicker layer saves more but costs more, so the best thickness balances the two."),
    ],
    "test": [
        ("What does thermal conductivity measure?",
         [("a", "The colour of a material"), ("b", "How easily heat flows through it"), ("c", "Its weight"), ("d", "Its smell")], "b"),
        ("How does mineral wool insulate?",
         [("a", "By burning"), ("b", "By being wet"), ("c", "By being metal"), ("d", "By trapping still air in its fibres")], "d"),
        ("What is aerogel?",
         [("a", "A very light solid, mostly air, with low conductivity"), ("b", "A metal"), ("c", "A paint"), ("d", "A glass cup")], "a"),
        ("What is multilayer insulation used for?",
         [("a", "Cups"), ("b", "Bread"), ("c", "Cutting radiant heat, as in spacecraft"), ("d", "Bicycles")], "c"),
        ("How is the best thickness of insulation found?",
         [("a", "By picking the thickest"), ("b", "By balancing the energy saved against the cost of the insulation"), ("c", "By guessing"), ("d", "By colour")], "b"),
    ],
}
