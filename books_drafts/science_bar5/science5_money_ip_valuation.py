"""Valuing Intellectual Property: estimating what a patent or other research asset is worth, and how much risk and time reduce that value."""
CODE = "science5_money_ip_valuation"
BOOK = {
    "title": "Valuing Intellectual Property",
    "subtitle": "Valuation methods, comparable deals, royalty-based estimates, risk adjustment, patent life and valuation disclosure",
    "chapters": [
        ("Why value IP", "Intellectual property, such as a patent or a set of know-how, can be bought, sold, licensed or used as security. Before any of these, someone must estimate what it is worth. A careful estimate protects both the seller and the buyer."),
        ("Valuation methods", "A valuation method is a way of estimating what an asset is worth. Three common families are cost-based, market-based and income-based methods. Each answers a different question, so good practice uses more than one."),
        ("Comparable deals", "Comparable deals are past licensing or sale deals for similar technology. They give a benchmark, though no two deals are exactly alike. The comparison is only as good as the match between the technologies and the markets."),
        ("Royalty-based estimates", "A royalty-based estimate values an asset from the royalties it might earn over time. It projects sales, applies a royalty rate, and discounts the result to today. The rate and the sales forecast drive the answer."),
        ("Risk adjustment", "A patent may fail, be challenged or never earn much, so its value must be reduced for these chances. Risk adjustment lowers the estimate in line with how likely each outcome is. An honest estimate always includes its uncertainty."),
        ("Patent life and disclosure", "A patent has a legal term, so its value period is limited, even if the technology stays useful. Valuations should state their assumptions, methods and limits. Clear disclosure lets readers judge how far to trust the number."),
    ],
    "test": [
        ("What is a valuation method?",
         [("a", "A method of cooking"), ("b", "A way to paint walls"), ("c", "A way of measuring a sport"), ("d", "A way of estimating what an asset is worth")], "d"),
        ("What are comparable deals?",
         [("a", "Deals done on the same street"), ("b", "Pay deals with equal salaries"), ("c", "Past licensing or sale deals for similar technology, used as a benchmark"), ("d", "Deals with the same name")], "c"),
        ("What is a royalty-based estimate?",
         [("a", "An estimate of value based on the royalties the asset might earn over time"), ("b", "An estimate of the value of a crown"), ("c", "The price of a royal wedding"), ("d", "A bank interest rate")], "a"),
        ("Why adjust a valuation for risk?",
         [("a", "Because risk is always zero"), ("b", "Because a patent may fail or earn little, so its value must be reduced for those chances"), ("c", "Because risk always adds value"), ("d", "Because banks forbid it")], "b"),
        ("Why does patent life matter for valuation?",
         [("a", "A patent lasts forever"), ("b", "The legal term is limited, so the period of value is limited"), ("c", "Patents never expire"), ("d", "Patents last only one day")], "b"),
    ],
}
