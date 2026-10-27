"""Packaging Design and Drop Tests: protecting a product on its way to the customer, and what damage costs."""
CODE = 'engineering4_packaging'
BOOK = {
    "title": "Packaging Design and Drop Tests",
    "subtitle": "Protecting a product on its way to the customer, and what damage costs",
    "chapters": [
        ("Cushioning",
         "Packaging absorbs shocks with foam, paper or moulded pulp. Cushioning spreads the force, so the product is not struck hard in one spot."),
        ("Drop heights",
         "A drop test drops a packed product from set heights onto set faces, edges and corners. The chosen height reflects how the product will really be handled."),
        ("Vibration tests",
         "Trucks and ships vibrate for hours. Vibration tests shake packed products to find loose parts and weak points that fatigue over time."),
        ("Damage cost",
         "Each damaged item costs the product itself, its replacement, the shipping and the customer's trust. Damage is often more costly than the packaging."),
        ("Cost per unit protected",
         "Divide the packaging cost by the number of units it protects. A cheap box that breaks often can cost more per unit than a stronger one."),
        ("Testing before shipping",
         "Testing a sample before a full run finds weak points early. Changes made at that stage cost far less than a recall or a flood of complaints."),
    ],
    "test": [
        ("What does cushioning do?",
         [("a", "Makes the box heavier"), ("b", "Spreads shock so the product is not struck hard in one spot"), ("c", "Stops air from moving"), ("d", "Adds colour")], "b"),
        ("What is a drop test?",
         [("a", "A test of paint"), ("b", "A test of colour"), ("c", "Dropping a packed product from set heights onto set faces and corners"), ("d", "A test of the price")], "c"),
        ("What do vibration tests look for?",
         [("a", "Loose parts and fatigue"), ("b", "The colour of the box"), ("c", "The shop name"), ("d", "The postal code")], "a"),
        ("What does a cheap box that breaks often cost per unit?",
         [("a", "Nothing"), ("b", "Less than before"), ("c", "Only the glue"), ("d", "More, once damage is counted")], "d"),
        ("Why test a sample before a full run?",
         [("a", "To waste time"), ("b", "To find weak points early, when changes cost far less"), ("c", "To skip packing"), ("d", "To hide faults")], "b"),
    ],
}
