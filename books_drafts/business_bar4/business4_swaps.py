"""Swaps: trading streams of payments."""
CODE = "business4_swaps"
BOOK = {
    "title": "Swaps",
    "subtitle": "Trading streams of payments",
    "chapters": [
        ("Exchanging payments",
         "A swap is a contract in which two parties agree to exchange streams of payments over time. In an interest-rate swap, the principal is usually not exchanged. Each side pays the other the amount its contract calls for."),
        ("The interest-rate swap",
         "Imagine a firm with a loan at a floating rate that would prefer a fixed rate. It agrees with a bank to pay a fixed rate and receive a floating rate. The floating receipts offset its floating loan payments, leaving it with a fixed cost."),
        ("A worked example",
         "Suppose a firm has a 10 million floating-rate loan and swaps to pay 5% fixed while receiving the floating rate. If the floating rate rises to 6%, the swap pays the firm 6%, which covers its loan interest. It still pays 5% fixed, so its net cost stays at the fixed rate."),
        ("The currency swap",
         "In a currency swap, the parties exchange principal and interest in two currencies. A firm can borrow cheaply in its home currency and swap into another currency to fund a project abroad. Currency swaps are a common tool for global firms."),
        ("Counterparty risk",
         "A swap relies on each side paying what it promised. If one side fails, the other can lose the payments it expected. Clearing houses and collateral reduce this risk. The 2008 crisis showed how large, interconnected swap books can spread trouble."),
        ("How banks use them",
         "Banks use swaps to manage mismatches between their fixed-rate assets and their floating-rate funding. They earn fees and spreads, and they hedge large exposures. Swaps are mainly a risk-management tool, though they can also be used for bets."),
    ],
    "test": [
        ("What is a swap?",
         [("a", "A trade of one share for another"), ("b", "A contract to exchange streams of payments over time"), ("c", "A bank note"), ("d", "A tax reform")], "b"),
        ("In the worked example, the firm pays 5% fixed. If the floating rate rises to 6%, what does its net cost stay at?",
         [("a", "6%"), ("b", "11%"), ("c", "5%"), ("d", "1%")], "c"),
        ("What is counterparty risk?",
         [("a", "The risk that the other side fails to pay what it promised"), ("b", "The risk of sun damage"), ("c", "The risk of a tax change"), ("d", "The risk of rising staff costs")], "a"),
        ("What does a currency swap exchange?",
         [("a", "Only pens"), ("b", "Share options"), ("c", "Staff"), ("d", "Principal and interest in two currencies")], "d"),
        ("What are swaps often used for by banks?",
         [("a", "To avoid all lending"), ("b", "To manage mismatches between fixed-rate assets and floating-rate funding"), ("c", "To pay dividends"), ("d", "To print money")], "b"),
    ],
}
