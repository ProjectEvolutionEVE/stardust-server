"""Cost-Benefit Analysis of Research Choices: comparing costs and gains, with expected values and checks."""
CODE = "science4_money_cost_benefit"
BOOK = {
    "title": "Cost-Benefit Analysis of Research Choices",
    "subtitle": "Weighing what a choice costs against what it gains",
    "chapters": [
        ("Costs and benefits", "A cost-benefit analysis lists every cost and every benefit of a choice. Costs are what must be given up, and benefits are what is gained. Writing both down side by side makes the trade-off visible."),
        ("Expected value", "Expected value multiplies each outcome by its chance and adds the results. A test with a 20% chance of a valuable result has an expected value of one fifth of that result. This helps compare choices with uncertain outcomes."),
        ("Comparing two experiments", "Suppose one experiment is cheap but less certain, and another is costly but more certain. Compare their expected values and their risks. The numbers help, but judgement is still needed."),
        ("Discounting basics", "Money received later is worth less than the same money received now, because it could be invested in the meantime. Discounting reduces future amounts by a rate for each year. Present value is the amount expressed in today's money."),
        ("Sensitivity checks", "A sensitivity check changes one assumption at a time to see whether the answer changes. If a small change flips the decision, the choice is fragile. Testing the assumptions makes the analysis more honest."),
        ("Decision summaries", "A short summary states the choice, the main costs, the main benefits and the key risks. It should be clear enough for a busy leader to read in a minute. A good summary shows the reasoning, not only the answer."),
    ],
    "test": [
        ("What does a cost-benefit analysis list?",
         [("a", "Only the colour of the project"), ("b", "Only the team names"), ("c", "Every cost and every benefit of a choice"), ("d", "Only the final grant letter")], "c"),
        ("How is expected value worked out?",
         [("a", "By adding the outcomes only"), ("b", "By multiplying each outcome by its chance and adding the results"), ("c", "By counting the pages"), ("d", "By choosing the largest number")], "b"),
        ("What does discounting do to future money?",
         [("a", "Makes it worth more"), ("b", "Makes it disappear"), ("c", "Makes it equal to today's money"), ("d", "Reduces its value in today's terms")], "d"),
        ("What is a sensitivity check?",
         [("a", "A test of lab staff's health"), ("b", "A check of the lab temperature"), ("c", "Changing one assumption at a time to see whether the answer changes"), ("d", "A check of the printer")], "c"),
        ("What should a decision summary state?",
         [("a", "The choice, the main costs and benefits, and the key risks"), ("b", "Only the name of the author"), ("c", "The length of the lunch break"), ("d", "Only the printer model")], "a"),
    ],
}
