"""Sensors and Their Errors: why no sensor is perfect, and how engineers check and combine their readings."""
CODE = "flight5_s_sensors"
BOOK = {
    "title": "Sensors and Their Errors",
    "subtitle": "Why no sensor is perfect, and how engineers check them",
    "chapters": [
        ("What a sensor does",
         "A sensor turns a physical quantity, such as temperature or speed, into an electrical signal. Every sensor has limits, so its readings must be treated with care."),
        ("Noise",
         "Noise is random jitter in a reading. Averaging several readings can reduce it, but averaging cannot remove a true error."),
        ("Bias",
         "Bias is a steady offset, where the sensor always reads a little high or a little low. Bias must be found and corrected, usually by calibration."),
        ("Scale error",
         "A scale error means the reading grows too fast or too slowly compared with the real value. Calibrating at several points reveals it."),
        ("Cross checks",
         "Engineers compare one sensor with another that measures the same thing. A mismatch shows that one of them may be wrong."),
        ("Sensor fusion",
         "Sensor fusion combines several imperfect readings into one better estimate. The result is often more accurate than any single sensor could give."),
    ],
    "test": [
        ("What does a sensor do?",
         [("a", "Paints a surface"), ("b", "Turns a physical quantity into an electrical signal"), ("c", "Lights up a room"), ("d", "Makes fuel")], "b"),
        ("What is noise in a reading?",
         [("a", "A steady offset"), ("b", "A colour"), ("c", "A spark"), ("d", "Random jitter")], "d"),
        ("What is bias?",
         [("a", "A steady offset in readings"), ("b", "A type of fuel"), ("c", "A kind of bolt"), ("d", "A radio mode")], "a"),
        ("How do engineers check a sensor for errors?",
         [("a", "They never look at it"), ("b", "They switch off the lights"), ("c", "They compare it with another sensor measuring the same thing"), ("d", "They ask a passenger")], "c"),
        ("What is sensor fusion?",
         [("a", "Melting sensors together"), ("b", "A kind of weld"), ("c", "A sensor that breaks"), ("d", "Combining several readings into one better estimate")], "d"),
    ],
}
