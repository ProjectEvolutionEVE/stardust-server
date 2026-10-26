"""The Bank's Desks (Broker, bar 2): how the Starship bank's buy and sell desks keep the market moving (rule 21)."""
CODE = "business2_bankdesks"
BOOK = {
    "title": "The Bank's Desks",
    "subtitle": "How the Starship bank's two market desks keep prices moving",
    "chapters": [
        ("Two desks",
         "The Starship bank runs two market desks: a buy desk and a sell desk. They trade small lots all day, so a price is usually there to meet, even when players are quiet. The two desks trade with each other and with players."),
        ("The standing quotes",
         "The desks keep a standing bid 10% under the last price and a standing ask 10% over it. That is how a player can always sell at once and always buy at once. The quotes move as the last price moves."),
        ("Leaning back to a reference",
         "Each item has a reference price, and prices lean back toward it. If the last price drifts away, the desks' trading pulls it back a little at a time. The lean is gentle, so a price can still move a long way on real demand."),
        ("The floor holds",
         "The desks never trade below an item's floor. Their standing bid is never under the floor, so the floor is the least a price can fall to, whoever is trading. A floor is a promise the desks keep."),
        ("Credit behind the desks",
         "The two market desks have an unlimited credit line, so the market works from day one. This is separate from the Starship Bank's own account, which collects the printing fees. Keeping the two apart is part of how the bank stays solvent."),
        ("Market makers in the real world",
         "Real markets have market makers: firms that stand ready to buy and sell, so that others can always trade. They earn the spread for doing it, and they take the risk of holding goods. The desks do the same job on the Starship."),
    ],
    "test": [
        ("How many market desks does the Starship bank run?",
         [("a", "One"), ("b", "Three"), ("c", "Two"), ("d", "Five")], "c"),
        ("Where does the bank's standing bid sit, compared with the last price?",
         [("a", "10% under the last price"), ("b", "10% over the last price"), ("c", "Exactly equal to the last price"), ("d", "50% under the last price")], "a"),
        ("What does it mean that prices lean back toward a reference price?",
         [("a", "The bank sets every price"), ("b", "Prices never move"), ("c", "Prices double each day"), ("d", "Prices drift back a little at a time toward a reference price for each item")], "d"),
        ("Can the desks trade below an item's floor?",
         [("a", "Yes, at night"), ("b", "Only for gold"), ("c", "No, never"), ("d", "Only for ore")], "c"),
        ("What is a market maker in the real world?",
         [("a", "A shopkeeper who never holds goods"), ("b", "A bank that never trades"), ("c", "A government official who sets all prices"), ("d", "A firm that stands ready to buy and sell, so others can always trade")], "d"),
    ],
}
