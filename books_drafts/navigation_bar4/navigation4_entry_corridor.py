"""Atmospheric entry corridors: entry angle, skip, heat, heat shields, g-load and the landing point."""
CODE = "navigation4_entry_corridor"
BOOK = {
    "title": "Atmospheric Entry Corridors",
    "subtitle": "The narrow band of angles that brings a craft home",
    "chapters": [
        ("Coming back down", "A spacecraft returning from orbit must enter the air at a careful angle. The entry corridor is the band of angles that works. Too steep or too shallow a path causes trouble."),
        ("The entry angle", "A steep entry gives very high heating and deceleration. A shallow entry may skip off the air and fly away. The right angle lies between these two."),
        ("The skip", "A skip is when the craft bounces off the top of the air and rises again. Planners may use a skip to slow down or to reach a target. Skips must be controlled."),
        ("Heat", "Entry heats the craft's surface very hot, from air being compressed in front of it. A heat shield protects the craft. The shield design is a major part of mission planning."),
        ("G-load", "G-load is the force on the crew or cargo during deceleration. A steep entry raises it sharply. Planners keep it within safe limits."),
        ("The landing point", "The entry path decides where the craft will land. Small changes in entry angle move the landing point by large distances. Precise targeting depends on the corridor."),
    ],
    "test": [
        ("What is an entry corridor?", [("a", "A hallway in the rocket"), ("b", "The band of entry angles that works"), ("c", "A line of satellites"), ("d", "A road to the launch pad")], "b"),
        ("What happens if the entry is too steep?", [("a", "The craft turns into a bird"), ("b", "Nothing happens at all"), ("c", "The craft stops falling and floats"), ("d", "Heating and deceleration become very high")], "d"),
        ("What is a skip?", [("a", "A missed radio call"), ("b", "A jump from one orbit to another without fuel"), ("c", "When the craft bounces off the top of the air and rises again"), ("d", "A break in the mission plan")], "c"),
        ("What protects a returning craft from heat?", [("a", "A heat shield"), ("b", "A bag of ice"), ("c", "A thin sheet of paper"), ("d", "A cooling fan")], "a"),
        ("What is G-load?", [("a", "The force on the crew or cargo during deceleration"), ("b", "The weight of the fuel tank"), ("c", "The number of windows"), ("d", "A rating of how bright the sky looks")], "a"),
    ],
}
