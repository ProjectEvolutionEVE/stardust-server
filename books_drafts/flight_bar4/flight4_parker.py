"""Case Study: Parker Solar Probe. A craft that flies closer to the Sun than any before it, using Venus to shrink its orbit."""
CODE = 'flight4_parker'
BOOK = {
    "title": "Case Study: Parker Solar Probe",
    "subtitle": "The closest approach to the Sun, a heat shield and Venus assists",
    "chapters": [
        ("Closest to the Sun",
         "The Parker Solar Probe was launched in 2018 to fly closer to the Sun than any craft before it. It dives through the Sun's outer atmosphere, the corona, and then reaches out again, over and over."),
        ("The shield",
         "A heat shield of carbon composite faces the Sun and keeps the instruments in its shade. The shield takes the extreme heat so that the instruments behind it can keep working."),
        ("Keeping cool",
         "The shield is designed so the spacecraft stays within safe limits for its systems. Every part of the design works together to manage heat in a place that would destroy most machines."),
        ("Speed records",
         "As Parker falls toward the Sun, the pull of gravity speeds it up. On its closest passes it has become the fastest human-made object ever built."),
        ("Venus assists",
         "Several flybys of Venus bent the probe's path and shrank its orbit step by step, until it reached its close passes near the Sun. Venus's gravity worked like a brake and a steering tool."),
        ("Findings",
         "Parker has measured the solar wind and magnetic fields up close. This helps scientists understand how the Sun drives space weather that can affect Earth."),
    ],
    "test": [
        ("When was the Parker Solar Probe launched?",
         [("a", "1969"), ("b", "1990"), ("c", "2018"), ("d", "2003")], "c"),
        ("What does the heat shield face?",
         [("a", "Earth"), ("b", "The Sun"), ("c", "The Moon"), ("d", "Space ice")], "b"),
        ("What did Parker become on its closest passes?",
         [("a", "The slowest probe"), ("b", "A lamp"), ("c", "The fastest human-made object"), ("d", "A satellite of Jupiter")], "c"),
        ("What helped shrink Parker's orbit step by step?",
         [("a", "Music"), ("b", "Snow"), ("c", "Sand"), ("d", "Venus flybys")], "d"),
        ("What did Parker measure up close?",
         [("a", "Solar wind and magnetic fields"), ("b", "Cakes"), ("c", "Lakes"), ("d", "Forests")], "a"),
    ],
}
