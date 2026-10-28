"""Gas Turbines and Jet Engines: compressing air, burning fuel and expanding the hot gas through a turbine."""
CODE = 'engineering4_gas_turbine'
BOOK = {
    "title": "Gas Turbines and Jet Engines",
    "subtitle": "Compressing air, burning fuel and expanding the hot gas through a turbine",
    "chapters": [
        ("The Brayton cycle",
         "A gas turbine compresses air, adds fuel and burns it, then expands the hot gas through a turbine. This sequence is the Brayton cycle."),
        ("The compressor",
         "The compressor squeezes incoming air to high pressure. It sits on the same shaft as the turbine, and the turbine drives it."),
        ("The combustor",
         "Fuel burns in the combustor, raising the temperature of the gas. The combustor must hold a stable flame across the engine's operating range."),
        ("The turbine",
         "Hot gas expands through the turbine blades and spins the shaft. In a jet, enough energy is left over to produce thrust."),
        ("Thrust",
         "A jet engine pushes the gas backwards out of its nozzle, and the reaction pushes the engine forward. Thrust comes from the change in momentum of the air."),
        ("Built up in stages",
         "A jet engine is built from stages of compressor and turbine, each designed for its job. Each stage adds pressure or extracts energy, and together they set the engine's efficiency."),
    ],
    "test": [
        ("What is the Brayton cycle?",
         [("a", "A paint process"), ("b", "The cycle of a gas turbine: compress, burn, expand"), ("c", "A type of rope"), ("d", "A car brake")], "b"),
        ("What does the compressor do?",
         [("a", "Cools the room"), ("b", "Burns fuel"), ("c", "Makes paint"), ("d", "Squeezes incoming air to high pressure")], "d"),
        ("How is a jet's thrust produced?",
         [("a", "By pushing the gas backwards out of the nozzle"), ("b", "By painting the wings"), ("c", "By heating the room"), ("d", "By cooling the fuel")], "a"),
        ("What drives the compressor?",
         [("a", "A battery"), ("b", "A bicycle"), ("c", "The turbine, on the same shaft"), ("d", "A windmill")], "c"),
        ("What does the combustor do?",
         [("a", "Cools the air"), ("b", "Reads the weather"), ("c", "Stores fuel"), ("d", "Burns fuel and raises the gas temperature")], "d"),
    ],
}
