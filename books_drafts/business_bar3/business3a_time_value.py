"""Money Today and Money Later (Manager, bar 3, part A): why a credit now is worth more than a credit later, and how to compare them."""
CODE = "business3a_time_value"
BOOK = {
    "title": "Money Today and Money Later",
    "subtitle": "Why a credit now is worth more than a credit later, and how to compare them",
    "chapters": [
        ("A credit now is worth more",
         "A credit you have today can be used, saved or put to work. A credit promised for later cannot be used yet, and it may never arrive. That is why money now is worth more than the same money later."),
        ("Discounting",
         "Discounting works the idea backwards. It asks what a future sum is worth today, using a rate that reflects what the money could earn in the meantime. That rate is called the discount rate."),
        ("A worked example",
         "At a discount rate of 10% a year, 110 credits received one year from now is worth 100 credits today. Check it: 110 divided by 1.10 is 100, and 100 credits put aside at 10% would grow to 110 in a year."),
        ("Net present value",
         "Net present value, or NPV, adds up the future money from a purchase, discounts each part back to today, and subtracts the cost paid now. A positive NPV means the purchase earns more than the discount rate. A negative NPV means it does not."),
        ("Why it beats a simple count",
         "NPV counts every period, and it counts later money for less than earlier money. A simple payback count cannot do that. So NPV answers a sharper question: is this purchase worth more than leaving the same money to earn at the discount rate?"),
        ("Choosing the rate",
         "The discount rate should be what the same money could earn with similar risk, such as a savings rate or a loan rate. A riskier purchase needs a higher rate, because its future money is less certain."),
    ],
    "test": [
        ("Why is a credit today usually worth more than the same credit later?",
         [("a", "Because later credits are always bigger"), ("b", "Because a credit today can be used or put to work, and a promise may not arrive"), ("c", "Because the Bank prints extra credits later"), ("d", "Because prices always fall")], "b"),
        ("At a 10% a year discount rate, what is 110 credits received in one year worth today?",
         [("a", "121 credits"), ("b", "110 credits"), ("c", "11 credits"), ("d", "100 credits")], "d"),
        ("What does a positive NPV mean?",
         [("a", "The purchase earns more than the discount rate"), ("b", "The purchase is paid for with a loan"), ("c", "The payback is zero"), ("d", "The discount rate is zero")], "a"),
        ("Which rate should you use to discount future money?",
         [("a", "The highest rate the market ever reached"), ("b", "The rate the Bank quotes on loans only"), ("c", "A rate reflecting what the same money could earn with similar risk"), ("d", "Zero, so that all money counts the same")], "c"),
        ("Why should a riskier purchase use a higher discount rate?",
         [("a", "Because risk makes money larger"), ("b", "Because its future money is less certain"), ("c", "Because the Bank asks for it"), ("d", "Because it returns the money sooner")], "b"),
    ],
}
