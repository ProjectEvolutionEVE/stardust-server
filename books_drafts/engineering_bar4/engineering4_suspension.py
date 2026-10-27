"""Vehicle Suspension Geometry: camber, caster, toe, springs and dampers, ride comfort and the trade between handling and comfort."""
CODE = "engineering4_suspension"
BOOK = {
    "title": "Vehicle Suspension Geometry",
    "subtitle": "Camber, caster, toe, springs and dampers",
    "chapters": [
        ("Camber",
         "Camber is the tilt of the wheel in or out, seen from the front. It affects how the tyre meets the road in corners."),
        ("Caster",
         "Caster is the forward or backward tilt of the steering axis, seen from the side. It helps the steering return to centre and keeps the wheel steady."),
        ("Toe",
         "Toe is how far the fronts of the wheels point in or out, seen from above. Correct toe reduces tyre wear and keeps the car running straight."),
        ("Springs and dampers",
         "Springs hold the body up and store energy from bumps. Dampers control how fast the springs move, so the ride settles quickly."),
        ("Ride comfort",
         "A soft ride feels comfortable but can give less control. A stiff ride gives better control but feels harsher."),
        ("The trade-off",
         "Handling and comfort pull against each other. Designers choose the settings that suit the vehicle's use."),
    ],
    "test": [
        ("What does camber describe?",
         [("a", "The tilt of the wheel in or out, seen from the front"), ("b", "Engine heat"), ("c", "Paint"), ("d", "Sound")], "a"),
        ("What does caster help?",
         [("a", "Engine sound"), ("b", "Colour"), ("c", "Steering return to centre"), ("d", "Bread")], "c"),
        ("What do dampers do?",
         [("a", "Add weight"), ("b", "Control how fast the springs move so the ride settles"), ("c", "Heat the car"), ("d", "Paint the wheels")], "b"),
        ("What does toe describe?",
         [("a", "Engine sound"), ("b", "Fuel"), ("c", "Colour"), ("d", "How far the wheel fronts point in or out, seen from above")], "d"),
        ("What do handling and comfort do with each other?",
         [("a", "Pull against each other"), ("b", "Always match"), ("c", "Cancel out the wheels"), ("d", "Stop the springs")], "a"),
    ],
}
