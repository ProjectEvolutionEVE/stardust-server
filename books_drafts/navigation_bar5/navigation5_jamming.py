"""Jamming and Interference Detection: what jammers are, how receivers see them, and how to respond."""
CODE = "navigation5_jamming"
BOOK = {
    "title": "Jamming and Interference Detection",
    "subtitle": "Spotting noise that drowns out satellite signals",
    "chapters": [
        ("Jammers", "A jammer is a transmitter that drowns out satellite signals with noise. Jammers range from small handheld units to large high-power ones."),
        ("Power spectra", "A receiver can look at the power spectrum of its input. A jammer shows up as a bump or spike at the frequencies the satellites use."),
        ("Automatic gain", "Automatic gain control adjusts the receiver's amplifier to keep the signal level steady. A jammer can push the gain down, which is a warning sign."),
        ("Detection", "Receivers combine spectrum, gain and signal-quality tests to detect interference. Good detection gives a clear warning to the user."),
        ("Response", "When jamming is found, the receiver can warn the user, switch to other signals or rely less on satellite positions. The right response depends on the application."),
        ("Mitigation", "Mitigation includes better antennas, filters and the use of several satellite systems. Good planning reduces the risk of losing a position."),
    ],
    "test": [
        ("What is a jammer?",
         [("a", "A jam maker"), ("b", "A fruit"), ("c", "A type of map"), ("d", "A transmitter that drowns out satellite signals with noise")], "d"),
        ("What shows a jammer in a power spectrum?",
         [("a", "The shape of a leaf"), ("b", "A flat, blank line"), ("c", "A bump or spike at the signal frequencies"), ("d", "A number")], "c"),
        ("What does automatic gain control do?",
         [("a", "Keeps the signal level steady"), ("b", "Changes colours"), ("c", "Prints maps"), ("d", "Cuts power")], "a"),
        ("Which combination helps detect interference?",
         [("a", "Paper and ink"), ("b", "Spectrum, gain and signal-quality tests"), ("c", "Music and dance"), ("d", "A bus timetable")], "b"),
        ("What is a good mitigation?",
         [("a", "Better filters and antennas"), ("b", "Ignoring the warning"), ("c", "Turning off the sky"), ("d", "Using paper maps only")], "a"),
    ],
}
