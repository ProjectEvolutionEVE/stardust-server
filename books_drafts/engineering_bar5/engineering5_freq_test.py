"""Frequency-Response Testing of Machines: exciting a machine with sine sweeps, checking coherence, and reading the results with care for estimation errors."""
CODE = "engineering5_freq_test"
BOOK = {
    "title": "Frequency-Response Testing of Machines",
    "subtitle": "Shaking a machine across its frequencies and reading how it answers",
    "chapters": [
        ("Sine sweeps", "A sine sweep drives the machine with a sine wave whose frequency rises slowly through a range. The response at each frequency gives the machine's frequency response. The method is clear and quick to run."),
        ("Excitation design", "The excitation must be strong enough to give a clear response, but not so strong that it damages the machine or drives it nonlinear. Engineers choose the sweep rate, range and amplitude with that balance in mind."),
        ("Coherence", "The coherence function runs from zero to one. A value near one means the output is caused by the input at that frequency. A low value warns of noise, nonlinearity or a poor measurement."),
        ("Estimation errors", "Random noise and leakage can bias the estimated response. Averaging several sweeps reduces random error. Good windowing reduces leakage from strong peaks."),
        ("Reading the results", "Peaks in the response show natural frequencies. The height and width of each peak show damping. A flat response shows the machine follows the input well at that range."),
        ("Checking the test", "Engineers repeat the test and compare results. They also check that the machine behaved the same way at both test levels. A test is only trusted once it passes these checks."),
    ],
    "test": [
        ("What is a sine sweep?", [("a", "A drawing of a wave on a wall"), ("b", "A cleaning cloth"), ("c", "A music song"), ("d", "A sine wave whose frequency rises slowly through a range")], "d"),
        ("What does coherence show?", [("a", "The colour of the machine"), ("b", "Whether the output is caused by the input at each frequency"), ("c", "The price of the test"), ("d", "The number of workers")], "b"),
        ("What does a low coherence value warn of?", [("a", "A perfect test"), ("b", "A new paint job"), ("c", "A longer lunch break"), ("d", "Noise, nonlinearity or a poor measurement")], "d"),
        ("What reduces the effect of random noise on the estimate?", [("a", "Testing once only"), ("b", "Turning the sensors off"), ("c", "Averaging several sweeps"), ("d", "Ignoring the peaks")], "c"),
        ("What do the peaks in a response show?", [("a", "Natural frequencies"), ("b", "The name of the operator"), ("c", "The weather"), ("d", "The cost of the machine")], "a"),
    ],
}
