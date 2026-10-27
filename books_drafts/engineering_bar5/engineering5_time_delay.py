"""Time-Delay Systems in Control: how delays from sensors, networks and actuators add phase lag and limit stability, with the Smith predictor as one remedy."""
CODE = "engineering5_time_delay"
BOOK = {
    "title": "Time-Delay Systems in Control",
    "subtitle": "Why late information makes a control loop unstable, and how to deal with it",
    "chapters": [
        ("Where delays come from", "A control system measures, decides and acts, and each step takes time. Sensors filter their signals, networks carry data, and actuators respond slowly. Together these add a delay between a change and the controller's knowledge of it."),
        ("Phase lag", "A delay shifts the timing of a signal. At higher frequencies a given delay causes a larger phase lag. Phase lag works against the controller, because it makes corrections arrive too late."),
        ("Stability limits", "A feedback loop that is stable with no delay can become unstable with enough delay. The gain that can be used safely falls as the delay grows. Engineers calculate the largest safe gain for a given delay."),
        ("Oscillation from delay", "A loop with too much delay tends to overshoot and oscillate. The controller keeps correcting for an error it has already fixed. The result is a growing swing that can damage equipment."),
        ("The Smith predictor", "The Smith predictor, introduced by O. J. M. Smith in 1957, uses a model of the process to predict the output without the delay. The controller reacts to the prediction. This works well when the model is accurate."),
        ("Practical choices", "Engineers reduce delay where they can, by faster sensors and shorter links. They also lower the gain, or use predictive methods. Tests on the real loop confirm that the margins are enough."),
    ],
    "test": [
        ("Which of these is a source of delay in a control system?", [("a", "The colour of the controller"), ("b", "The weight of the cabinet"), ("c", "The name of the engineer"), ("d", "Sensors that filter signals")], "d"),
        ("What does a delay add at higher frequencies for a given delay?", [("a", "No change at all"), ("b", "A larger phase lag"), ("c", "A smaller phase lag"), ("d", "More light")], "b"),
        ("What happens to the safe gain as delay grows?", [("a", "It rises"), ("b", "It stays exactly the same"), ("c", "It becomes infinite"), ("d", "It falls")], "d"),
        ("What is the Smith predictor?", [("a", "A type of sensor"), ("b", "A paint for pipes"), ("c", "A method that predicts the output using a process model, without the delay"), ("d", "A kind of motor")], "c"),
        ("What is the main practical way to reduce delay problems?", [("a", "Use faster sensors and shorter links"), ("b", "Remove the feedback entirely"), ("c", "Make the loop slower to think"), ("d", "Add more delay on purpose")], "a"),
    ],
}
