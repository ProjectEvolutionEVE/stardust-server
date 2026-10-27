"""Measuring Team Health: using anonymous signals to spot problems early and act on them."""
CODE = "computing5_team_health"
BOOK = {
    "title": "Measuring Team Health",
    "subtitle": "Using anonymous signals to spot problems early and act on them",
    "chapters": [
        ("Health surveys",
         "A health survey asks a few short, regular, anonymous questions about workload, clarity and support. Keep it brief so people answer every time. Anonymity makes honest answers more likely."),
        ("Flow signals",
         "Flow signals show how work moves: how long tasks wait, how often they are interrupted, and how many are blocked. Rising waits often show a team is overloaded. These signals can be seen in the work itself."),
        ("Burnout indicators",
         "Watch for long hours, rising sick days, falling energy and less enjoyment of the work. Look at the trend over months, not one bad week. Early signs are much easier to act on than a crisis."),
        ("Response plans",
         "For each signal, decide what the team will change and who will act. A signal with no response teaches people that the survey is pointless. Tell the team what you did about the last results."),
        ("Privacy of data",
         "Never report on individuals. Show results only for groups large enough that no one can be identified. Explain clearly how the data is used and who sees it."),
        ("Trends",
         "Look for change over several months rather than one number. A single result can be noise, while a steady trend is a real signal. Compare trends across teams to spot patterns."),
    ],
    "test": [
        ("What should a health survey be?",
         [("a", "Short, regular and anonymous"), ("b", "Long, once, and named"), ("c", "Secret from the team"), ("d", "About lunch")], "a"),
        ("What are flow signals?",
         [("a", "River signals"), ("b", "Signals of how work moves, such as waiting and blocked tasks"), ("c", "Signs for the car park"), ("d", "Phone sounds")], "b"),
        ("Why look at trends rather than one number?",
         [("a", "One bad week may not mean a real problem"), ("b", "One number is always wrong"), ("c", "Trends never matter"), ("d", "Numbers never change")], "a"),
        ("What should privacy of health data mean?",
         [("a", "Reporting individuals by name"), ("b", "Only showing groups large enough that no one can be identified"), ("c", "Publishing everything"), ("d", "Sharing with the public")], "b"),
        ("What should a response plan name?",
         [("a", "Nothing"), ("b", "Only the weather"), ("c", "A fine"), ("d", "The change to make and who will act")], "d"),
    ],
}
