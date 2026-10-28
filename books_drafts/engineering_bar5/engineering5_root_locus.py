"""Root Locus Design: how the closed-loop poles move as gain changes, how to aim for a damping target, and how a compensator reshapes the paths."""
CODE = "engineering5_root_locus"
BOOK = {
    "title": "Root Locus Design",
    "subtitle": "Following the closed-loop poles as the gain changes",
    "chapters": [
        ("Poles and the loop", "The poles of a closed loop decide how it responds. They move as the gain changes. A root locus is the plot of where those poles go as the gain rises from zero toward infinity."),
        ("Reading the locus", "The paths start at the open-loop poles and end at the open-loop zeros or at infinity. Poles on the left half of the plane give stable behaviour. A path that crosses into the right half means instability at that gain."),
        ("Damping targets", "Engineers often set a target damping ratio, which controls how much overshoot a step response shows. A line of constant damping ratio can be drawn on the plot. The gain where the locus meets that line gives the desired damping."),
        ("Compensator placement", "A compensator adds poles and zeros to the loop, which changes the shape of the locus. A zero placed to pull the paths left can add damping. The designer chooses where the new poles and zeros go, and checks the new plot."),
        ("Limits of the picture", "The locus shows the closed-loop poles, but not the zeros of the closed loop or the input effects. Engineers check the full response with a simulation after reading the plot. The plot guides the design but does not finish it."),
        ("Practical design", "Root locus design is quick to try by hand, and modern software draws it in a moment. It works well for single-input, single-output loops. The result is a gain and a shape that a test can confirm."),
    ],
    "test": [
        ("What do the poles of a closed loop decide?", [("a", "The colour of the controller"), ("b", "The weight of the cabinet"), ("c", "How it responds"), ("d", "The name of the operator")], "c"),
        ("Where does a root locus path start?", [("a", "At the open-loop poles"), ("b", "At the closed-loop zeros only"), ("c", "At the sensor"), ("d", "At the power supply")], "a"),
        ("What does a path that crosses into the right half of the plane mean?", [("a", "Perfect stability"), ("b", "A faster response with no risk"), ("c", "A broken label"), ("d", "Instability at that gain")], "d"),
        ("What does a target damping ratio control?", [("a", "The number of wires"), ("b", "How much overshoot a step response shows"), ("c", "The price of steel"), ("d", "The room colour")], "b"),
        ("Why must a root locus design be checked with a simulation?", [("a", "Because plots are always wrong"), ("b", "Because simulations are needed to draw the plot"), ("c", "Because gain never changes"), ("d", "Because the plot does not show the closed-loop zeros or the input effects")], "d"),
    ],
}
