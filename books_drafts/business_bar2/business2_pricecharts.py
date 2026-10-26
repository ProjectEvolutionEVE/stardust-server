"""Reading a Price Chart (Broker, bar 2): what a price line shows over time, and what it cannot show."""
CODE = "business2_pricecharts"
BOOK = {
    "title": "Reading a Price Chart",
    "subtitle": "What a price line shows, and what it cannot show",
    "chapters": [
        ("What a price chart shows",
         "A price chart plots a price over time. Each point is a trade, or the last price in a period. Read it from left to right: the left is the past, and the right is now. The chart answers one question at a time: how did the price move?"),
        ("The last price",
         "The line in a simple chart joins the last trade prices. It tells you what the most recent trade cost. It does not show how many were traded in each period, and it does not show who was on either side."),
        ("Time frames",
         "The same price can look calm or wild depending on the time frame. A chart of one hour and a chart of one month tell different stories. Look at more than one time frame before you decide anything."),
        ("Scales",
         "Check the scale on the side of the chart. A scale that starts at 150 instead of zero makes small moves look huge. The chart is not lying, but the eye can be fooled, so read the numbers as well as the shape."),
        ("Quiet stretches",
         "The market is open 24 hours a day, so a chart has no closing bell. A long flat stretch means few or no trades at that price during that time. Check the volume before you read a flat line as a fixed price."),
        ("A chart is a record, not a promise",
         "A chart shows what has already happened. Past prices may suggest a pattern, but they never promise one. Use a chart to understand the market, not to predict it with certainty."),
    ],
    "test": [
        ("On a price chart, which side shows the most recent prices?",
         [("a", "The top"), ("b", "The left"), ("c", "The right"), ("d", "The middle")], "c"),
        ("What does each point on a simple price line usually show?",
         [("a", "The name of the seller"), ("b", "The last trade price in a period"), ("c", "Only the volume"), ("d", "The floor price")], "b"),
        ("Why check the scale on the side of a chart?",
         [("a", "A scale that starts above zero can make small moves look huge"), ("b", "Scales are always wrong"), ("c", "The scale sets the floor"), ("d", "The scale shows the fee")], "a"),
        ("The market never closes. What does a long flat stretch on a chart often mean?",
         [("a", "The market closed for the night"), ("b", "Very few trades at that price"), ("c", "The floor rose"), ("d", "The bank went offline")], "b"),
        ("What can a price chart not do?",
         [("a", "Show what has already happened"), ("b", "Show past trades"), ("c", "Promise what will happen next"), ("d", "Show different time frames")], "c"),
    ],
}
