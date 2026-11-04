"""Consumables, Stock and Supply Costs: unit costs, shelf life, waste, stock levels and stock-outs."""
CODE = "science4_money_consumables"
BOOK = {
    "title": "Consumables, Stock and Supply Costs",
    "subtitle": "Keeping the shelves stocked without wasting money",
    "chapters": [
        ("Unit costs", "A unit cost is the price of one item, such as one vial or one pipette tip. Multiply the unit cost by the number used to find the total. Knowing unit costs helps compare suppliers fairly."),
        ("Bulk buying", "Buying in bulk often lowers the unit price, but it ties up money and space. Check shelf life before buying a large amount. A good deal is only good if the stock is used in time."),
        ("Shelf life", "Many reagents lose strength or change over time, and they carry an expiry date. Use older stock first, a method called first in, first out. Mark dates clearly on every item when it arrives."),
        ("Waste", "Waste includes out-of-date stock, broken items and items opened and thrown away unused. Track waste each month to find where money is lost. Small savings add up across a whole year."),
        ("Stock levels", "A reorder level is the stock amount that triggers a new order. Setting it too low risks running out, and setting it too high ties up money. Review levels as the research plans change."),
        ("The cost of a stock-out", "A stock-out happens when an item runs out before it is reordered. Experiments may stop, and staff time is lost while they wait. The cost of a stock-out can be much more than the cost of the item itself."),
    ],
    "test": [
        ("What is a unit cost?",
         [("a", "The cost of a whole building"), ("b", "The price of a lab coat only"), ("c", "The fee for a conference"), ("d", "The price of one item, such as one pipette tip")], "d"),
        ("What is the main risk of buying in bulk?",
         [("a", "The items become cheaper with time"), ("b", "Suppliers never deliver"), ("c", "Money and space are tied up and stock can expire"), ("d", "Staff cannot read labels")], "c"),
        ("What does first in, first out mean?",
         [("a", "Using the newest stock first"), ("b", "Using the oldest stock first"), ("c", "Ordering the most expensive item first"), ("d", "Keeping every item for ever")], "b"),
        ("What is waste in stock management?",
         [("a", "Out-of-date or broken items that are thrown away"), ("b", "Items kept on the shelf"), ("c", "Items that are ordered on time"), ("d", "Extra staff in the store")], "a"),
        ("What is a reorder level?",
         [("a", "The date of a lab inspection"), ("b", "The stock level that triggers a new order"), ("c", "The price of the largest item"), ("d", "The number of staff on duty")], "b"),
    ],
}
