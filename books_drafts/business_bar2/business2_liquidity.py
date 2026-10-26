"""Liquidity and Volume (Broker, bar 2): how easily an item trades, how much has changed hands, and how far a big order moves the price."""
CODE = "business2_liquidity"
BOOK = {
    "title": "Liquidity and Volume",
    "subtitle": "How easily an item trades, and how much of it has changed hands",
    "chapters": [
        ("What liquidity means",
         "Liquidity is how easily something can be bought or sold at a fair price, straight away. A liquid item has many buyers and sellers waiting, so a trade is quick and the price barely moves. An illiquid item may take a long time to trade, or it may force you to accept a worse price."),
        ("Volume",
         "Volume is how much has traded over a period, counted in lots. The market screen shows each item's volume over the last 24 hours. High volume tells you the item is busy. Low volume tells you to go carefully."),
        ("Depth",
         "Depth is how much is waiting at each price, not just at the best one. A market with deep orders can take a big buy without the price jumping. A market with thin orders can jump several prices on a small trade."),
        ("How a big order moves a price",
         "A large order uses up the waiting orders one price after another. The further it reaches down the book, the worse its average price becomes. Splitting a large order into smaller lots over time can keep the price from running away from you."),
        ("Stock that trades slowly",
         "Ore under one lot waits in your cargo hold until you have a full lot, and a thin item may not trade quickly. Before you hold stock, check how often the item trades. Make sure you can sell when you need the credits."),
        ("Liquidity in the real world",
         "In the real world, cash is the most liquid thing there is, while a house or an antique can take months to sell. Markets can dry up in a panic, when everyone wants to sell and no one wants to buy. Liquidity is easy to take for granted until it is gone."),
    ],
    "test": [
        ("What does liquidity mean?",
         [("a", "How much an item weighs"), ("b", "How long its price history is"), ("c", "How easily something can be bought or sold at a fair price, straight away"), ("d", "How much the bank owns")], "c"),
        ("Where can you see the last 24 hours of volume for an item?",
         [("a", "On the market screen"), ("b", "In the closet"), ("c", "In the filing cabinet"), ("d", "On the bookshelf")], "a"),
        ("What is market depth?",
         [("a", "The number of players"), ("b", "How many lots are waiting at each price, not just the best one"), ("c", "The height of the chart"), ("d", "The fee on a trade")], "b"),
        ("Why does a large order often move the price?",
         [("a", "It uses up the waiting orders one price after another"), ("b", "It is always sent to the WSC"), ("c", "Prices move only on certain days"), ("d", "Large orders are not allowed")], "a"),
        ("Why is a thin item risky to hold?",
         [("a", "It is always cheap to buy"), ("b", "It may sell slowly, or only at a worse price when you need to sell"), ("c", "Thin items cannot be listed"), ("d", "The bank buys it at double the price")], "b"),
    ],
}
