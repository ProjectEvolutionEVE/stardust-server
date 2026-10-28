"""Adaptive Control: Learning the Plant: how a controller estimates unknown parameters while it runs, the stability conditions it needs, and how adaptive systems can fail."""
CODE = "engineering5_adaptive"
BOOK = {
    "title": "Adaptive Control: Learning the Plant",
    "subtitle": "Controllers that estimate the machine while they work, and the conditions they need",
    "chapters": [
        ("Unknown plants", "Often the parameters of a machine are not known well, or they change with load, wear or temperature. An adaptive controller estimates them while it runs. It then adjusts its gains to match."),
        ("Parameter estimation", "The controller watches the input and output and fits the model parameters, often with a least squares or gradient method. The estimate improves as more data arrives. Good estimates depend on the input carrying enough information."),
        ("Model reference adaptive control", "In model reference adaptive control, the controller tries to make the plant follow a chosen reference model. The gap between the plant and the reference drives the adjustment of the gains. The reference model sets the desired behaviour."),
        ("Stability conditions", "Adaptive loops can be unstable even when each part seems sound. Proofs of stability use tools such as Lyapunov functions and need assumptions, such as bounded signals and slow changes in the plant. Engineers check these before relying on the design."),
        ("Failure cases", "A common failure is parameter drift, where estimates wander when the input is too quiet. Another is a sudden fault that the adaptive law reads wrongly. Protective limits and supervisors are added to catch these."),
        ("Good practice", "Engineers use adaptation to correct for slow changes, not to chase fast noise. They limit the rate of change of the estimates and test the controller with faults. Simple fixed controllers are kept as a backup."),
    ],
    "test": [
        ("What does an adaptive controller do with unknown parameters?", [("a", "Estimates them while it runs"), ("b", "Ignores them forever"), ("c", "Paints them"), ("d", "Sends them by post")], "a"),
        ("What does model reference adaptive control try to make the plant do?", [("a", "Stop moving"), ("b", "Change colour"), ("c", "Double its mass"), ("d", "Follow a chosen reference model")], "d"),
        ("What tools are often used to prove adaptive stability?", [("a", "Paint samples"), ("b", "Lyapunov functions"), ("c", "Recipe books"), ("d", "Bus timetables")], "b"),
        ("What is parameter drift?", [("a", "A boat moving across a lake"), ("b", "A type of wheel"), ("c", "A bolt coming loose"), ("d", "Estimates wandering when the input is too quiet")], "d"),
        ("What is a sensible safeguard for an adaptive controller?", [("a", "Remove all limits"), ("b", "Never test it"), ("c", "Keep a simple fixed controller as a backup"), ("d", "Adapt to fast noise on purpose")], "c"),
    ],
}
