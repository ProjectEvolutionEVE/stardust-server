"""Pole Placement and Observers: choosing where a closed loop's poles sit, using the Ackermann formula, and estimating hidden states with an observer."""
CODE = "engineering5_pole_place"
BOOK = {
    "title": "Pole Placement and Observers",
    "subtitle": "Setting the closed-loop poles directly, and estimating the states you cannot measure",
    "chapters": [
        ("Choosing the poles", "Pole placement sets the closed-loop poles where the designer wants them. The poles decide the speed and damping of the response. A controllable system can always be given any set of poles, in principle."),
        ("The Ackermann formula", "For a single-input system, the Ackermann formula gives the feedback gain that places the poles. It uses the desired characteristic polynomial and the controllability matrix. It is exact for small systems but can be badly conditioned for large ones."),
        ("Why state estimates are needed", "Often not every state can be measured. Position may be sensed, but velocity may not. The controller then needs an estimate of the missing states."),
        ("State observers", "A state observer is a model of the system that runs alongside the real one. It is corrected by the difference between the measured and predicted outputs. Its estimated states feed the feedback law."),
        ("The separation principle", "For linear systems, the separation principle says the controller and the observer can be designed separately. The closed loop then has the controller poles and the observer poles together. This makes the design simpler."),
        ("Sensor noise", "Measurements carry noise, and an observer that reacts fast also passes noise through. Engineers balance a fast observer against a noisy estimate. The choice is checked in simulation with realistic noise."),
    ],
    "test": [
        ("What do the closed-loop poles decide?", [("a", "The colour of the panel"), ("b", "The name of the test"), ("c", "The size of the box"), ("d", "The speed and damping of the response")], "d"),
        ("What does the Ackermann formula give for a single-input system?", [("a", "The price of the sensor"), ("b", "The time of day"), ("c", "The feedback gain that places the poles"), ("d", "The number of bolts")], "c"),
        ("What is a state observer?", [("a", "A model running alongside the real system, corrected by the measured output"), ("b", "A person who watches the machine"), ("c", "A type of motor"), ("d", "A kind of valve")], "a"),
        ("What does the separation principle allow?", [("a", "The controller to be ignored"), ("b", "The observer to be removed"), ("c", "Only one pole to be used"), ("d", "The controller and observer to be designed separately")], "d"),
        ("What is the trade-off with a fast observer?", [("a", "It makes the machine heavier"), ("b", "It passes more sensor noise through to the estimate"), ("c", "It stops all feedback"), ("d", "It changes the room colour")], "b"),
    ],
}
