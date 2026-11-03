"""Net Present Value for Research Investments: adding up what a project costs and returns over time, in today's money."""
CODE = "science5_money_npv"
BOOK = {
    "title": "Net Present Value for Research Investments",
    "subtitle": "Cash flows, the NPV calculation, hurdle rates, comparing projects, sensitivity analysis and limits of NPV",
    "chapters": [
        ("Cash flows", "Cash flows are the money coming into and going out of a project over time. They include the initial spending, the running costs and any income or savings. Listing them year by year is the first step in any NPV calculation."),
        ("The NPV calculation", "Net present value discounts each future cash flow back to today and adds them up, including the initial outlay. A positive result means the project returns more than the discount rate asks for. A negative result means it does not."),
        ("Hurdle rates", "A hurdle rate is the minimum return a project must earn to be worth doing. It reflects the cost of the money and the risk taken. Projects that clear the hurdle are candidates, and those that fall short need a strong reason to go ahead."),
        ("Comparing projects", "To compare projects, calculate each NPV at the same discount rate. Then the larger NPV usually points to the better use of money. Comparing NPVs at different rates gives misleading results."),
        ("Sensitivity analysis", "Sensitivity analysis changes the key inputs, such as costs, timing and income, to see how the NPV moves. It shows which assumptions matter most. Decisions can then focus on checking those assumptions."),
        ("Limits of NPV", "NPV depends on the discount rate and on forecasts of future cash flows, and both can be wrong. It does not capture flexibility or the value of learning as a project goes on. It is a strong tool, but not the only one."),
    ],
    "test": [
        ("What are cash flows?",
         [("a", "The flow of water in a pipe"), ("b", "Only the profit of a project"), ("c", "Money coming into and going out of a project over time"), ("d", "Changes in stock prices")], "c"),
        ("What does an NPV calculation do?",
         [("a", "Adds up cash flows without considering time"), ("b", "Discounts each cash flow to today and adds them, including the initial outlay"), ("c", "Doubles all of the costs"), ("d", "Counts the number of staff")], "b"),
        ("What is a hurdle rate?",
         [("a", "The minimum return a project must earn to be worth doing"), ("b", "A term used in sport"), ("c", "A type of tax"), ("d", "A laboratory test")], "a"),
        ("How is NPV used to compare projects?",
         [("a", "By choosing the project with the shortest name"), ("b", "By picking the project with the most staff"), ("c", "By picking the project that looks most colourful"), ("d", "By comparing their NPVs calculated at the same discount rate")], "d"),
        ("What is a limit of NPV?",
         [("a", "It needs no assumptions at all"), ("b", "It always predicts the future exactly"), ("c", "It has nothing to do with money"), ("d", "It depends on the discount rate and forecasts, which can be wrong")], "d"),
    ],
}
