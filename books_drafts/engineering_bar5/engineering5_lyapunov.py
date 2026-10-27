"""Lyapunov Stability Methods: proving a system is stable by finding an energy-like function that never grows and falls toward the equilibrium."""
CODE = "engineering5_lyapunov"
BOOK = {
    "title": "Lyapunov Stability Methods",
    "subtitle": "Proving stability with an energy-like function instead of solving the motion",
    "chapters": [
        ("The idea", "Lyapunov's method proves stability without solving the equations of motion. It uses a scalar function of the state, called a Lyapunov function, that behaves like an energy. If that energy keeps falling, the system settles to rest."),
        ("Positive definiteness", "A Lyapunov function must be positive, zero only at the equilibrium and positive everywhere else. This is called positive definiteness. It means the function acts like a bowl with its bottom at the equilibrium."),
        ("A decreasing derivative", "The derivative of the function along the motion must be negative, or zero only at the equilibrium. Then the function falls over time, and the state moves down the bowl toward the bottom. This is the core test."),
        ("Stability proofs", "If both conditions hold, the equilibrium is asymptotically stable. If only the derivative is non-positive, the equilibrium is stable but may not be reached. Engineers choose the level of proof the design needs."),
        ("Finding the function", "There is no single recipe. For mechanical systems, the total energy is often a good start. For linear systems, a quadratic function and a matrix equation give a systematic route."),
        ("Why it is useful", "Lyapunov methods handle nonlinear and adaptive systems, where simple tests fail. They give a way to prove that a design is safe for all starting points within a region. Designers still check the proof against simulations."),
    ],
    "test": [
        ("What does a Lyapunov function behave like?", [("a", "A price list"), ("b", "A calendar"), ("c", "A map of rivers"), ("d", "An energy")], "d"),
        ("What must a Lyapunov function be, away from the equilibrium?", [("a", "Negative only"), ("b", "Zero everywhere"), ("c", "Positive"), ("d", "Infinite everywhere")], "c"),
        ("What must its derivative along the motion do?", [("a", "Fall, or stay non-positive"), ("b", "Grow without limit"), ("c", "Oscillate with no end"), ("d", "Stay exactly fixed for all time")], "a"),
        ("What is a good starting function for a mechanical system?", [("a", "The price of the parts"), ("b", "The shape of the room"), ("c", "The name of the operator"), ("d", "The total energy")], "d"),
        ("Why is Lyapunov's method useful?", [("a", "It replaces every test on the real machine"), ("b", "It proves stability for nonlinear and adaptive systems where simple tests fail"), ("c", "It makes all systems stable"), ("d", "It removes the need for models")], "b"),
    ],
}
