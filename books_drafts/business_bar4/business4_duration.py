"""Duration and Convexity: how sensitive a bond's price is to changing rates."""
CODE = "business4_duration"
BOOK = {
    "title": "Duration and Convexity",
    "subtitle": "How sensitive a bond's price is to changing rates",
    "chapters": [
        ("A measure of time",
         "Macaulay duration was introduced by the economist Frederick Macaulay in 1938. It is the average time until a bond's cash flows arrive, weighted by their present values. A bond that pays more of its value early has a shorter duration."),
        ("Duration as sensitivity",
         "Modified duration turns Macaulay duration into a rate sensitivity. A bond with a modified duration of 5 falls by about 5% in price for each one percentage point rise in its yield. Prices and yields move in opposite directions."),
        ("Longer bonds, more risk",
         "A zero-coupon bond has a duration equal to its maturity. Higher coupons shorten duration, because more of the value comes early. So a long bond with a low coupon is the most sensitive to rate moves among ordinary bonds."),
        ("The curve of price",
         "The relationship between price and yield is curved, not straight. Duration gives a straight-line estimate of the price change. That estimate is fairly accurate for small moves, but for large moves the real price change differs from it."),
        ("Convexity as a correction",
         "Convexity measures the bend in the price curve. With everything else equal, more convexity means a bond gains more when yields fall and loses less when yields rise. Duration plus convexity gives a better estimate of the price change."),
        ("Managing a bond ladder",
         "A bond ladder spreads holdings across several maturities, so that some bonds mature each year. This keeps the average duration steady and reduces the need to guess which way rates will move. It is a common way to manage interest-rate risk."),
    ],
    "test": [
        ("What does Macaulay duration measure?",
         [("a", "The weight of a bond"), ("b", "The bond's rating"), ("c", "The coupon amount"), ("d", "The average time until cash flows arrive, weighted by present value")], "d"),
        ("A bond has a modified duration of 5. If yields rise by one point, what roughly happens to its price?",
         [("a", "It rises 5%"), ("b", "It falls about 5%"), ("c", "It does not change"), ("d", "Its coupon rises by 5")], "b"),
        ("Which bond is most sensitive to rate moves?",
         [("a", "A short bond with a high coupon"), ("b", "A long bond with a high coupon"), ("c", "A long bond with a low coupon"), ("d", "A short bond with a low coupon")], "c"),
        ("What does convexity correct?",
         [("a", "The straight-line estimate of price change from duration"), ("b", "The bond's rating"), ("c", "The tax on coupons"), ("d", "The face value")], "a"),
        ("What is a bond ladder?",
         [("a", "One bond held for life"), ("b", "Holdings spread across several maturities, so some mature each year"), ("c", "A bond with no coupon"), ("d", "A loan to a friend")], "b"),
    ],
}
