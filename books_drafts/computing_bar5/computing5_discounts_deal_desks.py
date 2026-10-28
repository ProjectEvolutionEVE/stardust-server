"""Discounting and Deal Desks: how list prices, discounts and deal rules protect margin."""
CODE = "computing5_discounts_deal_desks"
BOOK = {
    "title": "Discounting and Deal Desks",
    "subtitle": "How list prices, discounts and deal rules protect the margin",
    "chapters": [
        ("List versus net price",
         "The list price is the published price before any discount. The net price is what the customer actually pays after discounts. Revenue planning should use the net price, because the list price overstates what comes in."),
        ("Multi-year discounts",
         "A discount for a longer commitment can help both sides plan. It can also lock in a lower price for years. Check the price per year, and what the customer must commit to in return."),
        ("Minimum commitments",
         "A minimum commitment is the least a customer must spend or use. It protects the seller from a deal that is too small to cover its costs. Set minimums so the work of selling and supporting the account is paid for."),
        ("Renewal uplifts",
         "An uplift is a planned rise in price at renewal. Uplifts that are too large lose customers, and ones that are too small leave money on the table. Set them against the value delivered and the cost of switching."),
        ("Deal desk rules",
         "A deal desk is a team that reviews unusual or large discounts before they are offered. Its rules set who may approve each level of discount. Clear rules speed up good deals and stop poor ones."),
        ("Margin",
         "Margin is the share of revenue left after the direct costs of providing the product. Each extra discount shrinks it. Track margin deal by deal, so the effect of discounting is visible."),
    ],
    "test": [
        ("What is the net price?",
         [("a", "The published price before any discount"), ("b", "The price a customer actually pays after discounts"), ("c", "The price a competitor charges"), ("d", "The price of the office")], "b"),
        ("What does a minimum commitment protect?",
         [("a", "The customer from ever paying more"), ("b", "The office from noise"), ("c", "The product from being used"), ("d", "The seller from a deal too small to cover its costs")], "d"),
        ("What is a renewal uplift?",
         [("a", "A planned rise in price at renewal"), ("b", "A cut in price for new customers"), ("c", "A staff bonus"), ("d", "A free upgrade for all users")], "a"),
        ("What does a deal desk do?",
         [("a", "It cooks lunch for the sales team"), ("b", "It writes the product code"), ("c", "It reviews unusual or large discounts before they are offered"), ("d", "It sets office hours")], "c"),
        ("What does each extra discount do to margin?",
         [("a", "It always raises margin"), ("b", "It shrinks the share of revenue left after direct costs"), ("c", "It has no effect on margin"), ("d", "It only changes the list price")], "b"),
    ],
}
