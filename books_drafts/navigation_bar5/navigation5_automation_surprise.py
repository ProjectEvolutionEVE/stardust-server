"""Automation Surprises: mode confusion, trust, monitoring automated systems, design, accidents and training."""
CODE = "navigation5_automation_surprise"
BOOK = {
    "title": "Automation Surprises",
    "subtitle": "When the system does something the user did not expect",
    "chapters": [
        ("Mode confusion",
         "Mode confusion happens when a system is in a different mode from the one the user expects. The user then acts on a wrong picture of what the system will do. The result can be a surprise at the worst moment."),
        ("Trust",
         "People trust automation, and sometimes trust it too much. Trust is healthy when it matches the system's reliability, but excessive trust leads to complacency. Good users know a system's limits."),
        ("Monitoring",
         "Automation can make people less alert, so monitoring becomes harder. Operators must still check that the system is doing what they expect. Regular checks keep them in the loop."),
        ("Design",
         "Designers can reduce surprises by showing the current mode clearly and by making mode changes obvious. Simple logic is easier to understand. Feedback must come in time to be useful."),
        ("Accidents",
         "Several accidents in aviation and at sea have involved automation surprises. Investigators have found confusion about modes at key moments. Lessons from these accidents guide design."),
        ("Training",
         "Training teaches users how automated systems behave in every mode. Practice with surprises in simulators builds the habit of checking. Training makes automation a helper rather than a hidden risk."),
    ],
    "test": [
        ("What is mode confusion?",
         [("a", "A user thinking the system is in a different mode from the real one"), ("b", "A clock fault"), ("c", "A rough sea"), ("d", "A missing chart")], "a"),
        ("What can excessive trust lead to?",
         [("a", "Better sleep"), ("b", "Faster charts"), ("c", "More stars"), ("d", "Complacency")], "d"),
        ("What does automation make monitoring?",
         [("a", "Easier to forget"), ("b", "Harder"), ("c", "Unneeded"), ("d", "Faster")], "b"),
        ("How can designers reduce automation surprises?",
         [("a", "By hiding the current mode"), ("b", "By making feedback late"), ("c", "By showing the current mode clearly"), ("d", "By removing the displays")], "c"),
        ("What does training give users?",
         [("a", "Guessing"), ("b", "Practice with how the system behaves in each mode"), ("c", "New ships"), ("d", "Nothing")], "b"),
    ],
}
