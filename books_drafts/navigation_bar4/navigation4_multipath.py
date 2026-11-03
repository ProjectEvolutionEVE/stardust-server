"""Multipath in satellite navigation: reflected signals, urban canyons, antenna choice and mitigation."""
CODE = "navigation4_multipath"
BOOK = {
    "title": "Multipath in Satellite Navigation",
    "subtitle": "Reflected signals, urban canyons and how to tame them",
    "chapters": [
        ("Direct and bounced signals", "A satellite signal can reach the antenna straight, or after bouncing off a wall, a hill or water. The bounced copy travels a longer path, so it arrives late. The receiver may mix the two together and get the position wrong."),
        ("Urban canyons", "Tall buildings on both sides of a street form a canyon where many signals bounce. In such places a receiver may see more reflected signals than direct ones. Careful planners avoid relying on satellite fixes in these streets."),
        ("Antenna choice", "Some antennas reject signals that arrive from low angles, which is where many reflections come from. A choke ring uses rings of metal to trap the bounced signal. Reference stations, where accuracy matters most, often use this design."),
        ("The size of the error", "The error depends on how strong the reflection is, how long its delay is, and how well the receiver is built. A short delay is harder to separate from the direct signal than a long one. Good receivers reduce the effect but cannot remove it everywhere."),
        ("Mitigation in practice", "Ways to reduce multipath include placing the antenna high and away from reflecting surfaces, using a choke ring, and using receivers that study the shape of the signal. Averaging over time also helps, because the reflections change as the satellites move."),
        ("Why it matters", "Multipath is one of the main limits on how precise a satellite fix can be in cities. A navigator should always ask whether a fix could be a reflection. Knowing the problem is the first step to working around it."),
    ],
    "test": [
        ("What is multipath in satellite navigation?", [("a", "A satellite that has left its orbit"), ("b", "A signal that reaches the antenna by a bounced route as well as a direct one"), ("c", "A second receiver kept for backup"), ("d", "A type of atomic clock")], "b"),
        ("Why does a bounced signal cause trouble?", [("a", "It is always stronger than the direct signal"), ("b", "The atmosphere blocks it completely"), ("c", "It travels a longer path, so it arrives late and can confuse the receiver"), ("d", "It switches the receiver off")], "c"),
        ("Which antenna design helps reject low-angle reflections at reference stations?", [("a", "A plain wire loop"), ("b", "A sheet of glass"), ("c", "A rubber sleeve"), ("d", "A choke ring")], "d"),
        ("Where is multipath most common?", [("a", "In an urban canyon between tall buildings"), ("b", "On open farmland"), ("c", "On a calm lake far from shore"), ("d", "In deep space")], "a"),
        ("Which step is a good way to reduce multipath?", [("a", "Mount the antenna low against a metal wall"), ("b", "Place the antenna high and clear of nearby reflecting surfaces"), ("c", "Turn the receiver off in cities"), ("d", "Use only one satellite at a time")], "b"),
    ],
}
