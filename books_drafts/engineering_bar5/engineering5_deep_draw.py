"""Deep Drawing and Blank Holder Force: blank size, draw ratio, wrinkling and tearing, blank holder force and lubrication."""
CODE = "engineering5_deep_draw"
BOOK = {
    "title": "Deep Drawing and Blank Holder Force",
    "subtitle": "Pulling a flat sheet into a cup without tearing it",
    "chapters": [
        ("From flat sheet to cup",
         "Deep drawing pulls a flat blank of sheet metal into a die with a punch, forming a cup or box. It is used for drink cans, sinks and many car parts. The blank must flow into the die without tearing or wrinkling."),
        ("Blank size",
         "The blank must be the right size. Too small and the cup is short; too large and the extra metal wrinkles or wastes material. Engineers calculate the blank size from the part's shape before cutting."),
        ("Draw ratio",
         "The draw ratio compares the blank diameter with the punch diameter. A higher ratio means a harder draw. Above a limit, the cup tears, so most designs are planned in several draws."),
        ("Wrinkling and tearing",
         "Wrinkling happens when the flange of the blank buckles under compression. Tearing happens when the wall is pulled too thin at the punch corner. The two faults pull against each other, and the blank holder force is the tool for balancing them."),
        ("Blank holder force",
         "The blank holder presses the flange to control how fast the metal feeds in. Too little force lets it wrinkle; too much makes it tear. The force is set by calculation and then tuned on the press."),
        ("Lubrication",
         "Lubricant lets the blank slide across the die face. Good lubrication lowers the force needed and protects the die. The right lubricant and its even spread are part of the cost of each part."),
    ],
    "test": [
        ("What is deep drawing used to make?",
         [("a", "Paper lanterns"), ("b", "Glass windows"), ("c", "Cups, cans and boxes from flat sheet"), ("d", "Wooden boards")], "c"),
        ("What happens if the blank is too large?",
         [("a", "The cup gets taller with no other effect"), ("b", "The metal melts"), ("c", "Nothing at all"), ("d", "The extra metal can wrinkle or be wasted")], "d"),
        ("What does the draw ratio compare?",
         [("a", "The blank diameter with the punch diameter"), ("b", "The price with the weight"), ("c", "The colour with the shape"), ("d", "The speed with the noise")], "a"),
        ("What does the blank holder force control?",
         [("a", "The colour of the cup"), ("b", "How fast the metal feeds in, balancing wrinkles and tears"), ("c", "The temperature of the room"), ("d", "The name of the part")], "b"),
        ("What does good lubrication do?",
         [("a", "It makes the metal harder to shape"), ("b", "It stops the blank from moving at all"), ("c", "It lowers the force needed and protects the die"), ("d", "It adds weight to the part")], "c"),
    ],
}
