"""The BeiDou System: China's navigation network, built in stages with a mix of orbits."""
CODE = "navigation4_beidou"
BOOK = {
    "title": "The BeiDou System",
    "subtitle": "China's navigation network, built in stages",
    "chapters": [
        ("Regional and global stages", "BeiDou was built in stages. It began as a regional system over China and nearby areas. Later it grew into a global system."),
        ("A mix of orbits", "BeiDou uses geostationary, inclined geosynchronous and medium Earth orbit satellites. The mix helps cover the region and the globe. Each orbit type has its own strengths."),
        ("Short messages", "BeiDou can send short messages as well as position data. This service is useful in places with no phone signal. It has been used for rescue and emergency messages."),
        ("Its time system", "BeiDou has its own time system, called BeiDou Time. It is kept accurate with atomic clocks on the satellites and on the ground. Accurate time keeps positions accurate."),
        ("Use beyond China", "BeiDou is used by people across Asia and in other regions. Its open signals are free to use for positioning. Many devices now receive BeiDou alongside other systems."),
        ("Receiver interfaces", "Receivers use BeiDou through the same kind of interface as other systems. Multi-system receivers can track BeiDou together with GPS and Galileo. More satellites in view help the fix."),
    ],
    "test": [
        ("How did BeiDou begin?",
         [("a", "As a regional system over China and nearby areas"), ("b", "As a space hotel"), ("c", "As a railway"), ("d", "As a shipbuilder")], "a"),
        ("Which kinds of orbits does BeiDou mix?",
         [("a", "Only lake orbits"), ("b", "Only undersea orbits"), ("c", "Only the Moon's orbit"), ("d", "Geostationary, inclined geosynchronous and medium Earth orbits")], "d"),
        ("What extra service does BeiDou offer?",
         [("a", "Painting"), ("b", "Cooking"), ("c", "Short messages"), ("d", "Weather on the Moon")], "c"),
        ("What is BeiDou's time system called?",
         [("a", "Chinese Time"), ("b", "BeiDou Time"), ("c", "Sundial Time"), ("d", "Galileo Time")], "b"),
        ("What helps a receiver get a better fix?",
         [("a", "Fewer satellites"), ("b", "A dark room"), ("c", "A paper map"), ("d", "More satellites in view")], "d"),
    ],
}
