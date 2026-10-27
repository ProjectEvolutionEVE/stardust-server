"""Tyres and Rolling Resistance: the contact patch, tread, rolling losses, grip limits and the fuel cost of rolling resistance."""
CODE = "engineering4_tyres"
BOOK = {
    "title": "Tyres and Rolling Resistance",
    "subtitle": "Contact patch, tread, grip and rolling losses",
    "chapters": [
        ("The contact patch",
         "The contact patch is the small area where a tyre touches the road. All grip and braking force passes through it."),
        ("Tread",
         "Tread grooves carry water away and bite into the surface. A worn tread loses grip, especially in wet weather."),
        ("Rolling losses",
         "A tyre flexes as it rolls, and that flexing turns some energy into heat. This loss is rolling resistance."),
        ("Grip limits",
         "Grip is limited by the friction between the tyre and the road. Pushing past that limit makes the tyre slide."),
        ("The fuel cost of rolling resistance",
         "Lower rolling resistance saves fuel. A large share of the fuel used in steady driving goes to rolling losses and air drag."),
        ("Choosing a tyre",
         "Engineers balance grip, wear, noise, rolling resistance and cost when they choose a tyre. No single tyre is best for every road and climate."),
    ],
    "test": [
        ("What is the contact patch?",
         [("a", "The small area where the tyre touches the road"), ("b", "The engine"), ("c", "The paint"), ("d", "The sound")], "a"),
        ("What do tread grooves do?",
         [("a", "Add heat"), ("b", "Make sound"), ("c", "Stop the tyre rolling"), ("d", "Carry water away")], "d"),
        ("What causes rolling resistance?",
         [("a", "Engine music"), ("b", "Tyre flexing that turns energy into heat"), ("c", "Sunlight"), ("d", "Paint")], "b"),
        ("What limits grip?",
         [("a", "The colour of the car"), ("b", "The radio"), ("c", "The sun"), ("d", "Friction between the tyre and the road")], "d"),
        ("What does lower rolling resistance save?",
         [("a", "Fuel"), ("b", "Paint"), ("c", "Sound"), ("d", "Music")], "a"),
    ],
}
