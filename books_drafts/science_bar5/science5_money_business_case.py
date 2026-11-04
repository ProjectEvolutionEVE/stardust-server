"""Business Cases for Research Infrastructure: making the argument for a large investment in equipment, buildings or facilities."""
CODE = "science5_money_business_case"
BOOK = {
    "title": "Business Cases for Research Infrastructure",
    "subtitle": "Need statements, options appraisal, benefit estimates, sensitivity, stakeholder review and investment decisions",
    "chapters": [
        ("Why write a business case", "A business case explains why an investment is worth making, and what it will cost and bring. Research infrastructure, such as a new facility or a major instrument, is expensive and long-lived. The case lets decision makers compare it fairly with other uses of the money."),
        ("The need statement", "A need statement describes the problem in plain terms: what cannot be done now, who is affected and what it costs to leave things as they are. It is the foundation of the case. A vague need leads to a weak case."),
        ("Options appraisal", "An options appraisal compares several ways to meet the need. The list should include doing nothing, a smaller option, a larger option and a shared arrangement with others. Each option is judged on cost, benefit, risk and fit with the goals."),
        ("Benefit estimates", "A benefit estimate is a reasoned forecast of what the investment will bring. Benefits can include research output, savings, training, safety and income. Each estimate states its assumptions, so others can check them."),
        ("Sensitivity analysis", "Sensitivity analysis shows how the answer changes if key assumptions turn out wrong. If the case still stands when costs rise or use falls, it is robust. If a small change flips the answer, that assumption needs closer study."),
        ("Stakeholder review and decision", "Stakeholders such as users, managers, funders and technicians review the case. They may spot missing costs, unrealistic use or needs that the team has overlooked. The final decision rests on the case as revised after that review."),
    ],
    "test": [
        ("What is a need statement?",
         [("a", "A list of job titles in the department"), ("b", "A clear description of the problem the investment is meant to solve"), ("c", "A wish list of new gadgets"), ("d", "An invoice from a supplier")], "b"),
        ("What does an options appraisal compare?",
         [("a", "Only the cheapest option"), ("b", "Only the most expensive option"), ("c", "The colour of each option's documents"), ("d", "Several ways to meet the need, including doing nothing")], "d"),
        ("What is a benefit estimate?",
         [("a", "A guess about staff mood"), ("b", "A bill for work already done"), ("c", "A reasoned forecast of what the investment will bring, in money or other measures"), ("d", "A list of possible suppliers")], "c"),
        ("Why run a sensitivity analysis?",
         [("a", "To see how the answer changes if key assumptions turn out wrong"), ("b", "To prove the answer in advance"), ("c", "To remove all risk from the project"), ("d", "To avoid writing any numbers")], "a"),
        ("Why involve stakeholders in the review?",
         [("a", "They may spot missing costs and needs that the team has overlooked"), ("b", "They must approve their own work"), ("c", "It is only a formality"), ("d", "It saves all of the cost")], "a"),
    ],
}
