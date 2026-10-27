"""Linear Quadratic Regulators: choosing a feedback gain by minimising a cost on state error and effort, through the Riccati equation, with its known margins."""
CODE = "engineering5_lqr"
BOOK = {
    "title": "Linear Quadratic Regulators",
    "subtitle": "Choosing feedback by weighing error against effort",
    "chapters": [
        ("The cost", "A linear quadratic regulator picks the feedback that minimises a cost. The cost adds up the squared state errors and the squared control effort over time. Big errors and big control moves both count against the design."),
        ("The Riccati equation", "The best feedback gain comes from solving the algebraic Riccati equation for a matrix. It is a quadratic matrix equation with a unique stabilising solution under standard conditions. Computer routines solve it quickly."),
        ("Weighting choices", "The designer chooses weighting matrices, Q for the states and R for the control. A larger Q makes the system track its target more tightly. A larger R makes the controller more gentle. The choice is the main design decision."),
        ("Margins", "An LQR design has good robustness. For a single input it guarantees a gain margin from half to infinity, and a phase margin of at least 60 degrees. These margins are a major reason the method is trusted."),
        ("Tuning in practice", "Engineers start with simple weights, simulate the response and adjust. They check the control effort against the actuator limits. A tuned design balances speed, effort and noise."),
        ("What it does not cover", "The standard LQR assumes the full state is measured and the model is linear. Real systems need an observer and may need constraints. Other methods handle these cases, so the designer must know the limits."),
    ],
    "test": [
        ("What does an LQR minimise?", [("a", "The price of the machine"), ("b", "A cost on state errors and control effort"), ("c", "The number of cables"), ("d", "The colour of the sensor")], "b"),
        ("Which equation gives the best feedback gain?", [("a", "The price list"), ("b", "The calendar"), ("c", "The alphabet"), ("d", "The algebraic Riccati equation")], "d"),
        ("What do the weighting matrices Q and R set?", [("a", "The paint colour"), ("b", "The room size"), ("c", "The trade-off between tracking the target and control effort"), ("d", "The power bill")], "c"),
        ("What gain margin does a single-input LQR guarantee, from the book's list?", [("a", "From half to infinity"), ("b", "Exactly zero"), ("c", "Only one tenth"), ("d", "Exactly two")], "a"),
        ("What does the standard LQR assume about the state?", [("a", "That the state is never measured"), ("b", "That the model is random"), ("c", "That the system has no inputs"), ("d", "That the full state is measured and the model is linear")], "d"),
    ],
}
