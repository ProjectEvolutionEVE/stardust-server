"""Costing a Product (Broker, bar 2): materials bought in lots, and printing runs, added up per unit."""
CODE = "business2_costing"
BOOK = {
    "title": "Costing a Product",
    "subtitle": "Materials, lots and printing runs, added up per unit",
    "chapters": [
        ("What goes into a cost",
         "The cost of one unit is everything you paid to make it: the materials, any fees, and any service you hired. Start from the list of materials on the design, then add the fees. Forgetting one item is the most common costing mistake."),
        ("Materials by the lot",
         "Materials are bought in lots, so a unit's share of a lot is part of its cost. At the current price list, a 10 kg lot of silver ore costs 300 credits. If a part needs 2 kg of it, that part carries 60 credits of silver ore cost."),
        ("Printing costs per copy",
         "A first run costs 100 credits once, plus 10 credits a copy. The setup fee is shared by every copy in that run, so a small run costs more per copy. A first run of 10 copies costs 200 credits, which is 20 each. A later run of 40 copies has no setup fee, so it costs 400 credits, which is 10 each."),
        ("Copies that never sell",
         "Some copies may never sell, and their printing cost is spent all the same. Plan the size of a run with the auction in mind. A copy that stays in your filing cabinet has cost you money and earned nothing."),
        ("Write the cost down",
         "Write the cost per unit beside the design, with the date and the run it came from. A new run can cost differently from an old one, so keep each run's cost apart. Then you always know what each copy really cost you."),
        ("The habit of costing",
         "Businesses on Earth call this costing, and it is the start of every price. A baker who does not know the cost of a loaf cannot tell whether a sale is a loss. Know your costs first, and only then choose your price."),
    ],
    "test": [
        ("What is included in the cost of one unit?",
         [("a", "Only the price you hope to get"), ("b", "Only the bank's fee"), ("c", "Materials, fees and any service you hired"), ("d", "Only the floor")], "c"),
        ("A 10 kg silver ore lot costs 300 credits. What does 2 kg of it cost?",
         [("a", "30 credits"), ("b", "150 credits"), ("c", "300 credits"), ("d", "60 credits")], "d"),
        ("A first print run of 10 copies costs how much?",
         [("a", "110 credits"), ("b", "200 credits"), ("c", "100 credits"), ("d", "2,000 credits")], "b"),
        ("A later run of 40 copies, with no setup fee, costs how much?",
         [("a", "40 credits"), ("b", "500 credits"), ("c", "400 credits"), ("d", "10 credits")], "c"),
        ("Why does a small first run cost more per copy than a large one?",
         [("a", "The bank adds a tax"), ("b", "The setup fee is shared by fewer copies"), ("c", "The copies are bigger"), ("d", "Small runs skip the copy fee")], "b"),
    ],
}
