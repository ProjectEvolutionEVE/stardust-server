"""Bode Plots and Frequency-Domain Design: how to read gain and phase against frequency, sketch the plots quickly, and read the margins that show how safe a loop is."""
CODE = "engineering5_bode"
BOOK = {
    "title": "Bode Plots and Frequency-Domain Design",
    "subtitle": "Reading gain and phase against frequency to shape a control loop",
    "chapters": [
        ("Two plots", "A Bode plot shows two curves against frequency, plotted on a logarithmic scale. One is the gain, in decibels. The other is the phase, in degrees. Together they describe how a system responds to sine waves of every frequency."),
        ("Asymptotes", "Each simple part of a system has straight-line approximations on a Bode plot. A pole bends the gain down past its corner frequency. A zero bends it up. Adding the parts gives a quick sketch of the whole system."),
        ("Closed-loop bandwidth", "The bandwidth of a closed loop is the frequency where its response falls to about 70 percent of its low-frequency value, or 3 decibels down. A wider bandwidth means a faster response. It usually costs stability margin."),
        ("Loop shaping", "Loop shaping means changing the open-loop gain and phase to get the response you want. Engineers raise gain at low frequency for accuracy and reduce it at high frequency to resist noise. The plot shows the effect of each change."),
        ("Reading the margins", "The gain margin is how much gain can rise before the loop becomes unstable. The phase margin is how much extra phase lag the loop can take before instability. Good designs keep both margins comfortably positive."),
        ("A practical view", "Bode plots are easy to measure on a real machine by sending sine waves and recording the response. They connect theory to tests. Engineers use them to tune controllers on site."),
    ],
    "test": [
        ("What are the two curves on a Bode plot?", [("a", "Price and weight"), ("b", "Gain in decibels and phase in degrees"), ("c", "Speed and colour"), ("d", "Length and width")], "b"),
        ("What does a pole do to the gain curve past its corner frequency?", [("a", "It bends the gain up"), ("b", "It removes the gain"), ("c", "It turns the plot into a circle"), ("d", "It bends the gain down")], "d"),
        ("What is the usual meaning of closed-loop bandwidth?", [("a", "The number of wires"), ("b", "The width of the road"), ("c", "The frequency where the response falls about 3 decibels below its low-frequency value"), ("d", "The cost of the controller")], "c"),
        ("What does phase margin tell you?", [("a", "How much extra phase lag the loop can take before instability"), ("b", "The colour of the plot"), ("c", "The number of sensors"), ("d", "The length of the test")], "a"),
        ("Why are Bode plots easy to use on a real machine?", [("a", "They need no measurements"), ("b", "They work only on paper"), ("c", "They replace all sensors"), ("d", "Sine waves can be sent and the response recorded")], "d"),
    ],
}
