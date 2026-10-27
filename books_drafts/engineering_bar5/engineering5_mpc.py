"""Model Predictive Control: how a controller predicts the future over a horizon, solves an optimisation at each step, and respects limits, with industrial uses."""
CODE = "engineering5_mpc"
BOOK = {
    "title": "Model Predictive Control",
    "subtitle": "Looking ahead, solving for the best moves, and respecting the limits",
    "chapters": [
        ("The idea", "Model predictive control uses a model of the process to predict its future behaviour. At each step it works out the best sequence of control moves over a short look-ahead. It then applies only the first move and repeats the whole calculation at the next step."),
        ("The prediction horizon", "The prediction horizon is how far ahead the controller looks. A longer horizon sees problems earlier, but needs more calculation. The choice is a balance between foresight and computing time."),
        ("Constraints", "A key strength of MPC is that it can respect limits directly. Valve openings, motor torques, temperatures and pressures can all be kept inside bounds. The optimiser only picks moves that are allowed."),
        ("Computation time", "Each step solves an optimisation problem, which takes time. The problem must be solved within one sampling interval. Engineers choose a model size and horizon that the computer can handle in real time."),
        ("Industrial uses", "MPC is widely used in chemical plants, refineries and paper mills. It handles many inputs and outputs with limits at the same time. Its use in these plants is one of the main success stories of modern control."),
        ("Keeping it reliable", "The controller is only as good as its model. Engineers check the model against plant data and add safe fallbacks. If the optimiser fails, a simpler controller takes over."),
    ],
    "test": [
        ("What does a model predictive controller use to look ahead?", [("a", "A weather report"), ("b", "A shopping list"), ("c", "A model of the process to predict its future behaviour"), ("d", "A calendar of holidays")], "c"),
        ("What does the controller apply at each step?", [("a", "Only the first move of the best sequence"), ("b", "Every move at once forever"), ("c", "No move at all"), ("d", "A random move")], "a"),
        ("What is a strength of MPC?", [("a", "It needs no model at all"), ("b", "It works only in the dark"), ("c", "It removes the need for sensors"), ("d", "It can keep limits on valves, torques and temperatures")], "d"),
        ("What must the optimisation do within each step?", [("a", "Take a whole day"), ("b", "Finish inside one sampling interval"), ("c", "Wait for the next year"), ("d", "Print a report")], "b"),
        ("Where is MPC widely used?", [("a", "In paintings only"), ("b", "In musical instruments"), ("c", "In garden sheds"), ("d", "In chemical plants, refineries and paper mills")], "d"),
    ],
}
