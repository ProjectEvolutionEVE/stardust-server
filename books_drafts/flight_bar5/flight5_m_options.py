"""Options in Plain Words: calls and puts, the premium, the payoff, time value, common uses and the risks."""
CODE = "flight5_m_options"
BOOK = {
    "title": "Options in Plain Words",
    "subtitle": "Calls, puts, premiums and the risks in between",
    "chapters": [
        ("Calls",
         "A call option gives the holder the right to buy an asset at a set price, called the strike price, before a set date. The holder hopes the price will rise above the strike. If it does, the right has value."),
        ("Puts",
         "A put option gives the holder the right to sell an asset at the strike price before a set date. The holder hopes the price will fall below the strike. Puts are often used to protect a holding against a fall."),
        ("The premium",
         "The buyer pays the seller a premium for the option. This is the most the buyer can lose. The seller keeps the premium but may have to deliver the asset if the buyer chooses to use the option."),
        ("The payoff",
         "At expiry, a call pays out when the price is above the strike, and a put pays out when it is below. The payoff is the difference, less the premium paid. If the option is not worth using, it expires and the buyer loses only the premium."),
        ("Time value",
         "An option with time left has value beyond its immediate payoff, called time value. The longer until expiry, the more chance the price moves in the holder's favour. Time value fades as expiry gets close."),
        ("Uses and risks",
         "Options can protect, speculate or earn premium income. They are complex. Sellers can face large losses, and buyers can lose the whole premium. Learn the terms before trading them."),
    ],
    "test": [
        ("What does a call option give its holder?",
         [("a", "The right to sell at a set price"), ("b", "The right to buy at a set price before a set date"), ("c", "A monthly salary"), ("d", "A bank account")], "b"),
        ("What is the strike price?",
         [("a", "The price of a meal"), ("b", "The tax on a sale"), ("c", "The price of a pension"), ("d", "The price at which the option can be used")], "d"),
        ("What is the most a buyer of an option can lose?",
         [("a", "Everything they own"), ("b", "Nothing at all"), ("c", "The premium they paid"), ("d", "The strike price")], "c"),
        ("When does a put option pay out?",
         [("a", "When the price is below the strike"), ("b", "When the price is above the strike"), ("c", "When the price is exactly at the premium"), ("d", "Never")], "a"),
        ("Why does an option with more time left have more value?",
         [("a", "Because options are sold by the day"), ("b", "Because taxes fall with time"), ("c", "Because time value gives the holder more chance for the price to move favourably"), ("d", "Because the strike price drops")], "c"),
    ],
}
