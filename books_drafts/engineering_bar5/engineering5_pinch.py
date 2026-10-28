"""Pinch Analysis for Heat Integration: finding how much heat a plant can reuse internally, and the energy it must still buy."""
CODE = "engineering5_pinch"
BOOK = {
    "title": "Pinch Analysis for Heat Integration",
    "subtitle": "Composite curves, the pinch and heat recovery targets",
    "chapters": [
        ("Heat that goes to waste", "A plant often throws away heat that could be reused in another part of the same plant. Pinch analysis finds how much of that heat can be recovered."),
        ("Composite curves", "Composite curves combine all the hot streams and all the cold streams on one temperature and heat chart. The chart shows where heat is available and where it is needed."),
        ("The pinch", "The pinch temperature is the point where the hot and cold curves come closest. It limits how much heat can be recovered, and it guides the design."),
        ("Heat recovery targets", "The curves give the minimum hot and cold utilities that a plant needs. These targets show how far the design can go before the plant must buy more energy."),
        ("Network design", "Heat exchangers are matched above and below the pinch, following rules that avoid wasting energy. Crossing the pinch with the wrong match wastes energy."),
        ("The money side", "Saving energy cuts fuel and utility bills. A good pinch analysis can show where the savings are, and what it costs to get them."),
    ],
    "test": [
        ("What is pinch analysis used for?", [("a", "Painting the walls of a plant"), ("b", "Choosing shoes for the staff"), ("c", "Heat integration, reusing heat within a plant"), ("d", "Baking bread in the canteen")], "c"),
        ("What do composite curves combine?", [("a", "All the hot streams and all the cold streams"), ("b", "All the cats in the plant"), ("c", "All the cars in the car park"), ("d", "All the colours in the paint shop")], "a"),
        ("What is the pinch temperature?", [("a", "The price of heat per unit"), ("b", "Where the hot and cold curves come closest"), ("c", "The heat of a cup of tea"), ("d", "A pinch of salt in the sauce")], "b"),
        ("What do the curves give?", [("a", "The number of staff needed"), ("b", "The lunch menu for the week"), ("c", "The minimum hot and cold utilities a plant needs"), ("d", "The cinema times nearby")], "c"),
        ("Why does saving energy matter?", [("a", "It adds to the bills"), ("b", "It changes the colour of the plant"), ("c", "It stops the sun from shining"), ("d", "It cuts fuel and utility bills")], "d"),
    ],
}
