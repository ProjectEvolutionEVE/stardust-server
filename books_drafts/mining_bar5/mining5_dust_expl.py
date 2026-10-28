"""Dust Explosions and Their Prevention: how fine combustible dust can explode, and how inerting, venting, housekeeping and testing prevent it."""
CODE = "mining5_dust_expl"
BOOK = {
    "title": "Dust Explosions and Their Prevention",
    "subtitle": "Dust clouds, ignition energy, inerting, venting and housekeeping",
    "chapters": [
        ("Dust that can burn",
         "Fine combustible dust, such as coal, grain or some metals, can burn very fast when it is spread in air. A dust cloud of the right density can explode. Dust explosions have caused serious harm in many industries."),
        ("The dust cloud",
         "The dust must be in the right concentration to explode. Too little dust will not burn fully, and too much may not mix well with the air. Keeping dust clouds away from ignition is the first step in prevention."),
        ("Ignition energy",
         "A dust cloud needs an ignition source with enough energy. Sparks, hot surfaces and flames can all provide it. Testing shows how much energy a dust needs to catch fire."),
        ("Inerting",
         "Inerting reduces the oxygen in the space with an inert gas, such as nitrogen. With too little oxygen, the dust cloud cannot burn. Inerting needs careful control and monitoring of the gas level."),
        ("Explosion venting",
         "Explosion vents are weak panels that open to release pressure safely if an explosion starts. Venting limits the damage to the structure. Vents must be placed and sized by a qualified engineer."),
        ("Housekeeping and testing",
         "Settled dust can be lifted by a shock wave and make a larger cloud, so it must be removed regularly. Laboratory tests measure how explosive a dust is and guide the controls. Clean, tested and well-designed plants are much safer."),
    ],
    "test": [
        ("Which kind of dust can explode when spread in air?",
         [("a", "Fine combustible dust such as coal or grain"), ("b", "Clean water"), ("c", "Dry sand from a beach only"), ("d", "Snow")], "a"),
        ("What does inerting do?",
         [("a", "Adds more oxygen"), ("b", "Paints the dust"), ("c", "Reduces oxygen so a dust cloud cannot burn"), ("d", "Makes the dust heavier")], "c"),
        ("What is an explosion vent?",
         [("a", "A window for the view"), ("b", "A pipe for drinking water"), ("c", "A lamp"), ("d", "A weak panel that opens to release pressure safely")], "d"),
        ("Why must settled dust be removed regularly?",
         [("a", "Settled dust is always wet"), ("b", "A shock wave can lift it and make a larger cloud"), ("c", "Settled dust makes the floor shine"), ("d", "Settled dust is good for the plant")], "b"),
        ("What do laboratory tests show?",
         [("a", "How explosive a dust is, to guide the controls"), ("b", "The taste of the dust"), ("c", "The name of the dust's owner"), ("d", "The weather next week")], "a"),
    ],
}
