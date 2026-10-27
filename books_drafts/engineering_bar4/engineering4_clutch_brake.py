"""Clutches, Brakes and Friction Drives: friction torque, heat, wear, engagement and choosing a friction pad."""
CODE = "engineering4_clutch_brake"
BOOK = {
    "title": "Clutches, Brakes and Friction Drives",
    "subtitle": "Friction torque, heat, wear and engagement",
    "chapters": [
        ("Friction torque",
         "A friction clutch or brake transfers torque through friction between two surfaces. The torque depends on the friction coefficient, the clamping force and the radius of the friction surface."),
        ("Heat in brakes",
         "Braking turns the energy of motion into heat in the friction material. Too much heat can make a brake fade or damage it."),
        ("Wear",
         "Friction material wears with use. Wear changes the clamping force, so brakes and clutches need adjustment or replacement."),
        ("Engagement",
         "A clutch must engage smoothly to avoid shock. Slipping for a short time while it engages gives a smooth start."),
        ("Selecting a friction pad",
         "Choose a friction material by its coefficient, its heat limit, its wear rate and its noise. Cost matters too."),
        ("Trade-offs",
         "Higher friction grips harder, but it may wear faster or make more heat. Balance the choice against the duty cycle."),
    ],
    "test": [
        ("What does friction torque depend on?",
         [("a", "The friction coefficient, the clamping force and the radius"), ("b", "Colour"), ("c", "Music"), ("d", "Weather")], "a"),
        ("What does braking turn into?",
         [("a", "Light"), ("b", "Sound only"), ("c", "Water"), ("d", "Heat")], "d"),
        ("What happens to the clamping force as friction material wears?",
         [("a", "The brake grows"), ("b", "The colour improves"), ("c", "The clamping force changes"), ("d", "Friction becomes zero forever")], "c"),
        ("Why engage a clutch with a little slip?",
         [("a", "To paint it"), ("b", "To cool the Sun"), ("c", "To add weight"), ("d", "To make a smooth start with no shock")], "d"),
        ("What does choosing a friction pad weigh?",
         [("a", "Coefficient, heat limit, wear rate and noise"), ("b", "Only colour"), ("c", "Only the Moon"), ("d", "Only paint")], "a"),
    ],
}
