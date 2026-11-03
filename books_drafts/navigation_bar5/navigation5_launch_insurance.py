"""Pricing Launch Insurance: launch risk, premiums, the payout, the prior record, exclusions and the structure of cover."""
CODE = "navigation5_launch_insurance"
BOOK = {
    "title": "Pricing Launch Insurance",
    "subtitle": "How cover for a satellite launch is priced",
    "chapters": [
        ("Launch risk",
         "A launch can fail, damaging or losing the satellite. Insurers judge the risk of a launch before they offer cover. Risk is the core of the pricing."),
        ("Premiums",
         "The premium is the price paid for the cover. It depends on the risk, the value insured and the market. Premiums are set to cover expected losses, plus costs and a margin."),
        ("The payout",
         "The payout is the amount the insurer pays after a covered loss. Payouts are set out in the policy. A payout can be full or partial."),
        ("The prior record",
         "Past launches with the same rocket and team are a guide to risk. A strong record usually lowers the premium, and a poor record raises it. A limited history makes pricing harder."),
        ("Exclusions",
         "Exclusions are losses the policy does not cover, such as losses from certain causes. Clear exclusions prevent disputes later. Buyers should read them carefully."),
        ("The structure",
         "Cover can be arranged in layers, with different insurers sharing different slices of the risk. This spreads the exposure. The structure is part of the price."),
    ],
    "test": [
        ("What does launch risk mean?",
         [("a", "A sale"), ("b", "A meal"), ("c", "A star"), ("d", "The chance a launch fails and damages or loses the satellite")], "d"),
        ("What does the premium pay for?",
         [("a", "A fine"), ("b", "Cover"), ("c", "A car"), ("d", "A cake")], "b"),
        ("What is the payout?",
         [("a", "A list"), ("b", "A holiday"), ("c", "The amount the insurer pays after a covered loss"), ("d", "A parade")], "c"),
        ("What does a strong prior record do to premiums?",
         [("a", "Raises them"), ("b", "Doubles them"), ("c", "Hides them"), ("d", "Lowers them")], "d"),
        ("What do exclusions do?",
         [("a", "List losses the policy does not cover"), ("b", "List all the winners"), ("c", "List ships"), ("d", "List stars")], "a"),
    ],
}
