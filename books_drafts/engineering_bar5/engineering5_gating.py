"""Gating System Design: sprues, runners, ingates, filling speed, turbulence control and filter placement."""
CODE = "engineering5_gating"
BOOK = {
    "title": "Gating System Design",
    "subtitle": "The channels that bring molten metal safely into a mould",
    "chapters": [
        ("The route into the mould",
         "The gating system is the set of channels that carry molten metal from the pouring cup into the mould cavity. It is the route the metal takes. A good gating system fills the mould smoothly and cleanly."),
        ("Sprue, runner and ingate",
         "The sprue is the vertical channel from the pouring cup. The runner carries metal sideways, and the ingate is the last opening into the cavity. Each part has its own job along the route."),
        ("Filling speed",
         "The metal must fill the mould fast enough to avoid freezing early, but not so fast that it erodes the mould or churns. Engineers set the channel sizes to give a steady filling speed."),
        ("Turbulence control",
         "Turbulent metal traps oxides and gas, and these become defects in the casting. Gently shaped channels, and a steady flow, keep the metal calm. Sharp bends and sudden drops cause the most turbulence."),
        ("Filter placement",
         "A ceramic filter in the runner catches slag and oxide before they reach the cavity. Its place in the system matters, because it must be full of metal and not blocked early. Filters are a simple way to raise casting quality."),
        ("Designing the system",
         "The gating system is designed with the riser and the part, not on its own. Simulation shows the flow before the mould is made. Changes at the design stage are cheap, and changes after pouring are costly."),
    ],
    "test": [
        ("What does the gating system do?",
         [("a", "It cools the finished part"), ("b", "It paints the part"), ("c", "It counts the parts"), ("d", "It carries molten metal from the pouring cup into the mould")], "d"),
        ("What is the sprue?",
         [("a", "The vertical channel from the pouring cup"), ("b", "The label on the mould"), ("c", "The final coat of paint"), ("d", "The handle of the ladle")], "a"),
        ("Why must filling speed be controlled?",
         [("a", "Speed has no effect on casting"), ("b", "Too slow freezes early; too fast erodes the mould and churns the metal"), ("c", "Only slow pouring is allowed by law"), ("d", "Speed changes the colour of the metal")], "b"),
        ("What does turbulence cause in a casting?",
         [("a", "The casting becomes lighter"), ("b", "The casting becomes transparent"), ("c", "Oxides and gas get trapped and become defects"), ("d", "The casting is cooled faster")], "c"),
        ("What does a ceramic filter catch?",
         [("a", "Sunlight"), ("b", "Water vapour in the room"), ("c", "Wood chips"), ("d", "Slag and oxide before they reach the cavity")], "d"),
    ],
}
