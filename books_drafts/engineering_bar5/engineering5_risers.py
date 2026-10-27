"""Riser Design and Feeding of Castings: shrinkage porosity, feeding distance, riser sizing, chills and casting yield."""
CODE = "engineering5_risers"
BOOK = {
    "title": "Riser Design and Feeding of Castings",
    "subtitle": "Keeping molten metal flowing into a casting as it shrinks",
    "chapters": [
        ("Shrinkage in a casting",
         "As metal freezes, it shrinks. If no liquid metal can reach a spot to fill the gap, shrinkage porosity forms there. The casting looks sound from outside but can be weak inside."),
        ("What a riser does",
         "A riser is an extra reservoir of molten metal attached to the casting. It stays liquid longer than the part and feeds metal into the casting as the part shrinks. The riser is cut off after the casting cools."),
        ("Feeding distance",
         "Liquid metal can only feed so far from the riser before it freezes. This is the feeding distance. Engineers place risers so that every thick area is within reach of one."),
        ("Riser sizing",
         "A riser must stay liquid until the part it feeds has frozen. It is sized by its own freezing time and the shape of the casting. Too small a riser freezes first and does nothing."),
        ("Chills",
         "A chill is a block of metal placed in the mould to pull heat out of a spot quickly. It speeds the freezing there, so the riser can feed another area. Chills are used where a riser cannot reach."),
        ("Casting yield",
         "Yield is the share of the poured metal that ends up in good castings. Risers are metal that is removed and remelted, so a large riser lowers the yield. Engineers size the risers as small as sound feeding allows."),
    ],
    "test": [
        ("What causes shrinkage porosity?",
         [("a", "Metal is painted too thickly"), ("b", "The mould is too cold to touch"), ("c", "Liquid metal cannot reach a spot to fill the gap as it shrinks"), ("d", "The casting is too light")], "c"),
        ("What is a riser?",
         [("a", "A handle for carrying the part"), ("b", "A type of paint"), ("c", "A cooling fan"), ("d", "An extra reservoir of molten metal that feeds the casting")], "d"),
        ("What is feeding distance?",
         [("a", "How far liquid metal can flow from the riser before it freezes"), ("b", "The distance from the factory to the shop"), ("c", "The length of a tool"), ("d", "The height of the worker")], "a"),
        ("When must a riser stay liquid?",
         [("a", "Only during the first second"), ("b", "Until the part it feeds has frozen"), ("c", "Never"), ("d", "After the part is painted")], "b"),
        ("What is casting yield?",
         [("a", "The price of the mould"), ("b", "The speed of the crane"), ("c", "The share of poured metal that ends up in good castings"), ("d", "The number of colours used")], "c"),
    ],
}
