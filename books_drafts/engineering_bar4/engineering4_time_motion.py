"""Time and Motion Studies: timing the work fairly to set a standard, and checking the result."""
CODE = 'engineering4_time_motion'
BOOK = {
    "title": "Time and Motion Studies",
    "subtitle": "Timing the work fairly to set a standard, and checking the result",
    "chapters": [
        ("Timing elements",
         "A task is split into elements, and each element is timed separately. Elements make it easier to see where the time goes and which part of the job can be improved."),
        ("Standard time",
         "Standard time is the time a trained worker should take, working at a normal pace, to do the task. It is based on many observations, not on one lucky or unlucky run."),
        ("Allowances",
         "Allowances add time for rest, personal needs and unavoidable delays. Without them the standard is unrealistic and the work cannot be done at that pace."),
        ("Job design",
         "Good job design removes unnecessary motion and puts tools within easy reach. This makes the work safer and quicker, and it is less tiring."),
        ("Fairness to workers",
         "Workers must know about the study and be treated fairly by it. A standard set unfairly harms morale and quality, and it is hard to recover from."),
        ("Checking results",
         "Compare the standard against real output over time. A large gap between them means the study needs a second look."),
    ],
    "test": [
        ("What is a timing element?",
         [("a", "A chemical"), ("b", "A metal"), ("c", "A part of a task that is timed separately"), ("d", "A light")], "c"),
        ("What is standard time?",
         [("a", "The time of the lunch break"), ("b", "The time a trained worker should take at a normal pace"), ("c", "The time it takes to paint"), ("d", "The length of the shift")], "b"),
        ("What do allowances cover?",
         [("a", "The price of tools"), ("b", "Paint"), ("c", "The colour of the walls"), ("d", "Rest, personal needs and unavoidable delays")], "d"),
        ("What does good job design do?",
         [("a", "Removes unneeded motion and puts tools in easy reach"), ("b", "Adds more steps"), ("c", "Hides the tools"), ("d", "Makes the work harder")], "a"),
        ("What does a large gap between standard and real output suggest?",
         [("a", "The study is perfect"), ("b", "The factory is closed"), ("c", "The study needs a second look"), ("d", "The workers are idle")], "c"),
    ],
}
