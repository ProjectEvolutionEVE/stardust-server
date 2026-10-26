"""The After Action Review: a simple four-question review that learns from what happened without blame."""
CODE = 'flight4_aar'
BOOK = {
    "title": "The After Action Review",
    "subtitle": "Four questions, honest facts and lessons that get acted on",
    "chapters": [
        ("Where it began",
         "The after action review began in the United States Army. Units learned to look back on training and missions, to see what worked and what did not, without pointing fingers."),
        ("Four questions",
         "The review asks four simple questions. What was supposed to happen? What actually happened? Why was there a difference? What can we learn and do next time?"),
        ("Honest facts",
         "A good review starts with facts, not stories. Everyone brings what they saw, and the team agrees on what the record shows before deciding what it means."),
        ("Learning, not blame",
         "The goal is to learn, not to blame. People speak more freely when they know the review will focus on the process and on what can be improved."),
        ("Documenting",
         "Write the lessons down clearly, and share them with the team and with others who will need them. A lesson kept in one person's head is easily lost."),
        ("Follow-through",
         "A review is only worth it if someone acts on it. Give each lesson an owner and a date, then check that it has been done."),
    ],
    "test": [
        ("Where did the after action review start?",
         [("a", "The United States Army"), ("b", "The Navy"), ("c", "A hospital"), ("d", "A film studio")], "a"),
        ("How many simple questions does the review ask?",
         [("a", "Two"), ("b", "Three"), ("c", "Four"), ("d", "Ten")], "c"),
        ("What is the goal of the review?",
         [("a", "Punishment"), ("b", "Silence"), ("c", "Blame"), ("d", "Learning")], "d"),
        ("What does a good review start with?",
         [("a", "Guesses"), ("b", "Rumours"), ("c", "Stories"), ("d", "Facts")], "d"),
        ("What makes a lesson useful?",
         [("a", "An owner and a date to act on it"), ("b", "Hiding it"), ("c", "Forgetting it"), ("d", "Keeping it in one head")], "a"),
    ],
}
