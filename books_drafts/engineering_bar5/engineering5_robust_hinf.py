"""Robust Control and H-Infinity Design: designing a controller that still works when the real plant differs from the model, using norms and weighting functions."""
CODE = "engineering5_robust_hinf"
BOOK = {
    "title": "Robust Control and H-Infinity Design",
    "subtitle": "Designing for the gap between the model and the real machine",
    "chapters": [
        ("Why robustness matters", "A model is never exact. Parts wear, loads change and some effects are left out. A robust controller keeps working well across the range of plants it might face."),
        ("Uncertainty models", "Uncertainty is described as a set of possible plants around the nominal model. Engineers often describe it as a bounded multiplicative term at each frequency. The size of the bound grows where the model is least trusted."),
        ("Weighting functions", "Weighting functions express what matters at each frequency. A large weight at low frequency asks for good tracking there. A large weight at high frequency limits control effort and noise."),
        ("Norms and the H-infinity design", "The H-infinity norm is the largest gain of a system over all frequencies. The H-infinity design finds a controller that keeps this norm below a set bound. It gives a guaranteed worst-case performance across the uncertainty."),
        ("Mixed sensitivity", "In mixed sensitivity design, several weighted quantities are combined into one norm. These usually include the error, the control effort and the sensitivity to uncertainty. The designer adjusts the weights to balance them."),
        ("Performance margins", "A robust design reports margins that are checked by the norm bound. Engineers confirm that the margins remain above their target across all the uncertainty. A simulation and a test on the real plant confirm the result."),
    ],
    "test": [
        ("Why is a robust controller needed?", [("a", "Because controllers need paint"), ("b", "Because sensors are always wrong"), ("c", "Because no model is ever written"), ("d", "Because the model is never exact and the real machine differs")], "d"),
        ("What do weighting functions express?", [("a", "The price of parts"), ("b", "What matters at each frequency"), ("c", "The order of a meal"), ("d", "The colour of the room")], "b"),
        ("What is the H-infinity norm?", [("a", "The average weight of the parts"), ("b", "The number of sensors"), ("c", "The length of a cable"), ("d", "The largest gain of a system over all frequencies")], "d"),
        ("What does mixed sensitivity combine?", [("a", "Two paint colours"), ("b", "Two shift times"), ("c", "Several weighted quantities into one norm"), ("d", "Two bus routes")], "c"),
        ("What does an H-infinity design guarantee?", [("a", "A worst-case performance across the uncertainty, within a set bound"), ("b", "That the machine never fails at all"), ("c", "That the price falls"), ("d", "That no test is needed")], "a"),
    ],
}
