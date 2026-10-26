"""Cash Flow (Broker, bar 2): why a profitable trader can still run out of spendable credits."""
CODE = "business2_cashflow"
BOOK = {
    "title": "Cash Flow",
    "subtitle": "Why a profitable trader can still run out of credits",
    "chapters": [
        ("Profit is not cash",
         "Profit is what is left after the costs of a sale are taken away. Cash is the money you can spend today. A trader can show a profit on paper and still be short of cash, because the money from the sale has not arrived yet."),
        ("Timing",
         "Cash flow is the timing of money coming in and going out. Costs often come before the money from a sale, and cash flow tracks that gap. A business that runs out of cash between one payment and the next can fail, even when its sales are good."),
        ("The printing gap",
         "A print run has to be paid for before its copies can be sold, because the copies come from the run. So the printing cost goes out first, and the auction money comes later. Plan for that gap before you order a run."),
        ("Plan the reserve by date",
         "A reserve is credits kept free for bills that come due, and for a chance you do not want to miss. Plan the reserve around the dates money goes out, not only around your total. A large total can still leave you short on the day a payment is due."),
        ("A cash forecast",
         "A simple cash forecast lists the money you expect to come in and go out, in order of date, for the next few days. Update it after each trade or auction. It does not need to be exact. It needs to show the gap before the gap arrives."),
        ("Real-world cash flow",
         "Shops, farms and ships have all run short of cash while holding goods they could not yet sell. Many businesses that fail had sales, but ran short of cash at the wrong moment. Watching the timing is one of the oldest jobs of a merchant."),
    ],
    "test": [
        ("What is the difference between profit and cash?",
         [("a", "They are the same"), ("b", "Cash is always more than profit"), ("c", "Profit is what is left after costs; cash is what you can spend now"), ("d", "Profit is always in your wallet")], "c"),
        ("What does cash flow track?",
         [("a", "The timing of money coming in and going out"), ("b", "The size of the floor"), ("c", "The height of a chart"), ("d", "The number of players")], "a"),
        ("Why can a business with good sales still run short?",
         [("a", "Its sales are never paid"), ("b", "Fees are paid to the bank twice"), ("c", "Floors rise every day"), ("d", "Its costs often come before the money from sales arrives")], "d"),
        ("What is a cash forecast?",
         [("a", "A guess at the floor"), ("b", "A list of expected money in and out, by date"), ("c", "A receipt for each trade"), ("d", "A record of who bought what")], "b"),
        ("Why plan a reserve around dates, not only totals?",
         [("a", "Reserves expire"), ("b", "The bank asks for dates"), ("c", "Money goes out on certain days, so a healthy total can hide a short day"), ("d", "Totals are never correct")], "c"),
    ],
}
