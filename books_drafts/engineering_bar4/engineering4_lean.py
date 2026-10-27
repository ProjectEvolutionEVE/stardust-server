"""Lean Manufacturing and the Toyota Production System: flow, pull, the seven wastes, and the money saved by holding less stock."""
CODE = 'engineering4_lean'
BOOK = {
    "title": "Lean Manufacturing and the Toyota Production System",
    "subtitle": "Less waste, steady flow, and the money saved by holding less stock",
    "chapters": [
        ("Flow",
         "Lean aims for work to flow smoothly from step to step with little waiting. Each step should feed the next without a pile of parts sitting between them."),
        ("Pull",
         "Pull means making an item when the next step needs it, rather than pushing goods out in advance. This limits stock and cuts waste."),
        ("The seven wastes",
         "The classic list names seven wastes: overproduction, waiting, transport, over-processing, inventory, motion and defects. Spotting them is the start of any improvement."),
        ("Kaizen events",
         "A kaizen event is a short, focused team effort to improve one process. Many small improvements, made by the people who do the work, add up over time."),
        ("Value stream mapping",
         "A value stream map draws every step from raw material to customer, with the time each step takes. It shows clearly where time and money are being lost."),
        ("The money in less stock",
         "Stock ties up cash, takes up space and hides problems. Holding less stock frees money, although it depends on a reliable supply."),
    ],
    "test": [
        ("What does pull mean in lean?",
         [("a", "Pulling carts across the floor"), ("b", "Pushing goods out early"), ("c", "Making an item when the next step needs it"), ("d", "Adding a new coat of paint")], "c"),
        ("How many wastes does the classic list name?",
         [("a", "Seven"), ("b", "Three"), ("c", "Twelve"), ("d", "One")], "a"),
        ("What is a kaizen event?",
         [("a", "A machine failure"), ("b", "A sales meeting"), ("c", "A fine"), ("d", "A short, focused team effort to improve one process")], "d"),
        ("What does a value stream map show?",
         [("a", "The paint colours"), ("b", "Every step from raw material to customer, with times"), ("c", "The staff's pay"), ("d", "The weather")], "b"),
        ("Why does stock cost money?",
         [("a", "It ties up cash, takes space and hides problems"), ("b", "It is free to keep"), ("c", "It grows in value on the shelf"), ("d", "It makes the shop smaller on purpose")], "a"),
    ],
}
