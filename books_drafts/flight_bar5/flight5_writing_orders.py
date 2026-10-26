"""Writing Clear Orders: stating intent, who acts, what is needed, when, why it matters, and checking that the order was understood."""
CODE = "flight5_writing_orders"
BOOK = {
    "title": "Writing Clear Orders",
    "subtitle": "Say the intent, the who, the what, the when, and check it was understood",
    "chapters": [
        ("Intent",
         "An order starts with the intent: what the captain wants to achieve. A clear intent lets the crew adapt if the plan changes. It answers the question what are we trying to do."),
        ("Who",
         "An order should say who is to act. A vague order like someone should check the valves leaves no one clear on the task. Name the person or team."),
        ("What",
         "State the task in plain words, with the result that is needed. Use short sentences and no jargon the crew may not know. A clear task is easier to carry out correctly."),
        ("When",
         "Give a time or a clear trigger for the task. A deadline keeps the work moving. Without a time, orders drift and the job slips."),
        ("Why",
         "A short reason helps people understand the order and make better choices on the way. The why guards against errors when things change. People act more wisely when they know the purpose."),
        ("Check understanding",
         "Ask the person to say the order back in their own words. This shows whether the message was heard as intended. A quick check at the start prevents costly mistakes later."),
    ],
    "test": [
        ("What should an order start with?",
         [("a", "A joke"), ("b", "A list of menus"), ("c", "The intent: what the captain wants to achieve"), ("d", "A weather report")], "c"),
        ("Why name who is to act?",
         [("a", "So the task has a clear owner"), ("b", "So nobody has to do it"), ("c", "So the order can be hidden"), ("d", "So the captain can leave")], "a"),
        ("Why give a time for a task?",
         [("a", "So the crew can sleep longer"), ("b", "So the work keeps moving"), ("c", "So orders can be ignored"), ("d", "So the plan is forgotten")], "b"),
        ("What does the reason in an order help with?",
         [("a", "Hiding the purpose"), ("b", "Making orders longer"), ("c", "Ending the job"), ("d", "Better choices when things change")], "d"),
        ("How do you check an order was understood?",
         [("a", "Assume it was heard"), ("b", "Post it on a wall and leave"), ("c", "Ask the person to say it back in their own words"), ("d", "Wait until it fails")], "c"),
    ],
}
