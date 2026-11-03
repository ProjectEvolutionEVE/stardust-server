"""Planetary Interiors and Gravity Fields: gravity field measurement, moment of inertia, tidal Love numbers, internal layering, density models and interior uncertainty."""
CODE = "science4_planet_interiors"
BOOK = {
    "title": "Planetary Interiors and Gravity Fields",
    "subtitle": "Gravity fields, moment of inertia and what lies inside",
    "chapters": [
        ("Measuring gravity from orbit", "Small changes in a spacecraft's orbit reveal how a planet's gravity varies from place to place. Those variations tell scientists how the mass is spread inside the planet."),
        ("Moment of inertia", "The moment of inertia describes how a body's mass is spread around its spin axis. A value below that of a uniform sphere shows that the mass is concentrated toward the centre."),
        ("Tidal Love numbers", "A tidal Love number describes how much a planet deforms under the tidal pull of a nearby body. The number reveals how rigid or fluid the planet's interior is."),
        ("Internal layering", "A planet with a dense core and a lighter mantle has distinct layers. Gravity data can show that layers exist, but they do not always show how thick each layer is."),
        ("Density models", "Scientists build density models that fit the measured mass and size. Many different models can fit the same data, so the results carry uncertainty."),
        ("Interior uncertainty", "Models of a planet's interior always carry some uncertainty, and new measurements help narrow it. Honest error bars are a normal part of good planetary science."),
    ],
    "test": [
        ("What does a planet's gravity field reveal about its interior?",
         [("a", "Its colour"), ("b", "How its mass is spread inside"), ("c", "Its favourite food"), ("d", "Its exact temperature at noon")], "b"),
        ("What does the moment of inertia describe?",
         [("a", "How fast light travels"), ("b", "The number of moons"), ("c", "The colour of the surface"), ("d", "How a body's mass is spread around its spin axis")], "d"),
        ("What does a tidal Love number show?",
         [("a", "The number of craters"), ("b", "The speed of a comet"), ("c", "How much a planet deforms under tides, which reveals its rigidity"), ("d", "The colour of its sky")], "c"),
        ("What is true of density models?",
         [("a", "Many different models can fit the same data"), ("b", "Only one model can ever fit"), ("c", "They are always exact"), ("d", "They never use mass")], "a"),
        ("Which statement about planetary interiors is most accurate?",
         [("a", "They are always fully known"), ("b", "Telescopes can see them directly"), ("c", "They have no layers"), ("d", "Scientists work with honest uncertainty and narrow it with new data")], "d"),
    ],
}
