"""State-Space Models of Machines: describing a machine by its states, inputs and outputs in matrix form, and checking whether it can be steered and observed."""
CODE = "engineering5_state_space"
BOOK = {
    "title": "State-Space Models of Machines",
    "subtitle": "Describing a machine by its states, inputs and outputs in matrix form",
    "chapters": [
        ("The state", "The state of a machine is the smallest set of values that, together with the inputs, fixes its future motion. Positions and velocities are common states. The state is written as a vector of numbers."),
        ("Inputs and outputs", "Inputs are the things we can change, such as a motor voltage. Outputs are the things we measure, such as a position or a speed. The model links them to the states."),
        ("The matrices", "A linear state-space model has four matrices, called A, B, C and D. A describes how the states change on their own, B how the inputs act, C how the outputs read the states, and D how inputs reach outputs directly. Together they describe the whole linear system."),
        ("Controllability", "A system is controllable if its inputs can move the state to any target in finite time. A test uses a matrix built from A and B. If the test fails, some part of the machine cannot be steered."),
        ("Observability", "A system is observable if its outputs reveal the whole state over time. A test uses a matrix built from A and C. If the test fails, some part of the state is hidden from the sensors."),
        ("From transfer functions", "A transfer function, which relates input to output in frequency, can be turned into a state-space model. There are several standard forms. The state-space form is the one used for modern design and for computer simulation."),
    ],
    "test": [
        ("What is the state of a machine?", [("a", "The paint on its cover"), ("b", "The name of its maker"), ("c", "The price in the catalogue"), ("d", "The smallest set of values that with the inputs fixes its future motion")], "d"),
        ("How many matrices does a linear state-space model have?", [("a", "One"), ("b", "Four, called A, B, C and D"), ("c", "Two"), ("d", "Ten")], "b"),
        ("What does a system need to be controllable?", [("a", "A new colour"), ("b", "No inputs at all"), ("c", "A bigger room"), ("d", "Its inputs can move the state to any target in finite time")], "d"),
        ("What does observability ask?", [("a", "Whether the machine can be seen"), ("b", "Whether the paint is dry"), ("c", "Whether the outputs reveal the whole state over time"), ("d", "Whether the sensor is new")], "c"),
        ("What can a transfer function be turned into?", [("a", "A state-space model"), ("b", "A paint colour"), ("c", "A bill of materials"), ("d", "A map of the coast")], "a"),
    ],
}
