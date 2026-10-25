"""Risk and Patience (Trader, bar 1): real trading basics, tied to the Starship market."""
CODE = "business1_risk"
BOOK = {
    "title": "Risk and Patience",
    "subtitle": "Spreading your credits, keeping calm, and waiting for your price",
    "chapters": [
        ("What risk means",
         "Risk is the chance that a trade goes against you. Prices can fall after you buy and rise after you sell. Every market has risk. A good trader plans for it instead of hoping it will not happen."),
        ("Do not put everything in one item",
         "The market lists more than one item, so you can spread your credits across them. If one price goes the wrong way, the others may not, and one bad trade will not sink your whole account."),
        ("Do not panic-sell",
         "When a price drops fast, it is tempting to sell at once just to stop the feeling. Selling in a panic often means selling at the lowest point. The market leans prices back toward a reference price, so a sudden drop is not always the end."),
        ("Buy low and sell high is harder than it sounds",
         "Everyone wants to buy low and sell high. But no one rings a bell at the bottom. You can usually tell a price was low or high only when you look back. Decide your price before you place the order, and stick to it."),
        ("Patience with limit orders",
         "A limit order lets you wait for your price instead of taking whatever is on the board. Your credits stay set aside until the order fills or you cancel it. Patience can cost you a trade too, so set a time to review your orders."),
        ("Keep some credits in reserve",
         "Keep part of your credits free. A reserve lets you take a good chance when it comes, and it pays the printing and auction fees that come due. Do not spend every credit you have on one trade."),
    ],
    "test": [
        ("What is the main reason not to put all your credits in one item?",
         [("a", "It is against the rules"), ("b", "The bank only trades two items"), ("c", "One bad price could cost you a lot"), ("d", "It makes orders slower")], "c"),
        ("What is a common mistake when prices fall fast?",
         [("a", "Waiting for a limit order to fill"), ("b", "Selling in a panic at the lowest point"), ("c", "Checking your trade log"), ("d", "Reading the order book")], "b"),
        ("Why is buy low and sell high harder than it sounds?",
         [("a", "You can usually tell a low or high price only when looking back"), ("b", "Prices never move"), ("c", "Sellers are named on the board"), ("d", "Floor prices are always high")], "a"),
        ("What does a limit order let you do?",
         [("a", "Buy at any price instantly"), ("b", "Wait for your chosen price instead of taking whatever is on the board"), ("c", "Skip all fees"), ("d", "Trade without setting credits aside")], "b"),
        ("Why keep some credits in reserve?",
         [("a", "So you can sell at a loss"), ("b", "So you can take a good chance later or pay fees that come due"), ("c", "Because the bank requires it"), ("d", "Because credits expire")], "b"),
    ],
}
