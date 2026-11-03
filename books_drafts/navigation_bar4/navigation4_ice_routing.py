"""Routing Through Ice: ice charts, ice classes, convoy routing, escorts, risk and timing."""
CODE = "navigation4_ice_routing"
BOOK = {
    "title": "Routing Through Ice",
    "subtitle": "Planning a route where the sea is frozen, and knowing when to wait",
    "chapters": [
        ("Ice charts", "Ice charts show where ice lies and how thick and close it is. They are drawn from satellite images, aerial surveys and reports. A chart is a snapshot, so it must be checked against the latest version."),
        ("Ice classes", "Ships built for ice have an ice class. Polar classes run from PC1 to PC7, with PC1 the strongest. A ship's class tells you which ice it can safely enter."),
        ("Convoy routing", "Ships often sail in convoy through ice. The lead ship breaks a path that the others follow. Staying in the track of the leader saves effort and keeps the convoy together."),
        ("Escorts", "An icebreaker may escort a ship through heavy ice. The escort sets the speed and the path. The ship must keep to the escort's plan and stay in radio contact."),
        ("Risk", "Ice can damage a hull, trap a ship or push it off course. The risk depends on ice thickness, pressure and the ship's class. A careful master plans for the worst case."),
        ("Timing", "Ice moves with wind and current. A route that is open today may close tomorrow. Timing the passage well can save a long wait or a dangerous crossing."),
    ],
    "test": [
        ("What do ice charts show?", [("a", "Where ice lies and how thick and close it is"), ("b", "Where the shops are"), ("c", "The price of fuel"), ("d", "The names of the crew")], "a"),
        ("What does a polar ice class tell you?", [("a", "The colour of the hull"), ("b", "The number of cabins"), ("c", "The name of the captain"), ("d", "Which ice a ship can safely enter")], "d"),
        ("Why sail in the track of the leader?", [("a", "The leader is always faster in open water"), ("b", "Tracks are painted on the ice"), ("c", "It avoids the need for a chart"), ("d", "The leader breaks a path, which saves effort and keeps the convoy together")], "d"),
        ("What must a ship do when escorted by an icebreaker?", [("a", "Go a different way"), ("b", "Keep to the escort's plan and stay in radio contact"), ("c", "Switch off the radio"), ("d", "Ignore the escort")], "b"),
        ("Why does timing matter in ice?", [("a", "Ice never moves"), ("b", "Timing has no effect"), ("c", "Ice moves, so an open route can close"), ("d", "Ice only forms in summer")], "c"),
    ],
}
