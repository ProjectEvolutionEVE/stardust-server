"""The Yield Curve: what short and long interest rates say about the future."""
CODE = "business4_yieldcurve"
BOOK = {
    "title": "The Yield Curve",
    "subtitle": "What short and long interest rates say about the future",
    "chapters": [
        ("Rates for different times",
         "Lenders charge different rates depending on how long their money is tied up. Plot those rates against the time to maturity and you get the yield curve. Government bonds are the usual reference, because they carry little default risk."),
        ("The normal shape",
         "In most periods the curve slopes upward, so longer loans pay more. Investors want extra reward for locking money up longer, and for the uncertainty of future inflation. A normal curve is often seen as a sign of a growing economy."),
        ("Inversion",
         "Sometimes short rates rise above long rates. The curve is then inverted. Several recessions in the United States, including those of the early 1980s and 2001, followed periods of inversion. Some inversions were not followed by a recession soon after, so the signal is imperfect."),
        ("The term premium",
         "The term premium is the extra return investors want for holding longer bonds. It changes over time and is hard to measure directly. A flat or inverted curve can therefore reflect expected rate cuts, or a strong demand for safe long bonds."),
        ("What the curve signals",
         "The curve reflects expectations of future short rates, plus the term premium. Economists, central banks and investors all watch its shape. Because it reflects many views at once, it is a useful summary but never a guarantee."),
        ("Real-world history",
         "Curve shapes have changed many times across decades, in several countries. Each episode has its own causes, such as central bank policy, inflation surprises or a rush for safe assets. Read the curve as one clue among many, not as a timetable."),
    ],
    "test": [
        ("What is the yield curve?",
         [("a", "A bank's profit line"), ("b", "A rule for taxes"), ("c", "A chart of rates against time to maturity"), ("d", "A map of coins")], "c"),
        ("What is the usual normal shape of the curve?",
         [("a", "Slopes upward"), ("b", "Slopes downward always"), ("c", "Stays flat forever"), ("d", "Forms a circle")], "a"),
        ("What is an inverted yield curve?",
         [("a", "Long rates rise above short rates"), ("b", "Short rates rise above long rates"), ("c", "Rates do not change"), ("d", "Rates are removed from the curve")], "b"),
        ("What is the term premium?",
         [("a", "A tax on interest"), ("b", "The fee for buying a bond"), ("c", "The face value of a bond"), ("d", "The extra return investors want for holding longer bonds")], "d"),
        ("What does the curve reflect?",
         [("a", "A single guaranteed forecast"), ("b", "Expectations of future short rates plus the term premium"), ("c", "Only the price of gold"), ("d", "The rate of a single bank")], "b"),
    ],
}
