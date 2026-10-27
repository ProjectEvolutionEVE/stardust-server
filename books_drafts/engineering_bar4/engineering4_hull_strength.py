"""Hull Girder Strength and Longitudinal Bending: the ship as a beam, hogging and sagging, and the load cases in waves."""
CODE = "engineering4_hull_strength"
BOOK = {
    "title": "Hull Girder Strength and Longitudinal Bending",
    "subtitle": "Hogging, sagging and the ship as a beam",
    "chapters": [
        ("The ship as a beam",
         "A ship's hull acts like a long beam. Waves push it up and down along its length, so the hull must resist bending along its whole length."),
        ("Hogging",
         "Hogging happens when a wave crest lifts the middle of the hull and the ends droop. The hull arches upward, and the deck and bottom carry large loads."),
        ("Sagging",
         "Sagging is the opposite. The ends rest on wave crests and the middle sinks into a trough. Each case puts different parts of the hull under the greatest stress."),
        ("Frames and plating",
         "Transverse frames run across the hull and stop it folding in on itself. Longitudinal stiffeners and the plating carry bending along the length. The deck and bottom often carry the largest loads."),
        ("Load cases in waves",
         "Designers check the hull against standard wave cases, such as a crest at the middle and a crest at each end. The worst case sets the strength the hull needs."),
        ("Why it matters",
         "A hull that bends too much can crack or buckle. Careful strength checks keep the ship safe in a storm and over its whole life."),
    ],
    "test": [
        ("How is a ship's hull often modelled for bending?",
         [("a", "As a ball"), ("b", "As a long beam"), ("c", "As a flat sheet"), ("d", "As a tower")], "b"),
        ("What is hogging?",
         [("a", "The ends lift on crests and the middle drops"), ("b", "The ship spins on its axis"), ("c", "The ship sinks flat"), ("d", "The middle lifts on a crest and the ends droop")], "d"),
        ("What is sagging?",
         [("a", "The middle sits on a crest"), ("b", "The ship spins"), ("c", "The ends sit on crests and the middle sinks into a trough"), ("d", "The bow lifts")], "c"),
        ("What do the frames of a hull do?",
         [("a", "Stop the hull folding in on itself"), ("b", "Make paint"), ("c", "Steer the ship"), ("d", "Heat the hull")], "a"),
        ("What sets the strength a hull needs?",
         [("a", "The colour of the hull"), ("b", "The worst wave load case"), ("c", "The name of the cargo"), ("d", "The colour of the engine")], "b"),
    ],
}
