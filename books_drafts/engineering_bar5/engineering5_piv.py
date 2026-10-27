"""Particle Image Velocimetry and Flow Visualisation: measuring a whole slice of a flow by following tiny seeding particles."""
CODE = "engineering5_piv"
BOOK = {
    "title": "Particle Image Velocimetry and Flow Visualisation",
    "subtitle": "Seeding, laser sheets and the velocity map of a flow",
    "chapters": [
        ("Seeing the flow", "Particle Image Velocimetry, or PIV, measures a flow by following tiny particles carried by the fluid. The particles show how the fluid moves, and the pattern of their motion gives the velocity."),
        ("Seeding", "The flow is seeded with small particles that follow it closely and reflect light well. Particles that are too large or too heavy will not follow the flow, and the measurement will be wrong."),
        ("The laser sheet", "A thin sheet of laser light lights up one slice through the flow. A camera records two images in quick succession, so the particles appear in two positions."),
        ("Cross-correlation", "Software compares small patches of the two images. It finds how far the particles moved between them, and from that the speed and direction of the flow."),
        ("Velocity fields", "Repeated across the whole image, these results give a map of velocity over the slice. The map shows where the flow is fast, slow, or swirling."),
        ("Checking CFD", "PIV results are used to check computer flow simulations. When the simulation and the measured map agree, confidence in the simulation grows."),
    ],
    "test": [
        ("What does PIV track?", [("a", "Small particles carried by the flow"), ("b", "The temperature of the walls"), ("c", "The weight of the parts"), ("d", "The colour of the lab")], "a"),
        ("What is a laser sheet?", [("a", "A metal plate used to hold the model"), ("b", "A cloth used to clean optics"), ("c", "A thin plane of light that lights a slice of the flow"), ("d", "A type of seal")], "c"),
        ("What does cross-correlation find?", [("a", "The brand of the camera"), ("b", "How far the particles moved between two images"), ("c", "The price of the seeding"), ("d", "The weather in the lab")], "b"),
        ("What is a velocity field?", [("a", "A map of flow speed and direction across a slice"), ("b", "A field of grass beside the lab"), ("c", "A fuel tank for the rig"), ("d", "A frame for holding welds")], "a"),
        ("Why is PIV useful for CFD?", [("a", "It replaces all experiments"), ("b", "It heats the fluid"), ("c", "It removes the need for computers"), ("d", "It can check and validate simulations")], "d"),
    ],
}
