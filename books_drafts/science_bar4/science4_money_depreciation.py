"""Equipment Depreciation and Replacement Planning: spreading asset costs and planning for replacement."""
CODE = "science4_money_depreciation"
BOOK = {
    "title": "Equipment Depreciation and Replacement Planning",
    "subtitle": "Planning for the day equipment wears out",
    "chapters": [
        ("What depreciation means", "Depreciation spreads the cost of an asset over the years it is used. Each year the asset's book value falls by a share of its cost. This is an accounting method, and it does not always match the market price."),
        ("Straight-line depreciation", "The simplest method is straight-line. Take the cost, subtract any expected scrap value, and divide by the useful life in years. The same amount is then charged each year."),
        ("Useful life and obsolescence", "Useful life is how long an asset is expected to be of use. Obsolescence happens when newer equipment does the job better, even if the old machine still works. Both should be estimated honestly."),
        ("Replacement reserves", "A replacement reserve is money set aside each year to buy new equipment when the time comes. Saving a little each year avoids a large unplanned bill. Reserves turn a sudden cost into a steady one."),
        ("Repair or replace", "When a machine breaks, compare the repair cost with the cost of a new one. Consider how many years of use a repair would buy and whether the new machine saves time or money. Write the reasons down."),
        ("Asset registers", "An asset register lists each item with its purchase date, cost, location and expected life. Keeping it up to date helps with insurance, audits and planning. It also shows when items should be checked or replaced."),
    ],
    "test": [
        ("What does straight-line depreciation do?",
         [("a", "Doubles the cost each year"), ("b", "Spreads the cost evenly over the useful life"), ("c", "Ignores the asset's life"), ("d", "Sets a price for resale only")], "b"),
        ("How is the annual straight-line charge calculated?",
         [("a", "Cost times two"), ("b", "Cost plus the scrap value"), ("c", "Scrap value divided by the cost"), ("d", "Cost minus scrap value, divided by the useful life")], "d"),
        ("What is obsolescence?",
         [("a", "Equipment being painted"), ("b", "Equipment being sold at auction"), ("c", "Equipment made less useful by newer and better models"), ("d", "Equipment being moved to a new room")], "c"),
        ("What is a replacement reserve?",
         [("a", "Money saved each year for buying new equipment later"), ("b", "A spare part kept in a drawer"), ("c", "A loan from a bank"), ("d", "A type of insurance for staff cars")], "a"),
        ("What is an asset register?",
         [("a", "A list of staff holidays"), ("b", "A book of recipes"), ("c", "A list of journal articles"), ("d", "A list of equipment with purchase dates, costs and expected life")], "d"),
    ],
}
