"""Simulator Fidelity and Training Rigs: fidelity levels, transfer of training, scenario design, instructor roles and cost per training hour."""
CODE = "engineering5_sim_training"
BOOK = {
    "title": "Simulator Fidelity and Training Rigs",
    "subtitle": "How real a simulator must be to teach the real job",
    "chapters": [
        ("What a training rig is",
         "A training rig is a simulator that lets people practise a job safely before doing it for real. It can be a simple desk model or a full replica of a control room. Its value depends on how well it teaches the real task."),
        ("Fidelity levels",
         "Fidelity is how closely the simulator matches the real equipment and its behaviour. Low fidelity is cheap and good for learning basics. High fidelity costs much more and is needed when the real reactions must be learned exactly."),
        ("Transfer of training",
         "Transfer of training is how well skills learned in the simulator carry over to the real task. Good transfer means the trainee does better on the job. Designers test transfer by comparing trainees before and after training."),
        ("Scenario design",
         "A scenario is a planned exercise in the simulator, with a start, events and an end. Good scenarios have clear learning goals and realistic pressure. Scenarios are tested and refined with experienced staff."),
        ("Instructor roles",
         "The instructor sets up scenarios, guides the trainee, and watches how they perform. The instructor also stops the exercise to explain mistakes and to point out what went well. A good instructor makes the training feel safe but real."),
        ("Cost per training hour",
         "Cost per training hour compares the price of different training options fairly. It includes the rig, its upkeep, the instructor's time and the trainee's time. This figure helps a team choose the best mix of simulator and real practice."),
    ],
    "test": [
        ("What is simulator fidelity?",
         [("a", "The brightness of the paint"), ("b", "The loyalty of the crew"), ("c", "How closely the simulator matches the real equipment and behaviour"), ("d", "The price of the rig")], "c"),
        ("What is transfer of training?",
         [("a", "Skills learned in the simulator carry over to the real task"), ("b", "Moving the simulator house"), ("c", "Paint transfer"), ("d", "Money transfer")], "a"),
        ("What does an instructor do in a training rig?",
         [("a", "Paints the rig"), ("b", "Repairs the cables only"), ("c", "Sells tickets"), ("d", "Designs and runs scenarios and reviews performance")], "d"),
        ("Why is cost per training hour used?",
         [("a", "To choose paint"), ("b", "To compare the cost of different training options fairly"), ("c", "To set alarms"), ("d", "To count screws")], "b"),
        ("What matters most when designing a scenario?",
         [("a", "The colour of the rig"), ("b", "The shape of the chair"), ("c", "Its realism and learning goals"), ("d", "The lighting bulb")], "c"),
    ],
}
