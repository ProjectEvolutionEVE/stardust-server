"""Frame Stiffness and Frequency Response Testing: frame stiffness, impact hammer tests, damping, dynamic stiffness and reading a frequency response function."""
CODE = "engineering5_frame_dyn"
BOOK = {
    "title": "Frame Stiffness and Frequency Response Testing",
    "subtitle": "Measuring how a machine frame bends and rings",
    "chapters": [
        ("Stiff frames make good parts",
         "A machine frame that bends under load lets the tool move off its path. Stiffness is how much force it takes to bend the frame a set amount. A stiff frame helps keep the cut accurate and quiet."),
        ("The impact hammer test",
         "In an impact hammer test, a small instrumented hammer taps the frame. A sensor on the frame records how it responds. The tap is quick, and it excites the frame across many frequencies at once."),
        ("Damping",
         "Damping is how quickly the frame's vibration dies away. A damped frame stops ringing fast, which keeps the cut smooth. Damping can come from the materials, the joints and added damping devices."),
        ("Dynamic stiffness",
         "Dynamic stiffness is the stiffness of the frame at a particular frequency. It can be much lower than the static stiffness at resonance. Machines are tuned so the cutting frequencies avoid the weak spots."),
        ("Reading a frequency response function",
         "A frequency response function, or FRF, shows how the frame responds to force at each frequency. Its peaks mark resonances. The height and width of each peak show how stiff and how well damped that mode is."),
        ("Using the results",
         "Engineers use the FRF to change the frame, to pick cutting speeds that avoid chatter, and to check a redesign. Testing costs time and equipment, but it prevents guesswork and costly rework."),
    ],
    "test": [
        ("What does frame stiffness measure?",
         [("a", "How much force it takes to bend the frame a set amount"), ("b", "The colour of the frame"), ("c", "The number of bolts in the frame"), ("d", "The age of the workers")], "a"),
        ("What does the impact hammer test do?",
         [("a", "It paints the frame"), ("b", "It taps the frame and records its response"), ("c", "It cuts the frame in half"), ("d", "It cools the frame in ice")], "b"),
        ("What is damping?",
         [("a", "How heavy the frame is"), ("b", "How loud the motor is"), ("c", "How quickly the frame's vibration dies away"), ("d", "How bright the paint is")], "c"),
        ("What does an FRF show?",
         [("a", "The price of the frame"), ("b", "The name of the supplier"), ("c", "The number of hours worked"), ("d", "How the frame responds to force at each frequency")], "d"),
        ("What do the peaks on an FRF mark?",
         [("a", "Resonances of the frame"), ("b", "The colour changes"), ("c", "The positions of the workers"), ("d", "The sizes of the bolts")], "a"),
    ],
}
