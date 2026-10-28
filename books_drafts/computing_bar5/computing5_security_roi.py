"""Return on Security Investment: how to compare the cost of a security control with the losses it can prevent."""
CODE = "computing5_security_roi"
BOOK = {
    "title": "Return on Security Investment",
    "subtitle": "Comparing what a security control costs with the losses it can prevent",
    "chapters": [
        ("Loss expectancy",
         "Loss expectancy estimates how much a risk could cost. A common way is to multiply the cost of one incident by how often it is expected to happen each year. The result is an annual figure that can be compared with other costs."),
        ("Control costs",
         "A control is a measure that reduces a risk, such as training, a tool or a process. Its cost includes licences, staff time and upkeep over its life. Count every year, not just the purchase price."),
        ("Risk reduction estimates",
         "A control rarely removes a risk completely. Estimate how much it lowers the expected loss, and be honest about the uncertainty. Ask a second person to challenge the estimate."),
        ("Budget decisions",
         "Compare the expected reduction in loss with the yearly cost of the control. A control that costs more than the loss it prevents may not be worth buying. Look at the choice alongside other ways to lower the same risk."),
        ("Uncertainty",
         "Security estimates are rough, because attacks are hard to predict. Show a range instead of a single figure. Decisions that hold up across the range are the strongest."),
        ("Reporting",
         "Report the assumptions, the expected losses and the cost of each control in plain language. Explain which numbers are estimates. Leaders can then judge the trade-offs themselves."),
    ],
    "test": [
        ("What does loss expectancy estimate?",
         [("a", "The number of staff who will be hired"), ("b", "How much a risk could cost, often per year"), ("c", "The size of the office"), ("d", "The colour of the logo")], "b"),
        ("What should a control's cost include?",
         [("a", "Only the purchase price"), ("b", "The price of coffee"), ("c", "Nothing after the first day"), ("d", "Licences, staff time and upkeep over the control's life")], "d"),
        ("Why show a range rather than one figure for security estimates?",
         [("a", "Attacks are hard to predict, so estimates are uncertain"), ("b", "Ranges are always shorter"), ("c", "Ranges avoid all decisions"), ("d", "Single figures are illegal")], "a"),
        ("When may a control not be worth buying?",
         [("a", "When it is cheap"), ("b", "When it is easy to use"), ("c", "When it costs more each year than the loss it prevents"), ("d", "When staff like it")], "c"),
        ("What should a security report explain?",
         [("a", "Only the good news"), ("b", "The assumptions, the expected losses and which numbers are estimates"), ("c", "The names of the people who failed"), ("d", "Nothing about costs")], "b"),
    ],
}
