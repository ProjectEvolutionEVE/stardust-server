"""Fire Underground: how fires start in mines, how they are found and fought, and how escape, smoke control and practice drills save lives."""
CODE = "mining5_fire"
BOOK = {
    "title": "Fire Underground: Prevention and Response",
    "subtitle": "Ignition sources, detection, escape, suppression, smoke and drills",
    "chapters": [
        ("Fire in a closed space",
         "Fire is more dangerous underground because air is limited and smoke cannot easily escape. A small fire can fill tunnels quickly. Prevention and quick response are the keys to safety."),
        ("Ignition sources",
         "Common ignition sources include hot work such as welding, electrical faults, and overheated machinery or belts. Clear rules for hot work and regular checks of electrical gear remove many risks. Good housekeeping keeps fuel away from heat."),
        ("Fire detection",
         "Heat detectors, smoke sensors and gas monitors can warn of a fire early. Early warning gives people time to act. Detectors need regular testing to remain reliable."),
        ("Escape",
         "Every worker should know at least two escape routes. Marked routes, refuge chambers and self-rescuers help people reach safety. Routes must be kept clear at all times."),
        ("Suppression and smoke",
         "Water, foam and dry chemical systems can fight fires in some places. Smoke is often more dangerous than the flames, because it hides the way out and carries gas. Ventilation must be planned to keep smoke away from escape routes."),
        ("Drills",
         "Practice drills make the response automatic. Workers learn the alarm signals, the routes and the use of self-rescuers. Drills are reviewed afterwards, and the plan is improved."),
    ],
    "test": [
        ("Why is a fire more dangerous underground?",
         [("a", "Air is limited and smoke cannot easily escape"), ("b", "The rock is always too warm to burn"), ("c", "Fires cannot start underground"), ("d", "Underground fires are always tiny")], "a"),
        ("What is one common ignition source in a mine?",
         [("a", "Hot work such as welding"), ("b", "Cold water"), ("c", "Clean air"), ("d", "Fresh flowers")], "a"),
        ("What do fire detectors do?",
         [("a", "Make the fire bigger"), ("b", "Print the report"), ("c", "Give early warning so people have time to act"), ("d", "Turn the lights blue")], "c"),
        ("Why is smoke often more dangerous than flames?",
         [("a", "It is always cold"), ("b", "It cannot be breathed at all"), ("c", "It makes the walls wet"), ("d", "It hides the way out and carries gas")], "d"),
        ("What do practice drills achieve?",
         [("a", "They make fires more likely"), ("b", "They make the response automatic"), ("c", "They cancel the alarms"), ("d", "They remove all escape routes")], "b"),
    ],
}
