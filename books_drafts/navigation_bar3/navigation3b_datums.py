"""Datums: Agreeing Where Zero Is. The reference models that give every map its starting point."""
CODE = 'navigation3b_datums'
BOOK = {
    "title": "Datums: Agreeing Where Zero Is",
    "subtitle": "The reference models that give every map its starting point",
    "chapters": [
        ("A starting point for numbers",
         "A coordinate is only as good as the reference it is measured from. A datum is the agreed model of the Earth's shape and its origin, the starting point for every latitude, longitude and height. Two maps with different datums can place the same spot in different places."),
        ("The ellipsoid",
         "Most datums use an ellipsoid as the base for latitude and longitude. An ellipsoid is a smooth model shaped like the flattened Earth. A datum built to fit one country closely can fit the rest of the world poorly."),
        ("Local and global datums",
         "Older national datums were built to fit one region well. Modern global datums are fitted to the whole Earth at once. The satellite navigation used aboard ships and planes depends on a global datum, so positions agree from one part of the world to another."),
        ("The shift between datums",
         "Moving a position from one datum to another changes its numbers, sometimes by tens of metres and in some places by hundreds. The same road can sit on one side of a line on one map and the other side on another. Always write down which datum a position uses."),
        ("Heights have their own reference",
         "A height depends on its vertical reference as well. Many countries measure heights from a long-term mean sea level, worked out from tide gauges over many years. A height given without its reference is only half a number."),
        ("Write the datum down",
         "Careful surveyors record the datum with every measurement. A map or survey without a datum is like a sum without units: the figures may look right and still be wrong."),
    ],
    "test": [
        ("What is a datum?",
         [("a", "A type of compass"), ("b", "An agreed model of the Earth's shape and origin, the starting point for coordinates"), ("c", "A colour used on maps"), ("d", "A survey fee")], "b"),
        ("Why can the same spot have different coordinates on two datums?",
         [("a", "The Earth changes shape each morning"), ("b", "The spot moves from year to year"), ("c", "The datums use different reference models, so the numbers differ"), ("d", "The map paper stretches")], "c"),
        ("What is an ellipsoid in mapping?",
         [("a", "A smooth model of the flattened Earth, used as the base for latitude and longitude"), ("b", "A sea monster"), ("c", "A kind of laser"), ("d", "A grid of squares")], "a"),
        ("Which kind of datum is fitted to the whole Earth at once?",
         [("a", "A local datum"), ("b", "A global datum"), ("c", "A harbour chart"), ("d", "A sundial")], "b"),
        ("What should a careful surveyor always do with a position?",
         [("a", "Round it to the nearest kilometre"), ("b", "Leave the datum out, since it never matters"), ("c", "Use the datum of the nearest planet"), ("d", "Write down which datum it uses")], "d"),
    ],
}
