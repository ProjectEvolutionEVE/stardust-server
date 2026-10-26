"""The Spread (Broker, bar 2): the gap between the best bid and the best ask, and what it costs to trade straight away."""
CODE = "business2_spreads"
BOOK = {
    "title": "The Spread",
    "subtitle": "The gap between the best bid and the best ask, and what it costs you",
    "chapters": [
        ("What a spread is",
         "The spread is the gap between the best bid and the best ask. The best bid is the highest price a buyer is offering, and the best ask is the lowest price a seller will take. If you buy at once, you pay the ask; if you sell at once, you get the bid. The gap between them is the cost of trading straight away."),
        ("Reading the gap",
         "Suppose the best bid is 180 credits and the best ask is 200 for one lot. The spread is 20 credits. Buy at 200 and sell straight back at 180, and you lose 20 credits per lot before any fees. A narrow spread means buyers and sellers agree closely on the price, and trading is cheap."),
        ("The bank's built-in spread",
         "The Starship bank keeps a standing bid 10% under the last price and a standing ask 10% over it. Those two offers sit 20% of the last price apart. If the last price is 200 credits, the bank bids 180 and asks 220. The bank never bids below the floor, so if the floor is higher than 180, the bid sits at the floor."),
        ("Why spreads widen and narrow",
         "A spread widens when few orders are waiting on one side, and it narrows when many are waiting. A thin item usually has a wide spread, so a careful trader checks the gap before buying a little-traded item. The wider the gap, the further the price must move before a trade breaks even."),
        ("Posting inside the gap",
         "If you can wait, a limit order can sit inside the spread. A limit bid just above the best bid may fill at a better price than the ask. But it may never fill, and your credits stay set aside until it does or you cancel."),
        ("Dealers and the gap",
         "Real markets for shares, currencies and goods all have spreads. Dealers who stand ready to buy and sell earn the gap for holding goods and taking the risk of price moves. Merchants have always quoted a buying price and a selling price, and the difference paid for their trouble."),
    ],
    "test": [
        ("The best bid is 180 credits and the best ask is 200. How wide is the spread?",
         [("a", "180 credits"), ("b", "20 credits"), ("c", "380 credits"), ("d", "10 credits")], "b"),
        ("The last price is 200 credits. Where does the bank's standing bid sit?",
         [("a", "180 credits"), ("b", "220 credits"), ("c", "190 credits"), ("d", "150 credits")], "a"),
        ("What does a narrow spread mean?",
         [("a", "Nobody is trading"), ("b", "Buyers and sellers are far apart"), ("c", "Buyers and sellers agree closely on the price"), ("d", "The floor price is zero")], "c"),
        ("What can happen to a limit bid placed inside the spread?",
         [("a", "It always fills at once at the ask"), ("b", "It may fill at a better price, or may never fill"), ("c", "It is sent to the WSC"), ("d", "It turns into a receipt")], "b"),
        ("Why do dealers in real markets earn a spread?",
         [("a", "The government pays them a fixed salary"), ("b", "They never hold any goods"), ("c", "Their customers must pay them a fee on every visit"), ("d", "They take the risk of holding goods and earn the gap between buying and selling prices")], "d"),
    ],
}
