"""Dollar-Cost Averaging and Rebalancing: investing on a schedule, the maths of averaging, lump sum comparisons, rebalancing bands, tax effects, and staying the course."""
CODE = "business5_dca"
BOOK = {
    "title": "Dollar-Cost Averaging and Rebalancing",
    "subtitle": "Two habits for investing over time, and what they cost",
    "chapters": [
        ("Investing on a schedule",
         "Dollar-cost averaging means investing a fixed amount at set intervals, such as every month, whatever the price. It spreads the timing of purchases and can make investing a steady habit. It is a method of pacing, not a promise of gain."),
        ("The maths of averaging",
         "When prices are low, a fixed sum buys more units, and when prices are high, it buys fewer. The average cost per unit is then lower than the average price over the period. The averaging helps with timing, but it does not guarantee a better result."),
        ("Lump sum comparison",
         "Historical studies have often found that investing a lump sum all at once has done better on average than spreading it out, because markets have tended to rise over time. Spreading the money reduces the regret of investing just before a fall. This is a general finding, not advice for any one person."),
        ("Rebalancing bands",
         "Rebalancing restores a target mix when holdings drift apart, for example when shares grow faster than bonds. Some people rebalance on a calendar, and others when a holding moves outside a set band. Bands cut trading, but they must be set and kept."),
        ("Tax effects",
         "In a taxable account, selling winners to rebalance can create a taxable gain. Rebalancing with new money, or inside tax-sheltered accounts, can avoid that cost. The tax rules differ by country and by account type."),
        ("Staying the course",
         "Markets fall as well as rise, and panic selling after a fall often locks in a loss. A written plan helps you stick to it through hard times. Simple, low-cost and steady is often harder than it sounds, but it has a strong record."),
    ],
    "test": [
        ("What is dollar-cost averaging?",
         [("a", "Investing a fixed amount on a set schedule"), ("b", "Buying one item on sale"), ("c", "Paying with dollars only"), ("d", "Averaging the prices of shops")], "a"),
        ("Which approach has often beaten dollar-cost averaging in historical studies?",
         [("a", "Doing nothing at all"), ("b", "Burying cash in a garden"), ("c", "Paying tax first"), ("d", "Investing a lump sum all at once")], "d"),
        ("What is rebalancing?",
         [("a", "Restoring your target mix when holdings drift apart"), ("b", "Balancing a pen on a finger"), ("c", "Doubling the stake"), ("d", "Selling everything at once")], "a"),
        ("Why might rebalancing create a tax bill?",
         [("a", "Buying always costs tax"), ("b", "Staying still costs nothing"), ("c", "Selling winners to restore the mix can count as a taxable gain in some accounts"), ("d", "Tax is never due")], "c"),
        ("Which is a sound reason to stay the course?",
         [("a", "Ignoring the plan saves time"), ("b", "Panic selling after falls usually locks in losses"), ("c", "Stock prices never move"), ("d", "Fees are fun")], "b"),
    ],
}
