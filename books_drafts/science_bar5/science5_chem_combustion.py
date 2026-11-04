"""Combustion Chemistry and Flames: radical chains, flame speed, ignition, soot formation and pollutant chemistry."""
CODE = "science5_chem_combustion"
BOOK = {
    "title": "Combustion Chemistry and Flames",
    "subtitle": "Radical chains, flame speed, ignition and the pollutants of burning",
    "chapters": [
        ("Fire as chemistry", "Combustion is the rapid reaction of a fuel with an oxidant that releases heat and light. Behind the visible flame is a web of fast chemical steps. Radicals drive much of this web."),
        ("Radical chains", "Combustion runs through chain reactions with radical intermediates. Chain branching makes more radicals, which speeds the burning. Chain termination slows or stops the flame."),
        ("Flame speed", "Flame speed is how fast a flame front moves through an unburned mixture. It depends on the fuel, the mixture ratio and the temperature. Flame speed affects how stable a burner is."),
        ("Ignition", "Ignition is the start of self-sustaining combustion. It needs enough heat and radicals for the chain reaction to build. The ignition temperature varies with the fuel and conditions."),
        ("Soot formation", "Soot forms when fuel-rich regions break down into large carbon particles. Soot is a major pollutant and also shows incomplete combustion. Controlling mixing and temperature reduces soot."),
        ("Pollutants and modelling", "Burning produces pollutants such as carbon monoxide, nitrogen oxides and soot. Combustion models predict these from detailed chemical mechanisms and flow. Good models guide cleaner engines and burners."),
    ],
    "test": [
        ("What drives much of combustion chemistry?",
         [("a", "Sand grains"), ("b", "Sunlight on the floor"), ("c", "Radical intermediates in chain reactions"), ("d", "Water droplets")], "c"),
        ("What does chain branching do?",
         [("a", "It removes all oxygen"), ("b", "It cools the flame to zero"), ("c", "It stops every reaction"), ("d", "It makes more radicals and speeds the burning")], "d"),
        ("What is flame speed?",
         [("a", "How fast a flame front moves through an unburned mixture"), ("b", "How fast a candle is lit"), ("c", "How fast a person runs"), ("d", "How fast the room gets dark")], "a"),
        ("What is soot?",
         [("a", "A kind of pure water"), ("b", "Large carbon particles formed in fuel-rich, incomplete burning"), ("c", "A white metal"), ("d", "A type of glass")], "b"),
        ("What do combustion models predict?",
         [("a", "The taste of the fuel"), ("b", "Pollutants from detailed chemical mechanisms and flow"), ("c", "The colour of the sky"), ("d", "The price of the fuel tank")], "b"),
    ],
}
