"""Depreciating Navigation Equipment: asset life, straight-line depreciation, replacement, obsolescence, tax and planning."""
CODE = "navigation4_equipment_depreciation"
BOOK = {
    "title": "Depreciating Navigation Equipment",
    "subtitle": "Spreading the cost of instruments over the years they are useful",
    "chapters": [
        ("Asset life", "An asset's life is the number of years it is expected to be useful. Electronics may have shorter lives than ships. The life is an estimate, so it should be reviewed from time to time."),
        ("Straight-line depreciation", "Straight-line depreciation spreads the cost evenly over the asset's life. The same amount is charged each year. The formula is the cost, minus any scrap value, divided by the number of years."),
        ("Replacement", "Equipment is replaced when it is worn out or too costly to repair. Planning for replacement keeps money set aside. Sudden replacement needs can strain a budget."),
        ("Obsolescence", "An asset can become obsolete when newer equipment does the job better. It may still work but no longer be supported. Obsolescence can shorten an asset's useful life."),
        ("Tax", "Depreciation can change the tax a business pays, because it reduces taxable profit. Tax rules differ from country to country. A tax adviser should be consulted."),
        ("Planning", "Plan equipment purchases over many years. Include depreciation, replacement and upgrades. A clear plan avoids surprises and keeps costs steady."),
    ],
    "test": [
        ("What is an asset's life?", [("a", "The colour of the case"), ("b", "The number of years it is expected to be useful"), ("c", "The weight of the box"), ("d", "The price of the crew's food")], "b"),
        ("What does straight-line depreciation do?", [("a", "Spreads the cost evenly over the asset's life"), ("b", "Doubles the cost each year"), ("c", "Removes the cost completely"), ("d", "Charges all at once in year one")], "a"),
        ("What is obsolescence?", [("a", "When an asset gets a new paint job"), ("b", "When an asset is sold at a profit"), ("c", "When an asset is taken to sea"), ("d", "When newer equipment makes an asset outdated")], "d"),
        ("How can depreciation affect tax?", [("a", "It always adds tax"), ("b", "It has no link to tax"), ("c", "It reduces taxable profit"), ("d", "It doubles the bill")], "c"),
        ("Why plan purchases over many years?", [("a", "To avoid buying anything"), ("b", "To avoid surprises and keep costs steady"), ("c", "To make old equipment last forever"), ("d", "To hide the costs")], "b"),
    ],
}
