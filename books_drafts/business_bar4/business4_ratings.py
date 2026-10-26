"""Credit Ratings: what a letter grade says about the chance of repayment."""
CODE = "business4_ratings"
BOOK = {
    "title": "Credit Ratings",
    "subtitle": "What a letter grade says about the chance of repayment",
    "chapters": [
        ("What a rating is",
         "A credit rating is an opinion on how likely a borrower is to repay its debt in full and on time. Agencies such as Standard and Poor's, Moody's and Fitch publish ratings for governments, companies and some kinds of securities."),
        ("The letter scales",
         "Standard and Poor's and Fitch use AAA at the top, then AA, A and BBB, and then speculative grades from BB downward. Moody's uses a similar scale that starts at Aaa. Ratings of BBB- or higher are called investment grade."),
        ("Default history",
         "Over long periods, higher-rated bonds have defaulted far less often than lower-rated ones. A rating describes typical outcomes, not a promise about any one borrower. Even highly rated borrowers can fail in rare cases."),
        ("The agencies and their conflicts",
         "In most models, the issuer pays the agency that rates it, which creates a conflict of interest. The 2008 financial crisis showed that some ratings on mortgage-linked securities were too generous. Regulators and investors now read agency views more critically."),
        ("Spreads over safe bonds",
         "The spread is the extra yield a risky bond pays above a safe benchmark, such as a government bond of a similar term. Wider spreads usually mean the market sees more risk. Spreads can widen quickly in a downturn, before any rating changes."),
        ("Reading a rating critically",
         "A rating is one input among many. Read the issuer's accounts, check recent changes in its rating, and ask what the rating does not cover, such as the ability to sell quickly or sudden shocks. Treat a rating as a starting point for questions."),
    ],
    "test": [
        ("What is a credit rating an opinion on?",
         [("a", "The colour of a bond"), ("b", "How likely a borrower is to repay in full and on time"), ("c", "The price of gold"), ("d", "The coupon")], "b"),
        ("What does investment grade mean?",
         [("a", "Rated BBB- or higher"), ("b", "Rated only in the top country"), ("c", "Cannot be sold"), ("d", "Paying no interest")], "a"),
        ("Why is there a conflict of interest in credit ratings?",
         [("a", "Agencies are paid by the issuers they rate"), ("b", "Agencies own all bonds"), ("c", "Agencies never publish"), ("d", "Governments set ratings")], "a"),
        ("What is a credit spread?",
         [("a", "A tax on losses"), ("b", "A type of coupon"), ("c", "The number of letters in a rating"), ("d", "The extra yield a risky bond pays above a safe benchmark")], "d"),
        ("What have higher-rated bonds shown over long periods?",
         [("a", "They defaulted more often"), ("b", "They defaulted far less often than lower-rated ones"), ("c", "They never defaulted"), ("d", "They always paid double")], "b"),
    ],
}
