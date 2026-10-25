"""Reading the Order Book (Trader, bar 1): bids, asks, limit orders, Buy now and Sell now, and the Starship bank's desks."""
CODE = "business1_orderbook"
BOOK = {
    "title": "Reading the Order Book",
    "subtitle": "Bids, asks, limit orders and the instant buy and sell",
    "chapters": [
        ("Two lists",
         "The order book has two lists. Bids are offers to buy, and asks are offers to sell. The best bid is the highest price a buyer will pay. The best ask is the lowest price a seller will take. The best price always comes first."),
        ("Limit orders",
         "A limit order names your price. A limit bid buys at that price or lower, and it waits if no one is selling there yet. A limit ask sells at that price or higher. Your credits or your goods are set aside as soon as you place the order, and cancelling gives them back."),
        ("Buy now and Sell now",
         "Buy now and Sell now take the best orders already waiting, one price after another. They never wait. A trade fills at the price of the order that was already waiting, so you know what you will pay before you press the button."),
        ("Nobody is named",
         "Traders are never named. The book shows prices and amounts, not who is on the other side. Players never talk to each other, so you learn only from the prices and the trades you can see."),
        ("The Starship bank on the book",
         "The Starship bank trades on this market too. Its buy desk and sell desk keep a standing bid 10% under and a standing ask 10% over the last price, so you can always sell and always buy. The two desks trade with each other and with players."),
        ("Reading the trades",
         "Each trade shows its price, its quantity and the time it happened. When the price rises across several trades, the market is climbing. Traders call this running list of trades the tape, and it tells you more than one trade alone."),
    ],
    "test": [
        ("What is a limit order?",
         [("a", "An order that trades at any price at once"), ("b", "An order with a set price that waits until the market reaches it"), ("c", "An order the bank cancels for you"), ("d", "An order with no price at all")], "b"),
        ("What does Buy now do?",
         [("a", "Places a bid that waits in the queue"), ("b", "Cancels all your open orders"), ("c", "Sends a receipt to another player"), ("d", "Takes the best waiting sell orders, one price after another, without waiting")], "d"),
        ("Who is on the other side of a trade, as the book shows it?",
         [("a", "The name of the player who sold"), ("b", "The bank's name only"), ("c", "Nobody's name: traders are never named"), ("d", "The Captain")], "c"),
        ("Where is the Starship bank's standing bid, compared with the last price?",
         [("a", "10% over the last price"), ("b", "10% under the last price"), ("c", "Exactly equal to the last price"), ("d", "50% under the last price")], "b"),
        ("At what price does a trade fill?",
         [("a", "The price of the order that was already waiting"), ("b", "The price of the newer order"), ("c", "The average of both orders"), ("d", "The floor price")], "a"),
    ],
}
