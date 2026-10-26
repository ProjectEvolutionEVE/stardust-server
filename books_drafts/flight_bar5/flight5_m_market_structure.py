"""How Markets Work: supply and demand, equilibrium, elasticity, price floors, shocks and worked examples."""
CODE = "flight5_m_market_structure"
BOOK = {
    "title": "How Markets Work",
    "subtitle": "Supply, demand, and the price where they meet",
    "chapters": [
        ("Supply and demand",
         "Demand is how much buyers want at each price. Supply is how much sellers offer at each price. When prices are higher, buyers want less and sellers offer more. The two forces push the price toward a level where they meet."),
        ("Equilibrium",
         "Equilibrium is the price where the amount buyers want equals the amount sellers offer. At this point the market clears, and there is no pressure for the price to move. Real markets are rarely still, but they are always pulled toward it."),
        ("Elasticity",
         "Elasticity measures how much buyers or sellers change their amounts when the price changes. Bread is often inelastic, since people buy it anyway. Luxury goods are often more elastic, since buyers can wait or do without."),
        ("Price floors",
         "A price floor is a minimum price set above the equilibrium. It keeps prices from falling below that level. The result is often a surplus, because sellers offer more than buyers want at the higher price."),
        ("Shocks",
         "A shock is a sudden change, such as a poor harvest, a new invention or a war. It shifts supply or demand, and the price moves to a new equilibrium. The move can be sharp when supply is slow to respond."),
        ("Worked example",
         "Imagine fewer ships can carry ore in a year. Supply falls, the price rises, and buyers cut their orders a little. Over time new ships are built and the price drifts back down."),
    ],
    "test": [
        ("What is equilibrium in a market?",
         [("a", "The price where buyers want what sellers offer"), ("b", "The highest price ever paid"), ("c", "A tax on sales"), ("d", "A fixed rule set by the state")], "a"),
        ("What does elasticity measure?",
         [("a", "How tall a product is"), ("b", "The age of a company"), ("c", "How much buyers or sellers change their amounts when the price changes"), ("d", "How long a contract lasts")], "c"),
        ("What is a price floor?",
         [("a", "A limit on how high a price can go"), ("b", "A minimum price set above the equilibrium"), ("c", "A rule that prices always fall"), ("d", "A type of tax")], "b"),
        ("A minimum price above equilibrium often leads to what?",
         [("a", "A shortage of goods"), ("b", "No change at all"), ("c", "A falling supply"), ("d", "A surplus, as sellers offer more than buyers want")], "d"),
        ("Which is an example of a supply shock?",
         [("a", "A small change in shop opening times"), ("b", "A lower price for an old product"), ("c", "A poor harvest that cuts the amount of a crop"), ("d", "A new bank account")], "c"),
    ],
}
