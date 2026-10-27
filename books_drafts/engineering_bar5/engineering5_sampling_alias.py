"""Sampling, Aliasing and Anti-Alias Filters: how a digital system measures a signal, and how a signal can be misread if it is sampled too slowly."""
CODE = "engineering5_sampling_alias"
BOOK = {
    "title": "Sampling, Aliasing and Anti-Alias Filters",
    "subtitle": "Sample rates, false frequencies and keeping the data honest",
    "chapters": [
        ("Sampling a signal", "A digital system measures a signal at regular moments. This is sampling. The samples are the only picture of the signal the system will ever have."),
        ("The Nyquist rate", "To capture a frequency correctly, the sample rate must be more than twice that frequency. Twice the highest frequency of interest is the Nyquist rate, and it sets the lowest safe sample rate."),
        ("Aliasing", "A signal sampled too slowly appears in the data as a false, lower frequency. This false signal is called an alias, and the effect is aliasing. It can look just like a real signal."),
        ("Anti-alias filters", "A filter placed before the sampler removes frequencies above half the sample rate. Without it, those high frequencies fold down into the data as aliases."),
        ("Choosing a sample rate", "Pick a rate well above twice the highest frequency of interest. A margin is needed because real filters do not cut off sharply."),
        ("Data quality", "Aliasing that has entered the data cannot be cleanly removed later. The filter and the sample rate must be right from the start."),
    ],
    "test": [
        ("What is the Nyquist rate for a signal?", [("a", "Half the signal frequency"), ("b", "Twice the highest frequency in the signal"), ("c", "The same as the signal frequency"), ("d", "Ten times slower than the signal")], "b"),
        ("What is aliasing?", [("a", "A false lower frequency that appears when a signal is sampled too slowly"), ("b", "A type of paint for sensors"), ("c", "A kind of resistor"), ("d", "A tool for cutting cables")], "a"),
        ("What does an anti-alias filter do?", [("a", "Removes frequencies above half the sample rate before sampling"), ("b", "Adds noise to the data"), ("c", "Speeds up the computer"), ("d", "Stores the data on a disc")], "a"),
        ("Can aliasing be fixed afterwards?", [("a", "Yes, by smoothing the plot"), ("b", "Yes, by adding a larger screen"), ("c", "No, once it is in the data it cannot be cleanly removed"), ("d", "Yes, by recording for longer")], "c"),
        ("Why leave a margin above twice the highest frequency?", [("a", "Real filters are not perfect, so a margin helps"), ("b", "The sample rate must be zero"), ("c", "The data has no noise"), ("d", "It saves storage space")], "a"),
    ],
}
