"""Earthquake engineering: seismic waves, response spectra, ductile detailing, base isolation and lessons from real quakes."""
CODE = "engineering4_earthquake"
BOOK = {
    "title": "Earthquake Engineering: Ductility and Isolation",
    "subtitle": "Seismic waves, ductile detailing and base isolation",
    "chapters": [
        ("Shaking from the ground",
         "An earthquake sends seismic waves through the ground, and the waves shake buildings from below. The shaking is sideways as well as up and down. A building must be designed to move safely with the ground."),
        ("Response spectra",
         "A response spectrum shows how strongly structures of different stiffness respond to a given quake. Tall, flexible buildings respond differently from short, stiff ones. Designers use spectra to pick the design forces for their structure."),
        ("Ductile detailing",
         "Ductility is the ability to bend and deform without breaking suddenly. Ductile detailing places steel reinforcement so that a frame yields in a controlled way. A ductile building gives warning by bending before it fails."),
        ("Base isolation bearings",
         "Base isolation puts flexible bearings between the building and its foundation. The bearings let the ground move while the building above moves much less. This reduces the shaking the building feels."),
        ("Lessons from Kobe and Northridge",
         "The Kobe earthquake in 1995 and the Northridge earthquake in 1994 damaged many buildings and roads. Their lessons led to stronger connections at beam-to-column joints and better design codes. Both events changed how engineers detail steel frames."),
        ("Designing for the big one",
         "Engineers design for a level of shaking with a chosen chance of happening in a given time. They aim to protect life first, so that a building can be used again or safely evacuated after a strong quake. Every design is a balance of cost and risk."),
    ],
    "test": [
        ("What does a response spectrum show?", [("a", "How tall a building looks"), ("b", "How strongly structures of different stiffness respond to a quake"), ("c", "The colour of the soil"), ("d", "The price of cement")], "b"),
        ("What does ductility mean in a building?", [("a", "Having no steel at all"), ("b", "Being made of glass"), ("c", "The ability to bend and deform without suddenly breaking"), ("d", "Being unable to move")], "c"),
        ("What do base isolation bearings do?", [("a", "Hold the building rigidly to the rock"), ("b", "Make the building heavier on purpose"), ("c", "Let the ground move while the building above moves much less"), ("d", "Remove the foundation")], "c"),
        ("Which two earthquakes shaped lessons about steel frame connections?", [("a", "Kobe in 1995 and Northridge in 1994"), ("b", "Paris in 1910 and Rome in 1950"), ("c", "Lisbon in 1755 and Dublin in 1800"), ("d", "Sydney in 1980 and Toronto in 1990")], "a"),
        ("What is the main aim of earthquake design?", [("a", "To use only wood"), ("b", "To make buildings as tall as possible"), ("c", "To avoid all inspections"), ("d", "To protect life first")], "d"),
    ],
}
