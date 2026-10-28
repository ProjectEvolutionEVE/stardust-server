"""Noise Control: sound from machines, decibels, enclosures, damping and vibration isolation."""
CODE = "engineering4_noise_control"
BOOK = {
    "title": "Noise Control: Sound From Machines",
    "subtitle": "Decibels, sources, enclosures and damping",
    "chapters": [
        ("Sound and decibels",
         "Sound level is measured in decibels, on a logarithmic scale. Every 10 decibels is a tenfold rise in sound power. A small rise on the scale therefore means a large rise in energy."),
        ("Where noise comes from",
         "Machines make sound when their surfaces vibrate, when air moves, and when fluid flows through them. Gears, fans, pumps and motors are common sources. Finding the main source is the first step."),
        ("Enclosures",
         "A sound enclosure wraps a noisy machine in a heavy, lined panel. It blocks the sound from getting out. Gaps and openings let sound leak past the lining, so they must be sealed."),
        ("Damping",
         "Damping removes energy from a vibrating panel, so it rings less. A layer of damping material on thin metal reduces the ringing."),
        ("Isolation of vibration",
         "Springs or rubber mounts stop vibration passing from a machine into the floor or frame. A machine that shakes its mount can still make noise through the frame."),
        ("Hearing protection limits",
         "Ear protection lowers the noise that reaches the listener, but it does not reduce the noise the machine makes. Health rules set limits on exposure time. Use controls at the source first."),
    ],
    "test": [
        ("By how much does sound power rise for every 10 decibels?",
         [("a", "Twice"), ("b", "Ten times"), ("c", "One hundred times"), ("d", "Ten percent")], "b"),
        ("Which is a common source of machine noise?",
         [("a", "Gears and fans"), ("b", "Clean water"), ("c", "Dry air"), ("d", "Sunlight")], "a"),
        ("What does a sound enclosure do?",
         [("a", "Amplifies the noise"), ("b", "Blocks sound from leaving the machine"), ("c", "Cools the motor"), ("d", "Stores energy")], "b"),
        ("What do damping layers do to a vibrating panel?",
         [("a", "Make it heavier"), ("b", "Make it hotter"), ("c", "Make it ring less"), ("d", "Make it flow")], "c"),
        ("Why is ear protection not the first fix for machine noise?",
         [("a", "It makes machines louder"), ("b", "It protects only the listener and does not reduce the noise the machine makes"), ("c", "It is free of cost"), ("d", "Noise always needs it")], "b"),
    ],
}
