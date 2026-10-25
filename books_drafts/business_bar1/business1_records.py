"""Keeping Good Records (Trader, bar 1): receipts, profit and a simple trade log. Builds on the Bookkeeping book, not a repeat of it."""
CODE = "business1_records"
BOOK = {
    "title": "Keeping Good Records",
    "subtitle": "Receipts, profit and a simple trade log",
    "chapters": [
        ("Why records matter",
         "A trader who keeps good records knows what they paid, what they sold for, and what is still on the table. Without records, a lucky trade and a good trade look the same. Merchants have kept records for thousands of years for exactly this reason."),
        ("Receipts",
         "Every transfer of goods gives you a receipt with a code that anyone can check. Your receipts log lives in the filing cabinet in your Private Quarters. Keep it. It is the proof of what happened, and it is the first thing to check when a number looks wrong."),
        ("Credits exist only in the game",
         "Credits come from play, and they exist only inside the game. They never come from real money and never turn into real money. So your trade log records game credits only, and it is a record of the game, not of your savings."),
        ("Cost and profit",
         "Write down each buy: the item, the number of lots, the price and the date. When you sell, your profit is what you received minus what you paid, less any fees. For example, if you buy one silver ore lot for 300 credits and sell it for 340, you made 40 credits before fees."),
        ("A simple trade log",
         "Keep a log with one line for each trade: the date, the item, the lots, the price, the total and any fee. Check the log against your receipts from time to time. If the two do not match, find out why before you trust either one."),
        ("Good records, good decisions",
         "When you know your numbers, you can tell whether an item is worth holding or selling, and you can plan your next order. Good records let you tell a good trade from a lucky one, and that is how a trader gets better over time."),
    ],
    "test": [
        ("Where does your receipts log live?",
         [("a", "In the cargo hold"), ("b", "On the market board"), ("c", "In the filing cabinet"), ("d", "At the bank counter")], "c"),
        ("Can game credits be turned into real money?",
         [("a", "No: credits never turn into real money"), ("b", "Yes, at the bank"), ("c", "Yes, after a big trade"), ("d", "Only at the auction house")], "a"),
        ("What does every receipt carry?",
         [("a", "Only the price"), ("b", "Only the name of the seller"), ("c", "Nothing that can be checked"), ("d", "A code that anyone can check")], "d"),
        ("What is profit on a sale?",
         [("a", "The price you paid"), ("b", "What you received minus what you paid, less any fees"), ("c", "The total of all your credits"), ("d", "The floor price of the item")], "b"),
        ("Why check your trade log against your receipts?",
         [("a", "To make the log look longer"), ("b", "To make old receipts expire"), ("c", "So that a mistake in either one shows up"), ("d", "Receipts never need checking")], "c"),
    ],
}
