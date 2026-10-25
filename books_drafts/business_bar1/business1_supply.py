"""Supply and Demand (Trader, bar 1): how prices move on the Starship market, and the real-world basics behind them."""
CODE = "business1_supply"
BOOK = {
    "title": "Supply and Demand",
    "subtitle": "How prices move, and why the market sets them",
    "chapters": [
        ("What sets a price",
         "A price is what a buyer will pay and a seller will accept for one lot. When more people want an item than there is for sale, the price tends to rise. When there is more for sale than people want, the price tends to fall. Merchants have watched this happen for thousands of years."),
        ("Supply",
         "Supply is how much of a good sellers are willing to offer at a given price. In the game, supply is the ore that players bring in from the debris fields and put up for sale. More miners bring more ore to market, and the price has more to answer to."),
        ("Demand",
         "Demand is how much buyers want at a given price. A player who needs iron ore for a build will bid for it. When many buyers want the same item at once, their bids climb. Prices move because what people want moves, not because someone decides."),
        ("Prices on the Starship",
         "The Starship market sets the price. Every item starts from a set price, and every item has a floor. Nothing trades below its floor. Each trade sets the price for the next one, so the price changes as players buy and sell. The Starship bank trades on this market too."),
        ("Prices lean back",
         "The bank keeps a standing bid 10% under and a standing ask 10% over the last price, so you can always sell and always buy. Prices also lean back toward a reference price for each item. A sudden rush of buyers or sellers can move a price, but the market gives it a pull back toward normal."),
        ("The same idea everywhere",
         "In the real world, a price drops when a market fills with goods, and it rises when a shortage bites. Economists call the two sides supply and demand. The same idea works in a farm market, on a trading floor, or on a space station."),
    ],
    "test": [
        ("What tends to happen to a price when more people want an item than there is for sale?",
         [("a", "It tends to fall"), ("b", "It tends to rise"), ("c", "It stays fixed forever"), ("d", "It is banned")], "b"),
        ("What is supply?",
         [("a", "How much buyers want at a price"), ("b", "How much of a good sellers offer at a price"), ("c", "The number of players in the market"), ("d", "The floor price")], "b"),
        ("What is a floor price on the Starship market?",
         [("a", "The lowest price any trade can happen at"), ("b", "The highest price anyone can bid"), ("c", "The price of the Starship"), ("d", "The fee the bank keeps")], "a"),
        ("What does the Starship bank keep on the market as standing offers?",
         [("a", "A bid 50% over and an ask 50% under the last price"), ("b", "Only sell orders at the start price"), ("c", "Nothing, the bank never trades"), ("d", "A bid 10% under and an ask 10% over the last price")], "d"),
        ("Which real-world idea explains how prices move?",
         [("a", "Gravity"), ("b", "Supply and demand"), ("c", "Photosynthesis"), ("d", "The speed of light")], "b"),
    ],
}
