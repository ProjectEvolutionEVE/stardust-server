"""Feedback Linearisation of Nonlinear Systems: changing coordinates and inputs so a nonlinear machine behaves like a linear one, with zero dynamics and the limits of the method."""
CODE = "engineering5_feedback_lin"
BOOK = {
    "title": "Feedback Linearisation of Nonlinear Systems",
    "subtitle": "Cancelling the nonlinearity with a clever input, and knowing where it stops working",
    "chapters": [
        ("The idea", "Feedback linearisation changes the coordinates and the input of a nonlinear system so that, in the new view, it looks linear. A linear controller can then be used. The method cancels nonlinear terms rather than ignoring them."),
        ("Coordinate change", "A change of coordinates gives new state variables that make the structure clear. Some of these new states are outputs and their derivatives. The change must be one-to-one so that no information is lost."),
        ("Relative degree", "The relative degree is the number of times the output must be differentiated before the input appears. It sets how many states the input can directly control. A system with full relative degree can be linearised completely."),
        ("Zero dynamics", "Some states are not affected by the feedback. Their behaviour is the zero dynamics. If the zero dynamics are stable, the method works well. If they are unstable, the design can fail even when the output looks fine."),
        ("Limits of the method", "The method depends on an accurate model, because it cancels the real nonlinear terms. Errors in the model leave residual nonlinearity. Large uncertainty also makes the cancellation poor."),
        ("Practical use", "Engineers use the method for robot arms and some aircraft controls, often together with a robust outer loop. They check the zero dynamics and test with realistic uncertainty. The linear view makes the outer design easier."),
    ],
    "test": [
        ("What does feedback linearisation do?", [("a", "Makes the system heavier"), ("b", "Removes all sensors"), ("c", "Changes coordinates and input so a nonlinear system looks linear"), ("d", "Turns a machine into paper")], "c"),
        ("What is the relative degree?", [("a", "How many times the output must be differentiated before the input appears"), ("b", "The colour of the controller"), ("c", "The number of workers"), ("d", "The price of the model")], "a"),
        ("What are zero dynamics?", [("a", "A stopped machine"), ("b", "A test with no data"), ("c", "An empty file"), ("d", "The states the feedback does not affect")], "d"),
        ("What happens if the zero dynamics are unstable?", [("a", "The design always works better"), ("b", "The design can fail even when the output looks fine"), ("c", "The sensors turn off"), ("d", "Nothing changes at all")], "b"),
        ("What is a main limit of feedback linearisation?", [("a", "It works with no model at all"), ("b", "It cannot be used on any machine"), ("c", "It needs no computer"), ("d", "It depends on an accurate model to cancel the nonlinear terms")], "d"),
    ],
}
