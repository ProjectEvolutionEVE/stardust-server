"""Accelerometers and Vibration Measurement: the sensors that turn shaking into a signal, and how to mount and read them well."""
CODE = "engineering5_accelerometer"
BOOK = {
    "title": "Accelerometers and Vibration Measurement",
    "subtitle": "Piezoelectric and MEMS sensors, mounting and frequency range",
    "chapters": [
        ("Measuring shake", "An accelerometer turns acceleration, the rate of change of speed, into an electrical signal. Vibration is a repeated acceleration, so the sensor is the tool for measuring it."),
        ("Piezoelectric sensors", "Some crystals produce an electrical charge when they are squeezed. Piezoelectric accelerometers use this effect and cover a wide range of vibration levels and frequencies."),
        ("MEMS sensors", "MEMS sensors are tiny silicon structures made with methods similar to computer chips. They are small and cheap, and they appear in phones and cars, though they may have a narrower range than the best piezoelectric types."),
        ("Mounting", "How a sensor is fixed to a part changes what it reads. A loose or badly placed mount can add false peaks, so the mounting method matters as much as the sensor."),
        ("Sensitivity and range", "Sensitivity is the signal produced per unit of acceleration. Frequency range is the band over which the sensor measures accurately, and both must suit the job."),
        ("Data acquisition", "The signal must be sampled and recorded properly, following the rules for sample rate and filtering. Otherwise the vibration data will mislead the engineer."),
    ],
    "test": [
        ("What does an accelerometer measure?", [("a", "Acceleration, the change in speed"), ("b", "The colour of the surface"), ("c", "Sound pitch only"), ("d", "The mass of a bolt")], "a"),
        ("How do piezoelectric sensors work?", [("a", "They glow when heated"), ("b", "They freeze at low temperature"), ("c", "They make an electrical charge when squeezed"), ("d", "They float in oil")], "c"),
        ("What are MEMS sensors made of?", [("a", "Tiny silicon structures, similar to chips"), ("b", "Solid wood blocks"), ("c", "Beeswax"), ("d", "Rubber")], "a"),
        ("Why does mounting matter?", [("a", "It changes the colour of the reading"), ("b", "It stops the sound from the part"), ("c", "It lightens the signal"), ("d", "A loose mount can add false peaks to the reading")], "d"),
        ("What is sensitivity?", [("a", "The signal produced per unit of acceleration"), ("b", "The price of the sensor"), ("c", "The weight of the cables"), ("d", "The number of wires in the sensor")], "a"),
    ],
}
