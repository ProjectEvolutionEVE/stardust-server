"""Interest Rates (Manager, bar 3, part B): what a rate is, what moves it, and how it reaches savings, loans and bond prices."""
CODE = "business3b_interest_rates"
BOOK = {
    "title": "Interest Rates",
    "subtitle": "What the rate is, what moves it, and how it reaches your savings and loans",
    "chapters": [
        ("What a rate is",
         "An interest rate is the price of using money over time. Borrowers pay it to use someone else's money, and savers earn it for lending theirs. Rates are usually quoted per year."),
        ("The key rate",
         "Central banks set a key policy rate, and banks use it as a starting point for the rates they charge. When the key rate goes up, borrowing costs usually rise for most people. When it falls, borrowing usually gets cheaper."),
        ("Rates and saving",
         "Higher rates usually pay savers more, and they make borrowing dearer. Lower rates do the reverse. Because rates change how much people borrow and spend, they affect the whole economy."),
        ("Rates and bond prices",
         "A bond pays a fixed amount of interest. When new bonds pay more, older bonds that pay less become less attractive, so their price falls. Bond prices and interest rates usually move in opposite directions."),
        ("Nominal and real",
         "The rate printed on a loan or a savings account is the nominal rate. The real rate is the nominal rate minus inflation. A savings rate of 4% with inflation at 3% gives a real return of about 1%."),
        ("Read the terms",
         "Check whether a rate is fixed or variable. A fixed rate stays the same for an agreed time. A variable rate can move with market rates, so it can go up or down. Compare rates on the same basis before you choose."),
    ],
    "test": [
        ("What is an interest rate?",
         [("a", "The price of using money over time"), ("b", "A fee for opening an account"), ("c", "The number of years a loan lasts"), ("d", "The value of a building")], "a"),
        ("When a central bank raises its key rate, what usually happens to the cost of borrowing?",
         [("a", "It falls"), ("b", "It rises for most people"), ("c", "It stays exactly the same for everyone"), ("d", "It becomes free")], "b"),
        ("When new bonds pay more interest, what usually happens to the price of older bonds that pay less?",
         [("a", "It rises"), ("b", "It falls"), ("c", "It doubles"), ("d", "It stays the same")], "b"),
        ("A savings account pays 4% a year and inflation is 3%. What is the real return, roughly?",
         [("a", "4%"), ("b", "7%"), ("c", "1%"), ("d", "3%")], "c"),
        ("What is the difference between a fixed rate and a variable rate?",
         [("a", "A fixed rate can never be paid"), ("b", "A variable rate is always lower"), ("c", "A fixed rate stays the same, while a variable rate can move with market rates"), ("d", "A fixed rate is set by the customer")], "c"),
    ],
}
