"""Stochastic Processes in Engineering: describing random signals with autocorrelation, stationarity and ergodicity, and modelling noise that engineers meet every day."""
CODE = "engineering5_stoch_proc"
BOOK = {
    "title": "Stochastic Processes in Engineering",
    "subtitle": "Describing random signals so their behaviour can be predicted and tested",
    "chapters": [
        ("Random variables over time", "A stochastic process is a random quantity that changes over time. A noisy sensor reading or a wind speed is one. Each value is random, but the process has patterns that engineers can describe."),
        ("Autocorrelation", "The autocorrelation measures how strongly a signal at one time matches the same signal after a delay. It shows how long the memory of the signal lasts. It is the time-domain partner of the power spectrum."),
        ("Stationarity", "A process is stationary when its statistical properties do not change with time. Its mean is constant, and its autocorrelation depends only on the time gap. Many analysis tools assume stationarity."),
        ("Ergodicity", "An ergodic process is one where a single long record gives the same statistics as averaging over many copies. This lets engineers learn the statistics from one measurement. It is often assumed but should be checked."),
        ("Modelling noise", "Noise can be modelled as white, meaning it has the same power at all frequencies, or as coloured, meaning it has a shaped spectrum. Most sensor noise is closer to coloured. The model is chosen to match measured data."),
        ("Using the models", "Stochastic models are used in filters, controllers and reliability studies. They help engineers judge how much noise a design can take. The results are only as good as the assumptions behind them."),
    ],
    "test": [
        ("What is a stochastic process?", [("a", "A fixed number on a page"), ("b", "A kind of paint"), ("c", "A random quantity that changes over time"), ("d", "A type of gear")], "c"),
        ("What does autocorrelation measure?", [("a", "How strongly a signal matches itself after a delay"), ("b", "The colour of a signal"), ("c", "The price of a sensor"), ("d", "The number of cables")], "a"),
        ("When is a process stationary?", [("a", "When it never moves"), ("b", "When it is switched off"), ("c", "When it is painted"), ("d", "When its statistical properties do not change with time")], "d"),
        ("What does ergodicity allow an engineer to do?", [("a", "Stop all measurements"), ("b", "Learn the statistics from one long record"), ("c", "Change the colour of the signal"), ("d", "Skip the model")], "b"),
        ("What is white noise?", [("a", "Noise that is always silent"), ("b", "Noise made only of paint"), ("c", "Noise that only happens at night"), ("d", "Noise with the same power at all frequencies")], "d"),
    ],
}
