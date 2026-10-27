"""Combustion: Fuel, Air and Flame. Mixing fuel and air in the right ratio, and building burners that burn cleanly."""
CODE = 'engineering4_combustion'
BOOK = {
    "title": "Combustion: Fuel, Air and Flame",
    "subtitle": "Mixing fuel and air in the right ratio, and building burners that burn cleanly",
    "chapters": [
        ("Stoichiometry",
         "Stoichiometry is the exact fuel-to-air ratio at which all the fuel burns, with no spare fuel or air left over. It is the reference point for every burner."),
        ("Flame types",
         "In a premixed flame, the fuel and air are mixed before they burn. In a diffusion flame, they mix as they burn. Each type suits different burners."),
        ("Air-fuel ratio",
         "Too much air cools the flame and wastes heat. Too little air leaves unburnt fuel, which wastes energy and makes soot."),
        ("Emissions in general terms",
         "Good combustion burns the fuel fully and cuts harmful outputs. Controlling the air-fuel ratio is the main tool for doing so."),
        ("Burner design",
         "A burner must mix, ignite and hold the flame steady across its load range. Good design gives stable flames and clean burning."),
        ("Safety and checks",
         "Safe burners use flame sensors, pressure checks and a purge step before ignition. Skipping the purge can leave gas in the chamber."),
    ],
    "test": [
        ("What is stoichiometry?",
         [("a", "The study of paint"), ("b", "A type of steel"), ("c", "The exact ratio at which all fuel burns with no spare fuel or air left"), ("d", "A measure of weight")], "c"),
        ("What happens when there is too little air?",
         [("a", "Unburnt fuel and soot"), ("b", "More light"), ("c", "Cooler metal"), ("d", "A clean flame")], "a"),
        ("What is a premixed flame?",
         [("a", "A flame with fuel painted on"), ("b", "A flame made in a freezer"), ("c", "A flame that only burns in space"), ("d", "A flame where fuel and air are mixed before they burn")], "d"),
        ("What does a purge do in a burner?",
         [("a", "Paints the burner"), ("b", "Clears gas out of the chamber before ignition"), ("c", "Cools the fuel"), ("d", "Adds colour")], "b"),
        ("What is the main tool for cleaner burning?",
         [("a", "Controlling the air-fuel ratio"), ("b", "Painting the pipe"), ("c", "Louder fans"), ("d", "Cheaper paint")], "a"),
    ],
}
