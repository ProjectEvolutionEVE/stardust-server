"""Vibration and Sensor Noise: vibration rectification, sensor response, mounts, spectra and damping."""
CODE = "navigation5_vibration"
BOOK = {
    "title": "Vibration and Sensor Noise",
    "subtitle": "How shaking can look like motion",
    "chapters": [
        ("Shaking and sensing", "Vibration can make a sensor report motion that is not really there. Engineers design mounts and filters to reduce these effects."),
        ("Vibration rectification", "Vibration rectification is an error in which high-frequency vibration produces an average shift in a sensor's output. The shift can look like drift."),
        ("Sensor response", "Each sensor has a frequency response that shows how it reacts to vibration at different frequencies. Designers check this response before they choose a sensor."),
        ("Mounts", "Mounts that isolate vibration help keep a sensor steady. Their stiffness and damping must be chosen with care."),
        ("Spectra", "A vibration spectrum shows how the energy is spread across frequencies. Test engineers use spectra to plan their tests."),
        ("Damping", "Damping reduces the size of vibrations. Designers add it with suitable materials and mount design."),
    ],
    "test": [
        ("What can vibration cause a sensor to read?",
         [("a", "A sunny day"), ("b", "A chair"), ("c", "A sound"), ("d", "Motion that is not really there")], "d"),
        ("What is vibration rectification?",
         [("a", "An error that gives an average shift from high-frequency vibration"), ("b", "A painting"), ("c", "A rope"), ("d", "A bridge")], "a"),
        ("What does a sensor's frequency response show?",
         [("a", "Its colour"), ("b", "Its price"), ("c", "How it reacts to vibration at different frequencies"), ("d", "Its age")], "c"),
        ("What do isolating mounts do?",
         [("a", "Add noise"), ("b", "Help keep sensors steady"), ("c", "Paint sensors"), ("d", "Sink")], "b"),
        ("What does damping do?",
         [("a", "Increases shaking"), ("b", "Adds colour"), ("c", "Makes a clock"), ("d", "Reduces the size of vibrations")], "d"),
    ],
}
