"""Magnetic Recording Media: the thin cobalt-based films that store data on hard drives, and why heat-assisted recording was needed."""
CODE = "mining5_magrec"
BOOK = {
    "title": "Magnetic Recording Media",
    "subtitle": "Tiny magnetic grains that hold data bits on a hard drive",
    "chapters": [
        ("A magnetic film", "A hard disk stores data as tiny magnetic regions in a thin film on a disc. Each bit is a small area that points one way or the other. The film is built from many small grains."),
        ("Grain size", "Smaller grains let more bits fit on the same area. But grains that are too small can lose their magnetism to heat and time. Finding the balance is the central problem."),
        ("Coercivity", "Coercivity is the strength of magnetic field needed to flip a region. High coercivity keeps data stable, but it also makes writing harder. Cobalt alloys with platinum and chromium are commonly used."),
        ("The superparamagnetic limit", "When grains get too small, heat can flip their magnetism at random. This limit was a barrier to packing more data in the same space."),
        ("Heat-assisted recording", "Heat-assisted magnetic recording warms a tiny spot with a laser just before writing. The heat lowers the coercivity for a moment, so a stronger grain can be written. Then the spot cools and holds the bit."),
        ("Future media", "Engineers study patterned media, where each bit has its own island, and other designs. The aim is more storage in the same space without losing data."),
    ],
    "test": [
        ("How is data stored on a hard disk film?",
         [("a", "As ink marks"), ("b", "As tiny magnetic regions"), ("c", "As paper holes"), ("d", "As sugar crystals")], "b"),
        ("What does coercivity describe?",
         [("a", "The weight of a disc"), ("b", "The colour of a disc"), ("c", "The speed of a fan"), ("d", "The strength of field needed to flip a magnetic region")], "d"),
        ("What is the superparamagnetic limit?",
         [("a", "A speed limit for cars"), ("b", "A rule about paper size"), ("c", "Heat can flip very small grains at random"), ("d", "A price limit for coffee")], "c"),
        ("What does heat-assisted recording use to warm the spot?",
         [("a", "A laser"), ("b", "A candle"), ("c", "A kettle"), ("d", "A sponge")], "a"),
        ("Which metal is commonly used in these recording films?",
         [("a", "Potassium"), ("b", "Mercury"), ("c", "Cobalt"), ("d", "Sodium")], "c"),
    ],
}
