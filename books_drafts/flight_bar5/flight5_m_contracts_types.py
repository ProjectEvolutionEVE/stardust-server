"""Types of Contract: fixed price, cost plus, incentive, time and materials, how risk is split, and space examples."""
CODE = "flight5_m_contracts_types"
BOOK = {
    "title": "Types of Contract",
    "subtitle": "Who carries the risk of cost and time",
    "chapters": [
        ("Why contract type matters",
         "A contract sets how the price is paid and who carries the risk if costs rise. The type of contract shapes how the work is run and how much each side can trust the other. Choose the type that fits the work."),
        ("Fixed price",
         "In a fixed price contract, the supplier agrees one price for the whole job. The supplier carries the risk of overspending. This suits work that is well understood, and it gives the buyer a clear cost."),
        ("Cost plus",
         "In a cost plus contract, the buyer pays the actual costs and a fee on top. The buyer carries most of the cost risk. This suits new or uncertain work, where a fixed price would be hard to set."),
        ("Incentive contracts",
         "An incentive contract rewards the supplier for good results, such as finishing early or meeting targets, and may penalise poor results. It shares the risk and rewards efficiency, but it needs clear targets to work well."),
        ("Time and materials",
         "Under time and materials, the buyer pays for hours worked and for the materials used. It is quick to start but gives the buyer less control over the final cost. Clear limits on hours and spending help."),
        ("Space examples",
         "Space projects use a mix of these types. A well-known product may be bought at a fixed price, while a new design often starts on cost plus, with incentives added as it matures."),
    ],
    "test": [
        ("In a fixed price contract, who carries the risk of overspending?",
         [("a", "The buyer, always"), ("b", "The government, always"), ("c", "The supplier"), ("d", "Nobody")], "c"),
        ("What does a cost plus contract pay for?",
         [("a", "The actual costs, plus a fee on top"), ("b", "A single fixed price"), ("c", "Only the buyer's time"), ("d", "Nothing at all")], "a"),
        ("What is an incentive contract?",
         [("a", "One that offers free goods"), ("b", "One that never pays"), ("c", "One that rewards good results and may penalise poor ones"), ("d", "One that bans targets")], "c"),
        ("When does time and materials suit a job?",
         [("a", "When the price must be fixed exactly"), ("b", "When the work is hard to define, so the buyer pays for hours and materials"), ("c", "When no work is done"), ("d", "When the buyer wants no control")], "b"),
        ("Which contract type suits well understood work with a clear cost?",
         [("a", "Cost plus"), ("b", "Time and materials"), ("c", "No contract"), ("d", "Fixed price")], "d"),
    ],
}
