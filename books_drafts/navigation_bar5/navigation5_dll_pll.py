"""Delay and Phase Lock Loops: how a receiver keeps step with a satellite signal, and what can break that."""
CODE = "navigation5_dll_pll"
BOOK = {
    "title": "Delay and Phase Lock Loops",
    "subtitle": "How a receiver keeps step with the signal",
    "chapters": [
        ("Tracking the signal", "A satellite receiver must keep track of the signal's timing and frequency. Two loops do this work: the code tracking loop and the carrier tracking loop."),
        ("Code tracking", "The delay lock loop, or DLL, lines up a local copy of the spreading code with the incoming signal. It seeks the point where the match is strongest."),
        ("Carrier tracking", "The phase lock loop, or PLL, follows the phase and frequency of the carrier wave. It keeps the local carrier in step with the incoming one."),
        ("Noise bandwidth", "A narrow loop bandwidth reduces noise but reacts slowly to change. A wide bandwidth follows fast changes but lets in more noise."),
        ("Loss of lock", "If the signal is weak, or the receiver moves very fast, a loop can lose lock. The receiver must then search for the signal again."),
        ("Tuning", "Engineers set the bandwidth and damping of each loop to balance noise against response. Signal strength also affects the best choice."),
    ],
    "test": [
        ("What are the two main tracking loops?",
         [("a", "Sound and light"), ("b", "Gears and belts"), ("c", "Code tracking and carrier tracking"), ("d", "Day and night")], "c"),
        ("What does a delay lock loop line up?",
         [("a", "The screen brightness"), ("b", "The antenna colour"), ("c", "The printer"), ("d", "A local copy of the code with the incoming signal")], "d"),
        ("What does a phase lock loop follow?",
         [("a", "The price of fuel"), ("b", "The time of day"), ("c", "The phase and frequency of the carrier"), ("d", "The weather")], "c"),
        ("What is the trade-off of a narrow noise bandwidth?",
         [("a", "Less noise, but a slower response"), ("b", "More noise, and a faster response"), ("c", "No effect at all"), ("d", "No receiver is needed")], "a"),
        ("What happens when a loop loses lock?",
         [("a", "The receiver must search for the signal again"), ("b", "The receiver turns into a radio"), ("c", "The battery is recharged"), ("d", "The map is printed")], "a"),
    ],
}
