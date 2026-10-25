"""Lots, Floors and Fees (Trader, bar 1): minimum lots, floor prices, the auction fee and the printing fees."""
CODE = "business1_lots"
BOOK = {
    "title": "Lots, Floors and Fees",
    "subtitle": "The smallest orders, the lowest prices, and the fees you will pay",
    "chapters": [
        ("What a lot is",
         "A lot is the smallest order you can place. Prices are whole credits per lot. Iron ore and copper ore trade in 100 kg lots, silver ore in 10 kg lots, and native gold and industrial diamond in 1 kg lots. Your order always counts in whole lots."),
        ("Why lots are sized this way",
         "Goods with wide price swings get bigger minimum orders, so there are no really small orders. Ore that is less than one lot waits in your space in the cargo hold until you have a full lot to sell."),
        ("Floor prices",
         "Each item has a floor price, and nothing trades below it. In the current price list, the floor is half of the starting price. For example, iron ore starts at 200 credits per 100 kg lot, and its floor is 100 credits."),
        ("The auction fee",
         "When a blueprint copy sells at auction, the winner pays the winning bid plus a 2.5% Starship fee on top. The fee is rounded up to whole credits and goes to the WSC, the governing body. The designer receives the full winning bid."),
        ("Printing fees",
         "A blueprint is printed in runs. The first run of a design costs a one-time setup fee of 100 credits, plus 10 credits for each copy. Later runs cost 10 credits for each copy. Printing credits go to the Starship Bank. So a first run of 25 copies costs 350 credits."),
        ("Pricing your copies",
         "A designer sets a floor for the copies they auction. Setting it above what each copy cost is how a designer makes a profit. A floor below cost is allowed only after you tick a warning box that confirms you know you are selling below your costs."),
    ],
    "test": [
        ("What is the smallest order you can place for native gold?",
         [("a", "1 kg"), ("b", "10 kg"), ("c", "100 kg"), ("d", "1 g")], "a"),
        ("What is an item's floor price?",
         [("a", "The highest price anyone can bid"), ("b", "The lowest price a trade can happen at, half of its starting price"), ("c", "The price the WSC pays"), ("d", "The fee on each order")], "b"),
        ("What is the auction fee on a winning bid?",
         [("a", "25% of the bid, paid by the designer"), ("b", "2.5% on top of the bid, paid by the winner"), ("c", "10% of the bid, paid by the bank"), ("d", "Nothing at all")], "b"),
        ("Where do the printing fees go?",
         [("a", "To the WSC"), ("b", "To the buyer of the copy"), ("c", "To the Starship Bank"), ("d", "To nobody; they are refunded")], "c"),
        ("How many credits does a first print run of 25 copies cost?",
         [("a", "250"), ("b", "100"), ("c", "2,500"), ("d", "350")], "d"),
    ],
}
