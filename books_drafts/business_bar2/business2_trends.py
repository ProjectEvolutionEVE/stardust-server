"""Trends and Reversals (Broker, bar 2): which way a price is heading, and the signs that it may turn."""
CODE = "business2_trends"
BOOK = {
    "title": "Trends and Reversals",
    "subtitle": "Which way a price is heading, and when it may turn",
    "chapters": [
        ("What a trend is",
         "A trend is the general direction a price keeps moving in. An uptrend makes higher highs and higher lows. A downtrend makes lower highs and lower lows. Sideways means the price moves about without a clear direction."),
        ("Count the swings",
         "To see a trend, look at several swings, not one jump. Note the peaks and the dips in order. If each peak is higher than the last, and each dip is higher than the last, the uptrend is holding."),
        ("Trade with the direction",
         "Many traders say the trend is your friend, meaning it is usually harder to trade against the direction than with it. A trend can still end at any time, so set your price before you act."),
        ("Signs of a turn",
         "A reversal is when a trend changes direction. Traders watch for a rising price that stops making new highs, a sharp move that fails to hold, or volume that falls as the price climbs. None of these is proof on its own."),
        ("False signals",
         "Not every turn is a real reversal. A price can dip, look as if it has turned, and then carry on in the same direction. Traders call this a false signal, and it catches out the eager often enough to be worth knowing."),
        ("Trends beyond the market",
         "Trends happen outside any market too. A crop may grow dearer for years, or a trade route may grow and then fade. Economists read such trends in data over long periods, and a trader should look at the longer picture as well."),
    ],
    "test": [
        ("What does an uptrend look like?",
         [("a", "Lower highs and lower lows"), ("b", "Random jumps"), ("c", "Higher highs and higher lows"), ("d", "Flat tops and bottoms")], "c"),
        ("What does sideways mean for a price?",
         [("a", "The price falls steadily"), ("b", "The price rises steadily"), ("c", "The market is closed"), ("d", "Neither a clear rise nor a clear fall")], "d"),
        ("What is a reversal?",
         [("a", "A cancelled trade"), ("b", "A receipt sent back to the bank"), ("c", "A copy returned to its designer"), ("d", "A trend that changes direction")], "d"),
        ("What is a false signal?",
         [("a", "A sign of a turn that does not last"), ("b", "A message from another player"), ("c", "A missing receipt"), ("d", "A wrong fee")], "a"),
        ("Why set your price before you act on a trend?",
         [("a", "Trends never end"), ("b", "The bank sets trend prices"), ("c", "Trends can end at any time, and a set price keeps you from acting in a panic"), ("d", "Trends are paid by the WSC")], "c"),
    ],
}
