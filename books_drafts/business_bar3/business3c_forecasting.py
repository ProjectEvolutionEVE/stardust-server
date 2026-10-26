"""Forecasting the Next Season (Business, bar 3, part C): averages, trends and ranges, and how sure you can be."""
CODE = "business3c_forecasting"
BOOK = {
    "title": "Forecasting the Next Season",
    "subtitle": "Averages, trends and ranges: estimating what comes next, and how sure you can be",
    "chapters": [
        ("A forecast is a method",
         "A forecast estimates what will happen next. A good forecast uses past numbers and says how far it could be wrong. No forecast is certain, so the aim is a sensible estimate you can act on."),
        ("The average",
         "A simple forecast is the average of recent weeks. Add up the last four weeks of sales and divide by four. The average smooths out one unusually good or bad week, so it shows the usual level more clearly."),
        ("Trends",
         "If sales rise by about the same amount each week, that is a trend. A trend helps you see where the numbers may go next, but a trend can turn, so check it again every week."),
        ("Seasons",
         "Some items sell more at certain times of the year. Compare the same weeks from the last season, not only the last few weeks, so that a seasonal rise is not mistaken for growth."),
        ("Ranges, not single numbers",
         "Give your forecast as a range, such as between 40 and 60 units. A range shows the risk, and it helps you keep enough stock and cash for a low week as well as a high one."),
        ("Update and compare",
         "Compare each forecast with what really happened, then adjust your method. Forecasts that are checked against results get better over time, and the misses teach you the most."),
    ],
    "test": [
        ("Sales for the last four weeks were 40, 44, 48 and 52. What is their average?",
         [("a", "46"), ("b", "44"), ("c", "48"), ("d", "184")], "a"),
        ("What is a forecast?",
         [("a", "A certain prediction"), ("b", "A promise from the Bank"), ("c", "An estimate of what will happen next, with a sense of how far it could be wrong"), ("d", "The price of an item on one given day")], "c"),
        ("What is a trend?",
         [("a", "A single week's record"), ("b", "A fee paid to the WSC"), ("c", "A rule set by the Bank"), ("d", "A steady direction over time in the numbers, such as sales rising by about the same amount each week")], "d"),
        ("Why compare the same weeks from past seasons?",
         [("a", "Because the last few weeks never matter"), ("b", "Because some items sell more at certain times of the year"), ("c", "Because prices are fixed each season"), ("d", "Because forecasts must come in pairs")], "b"),
        ("Why give a forecast as a range?",
         [("a", "Because single numbers are illegal"), ("b", "Because ranges are easier to spend"), ("c", "Because it shows the risk, so you can keep enough stock and cash for a low week"), ("d", "Because the market only accepts ranges")], "c"),
    ],
}
