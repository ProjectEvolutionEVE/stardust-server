"""Costing a Space Mission and Cost Overruns: estimating what a mission costs, why overruns happen and how reserves protect a project."""
CODE = "science5_money_space_cost"
BOOK = {
    "title": "Costing a Space Mission and Cost Overruns",
    "subtitle": "Cost estimation, launch costs, development risk, causes of overrun, reserves and cost reviews",
    "chapters": [
        ("Cost estimation", "Cost estimation predicts the cost of a project from its scope, its risks and past data from similar work. A good estimate states its assumptions and gives a range. Early estimates are rough, and they improve as the design matures."),
        ("Launch costs", "Launch costs are high because rockets are costly to build and fly, and each launch needs much specialised work. Preparation, range support and insurance add to the total. Launch is often a large share of a mission's budget."),
        ("Development risk", "Development risk is the chance that new technology or an untested design needs rework or fails. Risk grows when a mission pushes beyond proven designs. Cost estimates should carry a provision for this risk."),
        ("Causes of overrun", "Common causes of overrun include optimistic early estimates, growth in scope, late design changes and delays in suppliers. Each cause can be spotted early with regular reviews. Naming the causes helps stop them repeating."),
        ("Reserves", "A reserve is money held back to cover risks that may cause extra cost. Reserves are set by looking at the size and likelihood of each risk. A project with no reserve has no room to absorb a surprise."),
        ("Cost reviews", "Cost reviews check the actual spending against the estimate at set points in the project. They show trends early, so decisions can be made in time. Honest reviews are one of the best protections against overrun."),
    ],
    "test": [
        ("What is cost estimation?",
         [("a", "Guessing at random"), ("b", "Predicting the cost of a project from its scope, risks and past data"), ("c", "Reading a bill that has arrived"), ("d", "Counting the planets in the solar system")], "b"),
        ("Why are launch costs so high?",
         [("a", "Rockets are costly to build and fly, and each launch needs much specialised work"), ("b", "Rocket fuel is free"), ("c", "Launches are very small events"), ("d", "Launches happen at no cost at all")], "a"),
        ("What drives development risk in a space mission?",
         [("a", "The weather at home"), ("b", "New technology and untested designs that may need rework"), ("c", "Staff holidays"), ("d", "The colour of the office")], "b"),
        ("What is a common cause of cost overrun?",
         [("a", "Too little paperwork"), ("b", "Finishing the work on time"), ("c", "Optimistic early estimates, growth in scope and late design changes"), ("d", "Cheap parts")], "c"),
        ("What is a reserve in a project budget?",
         [("a", "A table booked at a restaurant"), ("b", "A seat on a plane"), ("c", "A bed in a hostel"), ("d", "Money held back to cover risks that may cause extra cost")], "d"),
    ],
}
