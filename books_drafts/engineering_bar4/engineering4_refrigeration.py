"""Refrigeration and Heat Pumps: moving heat against its natural direction, using a refrigerant that boils and condenses."""
CODE = 'engineering4_refrigeration'
BOOK = {
    "title": "Refrigeration and Heat Pumps",
    "subtitle": "Moving heat against its natural direction, using a refrigerant that boils and condenses",
    "chapters": [
        ("Vapour compression cycle",
         "A refrigerant boils at low pressure and absorbs heat. It is then compressed, releases heat as it condenses, and expands back to low pressure to begin again."),
        ("Refrigerant choice",
         "Refrigerants are chosen for their pressure, their heat-carrying properties and their environmental impact. Regulations limit which ones may be used."),
        ("Coefficient of performance",
         "The coefficient of performance, or COP, is the heat moved divided by the work put in. A higher number means less energy is needed for the same cooling or heating."),
        ("Heat pumps",
         "A heat pump moves heat from the cold outside into the warm inside. It can deliver more heat than the electricity it uses, and it can run in reverse to cool."),
        ("Service intervals",
         "The refrigerant charge, filters and coils need regular service. A low charge or a dirty coil cuts performance and raises running cost."),
        ("Running cost",
         "Running cost depends on the COP, the hours of use and the price of electricity. Good controls and servicing keep it low."),
    ],
    "test": [
        ("What does the refrigerant do in the evaporator?",
         [("a", "Freezes the room"), ("b", "Absorbs heat as it boils"), ("c", "Paints the pipes"), ("d", "Burns")], "b"),
        ("What is the coefficient of performance?",
         [("a", "The paint colour"), ("b", "The size of the room"), ("c", "The price"), ("d", "The heat moved divided by the work put in")], "d"),
        ("What does a heat pump do?",
         [("a", "Moves heat from cold to warm"), ("b", "Makes electricity from paint"), ("c", "Stops all heat flow"), ("d", "Only cools the sun")], "a"),
        ("What lowers the performance of a refrigerator?",
         [("a", "Clean coils"), ("b", "A full charge"), ("c", "A low refrigerant charge or a dirty coil"), ("d", "The right filters")], "c"),
        ("What decides running cost?",
         [("a", "The colour of the unit"), ("b", "The COP, the hours used and the price of electricity"), ("c", "The room number"), ("d", "The shop's name")], "b"),
    ],
}
