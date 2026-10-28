"""Warranty Claim Analysis: using claim records to see how products fail over their life, and to feed what is learned back into design."""
CODE = "engineering5_warranty"
BOOK = {
    "title": "Warranty Claim Analysis",
    "subtitle": "Claims, failure over product life and the cost of each claim",
    "chapters": [
        ("Why claims matter", "A warranty claim is a customer asking the maker to repair or replace a product under its promise. Claims are a record of what really fails in the hands of customers, which tests in the lab may not show."),
        ("Failure over product life", "Failures often come in three phases. Many appear early, fewer appear during the middle of the product's life, and more appear as parts wear out. Plotting this gives a curve shaped like a bathtub."),
        ("Cost per claim", "Each claim costs money in parts, labour, travel and shipping. Cost per claim is a key number, because it shows how much a failure really costs the business."),
        ("Setting a reserve", "A company sets aside money, called a reserve, to cover the claims it expects on products already sold. A reserve that is too small can hurt the accounts, and one that is too large ties up cash."),
        ("Feeding back into design", "Claim data shows which parts fail and why. Designers can use this to fix the weak part, change the material or change the test before the next product is built."),
        ("The money side", "A lower claim rate saves money and protects the brand. Claims analysis therefore pays for itself when it leads to fewer failures in the field."),
    ],
    "test": [
        ("What is a warranty claim?", [("a", "A customer asking for repair or replacement under the promise"), ("b", "A bank loan for a new factory"), ("c", "A patent for a new design"), ("d", "A sales tax on goods")], "a"),
        ("What does a bathtub curve show?", [("a", "How a bath is filled"), ("b", "Failure rate over product life, high early, low in the middle and rising at the end"), ("c", "The price of steel over a year"), ("d", "The path of a laser beam")], "b"),
        ("What is a reserve?", [("a", "Money set aside to cover expected claims"), ("b", "A spare part kept in stock"), ("c", "A type of weld"), ("d", "A sample of rock")], "a"),
        ("Why feed claim data back to design?", [("a", "To make the box bigger"), ("b", "To find which parts fail and fix them"), ("c", "To make the product colder"), ("d", "To avoid testing altogether")], "b"),
        ("Cost per claim includes what?", [("a", "Only the colour of the product"), ("b", "The weather on the day of repair"), ("c", "Parts, labour and shipping"), ("d", "The cost of office plants")], "c"),
    ],
}
