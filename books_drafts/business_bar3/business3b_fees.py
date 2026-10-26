"""Fees and Returns (Manager, bar 3, part B): how small charges take a large share of what money earns over time."""
CODE = "business3b_fees"
BOOK = {
    "title": "Fees and Returns",
    "subtitle": "How small charges take a large share of what your money earns over time",
    "chapters": [
        ("A fee is a charge",
         "A fee is a charge taken from your money or your trades. Fees can be a fixed amount, a percentage of the amount held, a charge per trade, or a spread built into the price you pay."),
        ("Percentage fees add up",
         "A fee of 1% a year sounds small. Over decades, it compounds against you. Each year the fee takes a slice of the amount, so the money that grows is smaller, and so is every later gain."),
        ("A worked example",
         "Take 10,000 credits growing 7% a year for 30 years. With no fee, it reaches about 76,100 credits. With a 1% yearly fee, which cuts the growth to 6%, it reaches about 57,400. The fee has cost about 18,700 credits."),
        ("Trading costs",
         "Every trade can carry a fee and a spread, and a frequent trader pays them again and again. Ask what a trade costs before you make it. Count that cost against the gain you expect."),
        ("Read the fee list",
         "Read the full list of charges before you commit. Look for entry fees, exit fees, yearly charges and performance charges. A fee you cannot find on the summary is still a fee."),
        ("The auction fee",
         "On the Starship, the winner of a blueprint auction pays a 2.5% fee on top of the winning bid. The designer receives the full winning bid. Count that fee into your top bid before you place it."),
    ],
    "test": [
        ("What is a fee?",
         [("a", "A charge taken from your money or your trades"), ("b", "A gift from a bank"), ("c", "A rate that rises with inflation"), ("d", "A deposit you get back")], "a"),
        ("A fee of 1% a year cuts growth from 7% to 6%. Why does it cost more than it looks?",
         [("a", "Because it is paid only once"), ("b", "Because the fee is never charged on gains"), ("c", "Because it compounds, so the lost growth builds up over the years"), ("d", "Because banks keep the fee for themselves")], "c"),
        ("Using the worked example, about how much does a 1% yearly fee cost over 30 years on 10,000 credits growing at 7%?",
         [("a", "1,000 credits"), ("b", "About 18,700 credits"), ("c", "About 76,100 credits"), ("d", "About 57,400 credits")], "b"),
        ("What is a spread, as a kind of cost?",
         [("a", "A fee for opening an account"), ("b", "The gap between the buy and sell prices, which you pay on each round trip"), ("c", "A yearly charge on savings"), ("d", "A tax on gains")], "b"),
        ("On a winning bid of 1,000 credits, how much is the 2.5% auction fee the winner pays on top?",
         [("a", "2.5 credits"), ("b", "250 credits"), ("c", "1,025 credits"), ("d", "25 credits")], "d"),
    ],
}
