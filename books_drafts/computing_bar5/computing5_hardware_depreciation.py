"""Hardware Depreciation and Refresh Cycles: how the cost of equipment is spread over its life, and when to replace it."""
CODE = "computing5_hardware_depreciation"
BOOK = {
    "title": "Hardware Depreciation and Refresh Cycles",
    "subtitle": "Spreading equipment costs over its life, and planning when to replace it",
    "chapters": [
        ("Useful lives",
         "The useful life is the number of years an asset is expected to be worth using. It is an estimate, set by the team and its accountants. Servers, laptops and network gear each have their own typical lives."),
        ("Depreciation methods",
         "Depreciation spreads the cost of an asset over its useful life, so it does not all land in one year. The straight-line method charges the same amount each year. A reducing-balance method charges more in the early years and less later."),
        ("Refresh timing",
         "A refresh cycle is the planned time to replace equipment before it fails or falls behind. Replacing too early wastes money, and replacing too late raises repair and downtime costs. The right point is where the total cost is lowest."),
        ("Residual value",
         "Residual value is what an asset may be worth at the end of its life, such as its scrap or resale value. It is subtracted from the cost before depreciation is spread out. Estimates of residual value should be cautious."),
        ("Capital plans",
         "A capital plan lists the equipment to be bought over several years, with its cost and timing. It shows when large payments fall due, so cash can be set aside. Good plans are reviewed each year as needs and prices change."),
        ("Reading the asset register",
         "The asset register is the list of owned equipment, with the cost, purchase date, useful life and location of each item. Check it against what is really in use. Items still on the list but no longer in use may need to be written off."),
    ],
    "test": [
        ("What does straight-line depreciation do?",
         [("a", "It charges the whole cost in year one"), ("b", "It spreads the cost evenly over the useful life"), ("c", "It charges random amounts each year"), ("d", "It charges only when the asset is sold")], "b"),
        ("What is residual value?",
         [("a", "The cost of the first year"), ("b", "The total repair bill"), ("c", "The number of users of the asset"), ("d", "What an asset may be worth at the end of its life")], "d"),
        ("How does a reducing-balance method charge depreciation?",
         [("a", "More in the early years and less later"), ("b", "The same amount every year"), ("c", "Nothing until the asset is sold"), ("d", "Double the amount every year")], "a"),
        ("What is an asset register?",
         [("a", "A staff rota"), ("b", "A sales ledger"), ("c", "A list of owned assets with cost, date and life"), ("d", "A bank statement")], "c"),
        ("What is a refresh cycle?",
         [("a", "A fire drill"), ("b", "The planned time to replace equipment"), ("c", "A cleaning schedule"), ("d", "A tax form")], "b"),
    ],
}
