"""The True Cost of Scientific Instruments: purchase, installation, service, consumables and training."""
CODE = "science4_money_instrument_cost"
BOOK = {
    "title": "The True Cost of Scientific Instruments",
    "subtitle": "The price tag is only the start",
    "chapters": [
        ("The purchase price", "The price on the quote is the first cost of an instrument, but rarely the only one. Buyers should look at the full cost over the instrument's working life. A cheap machine can cost more over time than a dearer one."),
        ("Installation and set-up", "Many instruments need a special room, a steady power supply, cooling or gas lines before they work. Delivery, installation and first calibration can add a large sum. Planning these costs early avoids surprises."),
        ("Service contracts", "A service contract covers regular checks and repairs by the maker or an approved firm. Without one, a breakdown can be expensive and slow. Compare the yearly fee with the cost of a single major repair."),
        ("Consumables and training", "Consumables are the items used up in each run, such as columns, lamps, gases and reagents. Training staff takes time and money, and poorly trained users can damage an instrument. Both costs belong in the budget."),
        ("The total spend", "Total cost of ownership adds up purchase, installation, service, consumables, training and eventual disposal. Comparing options on this total shows which choice is truly cheaper. It also shows how long the money must be found."),
        ("Using the numbers", "A simple table with one row for each cost, year by year, makes the comparison clear. Reviewers and funders often ask for this kind of table. The table should be checked against supplier quotes, not guessed."),
    ],
    "test": [
        ("What is the main reason to look beyond the purchase price?",
         [("a", "Prices never change"), ("b", "Suppliers hide the price"), ("c", "Instruments are free to run"), ("d", "Costs continue over the instrument's working life")], "d"),
        ("Which item is often needed before an instrument can work?",
         [("a", "A new car"), ("b", "A suitable power supply or special room"), ("c", "A painted label"), ("d", "A paper certificate only")], "b"),
        ("What does a service contract usually cover?",
         [("a", "Regular checks and repairs"), ("b", "Free coffee for staff"), ("c", "The cost of the building"), ("d", "The rent of the laboratory")], "a"),
        ("What are consumables?",
         [("a", "Items that never wear out"), ("b", "The laboratory furniture"), ("c", "Items used up in each run, such as reagents and gases"), ("d", "Staff salaries")], "c"),
        ("What does total cost of ownership add up?",
         [("a", "Only the purchase price"), ("b", "Purchase, installation, service, consumables, training and disposal"), ("c", "Only the yearly fee"), ("d", "Only the cost of the room")], "b"),
    ],
}
