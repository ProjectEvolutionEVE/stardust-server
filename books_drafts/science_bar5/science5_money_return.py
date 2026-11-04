"""Measuring the Economic Return on Research: how economists estimate what research gives back, and why those estimates are hard to pin down."""
CODE = "science5_money_return"
BOOK = {
    "title": "Measuring the Economic Return on Research",
    "subtitle": "Return metrics, spillover effects, time lags, attribution problems, case studies and limits of estimates",
    "chapters": [
        ("Return metrics", "A return metric compares the benefit of research with its cost. A common example is the benefit-cost ratio, which divides estimated benefits by costs. Metrics make different projects comparable, but only if the benefits are measured fairly."),
        ("Spillover effects", "A spillover effect is a benefit that reaches people or firms beyond the original research. A new technique may help other labs, industries and users who never paid for it. Spillovers are often a large part of the total return."),
        ("Time lags", "Research can take years or decades before its returns appear. A discovery may sit unused until a technology catches up with it. Long lags make the return hard to measure and easy to underestimate."),
        ("Attribution problems", "Attribution asks how much of an outcome can be credited to a specific research input. Many factors, including other research, markets and policy, contribute to the same result. Careful studies try to separate these influences."),
        ("Case studies", "Case studies trace the path from a specific piece of research to its economic effects. They show how a discovery became a product, a process or a policy. Case studies are vivid, but a single case cannot show the typical return."),
        ("Limits of estimates", "Estimates depend on assumptions about timing, attribution and value, and each assumption carries uncertainty. A good estimate states its assumptions and shows a range rather than a single number. Estimates guide choices, but they do not settle them."),
    ],
    "test": [
        ("What is a return metric?",
         [("a", "A product sent back to a shop"), ("b", "A refund of a ticket price"), ("c", "A measure of benefit compared with cost, such as a benefit-cost ratio"), ("d", "A tax form")], "c"),
        ("What is a spillover effect?",
         [("a", "Benefits that reach people or firms beyond the original research"), ("b", "A kitchen accident"), ("c", "Water spilled on the floor"), ("d", "A type of loan")], "a"),
        ("Why do time lags matter when measuring research return?",
         [("a", "They do not matter at all"), ("b", "Returns always appear the next day"), ("c", "They only apply to lunch breaks"), ("d", "Research can take years or decades before its returns appear, which makes measurement hard")], "d"),
        ("What is attribution in this context?",
         [("a", "A list of names on a paper"), ("b", "A type of cheque"), ("c", "Working out how much of an outcome can be credited to a specific research input"), ("d", "A method of painting")], "c"),
        ("Why are economic estimates of research return limited?",
         [("a", "Estimates are always exact"), ("b", "Results depend on assumptions and many other factors, so estimates carry uncertainty"), ("c", "Economics has no uncertainty"), ("d", "Estimates ignore all data")], "b"),
    ],
}
