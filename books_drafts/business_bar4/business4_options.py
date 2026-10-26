"""Options Explained: the right to buy or sell, for a price."""
CODE = "business4_options"
BOOK = {
    "title": "Options Explained",
    "subtitle": "The right to buy or sell, for a price",
    "chapters": [
        ("What an option is",
         "An option gives its buyer the right, but not the duty, to buy or sell an asset at an agreed price by a set date. The seller takes the other side, and must honour the deal if the buyer chooses to use it. An option is a contract."),
        ("Calls and puts",
         "A call option gives the right to buy. A put option gives the right to sell. Buyers of calls expect the price to rise, and buyers of puts expect it to fall. Each contract covers a set amount of the underlying asset."),
        ("Strike and expiry",
         "The strike price is the agreed price. The expiry is the last date on which the right can be used. After expiry, an unused option is worthless. The gap between the strike and the market price drives much of the value."),
        ("The payoff diagram",
         "At expiry, a call pays the market price minus the strike, if that is positive, and nothing otherwise. A put pays the strike minus the market price, if that is positive. Drawn as a graph, the payoff has a sharp bend at the strike."),
        ("Premium, intrinsic and time value",
         "The premium is the price paid for the option. Intrinsic value is the gain available if the option were used right now. Time value is the rest, reflecting the chance of a better move before expiry. The premium equals intrinsic value plus time value."),
        ("Why options exist",
         "Options let people protect against price moves, such as a farmer insuring a crop, or take a view with a limited loss. The buyer's loss is capped at the premium paid. Options are useful tools, but they are complex, so learn the basics first."),
    ],
    "test": [
        ("What does a call option give its buyer?",
         [("a", "The right to sell"), ("b", "The right to buy at the agreed price by a set date"), ("c", "A bank loan"), ("d", "Ownership of a company")], "b"),
        ("What is the strike price?",
         [("a", "The agreed price in the option"), ("b", "The tax rate"), ("c", "The number of shares"), ("d", "The date of expiry")], "a"),
        ("What does a put option give its buyer?",
         [("a", "The right to buy"), ("b", "The right to sell"), ("c", "Free shares"), ("d", "A fixed coupon")], "b"),
        ("What is the premium of an option?",
         [("a", "The price paid for the option"), ("b", "The strike price"), ("c", "The expiry date"), ("d", "The seller's profit only")], "a"),
        ("What is the most an option buyer can lose?",
         [("a", "The whole market value of the asset"), ("b", "Nothing, ever"), ("c", "The premium paid"), ("d", "The strike price")], "c"),
    ],
}
