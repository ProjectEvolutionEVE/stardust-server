"""Blast Vibration and Structural Limits: how ground shaking from blasts is measured, scaled and limited to protect nearby buildings and people."""
CODE = "mining5_blast_vib"
BOOK = {
    "title": "Blast Vibration and Structural Limits",
    "subtitle": "Peak particle velocity, scaled distance, monitoring and regulation",
    "chapters": [
        ("Shaking from a blast",
         "A blast sends waves through the ground. Nearby buildings and people feel the shaking. Blast design aims to keep that shaking within safe limits for the places around the mine."),
        ("Peak particle velocity",
         "Peak particle velocity is the fastest speed the ground moves during a blast. It is measured in millimetres per second. Many limits and guidelines are written in terms of this value."),
        ("Scaled distance",
         "Scaled distance combines the distance from the blast with the charge size used in each delay. Closer blasts and bigger charges give higher vibration. Scaled distance is a simple way to predict the vibration before a blast is fired."),
        ("Monitoring",
         "Seismographs placed near structures record the vibration of each blast. The records show whether the design is working. If readings come close to a limit, the blast plan is changed."),
        ("Structures and models",
         "Different buildings react differently. Old or fragile structures need lower limits than strong modern ones. Models of the ground and structures help set site-specific limits."),
        ("Regulation",
         "Many authorities set limits for blast vibration and require records of each blast. Mines must follow these rules and show their monitoring data. Clear records build trust with the community."),
    ],
    "test": [
        ("What is peak particle velocity?",
         [("a", "The number of people on a blast crew"), ("b", "The price of explosives"), ("c", "The height of a tower"), ("d", "The fastest speed the ground moves during a blast")], "d"),
        ("What does scaled distance combine?",
         [("a", "The colour and the weight of the rock"), ("b", "The distance from the blast and the charge size per delay"), ("c", "The name of the mine and its owner"), ("d", "The price of diesel and the time of day")], "b"),
        ("What do seismographs near structures record?",
         [("a", "The vibration of each blast"), ("b", "The number of birds"), ("c", "The price of ore"), ("d", "The name of the mayor")], "a"),
        ("Why do old or fragile buildings need lower limits?",
         [("a", "They react more strongly to shaking"), ("b", "They are always taller"), ("c", "They cost more to paint"), ("d", "They never move")], "a"),
        ("What does regulation usually require?",
         [("a", "No records at all"), ("b", "Blasts at any time without checks"), ("c", "Limits for blasts and records of each blast"), ("d", "Fewer people in the team")], "c"),
    ],
}
