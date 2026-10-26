"""The DuPont analysis: return on equity broken into margin, turnover and leverage, how to compare firms and how to find the real driver."""
CODE = "business4_dupont"
BOOK = {
    "title": "The DuPont Analysis",
    "subtitle": "Breaking return on equity into margin, turnover and leverage",
    "chapters": [
        ("Return on equity",
         "Return on equity, or ROE, measures how much profit a firm earns for each unit of shareholders' equity. It is a common measure of how well owners' money is used. A high number is not always a good sign on its own."),
        ("Three parts",
         "The DuPont analysis splits ROE into three parts: net profit margin, asset turnover and equity multiplier. Multiplied together, the three give ROE. Each part tells a different story about the firm."),
        ("Margin",
         "The profit margin is the share of each unit of sales that remains as profit. A firm with high margins keeps more of what it sells. This often reflects strong pricing or low costs."),
        ("Turnover",
         "Asset turnover shows how much sales a firm earns from each unit of assets. A business with high turnover uses its assets hard. Shops and airlines often run on high turnover and thin margins."),
        ("Leverage",
         "The equity multiplier shows how much of the firm's assets are funded by debt, compared with equity. Borrowing can raise ROE, but it also raises risk. A high ROE built on heavy debt can fall sharply in a downturn."),
        ("Finding the driver",
         "Compare the three parts across firms or across years. The analysis shows whether a change in ROE came from margin, from turnover or from debt. Knowing the driver helps you judge whether the result will last."),
    ],
    "test": [
        ("What does return on equity measure?",
         [("a", "The number of staff"), ("b", "The age of a building"), ("c", "The colour of the logo"), ("d", "Profit earned for each unit of shareholders' equity")], "d"),
        ("How many main parts does the DuPont analysis split ROE into?",
         [("a", "Three"), ("b", "One"), ("c", "Seven"), ("d", "Twelve")], "a"),
        ("What does asset turnover show?",
         [("a", "How often the logo is changed"), ("b", "How much sales a firm earns from each unit of assets"), ("c", "How many shares a firm owns"), ("d", "The temperature of the office")], "b"),
        ("What does leverage add to the picture?",
         [("a", "The number of windows"), ("b", "The price of stamps"), ("c", "How much of the firm is funded by debt, which raises risk"), ("d", "The weather forecast")], "c"),
        ("Why is high ROE built on heavy debt a warning sign?",
         [("a", "It always means the firm will never fail"), ("b", "It means the firm has no sales"), ("c", "It makes the firm pay no tax"), ("d", "It can fall sharply in a downturn")], "d"),
    ],
}
