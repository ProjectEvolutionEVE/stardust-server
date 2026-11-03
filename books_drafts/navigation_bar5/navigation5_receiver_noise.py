"""Thermal Noise and the Receiver's Floor: noise temperature, carrier-to-noise ratio, tracking threshold and the link budget."""
CODE = "navigation5_receiver_noise"
BOOK = {
    "title": "Thermal Noise and the Receiver's Floor",
    "subtitle": "How much noise a signal must rise above",
    "chapters": [
        ("Noise is everywhere", "Every receiver has thermal noise from its electronics and antenna. The noise sets a floor below which a signal cannot be tracked."),
        ("Noise temperature", "Noise temperature is one way to describe the noise power of a receiver. A lower noise temperature means a quieter receiver."),
        ("Carrier-to-noise ratio", "The carrier-to-noise ratio compares signal power with noise density. It is a key measure of signal quality."),
        ("Tracking threshold", "Below a certain carrier-to-noise ratio, a receiver cannot keep its loops locked. Designers keep a margin above this threshold."),
        ("Antenna gain", "A higher-gain antenna helps the signal stand out from the noise. The antenna must be aimed well at the sky to get that gain."),
        ("Link budget and margins", "A link budget adds up gains and losses to find the signal level at the receiver. Margins protect the link against fading and other losses."),
    ],
    "test": [
        ("What is thermal noise?",
         [("a", "A loud sound"), ("b", "Random noise from electronics and the antenna"), ("c", "A colour"), ("d", "A menu")], "b"),
        ("What does the carrier-to-noise ratio compare?",
         [("a", "Price and size"), ("b", "Time and weight"), ("c", "Colour and taste"), ("d", "Signal power with noise density")], "d"),
        ("What happens below the tracking threshold?",
         [("a", "The receiver cannot keep its loops locked"), ("b", "The map gets bigger"), ("c", "The battery grows"), ("d", "It prints")], "a"),
        ("What does a higher-gain antenna do?",
         [("a", "Makes the noise louder"), ("b", "Turns the sky grey"), ("c", "Helps the signal stand out from the noise"), ("d", "Removes the satellite")], "c"),
        ("What does a link budget do?",
         [("a", "Adds gains and losses to find the signal level"), ("b", "Prints paper"), ("c", "Colours a map"), ("d", "Counts pencils")], "a"),
    ],
}
