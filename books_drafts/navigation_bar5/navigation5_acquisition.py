"""Signal Acquisition by FFT: searching for a satellite's Doppler shift and code phase, and doing it quickly with the FFT."""
CODE = "navigation5_acquisition"
BOOK = {
    "title": "Signal Acquisition by FFT",
    "subtitle": "Finding a satellite before tracking it",
    "chapters": [
        ("Finding the signal", "Before a receiver can track a satellite, it must first find the signal. This first step is called acquisition."),
        ("The Doppler search", "The motion of the satellite shifts the signal's frequency, which is the Doppler effect. The receiver searches a range of frequencies to match the shift."),
        ("The code phase search", "The receiver also searches for the timing offset of the spreading code, called the code phase. Together, the two searches form a grid of possible answers."),
        ("FFT correlation", "The Fast Fourier Transform, or FFT, lets the receiver test many code phases at once. This cuts the processing time greatly."),
        ("Noise and time", "A weak signal needs a longer integration time to stand out from the noise. More processing time gives more reliable acquisition."),
        ("Hardware", "Receivers use parallel channels and fast processors to speed acquisition. Simpler receivers use simpler methods that take longer."),
    ],
    "test": [
        ("What is acquisition?",
         [("a", "Printing a map"), ("b", "Finding a satellite signal before tracking it"), ("c", "Painting a car"), ("d", "Stopping a clock")], "b"),
        ("What does the Doppler effect change?",
         [("a", "Colour"), ("b", "The size of paper"), ("c", "The time of day"), ("d", "The frequency of the signal")], "d"),
        ("What is a code phase?",
         [("a", "The timing offset of the spreading code"), ("b", "A colour"), ("c", "The fuel level"), ("d", "The speed of a car")], "a"),
        ("What does the FFT help with?",
         [("a", "Painting"), ("b", "Printing"), ("c", "Testing many code phases at once"), ("d", "Typing")], "c"),
        ("What helps a weak signal stand out from noise?",
         [("a", "Skipping the search"), ("b", "Turning the screen off"), ("c", "Driving faster"), ("d", "A longer integration time")], "d"),
    ],
}
