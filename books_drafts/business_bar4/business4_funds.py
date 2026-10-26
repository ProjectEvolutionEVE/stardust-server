"""Mutual Funds and ETFs: pooled money, net asset values and how the two differ."""
CODE = "business4_funds"
BOOK = {
    "title": "Mutual Funds and ETFs",
    "subtitle": "Pooled money, net asset values and how the two differ",
    "chapters": [
        ("Pooling money",
         "A mutual fund pools money from many investors and buys a portfolio chosen by a manager. Each investor owns units or shares in the fund. The pool gives small investors access to a diversified set of assets."),
        ("Net asset value",
         "A mutual fund's price is its net asset value per unit: the total value of its holdings, minus its liabilities, divided by the number of units. It is usually set once a day after markets close. You buy or sell at that day's price."),
        ("How an ETF trades",
         "An exchange-traded fund is a fund whose shares trade on an exchange throughout the day, like a company's stock. Its price can move slightly above or below its net asset value. Large traders keep it close to fair value."),
        ("Active against passive",
         "Active funds try to beat a benchmark through research and trading. Passive funds aim to match an index. Over long periods, many active funds have struggled to beat their benchmark after fees, which is one reason passive funds have grown."),
        ("Expense ratios",
         "The expense ratio is the yearly fee as a share of assets. A fund with a 0.2% ratio charges 2 for every 1,000 invested each year. Small ratios add up over time, so compare them carefully."),
        ("Choosing a vehicle",
         "Compare the cost, the holdings, how closely the fund tracks its aim, how it trades, and the rules for buying and selling. A fund is a tool for reaching a goal, not the goal itself. This is general education, not personal advice."),
    ],
    "test": [
        ("What does a mutual fund pool?",
         [("a", "Only one investor's money"), ("b", "Money from many investors, invested in one portfolio"), ("c", "Bank deposits"), ("d", "Tax payments")], "b"),
        ("How is a mutual fund's price usually set?",
         [("a", "By the buyer's offer"), ("b", "Every hour by law"), ("c", "Never"), ("d", "Once a day, as its net asset value per unit")], "d"),
        ("How do ETF shares trade?",
         [("a", "On an exchange through the day, like a stock"), ("b", "Only once a year"), ("c", "Only by post"), ("d", "Only with the government")], "a"),
        ("What is an expense ratio?",
         [("a", "A tax on profits"), ("b", "The number of holdings"), ("c", "The yearly fee as a share of assets"), ("d", "The price per share")], "c"),
        ("What does a passive fund aim to do?",
         [("a", "Beat the market every year"), ("b", "Match an index"), ("c", "Trade as often as possible"), ("d", "Avoid all shares")], "b"),
    ],
}
