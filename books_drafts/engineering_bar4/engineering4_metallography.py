"""Metallography: sample preparation, etching, grain size measurement, inclusions and linking microstructure to strength."""
CODE = "engineering4_metallography"
BOOK = {
    "title": "Metallography: Grains Under the Microscope",
    "subtitle": "Preparing samples, etching and reading the grains",
    "chapters": [
        ("Looking inside metal",
         "Metallography studies the structure of metal, usually with a microscope. The grains, the phases and the inclusions tell a story about how the metal was made and treated. The structure links directly to the strength of the part."),
        ("Preparing a sample",
         "A sample is cut, mounted, ground and polished to a smooth mirror finish. Each step removes the damage left by the step before. A poor preparation hides the real structure."),
        ("Etching",
         "Etching uses a chemical to reveal the grain boundaries and phases. Different phases react differently and show up as contrast under the microscope. The right etchant depends on the metal."),
        ("Grain size",
         "Grain size is measured by counting grains or comparing with standard charts. Smaller grains usually give a stronger and tougher metal. The measurement is a standard test used in quality control."),
        ("Inclusions",
         "Inclusions are small particles of oxides, sulphides or other material trapped in the metal. They can start cracks, especially under fatigue. Inspectors look at the size and number of inclusions when they judge a steel."),
        ("Linking structure to strength",
         "Engineers use the structure seen in a sample to predict strength, toughness and fatigue life. A fine, even structure usually performs better than a coarse, uneven one. Metallography connects what the furnace did to what the part can do."),
    ],
    "test": [
        ("What does metallography study?", [("a", "The structure of metal, usually under a microscope"), ("b", "The price of a metal in shops"), ("c", "The weather above a factory"), ("d", "The sound a metal makes")], "a"),
        ("Why must a sample be polished smooth?", [("a", "Polishing changes the grain size to zero"), ("b", "A rough sample is always stronger"), ("c", "Polishing adds more metal"), ("d", "Each step removes damage from the step before, so the real structure shows")], "d"),
        ("What does etching reveal?", [("a", "The price of the sample"), ("b", "The grain boundaries and phases"), ("c", "The temperature of the room"), ("d", "The weight of the furnace")], "b"),
        ("Usually, what do smaller grains give a metal?", [("a", "A metal that cannot be measured"), ("b", "A weaker metal"), ("c", "A stronger and tougher metal"), ("d", "A metal with no structure")], "c"),
        ("Why are inclusions a concern?", [("a", "They make metal lighter for free"), ("b", "They make metal shiny"), ("c", "They can start cracks, especially under fatigue"), ("d", "They have no effect")], "c"),
    ],
}
