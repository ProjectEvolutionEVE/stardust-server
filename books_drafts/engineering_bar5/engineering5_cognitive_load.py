"""Cognitive Load in Control Rooms: workload measures, situation awareness, task design, interface layout and error reduction."""
CODE = "engineering5_cognitive_load"
BOOK = {
    "title": "Cognitive Load in Control Rooms",
    "subtitle": "How much a person can hold in mind, and how to design for it",
    "chapters": [
        ("Mental workload",
         "Workload is the mental and physical effort needed to do a job. In a control room, operators watch many displays and make decisions quickly. Too little workload leads to boredom, and too much leads to errors."),
        ("Measuring workload",
         "Engineers measure workload with questionnaires, task timing, and measures of the operator's performance. Some methods also watch how the operator's attention shifts. No single measure tells the whole story."),
        ("Situation awareness",
         "Situation awareness means knowing what is happening, what it means, and what will happen next. It has three levels: noticing the facts, understanding them, and predicting the future. Good design supports all three levels."),
        ("Task design",
         "Task design shapes the work so it matches what people can perceive and do. Tasks should be clear, in a sensible order, and not overloaded at peak times. Good task design spreads the work across the shift."),
        ("Interface layout",
         "Good layout puts the most important information where it is easy to find. Related items sit together, and colours and shapes are used with care. A poor layout makes operators search for the facts they need."),
        ("Reducing error",
         "Most control-room errors come from overload, confusion or missing information. Reducing workload and improving layout lowers the error rate. Designers also add checks and clear feedback so mistakes are caught early."),
    ],
    "test": [
        ("What is workload in a control room?",
         [("a", "The paint on the floor"), ("b", "The noise of printers"), ("c", "The lunch rota"), ("d", "The mental and physical effort needed to do the job")], "d"),
        ("What is situation awareness?",
         [("a", "Being aware of paint"), ("b", "Knowing what is happening, what it means and what will happen next"), ("c", "Knowing the price"), ("d", "A camera")], "b"),
        ("What does good interface layout help with?",
         [("a", "Finding information quickly and avoiding mistakes"), ("b", "Painting the screens"), ("c", "Making screens heavy"), ("d", "Hiding alarms")], "a"),
        ("What is the purpose of task design?",
         [("a", "To paint tasks"), ("b", "To give tasks lunch breaks only"), ("c", "To shape work so it matches what people can perceive and do"), ("d", "To hide tasks")], "c"),
        ("How does workload relate to error?",
         [("a", "Errors are good"), ("b", "Errors need more paint"), ("c", "Errors cost nothing"), ("d", "Overload tends to raise errors, and good design tends to reduce them")], "d"),
    ],
}
