"""Arbitrage (Manager, bar 3, part B): the same thing at two prices, why the gap closes, and why costs decide whether it pays."""
CODE = "business3b_arbitrage"
BOOK = {
    "title": "Arbitrage",
    "subtitle": "The same thing at two prices, and why the gap usually closes",
    "chapters": [
        ("The idea",
         "Arbitrage means buying something in one place and selling it at once in another place for more. It needs the same thing to sell for two different prices at the same moment. Traders who spot the gap earn a small profit from it."),
        ("Why gaps appear",
         "Gaps appear when information or access is slow. A price in one place may not yet match a price in another, or a rule may keep buyers in one market away from sellers in another. Real gaps are usually small and short-lived."),
        ("Why gaps close",
         "When traders buy in the cheap place and sell in the dear one, the cheap price rises and the dear price falls. The gap shrinks until it is gone. This is how arbitrage keeps prices in line across places."),
        ("Costs can eat the gap",
         "A gap is only a profit if it is bigger than the costs. Fees, transport, delays, and the risk that the price moves before you finish can use up the whole gap. Work out the net gain before you act."),
        ("One book per item",
         "The Starship market keeps one order book for each item, so there is no second book at a different price to trade against. The bank's standing quotes lean back toward a reference price, which keeps the book steady. The lesson still applies: compare what you pay with what you can really sell for."),
        ("Real markets",
         "In real markets, large firms run computers that spot and close tiny gaps in a fraction of a second. Most people never need to do this. For an ordinary person, the lesson is to count every cost before you believe a gap is a profit."),
    ],
    "test": [
        ("What is arbitrage?",
         [("a", "Buying a thing in one place and selling it at once in another place for more"), ("b", "Holding a thing for twenty years"), ("c", "Lending money at a fixed rate"), ("d", "Setting a floor price for an item")], "a"),
        ("What must be true for an arbitrage gap to exist?",
         [("a", "Two different things sell for the same price"), ("b", "The same thing sells for two different prices at the same moment"), ("c", "Prices never change"), ("d", "A single bank sets every price")], "b"),
        ("What usually happens to an arbitrage gap once traders act on it?",
         [("a", "It grows larger every day"), ("b", "It stays exactly the same"), ("c", "It shrinks and closes"), ("d", "It turns into a fixed fee")], "c"),
        ("A gap is 5 credits a unit, and fees and transport cost 6 credits a unit. What is the net result?",
         [("a", "A loss of 1 credit"), ("b", "A profit of 11 credits"), ("c", "A profit of 5 credits"), ("d", "No difference at all")], "a"),
        ("How many order books does each item have on the Starship market?",
         [("a", "Two, one for each bank desk"), ("b", "None"), ("c", "One"), ("d", "One for each player")], "c"),
    ],
}
