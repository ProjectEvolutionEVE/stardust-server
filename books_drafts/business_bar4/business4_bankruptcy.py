"""Bankruptcy and restructuring: insolvency, liquidation against reorganisation, Chapter 11, the order of creditors, turnaround and Altman's Z-score."""
CODE = "business4_bankruptcy"
BOOK = {
    "title": "Bankruptcy and Restructuring",
    "subtitle": "Insolvency, reorganisation, the order of creditors and an early warning score",
    "chapters": [
        ("Insolvency",
         "A firm is insolvent when it cannot pay its debts as they fall due, or when its debts are larger than its assets. Insolvency is a legal and financial state, and it can lead to formal bankruptcy proceedings."),
        ("Liquidation or reorganisation",
         "In liquidation, a firm's assets are sold and the money is shared among creditors, and the firm closes. In reorganisation, the firm keeps running while its debts and operations are restructured under a plan."),
        ("Chapter 11",
         "In the United States, Chapter 11 is a common route for reorganising a business while it continues to trade. Creditors and the firm negotiate a plan, which must be approved by a court."),
        ("The order of creditors",
         "In most bankruptcies, secured creditors are paid first from the assets pledged to them. Then come other creditors in a set order, and shareholders are usually last. The order matters a great deal for who gets paid."),
        ("Turnaround",
         "A turnaround plan may cut costs, sell parts of the business, renegotiate debts or find new funding. The plan works best when it is started early, while the firm still has options."),
        ("Altman's Z-score",
         "Edward Altman's Z-score combines several financial ratios into one number. A low score has been linked with a higher chance of bankruptcy. It is a useful warning sign, though it is not a sure prediction."),
    ],
    "test": [
        ("When is a firm insolvent?",
         [("a", "When it cannot pay its debts as they fall due"), ("b", "When it has a new logo"), ("c", "When it wins an award"), ("d", "When it moves office")], "a"),
        ("What happens in liquidation?",
         [("a", "The firm doubles its size"), ("b", "The assets are sold and the money shared among creditors"), ("c", "Every creditor is paid in full"), ("d", "The firm moves abroad for free")], "b"),
        ("What is Chapter 11?",
         [("a", "A chapter of a school book"), ("b", "A type of share"), ("c", "A route for reorganising a business while it keeps trading, in the United States"), ("d", "A tax form for holidays")], "c"),
        ("Who is usually paid last in a bankruptcy?",
         [("a", "Secured creditors"), ("b", "Employees owed wages"), ("c", "Tax authorities"), ("d", "Shareholders")], "d"),
        ("What is Altman's Z-score?",
         [("a", "A score combining several ratios that can warn of bankruptcy"), ("b", "A score for football matches"), ("c", "A measure of paint colour"), ("d", "A grade in a school test")], "a"),
    ],
}
