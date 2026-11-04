"""Costs of Data Storage and Computing: what research data and computation cost to keep, process and move, and how to plan for them."""
CODE = "science5_money_data_costs"
BOOK = {
    "title": "Costs of Data Storage and Computing",
    "subtitle": "Storage tiers, computing budgets, cloud versus local, data lifecycle costs, energy and cooling and cost forecasting",
    "chapters": [
        ("Storage tiers", "Storage tiers are levels of storage with different speed and cost. Fast storage is expensive, and slow archive storage is cheap. Matching each dataset to the right tier keeps costs down without slowing the work that needs speed."),
        ("Computing budgets", "A computing budget is a plan for the money spent on processing power, software and data handling. Large analyses can use a lot of time on powerful machines. A budget keeps these costs visible and under control."),
        ("Cloud versus local", "Cloud services can scale up quickly and reduce the upkeep of hardware, but their running fees add up over time. Local systems give more control and may have lower ongoing fees, but they need upfront spending and staff to maintain them. The right choice depends on how the work is used."),
        ("Data lifecycle costs", "Data lifecycle costs cover keeping, moving, archiving and eventually deleting data over its whole life. Many projects count only the cost of storing it now. Planning the full lifecycle gives a truer picture of the bill."),
        ("Energy and cooling", "Servers use power and produce heat, and the heat must be removed. Cooling can add as much cost as the machines themselves. Efficient hardware and good cooling reduce both running costs and emissions."),
        ("Cost forecasting", "Cost forecasting estimates how storage and computing needs will grow over the life of a project. It accounts for new data, longer retention and new kinds of analysis. Forecasts should be revisited as the project's needs change."),
    ],
    "test": [
        ("What are storage tiers?",
         [("a", "Levels of storage with different speed and cost, from fast and expensive to slow and cheap"), ("b", "Shelves in a bank vault"), ("c", "Steps in a sports stadium"), ("d", "Layers of paint on a wall")], "a"),
        ("What is a computing budget?",
         [("a", "A budget for food in the canteen"), ("b", "A budget for holidays"), ("c", "A plan for the money spent on processing power, software and data handling"), ("d", "A budget for school supplies")], "c"),
        ("What is a key trade-off between cloud and local computing?",
         [("a", "Cloud is always free"), ("b", "Local systems are always faster"), ("c", "There are no trade-offs at all"), ("d", "Cloud can scale and reduce upkeep, while local gives control and may have lower ongoing fees, so the choice depends on use")], "d"),
        ("What are data lifecycle costs?",
         [("a", "The cost of one single file"), ("b", "The cost of keeping, moving, archiving and eventually deleting data over its whole life"), ("c", "The cost of a laptop"), ("d", "The price of a cup of coffee")], "b"),
        ("Why do energy and cooling matter for computing costs?",
         [("a", "They do not matter at all"), ("b", "Machines never get warm"), ("c", "Servers use power and produce heat that must be removed, which adds to running costs"), ("d", "Cooling only matters for fridges in kitchens")], "c"),
    ],
}
