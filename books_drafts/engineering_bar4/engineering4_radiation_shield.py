"""Radiation Shielding and Materials: radiation types, shielding by mass and density, hydrogen-rich shields, placement and dose."""
CODE = "engineering4_radiation_shield"
BOOK = {
    "title": "Radiation Shielding and Materials",
    "subtitle": "Mass, density, hydrogen-rich shields and measuring dose",
    "chapters": [
        ("Types of radiation",
         "Radiation in space includes charged particles from the Sun and from cosmic rays, and it can include gamma rays and neutrons. Each type needs a different kind of shield."),
        ("Shielding by mass",
         "Dense materials stop gamma rays well. Light materials rich in hydrogen slow down fast neutrons and charged particles better, so the right shield depends on the radiation."),
        ("Hydrogen-rich shields",
         "Water, polyethylene and other hydrogen-rich materials are good at slowing fast neutrons and charged particles. Water stored around a crew area can do double duty as supply and shielding."),
        ("Shield placement",
         "A shield placed close around a crew area protects better than one placed far away. Supplies stored around the living area add shielding for free."),
        ("Measuring dose",
         "Absorbed dose is measured in grays, and the dose that matters to the body is measured in sieverts. Dosimeters record the dose a person receives over time."),
        ("Designing with mass limits",
         "Shielding is heavy. Designers balance dose limits, mass, cost and the length of the mission."),
    ],
    "test": [
        ("What does shielding performance depend on?",
         [("a", "The number of crew"), ("b", "Mass and density"), ("c", "Paint colour"), ("d", "Sound level")], "b"),
        ("What are hydrogen-rich materials good at?",
         [("a", "Stopping sound"), ("b", "Making fuel"), ("c", "Slowing fast neutrons and charged particles"), ("d", "Cooling engines")], "c"),
        ("Which unit measures absorbed dose?",
         [("a", "Grays"), ("b", "Kilograms"), ("c", "Newtons"), ("d", "Decibels")], "a"),
        ("What does a dosimeter do?",
         [("a", "Makes shields"), ("b", "Cools metal"), ("c", "Calculates orbits"), ("d", "Records the dose a person receives")], "d"),
        ("What is a design trade-off in shielding?",
         [("a", "Dose limits, mass, cost and mission length"), ("b", "Colour against paint"), ("c", "Sound against light"), ("d", "Crew size only")], "a"),
    ],
}
