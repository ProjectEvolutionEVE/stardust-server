"""Insurance Basics (Manager, bar 3, part A): premiums, deductibles and limits, and how spreading a risk across many people makes it affordable."""
CODE = "business3a_insurance"
BOOK = {
    "title": "Insurance Basics",
    "subtitle": "Premiums, deductibles and limits, and how sharing a risk makes it affordable",
    "chapters": [
        ("What insurance does",
         "Insurance moves a risk from one party to another. You pay a regular amount, and if a covered loss happens, the insurer pays part or all of it. You trade a small, certain cost for protection against a large, uncertain one."),
        ("The premium",
         "The premium is the regular amount you pay to keep the cover in place. It is set so that, across many people, the money collected covers the claims and the insurer's own costs. The premium is paid whether or not a loss happens."),
        ("The deductible",
         "The deductible is the part of a loss you pay yourself before the insurer pays. A higher deductible usually means a lower premium, because you carry more of the risk. Choose a deductible you could pay without borrowing in a hurry."),
        ("The cover limit",
         "The cover limit is the most the insurer will pay for a loss or in a period. Any loss above the limit falls back on you. Read the limit as carefully as the premium."),
        ("A worked example",
         "Suppose your premium is 60 credits, your deductible is 200 and a loss costs 1,000. You pay the 200 deductible, and the insurer pays the remaining 800. Your total cost is 260 credits, not 1,000. Without the cover, the whole 1,000 would be yours."),
        ("Sharing the risk",
         "Insurance works because many people pay in, and only a few have a loss in a given year. That sharing makes large, rare losses affordable for everyone in the pool. Buy cover for the risks you could not carry alone, rather than for every small cost."),
    ],
    "test": [
        ("What is the premium?",
         [("a", "The part of a loss you pay yourself"), ("b", "The regular amount you pay to keep the cover in place"), ("c", "The most the insurer will ever pay"), ("d", "The price of the insured item")], "b"),
        ("What is a deductible?",
         [("a", "The total cover limit"), ("b", "A bonus paid by the insurer"), ("c", "The price of a new policy"), ("d", "The part of a loss you pay yourself before the insurer pays")], "d"),
        ("A premium is 60 credits, a deductible is 200 and a loss costs 1,000. What do you pay in total?",
         [("a", "260 credits"), ("b", "1,000 credits"), ("c", "800 credits"), ("d", "1,060 credits")], "a"),
        ("Why does sharing a risk make large, rare losses affordable?",
         [("a", "Because insurers never pay out"), ("b", "Because the cover is free"), ("c", "Because many people pay in, and only a few have a loss in a given year"), ("d", "Because losses are always small")], "c"),
        ("What does a cover limit tell you?",
         [("a", "How many years the policy lasts"), ("b", "The most the insurer will pay for a loss or period, so any loss above it falls on you"), ("c", "The discount for paying early"), ("d", "The price of the premium")], "b"),
    ],
}
