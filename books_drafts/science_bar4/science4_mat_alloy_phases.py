"""Alloy Phase Diagrams and Heat Treatment: binary phase diagrams, eutectic and peritectic points, the lever rule, quenching and tempering, precipitation hardening and microstructure control."""
CODE = "science4_mat_alloy_phases"
BOOK = {
    "title": "Alloy Phase Diagrams and Heat Treatment",
    "subtitle": "Phase diagrams, quenching, tempering and microstructure",
    "chapters": [
        ("Binary phase diagrams", "A binary phase diagram shows which phases of a two-component alloy are stable at each temperature and composition. Engineers use it as a map when they plan heat treatments."),
        ("Eutectic and peritectic points", "A eutectic point is where a liquid turns into two solid phases at one temperature. A peritectic point is where a liquid and one solid react to form a different solid."),
        ("The lever rule", "The lever rule gives the amount of each phase in a two-phase region. The fractions depend on how far the alloy's composition sits from each phase boundary."),
        ("Quenching and tempering", "Quenching cools steel quickly, which can make it hard but brittle. Tempering reheats the hardened steel to a lower temperature, trading some hardness for toughness."),
        ("Precipitation hardening", "Some alloys become stronger when they are heated to dissolve the added element, quenched quickly, then held at a moderate temperature so fine particles form. Tiny particles form inside the metal and block the movement of defects called dislocations."),
        ("Microstructure control", "The microstructure, including grain size and the mix of phases, sets the strength and toughness of an alloy. Heat treatment is how engineers control the microstructure."),
    ],
    "test": [
        ("What does a binary phase diagram show?",
         [("a", "Which phases are stable at each temperature and composition"), ("b", "Sales of steel"), ("c", "The shape of a bridge"), ("d", "The colour of a metal")], "a"),
        ("What is a eutectic point?",
         [("a", "The melting point of ice"), ("b", "The place where a planet's core forms"), ("c", "A type of crystal dome"), ("d", "Where one liquid turns into two solid phases at one temperature")], "d"),
        ("What does the lever rule give?",
         [("a", "The price of an alloy"), ("b", "The colour of a phase"), ("c", "The amount of each phase in a two-phase region"), ("d", "The speed of a tool")], "c"),
        ("What does quenching do to steel?",
         [("a", "Makes it soft and slow"), ("b", "Cools it fast, which can make it hard but brittle"), ("c", "Turns it into a gas"), ("d", "Makes it float")], "b"),
        ("What does tempering do?",
         [("a", "It melts steel"), ("b", "It cools steel instantly"), ("c", "It paints steel"), ("d", "It reheats hardened steel to a lower temperature, trading some hardness for toughness")], "d"),
    ],
}
