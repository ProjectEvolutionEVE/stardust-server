"""Costs of Running AI Models: why training and running a model cost different amounts, and how to budget for each query."""
CODE = "computing5_running_ai_costs"
BOOK = {
    "title": "Costs of Running AI Models",
    "subtitle": "Training versus running a model, and how to budget for each query",
    "chapters": [
        ("Training versus inference",
         "Training is the one-off or occasional work of building a model. Inference is running the model to produce an answer. Training is usually a large single cost, while inference adds up with every use."),
        ("Accelerator hours",
         "Specialised chips called accelerators do much of this work, and they are priced by the hour. Their cost depends on how many are used and for how long. Measure hours used, not just the number of machines owned."),
        ("Caching outputs",
         "If the same question is asked often, storing the answer can avoid running the model again. Caching cuts cost and speeds up replies. Check that the stored answer is still correct before reuse."),
        ("Budgets per query",
         "A budget per query divides the total running cost by the number of queries served. It shows the cost of each answer. Use it to decide which uses are worth their cost."),
        ("Efficiency",
         "A smaller or better-tuned model can often do a task for less cost. Efficiency work trades a little quality for lower cost, which is a choice to make openly. Test the quality impact before changing a model."),
        ("Forecasting",
         "Forecast running costs from expected query volume and the cost per query. Update the forecast as usage grows. Watch for sudden spikes, which can come from a new feature."),
    ],
    "test": [
        ("What is inference in running a model?",
         [("a", "Painting the office walls"), ("b", "Running the model to produce an answer"), ("c", "Paying the staff"), ("d", "Writing the company report")], "b"),
        ("What are accelerators?",
         [("a", "Garden tools"), ("b", "A type of office chair"), ("c", "Kitchen devices"), ("d", "Specialised chips that do much of the model's work")], "d"),
        ("Why can caching outputs reduce cost?",
         [("a", "A stored answer avoids running the model again"), ("b", "It doubles the number of queries"), ("c", "It stops all answers"), ("d", "It has no effect at all")], "a"),
        ("What does a budget per query show?",
         [("a", "The colour of the screen"), ("b", "The number of staff in a team"), ("c", "The total cost divided by the number of queries served"), ("d", "The length of the office lunch break")], "c"),
        ("What should be tested before changing a model for efficiency?",
         [("a", "The office temperature"), ("b", "The quality impact of the change"), ("c", "The name of the model"), ("d", "The price of the coffee")], "b"),
    ],
}
