"""Case Study: Galileo's Stuck Antenna. A main antenna that would not open, a slower route and saved science."""
CODE = 'flight4_galileo'
BOOK = {
    "title": "Case Study: Galileo's Stuck Antenna",
    "subtitle": "A slower route, clever compression and science saved",
    "chapters": [
        ("A planned mission",
         "Galileo was a NASA probe sent to study Jupiter and its moons. Its main radio antenna was meant to open like an umbrella, so it could send large amounts of data to Earth."),
        ("The umbrella that stuck",
         "After launch in 1989, the large antenna failed to open fully. Only part of it unfolded, so the main radio link was weak. The team had to find another way to talk to the probe."),
        ("A slower route",
         "Engineers used a small low-gain antenna instead. Its signal was much weaker, so data came back slowly. The probe had to be commanded with great care."),
        ("Clever compression",
         "The team wrote new software to squeeze data before it was sent. Clever compression let the science continue even with a weak link. Hard work by the team saved much of the mission."),
        ("Science saved",
         "Galileo reached Jupiter in 1995 and dropped a probe into the planet's atmosphere. It studied the moons, and its data pointed to possible salty oceans under the icy surface of Europa."),
        ("A lesson",
         "Galileo teaches that a plan must allow for failure. A team that thinks through many paths can save a mission when the first plan breaks."),
    ],
    "test": [
        ("What was Galileo sent to study?",
         [("a", "Jupiter and its moons"), ("b", "The Moon"), ("c", "Mars"), ("d", "Sunspots")], "a"),
        ("What got stuck?",
         [("a", "A wheel"), ("b", "A door"), ("c", "A radio antenna"), ("d", "A rock")], "c"),
        ("What did the team use instead?",
         [("a", "A small low-gain antenna"), ("b", "A telescope"), ("c", "Their voices"), ("d", "A boat")], "a"),
        ("What was the new software for?",
         [("a", "Painting images"), ("b", "Compressing data before it was sent"), ("c", "Playing music"), ("d", "Steering boats")], "b"),
        ("What is the lesson?",
         [("a", "A plan must allow for failure"), ("b", "Never send probes"), ("c", "Antennas are useless"), ("d", "Jupiter is small")], "a"),
    ],
}
