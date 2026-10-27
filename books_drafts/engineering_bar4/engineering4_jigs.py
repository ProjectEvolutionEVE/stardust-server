"""Jigs, Fixtures and Tooling Design: locating, clamping and repeatability, and the payback of a good fixture."""
CODE = 'engineering4_jigs'
BOOK = {
    "title": "Jigs, Fixtures and Tooling Design",
    "subtitle": "Holding and guiding parts so every one comes out the same",
    "chapters": [
        ("Jigs and fixtures",
         "A fixture holds a part in a fixed position while work is done on it. A jig does the same and also guides the cutting tool. Both save time and reduce errors from one part to the next."),
        ("Locating principles",
         "A part is located by resting it on a few fixed points, arranged so it cannot move. Locating on the same points every time gives repeatable positions. The layout is planned from the part's datums."),
        ("Clamping",
         "Clamps hold the part firmly without distorting it. They should press on solid points that the locators support. A clamp pressing on a thin, unsupported area can bend the part."),
        ("Repeatability",
         "A good fixture lets any trained operator get the same result as an expert. Repeatability is the main reason fixtures are built, and it keeps quality steady over a run."),
        ("Recovering tooling cost",
         "A fixture costs money to design and build. That cost is spread across the parts made in a run. Comparing it with the saving per part shows whether the fixture pays."),
        ("The payback of a good fixture",
         "If a fixture saves minutes on each part, the saving adds up over the run. Payback time is the build cost divided by the saving per part. A shorter payback makes a fixture a safe investment."),
    ],
    "test": [
        ("What is the main job of a locating point?",
         [("a", "To paint the part"), ("b", "To place the part in the same position every time"), ("c", "To cool the part"), ("d", "To weigh the part")], "b"),
        ("What is the main reason for building a fixture?",
         [("a", "To add colour to the part"), ("b", "To make parts heavier"), ("c", "To slow production down"), ("d", "To get repeatable results from every part")], "d"),
        ("Where should clamps press?",
         [("a", "On solid points that the locators support"), ("b", "On the thinnest edge"), ("c", "Over a hole"), ("d", "On any loose corner")], "a"),
        ("How is payback time worked out?",
         [("a", "Build cost times number of parts"), ("b", "Saving per part times build cost"), ("c", "Build cost divided by saving per part"), ("d", "Number of parts plus the paint cost")], "c"),
        ("How does a jig differ from a fixture?",
         [("a", "A jig also guides the cutting tool"), ("b", "A jig cools the part"), ("c", "A jig weighs the part"), ("d", "A jig paints the part")], "a"),
    ],
}
