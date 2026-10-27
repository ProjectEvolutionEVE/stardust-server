"""Laplace Transforms for Engineering Systems: turning differential equations into algebra, with transform pairs, the initial and final value theorems, and step responses."""
CODE = "engineering5_lt_transform"
BOOK = {
    "title": "Laplace Transforms for Engineering Systems",
    "subtitle": "Turning differential equations into algebra, and reading the answer from the poles",
    "chapters": [
        ("What the transform does", "The Laplace transform turns a function of time into a function of a complex variable s. Derivatives become multiplication by s, so differential equations become algebra. The answer is then turned back into time."),
        ("Transform pairs", "A table of transform pairs lists common functions with their transforms. A step, an exponential and a sine each have a known form. Engineers look up pairs rather than integrating each time."),
        ("The value theorems", "The initial value theorem gives the function at time zero from the transform. The final value theorem gives the steady value as time grows, when it exists. The final value theorem applies only to stable systems."),
        ("Poles and zeros", "The poles of the transform decide the modes of the response. Poles in the left half of the plane decay over time, and those on the right grow. Zeros shape the size and mix of the modes."),
        ("System step responses", "The response to a step input follows from the transfer function and the step's transform. The result shows rise time, overshoot and settling. Engineers read these directly from the pole positions."),
        ("Using the tool", "Laplace methods are fast for linear systems with constant coefficients. They also handle delays and piecewise inputs. Computer tools use the same ideas to draw and check responses."),
    ],
    "test": [
        ("What do derivatives become after a Laplace transform?", [("a", "Addition of colours"), ("b", "Multiplication by s"), ("c", "Division by the clock"), ("d", "Nothing at all")], "b"),
        ("What does the final value theorem give?", [("a", "The starting colour"), ("b", "The cost of the parts"), ("c", "The name of the test"), ("d", "The steady value as time grows, when it exists")], "d"),
        ("To which systems does the final value theorem apply?", [("a", "Only systems that are on fire"), ("b", "Systems with no inputs at all"), ("c", "Stable systems"), ("d", "Systems that have no poles")], "c"),
        ("What do poles in the left half of the plane do?", [("a", "Decay over time"), ("b", "Grow without limit"), ("c", "Turn the response into a square"), ("d", "Remove the input")], "a"),
        ("What can the step response show?", [("a", "The weight of the room"), ("b", "The number of doors"), ("c", "The name of the company"), ("d", "Rise time, overshoot and settling")], "d"),
    ],
}
