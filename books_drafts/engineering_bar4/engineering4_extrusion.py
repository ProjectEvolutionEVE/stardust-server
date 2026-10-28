"""Extrusion: Shapes Pushed Through a Die. Heating a billet and forcing it through a die to make a long profile."""
CODE = 'engineering4_extrusion'
BOOK = {
    "title": "Extrusion: Shapes Pushed Through a Die",
    "subtitle": "Heating a billet and forcing it through a die to make a long profile",
    "chapters": [
        ("What extrusion is",
         "A billet of metal is pushed through an opening in a die, and it comes out in the shape of that opening. Aluminium window frames and rails are a common example. The result is a long profile of constant cross-section."),
        ("Billet heating",
         "The billet is heated so it becomes soft enough to flow, but not so hot that it melts. The right temperature keeps the surface clean and the shape true. Heating is carefully controlled for each alloy."),
        ("Die design",
         "The die sets the profile. Hollow shapes need special dies that split and rejoin the flow. Sharp corners and thin walls are harder to fill, so the design allows for how the metal flows."),
        ("Speed and quality",
         "Pushing faster saves time, but it can overheat the surface and spoil the profile. The ram speed is set so the profile comes out straight and smooth. Operators watch the surface as the run goes on."),
        ("Profile tolerances",
         "An extruded profile can change size a little as it cools. Dimensions are checked after each run, and the results are kept within the stated tolerance. Small drifts are corrected early."),
        ("Why aluminium suits many jobs",
         "Aluminium is light, takes extrusion well, and resists rust in ordinary air. These qualities explain why it is used for so many frames, rails and heat sinks. Many shapes can be made in one pass through the die."),
    ],
    "test": [
        ("What comes out of an extrusion die?",
         [("a", "Metal with the shape of the die opening"), ("b", "Liquid metal"), ("c", "Metal powder"), ("d", "A wire of random shape")], "a"),
        ("Why is a billet heated before extrusion?",
         [("a", "To paint it"), ("b", "To make it heavier"), ("c", "To make it soft enough to flow without melting"), ("d", "To remove oxygen from the air")], "c"),
        ("Which shape is hardest to fill in extrusion?",
         [("a", "A simple round rod"), ("b", "A thin wall with sharp corners"), ("c", "A square block"), ("d", "A large flat plate")], "b"),
        ("Why is aluminium common in extruded frames?",
         [("a", "It is heavy and cheap to melt"), ("b", "It is magnetic"), ("c", "It is brittle"), ("d", "It is light and resists rust in air")], "d"),
        ("What is the risk of pushing a billet too fast?",
         [("a", "Overheating the surface and spoiling the profile"), ("b", "The profile gets longer for free"), ("c", "The die grows by itself"), ("d", "The billet cools to ice")], "a"),
    ],
}
