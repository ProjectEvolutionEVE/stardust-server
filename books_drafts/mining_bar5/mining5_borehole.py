"""Borehole Geophysics: lowering instruments into a drill hole to log the rock, the fluid and the layers around it."""
CODE = "mining5_borehole"
BOOK = {
    "title": "Borehole Geophysics: Logging the Hole",
    "subtitle": "Logging tools, gamma and density, resistivity and fluids",
    "chapters": [
        ("A tool down the hole",
         "A borehole logging tool is lowered on a cable and slowly raised back up. As it moves, it records readings against depth. The result is a log, a continuous picture of the rock along the hole."),
        ("Gamma and density",
         "A gamma tool measures the natural radioactivity of the rock, which is higher in some shales and granites. A density tool sends gamma rays from a small sealed source and measures how many come back. The density tool uses a licensed sealed source, and both tools are run by trained crews."),
        ("Resistivity",
         "A resistivity tool measures how well the rock conducts electricity. Wet, salty or clay-rich layers conduct more, and dry or solid rock conducts less. Changes in resistivity often mark a change in rock type or in the fluid it holds."),
        ("Fluid logs",
         "Temperature and conductivity logs show how water moves in the hole. A change in temperature can show where water enters, and a change in salt content can show where it comes from. These logs help find water-bearing zones."),
        ("Calibration",
         "Every tool must be checked against known standards before and after each run. Readings are also compared with core samples from the same hole. A log that does not match the core needs investigating before anyone trusts it."),
        ("Interpretation",
         "A good geologist reads the logs together, not one at a time. Gamma, density and resistivity can agree on a layer, and that agreement makes the picture stronger. Interpretation turns the raw curves into a story about the rock."),
    ],
    "test": [
        ("What does a borehole log record?",
         [("a", "The number of birds nearby"), ("b", "Readings of the rock and fluid against depth"), ("c", "The price of the drill rig"), ("d", "The speed of the wind")], "b"),
        ("What does a gamma tool measure?",
         [("a", "The natural radioactivity of the rock"), ("b", "The temperature of the air"), ("c", "The colour of the mud"), ("d", "The weight of the cable")], "a"),
        ("What does a resistivity tool measure?",
         [("a", "How well the rock conducts electricity"), ("b", "How loud the drill is"), ("c", "How tall the tower is"), ("d", "How many workers are below")], "a"),
        ("Why are logs checked against standards?",
         [("a", "So the cable stays dry"), ("b", "So the drill runs faster"), ("c", "So the tool is calibrated and the readings can be trusted"), ("d", "So the hole gets deeper")], "c"),
        ("Why are several logs read together?",
         [("a", "Because one log alone can never show anything"), ("b", "Because logs must be printed in colour"), ("c", "Because the cable needs a second reel"), ("d", "Because agreement between logs makes the picture stronger")], "d"),
    ],
}
