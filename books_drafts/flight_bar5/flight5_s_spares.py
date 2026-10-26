"""Spares and Logistics: having the right part in the right place, on time."""
CODE = "flight5_s_spares"
BOOK = {
    "title": "Spares and Logistics",
    "subtitle": "Having the right part in the right place, on time",
    "chapters": [
        ("What a spare is",
         "A spare part is kept ready so a broken unit can be swapped quickly. The right spare saves time, and time can decide whether a mission succeeds."),
        ("Lead times",
         "Some parts take months to make. Engineers plan ahead so that spares are in place before they are needed."),
        ("Orbital replacement units",
         "On the International Space Station, many parts are built as orbital replacement units, or ORUs. A crew member can swap one out with standard tools, and the faulty unit then goes back for repair."),
        ("Cannibalising",
         "Sometimes a working part is taken from one unit to fix another. This keeps a craft running, but it leaves a gap that must be filled later."),
        ("The cost of stock",
         "Spares cost money to buy and to store. Too many tie up funds, and too few risk long delays."),
        ("Resupply",
         "Spacecraft carry spares to the station on cargo flights. Careful planning decides what goes up and what waits."),
    ],
    "test": [
        ("What is a spare part?",
         [("a", "A part that is sold on"), ("b", "A part that is painted"), ("c", "A part kept ready to replace a broken one"), ("d", "A part kept on display")], "c"),
        ("What is a lead time?",
         [("a", "The time between ordering a part and receiving it"), ("b", "The time a craft spends in orbit"), ("c", "The age of a crew member"), ("d", "The length of a radio call")], "a"),
        ("What are ORUs on the International Space Station?",
         [("a", "Orbital radio units"), ("b", "Orange rubber units"), ("c", "Ordinary rooms"), ("d", "Orbital replacement units")], "d"),
        ("What is cannibalising?",
         [("a", "Eating food in orbit"), ("b", "Taking a working part from one unit to repair another"), ("c", "Selling parts"), ("d", "Painting a craft")], "b"),
        ("What is the main risk of holding too few spares?",
         [("a", "Long delays when something breaks"), ("b", "Too much weight"), ("c", "Fire"), ("d", "Poor radio reception")], "a"),
    ],
}
