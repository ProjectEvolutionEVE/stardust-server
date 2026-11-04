"""Monte Carlo Cost Estimates for Surveys: cost drivers, distributions, simulations, confidence levels, reserves and communicating risk."""
CODE = "navigation5_survey_cost_risk"
BOOK = {
    "title": "Monte Carlo Cost Estimates for Surveys",
    "subtitle": "Budgeting for the range of outcomes, not a single guess",
    "chapters": [
        ("Cost drivers",
         "Cost drivers are the factors that most affect the total cost of a survey, such as the number of days at sea or the equipment used. Finding them shows where to focus. Good estimates name them clearly."),
        ("Distributions",
         "Each uncertain cost is described by a distribution, which is a range of values with their likelihoods. A triangle with a low, a most likely and a high value is one simple form. Choosing the shape is a matter of judgement."),
        ("Simulations",
         "A Monte Carlo simulation draws random values from the distributions many times. Each run gives one possible total cost. Taken together, the runs show the spread of likely outcomes."),
        ("Confidence levels",
         "A confidence level says how likely a budget is to be enough. For example, an 80 per cent level means the budget is expected to cover the costs in four runs out of five. Teams pick a level they can defend."),
        ("Reserves",
         "A reserve is money set aside above the expected cost to cover the risk. The size of the reserve depends on the confidence level chosen. Reserves are part of a sound budget."),
        ("Communicating risk",
         "Results should be shown as ranges, with the assumptions stated clearly. Decision-makers need to know what the numbers mean and what could change them. Honest communication builds trust."),
    ],
    "test": [
        ("What are cost drivers?",
         [("a", "The paint colours"), ("b", "The sea level"), ("c", "The stars"), ("d", "The factors that most affect the total cost")], "d"),
        ("What describes an uncertain cost?",
         [("a", "A distribution of likely values"), ("b", "A single lucky guess"), ("c", "A poem"), ("d", "A fish")], "a"),
        ("What does a Monte Carlo simulation do?",
         [("a", "Runs ships"), ("b", "Paints maps"), ("c", "Draws random values from distributions many times"), ("d", "Sings")], "c"),
        ("What does an 80 per cent confidence level mean?",
         [("a", "The budget is always wrong"), ("b", "The budget is expected to cover costs in four runs out of five"), ("c", "The budget is zero"), ("d", "The budget is secret")], "b"),
        ("What is a reserve?",
         [("a", "Money for a holiday"), ("b", "Money for fish"), ("c", "Money set aside above the expected cost to cover risk"), ("d", "Money for paint")], "c"),
    ],
}
