"""Bookkeeping (10-20): credits, receipts and the ledger. Built on rules 2, 13, 21, 23 and store.py."""
CODE = "bookkeeping"
BOOK = {
    "title": "Bookkeeping",
    "subtitle": "Keeping track of your credits and your goods",
    "chapters": [
        ("Why keep books",
         "Bookkeeping is writing down every time money or goods come in or go out. It tells you where you stand, and "
         "it proves what happened. Merchants have done it for thousands of years."),
        ("Credits",
         "Credits are the Starship's money. They exist only inside the game: they never come from real money and never "
         "turn into money. Your wallet is at your Desk, with a history of every credit in and out."),
        ("Every credit has two sides",
         "Good books record each payment twice: where it left and where it arrived. The Starship's ledger works this "
         "way, so credits can never be created, lost or spent twice. Across every account, it always adds up."),
        ("Set-aside credits",
         "When you post a bid or bid at an auction, those credits are set aside. They're still yours, but you can't "
         "spend them twice. Cancelling an order, or being outbid, hands them back. Count them when you plan."),
        ("Receipts",
         "Every transfer of goods gives you a receipt with a code, like WSC-XXXX-XXXX. Your receipts log is in your "
         "filing cabinet, and you can save a copy to your own device. Anyone can check a code against the server, "
         "which never shows who owns it."),
        ("The three organizations",
         "Some credits go to the ship's organizations, each with its own account. The WSC collects the 2.5% auction "
         "fee. The Bank treasury collects blueprint printing fees: 100 credits once for a design's first run, plus 10 "
         "per copy. The Auction House has its own account but no fees of its own yet."),
        ("Know your cost",
         "Add up what something cost you before you sell it. Example: printing 25 copies on a first run costs 350 "
         "credits, which is 14 a copy. Sell above that and you made a profit."),
    ],
    "test": [
        ("Can credits be turned into real money?",
         [("a", "Yes"), ("b", "No, never"), ("c", "Only by the bank"), ("d", "Only after a year")], "b"),
        ("Where is your receipts log kept?",
         [("a", "In the filing cabinet"), ("b", "Under the bed"), ("c", "In the closet"), ("d", "On the market board")], "a"),
        ("What happens to set-aside credits when you're outbid?",
         [("a", "They are lost"), ("b", "They go to the WSC"), ("c", "They are handed back"), ("d", "They stay locked forever")], "c"),
        ("Who collects blueprint printing fees?",
         [("a", "The WSC"), ("b", "The Bank treasury"), ("c", "The Auction House"), ("d", "The designer")], "b"),
        ("A first run of 25 copies costs 350 credits. What is the cost per copy?",
         [("a", "10"), ("b", "14"), ("c", "25"), ("d", "35")], "b"),
    ],
}
