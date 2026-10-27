"""Damping Identification from Test Data: how to measure how quickly a structure's vibration dies away, using the logarithmic decrement and the half-power bandwidth."""
CODE = "engineering5_damping_id"
BOOK = {
    "title": "Damping Identification from Test Data",
    "subtitle": "Measuring how quickly vibration dies away, from real test records",
    "chapters": [
        ("Why damping matters", "Damping is what makes vibration die away. It limits the peak response at resonance and affects how long a structure rings after a knock. Designers need a good number for it, and tests give the best one."),
        ("The logarithmic decrement", "If you ring a system and record two peaks one cycle apart, the logarithmic decrement is the natural log of their ratio. For light damping it equals two pi times the damping ratio. The method is simple and needs only a clean decaying record."),
        ("The half-power bandwidth", "In a frequency sweep, the half-power bandwidth is the width of the peak at a level 3 decibels below its top. The damping ratio is about the bandwidth divided by twice the natural frequency. This works well for lightly to moderately damped modes."),
        ("Curve fitting", "A better way is to fit a decaying curve to the whole record. The fit gives the frequency and damping together, and it averages out noise. Engineers check the fit by plotting the curve over the data."),
        ("Where damping comes from", "Damping comes from friction in joints, air resistance, material losses and added dampers. A structure's damping often differs from the design estimate. Testing reveals the true value."),
        ("Careful testing", "Good damping tests use a clean input, low noise and enough cycles to fit. Nonlinear behaviour can make the answer depend on the size of the test. Engineers report the test level with every number."),
    ],
    "test": [
        ("What does damping control?", [("a", "How quickly vibration dies away"), ("b", "The colour of a surface"), ("c", "The price of steel"), ("d", "The number of doors")], "a"),
        ("How is the logarithmic decrement found?", [("a", "From the weight of the structure"), ("b", "From the room temperature"), ("c", "From the number of bolts"), ("d", "From the natural log of the ratio of two peaks one cycle apart")], "d"),
        ("What is the half-power bandwidth measured at?", [("a", "The top of the peak"), ("b", "A level 3 decibels below the peak"), ("c", "Zero hertz"), ("d", "Ten times the peak")], "b"),
        ("What is a better method than counting peaks, according to this book?", [("a", "Guessing from the colour"), ("b", "Ignoring the record"), ("c", "Weighing the structure"), ("d", "Fitting a decaying curve to the whole record")], "d"),
        ("Why should a damping test report the test level?", [("a", "Because the level sets the colour of the report"), ("b", "Because no one reads the number"), ("c", "Because nonlinear behaviour can make the answer depend on the size of the test"), ("d", "Because damping never changes")], "c"),
    ],
}
