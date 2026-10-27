"""Microchannel Cooling and Small-Scale Flow: how very small channels move heat well, and the pressure and clogging problems they bring."""
CODE = "engineering5_microchannel"
BOOK = {
    "title": "Microchannel Cooling and Small-Scale Flow",
    "subtitle": "Size effects, pressure drop, heat transfer and clogging",
    "chapters": [
        ("Very small channels", "Microchannels are channels less than about a millimetre across. They are used where compact, powerful cooling is needed in a small space."),
        ("Size effects", "At small sizes, surface forces and wall effects matter more, and simple flow rules can change. Designs must allow for this, not just scale down a large channel."),
        ("Pressure drop", "Narrow channels raise the pressure drop, so pumps must do more work to move the fluid. The extra pumping power is part of the cost of the design."),
        ("Heat transfer enhancement", "A microchannel has a large surface area for its volume. This gives high heat transfer in a small space, which is why the method is used for cooling electronics."),
        ("Manufacturing channels", "Channels are made by etching, machining or other methods. Very small features are hard to make consistently from part to part."),
        ("Clogging", "Small channels can clog with particles or deposits. Filtering and clean fluids are needed to keep the channels open over their life."),
    ],
    "test": [
        ("What are microchannels?", [("a", "Big tunnels for water"), ("b", "Very small channels for compact cooling"), ("c", "Pipes for a city's water supply"), ("d", "A type of flour")], "b"),
        ("What happens to pressure drop in narrow channels?", [("a", "It rises, so pumps must work harder"), ("b", "It falls to zero"), ("c", "It changes colour"), ("d", "It vanishes at once")], "a"),
        ("Why do microchannels transfer heat well?", [("a", "They are very hot in use"), ("b", "They are made of paper"), ("c", "They have no surface at all"), ("d", "They have a large surface area for their volume")], "d"),
        ("How are the channels made?", [("a", "By baking them in an oven"), ("b", "By etching, machining or other methods"), ("c", "By singing to the metal"), ("d", "By weaving the material")], "b"),
        ("What causes clogging?", [("a", "Too much sunlight"), ("b", "Cold tea spilled on the parts"), ("c", "Particles or deposits in small channels"), ("d", "Tall buildings nearby")], "c"),
    ],
}
