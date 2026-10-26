"""Candlesticks (Broker, bar 2): the open, high, low and close of each period, shown as one shape."""
CODE = "business2_candles"
BOOK = {
    "title": "Candlesticks",
    "subtitle": "Open, high, low and close in one shape",
    "chapters": [
        ("One candle per period",
         "A candlestick chart packs four prices into one shape for each period: the open, the high, the low and the close. The open is the first price of the period, and the close is the last. The high and the low are the most and the least the price reached."),
        ("The body",
         "The thick part of a candle, its body, runs from the open to the close. A long body means the price moved a lot in that period. A short body means it ended close to where it began, even if it swung about in between."),
        ("The wicks",
         "The thin lines above and below the body are called wicks, or shadows. They reach out to the high and the low. A long wick shows that the price went further than where it closed, and then came back."),
        ("Colours",
         "Many charts colour a candle one way when it closed higher than it opened, and another way when it closed lower. Read the key on the chart before you rely on the colours. Colours are a choice the chart makes, not a rule of nature."),
        ("A short history",
         "Candlestick charts are often credited to rice traders in Japan in the 1700s, at the Dōjima rice market in Osaka. Western traders took up the method much later. The idea is simple: four prices, one shape, one period."),
        ("Read the shapes together",
         "A single candle says little on its own. A run of candles tells the story of several periods in a row. Read the shapes together with the volume and the time frame, not one candle alone."),
    ],
    "test": [
        ("What are the four prices a candle shows?",
         [("a", "Open, high, low, close"), ("b", "Bid, ask, floor, bank"), ("c", "Buy, sell, fee, total"), ("d", "Day, week, month, year")], "a"),
        ("What is the body of a candle?",
         [("a", "The high to the low"), ("b", "The open to the close"), ("c", "The fee paid"), ("d", "The volume")], "b"),
        ("What do the thin lines above and below a candle's body show?",
         [("a", "The volume"), ("b", "The floor"), ("c", "The names of traders"), ("d", "Where the price reached, its high and its low")], "d"),
        ("Where are candlestick charts often credited to first?",
         [("a", "Medieval wine guilds in Spain"), ("b", "Early tea merchants in London"), ("c", "Rice traders in Japan in the 1700s"), ("d", "The first banks of Venice")], "c"),
        ("Why read the key on a chart before relying on its colours?",
         [("a", "Colours are a choice the chart makes, not a law"), ("b", "Colours show the floor"), ("c", "Colours are fixed by the WSC"), ("d", "Colours show the volume")], "a"),
    ],
}
