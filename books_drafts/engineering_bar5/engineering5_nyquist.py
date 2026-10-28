"""Nyquist Stability Criterion: how a plot of a loop's frequency response shows whether a feedback system is stable, and how far it is from trouble."""
CODE = "engineering5_nyquist"
BOOK = {
    "title": "Nyquist Stability Criterion",
    "subtitle": "Reading stability from the path a loop traces on a plot",
    "chapters": [
        ("The idea", "The Nyquist criterion, named after Harry Nyquist, checks stability from the frequency response of the open loop. You draw the path the response traces as frequency rises. Where that path lies relative to a critical point tells you whether the closed loop is stable."),
        ("Encirclements", "An encirclement is when the path winds around the critical point at minus one. The number of times it winds, counted with direction, links to the number of unstable closed-loop poles. Zero net encirclements with no unstable open-loop poles means stability."),
        ("The Nyquist plot", "The plot is drawn for positive frequencies and then mirrored. It can be sketched from the gain and phase of each part. The plot shows the whole behaviour of the loop on one picture."),
        ("Gain and phase margins", "The gain margin is how far the gain can rise before the path reaches the critical point. The phase margin is how far the phase can slip at the frequency where the gain is one. Both are read directly from the plot."),
        ("The robustness reading", "A plot that passes far from the critical point is robust. Small changes in gain or lag will not cause instability. A plot that passes close to it warns the designer that the real machine may misbehave."),
        ("Practical use", "Nyquist plots can be measured on a real system, which makes them useful for checking models. They also help engineers compare designs side by side. A clear margin is the usual goal."),
    ],
    "test": [
        ("What does the Nyquist criterion use to check stability?", [("a", "The weight of the controller"), ("b", "The colour of the wires"), ("c", "The length of the cabinet"), ("d", "The frequency response of the open loop")], "d"),
        ("What is an encirclement?", [("a", "A ring of bolts"), ("b", "A fence around a machine"), ("c", "When the path winds around the critical point at minus one"), ("d", "A type of paint")], "c"),
        ("What is the gain margin?", [("a", "How far the gain can rise before the path reaches the critical point"), ("b", "The price of the gain board"), ("c", "The number of gain settings"), ("d", "The length of the test")], "a"),
        ("What does a plot passing far from the critical point show?", [("a", "A broken sensor"), ("b", "A paint fault"), ("c", "An unstable fuel line"), ("d", "A robust design")], "d"),
        ("Who is the criterion named after?", [("a", "Isaac Newton"), ("b", "Harry Nyquist"), ("c", "James Clerk Maxwell"), ("d", "Galileo Galilei")], "b"),
    ],
}
