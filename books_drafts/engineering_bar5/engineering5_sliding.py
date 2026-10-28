"""Sliding Mode Control: forcing a system onto a chosen surface with a switching law, the chattering problem, and the boundary layer used to soften it."""
CODE = "engineering5_sliding"
BOOK = {
    "title": "Sliding Mode Control",
    "subtitle": "Forcing a system onto a chosen surface, and taming the chatter",
    "chapters": [
        ("The switching surface", "Sliding mode control defines a surface in the state space, called the switching surface. The controller drives the state onto this surface and keeps it there. Once on the surface, the motion follows a simpler, chosen behaviour."),
        ("The switching law", "The control switches between two values, depending on which side of the surface the state lies. This strong switching is what keeps the state on the surface, even when the model is uncertain."),
        ("Chattering", "Ideal switching at high speed causes chattering, a rapid buzz in the control and the output. Chattering wears actuators and excites unmodelled resonances. It is the main practical problem of the method."),
        ("Equivalent control", "On the surface, the average control that keeps the state there is called the equivalent control. It can be found from the model. The switching term only has to cover the uncertainty, which keeps the switching small."),
        ("The boundary layer", "A boundary layer replaces the sharp switch with a smooth function near the surface. The chatter is reduced, but the state now stays only near the surface. The width of the layer sets the trade-off between smoothness and accuracy."),
        ("Robustness", "Once on the surface, the motion is robust to matched uncertainties, such as unknown loads at the input. This is the main appeal of the method. Engineers still test it on the real machine to check the chattering level."),
    ],
    "test": [
        ("What is the switching surface?", [("a", "A painted panel on the wall"), ("b", "A surface in the state space that the controller drives the state onto"), ("c", "A screen for the operator"), ("d", "A bolt head")], "b"),
        ("What is chattering?", [("a", "A type of conversation"), ("b", "A slow drift"), ("c", "A calm hum"), ("d", "A rapid buzz in the control and output from ideal switching")], "d"),
        ("What is equivalent control?", [("a", "Two controllers with the same colour"), ("b", "A backup power supply"), ("c", "The average control that keeps the state on the surface"), ("d", "A type of cable")], "c"),
        ("What does a boundary layer do?", [("a", "Replaces the sharp switch with a smooth function near the surface"), ("b", "Removes the surface"), ("c", "Adds weight to the machine"), ("d", "Stops all sensors")], "a"),
        ("What is the main appeal of sliding mode control?", [("a", "Low cost in every case"), ("b", "No need for any model at all"), ("c", "No need for testing"), ("d", "Robustness to matched uncertainties once on the surface")], "d"),
    ],
}
