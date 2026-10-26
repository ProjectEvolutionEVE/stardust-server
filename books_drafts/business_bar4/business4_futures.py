"""Futures and Forwards: agreeing today on a price for later."""
CODE = "business4_futures"
BOOK = {
    "title": "Futures and Forwards",
    "subtitle": "Agreeing today on a price for later",
    "chapters": [
        ("An agreement for later",
         "A forward contract is a private deal to buy or sell something at a set price on a future date. A futures contract is a standard version traded on an exchange. Both lock in a price now for a delivery later."),
        ("The Dojima rice market",
         "Early futures-style trading is often traced to the Dojima rice market in Osaka, in the 1700s. Rice merchants and the samurai paid in rice used forward contracts to manage price swings at harvest. Exchanges later standardised such contracts."),
        ("Margin and marking to market",
         "Futures holders post margin, a deposit held as security. Each day, gains and losses are settled through the margin account. This daily settlement is called marking to market, and it keeps the exchange protected from unpaid losses."),
        ("Delivery or cash",
         "Some contracts end with physical delivery of the goods, such as oil or grain. Many are settled in cash by the difference from the final price. Most traders close their positions before the delivery date."),
        ("Basis",
         "Basis is the gap between the spot price today and the futures price for the same asset. It narrows as delivery approaches. Changes in the basis can make a hedge less than perfect."),
        ("Hedgers and speculators",
         "Hedgers, such as a farmer or an airline, use futures to reduce price risk. Speculators take the other side, hoping to profit from price moves. Both are needed for the market to work well."),
    ],
    "test": [
        ("What is a forward contract?",
         [("a", "A private deal to buy or sell at a set price on a future date"), ("b", "A bank account"), ("c", "A tax form"), ("d", "An option to sell at any time")], "a"),
        ("What is marking to market?",
         [("a", "Printing prices on shop signs"), ("b", "Setting prices once a year"), ("c", "Selling all holdings"), ("d", "Daily settlement of gains and losses through the margin account")], "d"),
        ("What is basis?",
         [("a", "The exchange's building"), ("b", "The margin deposit"), ("c", "The gap between the spot price and the futures price for the same asset"), ("d", "The name of the contract")], "c"),
        ("Which of these is a hedger?",
         [("a", "A trader hoping to profit from price moves only"), ("b", "A farmer using futures to reduce price risk"), ("c", "A bank teller"), ("d", "A tax office")], "b"),
        ("What do most futures traders do before delivery?",
         [("a", "Wait for delivery always"), ("b", "Give up the contract"), ("c", "Pay tax"), ("d", "Close their position before the delivery date")], "d"),
    ],
}
