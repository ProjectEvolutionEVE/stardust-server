"""Calibration: Knowing What an Instrument Gets Wrong. Scale and alignment, measured so they can be allowed for."""
CODE = "navigation3c_calibration"
BOOK = {
    "title": "Calibration: Knowing What an Instrument Gets Wrong",
    "subtitle": "Scale, alignment and temperature: how to measure an instrument's errors so they can be allowed for",
    "chapters": [
        ("A reading is not the truth",
         "Every instrument has its own quirks. Calibration is the work of finding out how an instrument's readings differ from the true values, so the navigator can correct them. It is done before a flight and checked again during it."),
        ("Scale",
         "A scale error means the reading grows too fast or too slow as the true value grows. A sensor that reads ten percent low on large values, yet is right on small ones, needs its scale corrected as well as its zero point."),
        ("Alignment",
         "Sensors are fixed to the hull by hand, and no mounting is perfect. A sensor set a few degrees out of line reads a mix of the craft's axes. The navigator measures that misalignment once and writes it into the model."),
        ("Temperature",
         "Many sensors change their readings as they warm or cool. A calibration made at one temperature may be wrong at another. Careful navigators record the temperature with each calibration, and check again when an instrument moves to a new environment."),
        ("Calibrating against a known truth",
         "The best calibration compares the sensor with a known standard: a fixed star field, a known rate of rotation, or a set of reference positions. The known value is the truth, and the difference is the error to correct."),
        ("A calibration has a date",
         "A calibration is good only for a time. Parts age, and knocks and heat move things. Write the date on every calibration, and treat an old one as a question rather than an answer."),
    ],
    "test": [
        ("What is the main purpose of calibration?",
         [("a", "To make the instrument louder"), ("b", "To find how its readings differ from true values, so they can be corrected"), ("c", "To paint the sensor"), ("d", "To remove the need for power")], "b"),
        ("What is a scale error?",
         [("a", "A reading that grows too fast or too slow as the true value grows"), ("b", "A sensor painted the wrong colour"), ("c", "A change in the hull's length"), ("d", "A wrong radio channel")], "a"),
        ("Why must a sensor's alignment be measured?",
         [("a", "Because sensors are always perfectly aligned"), ("b", "Because the stars move the hull"), ("c", "Because no mounting is perfect, so a sensor can mix up the craft's axes"), ("d", "Because alignment sets the clock")], "c"),
        ("Why might a calibration made at one temperature be wrong at another?",
         [("a", "Temperature has no effect on anything"), ("b", "Cold makes the craft longer"), ("c", "Heat makes stars brighter"), ("d", "Many sensors change their readings with temperature")], "d"),
        ("What makes a calibration trustworthy over time?",
         [("a", "Never checking it"), ("b", "Recording its date and treating an old one as a question"), ("c", "Painting it on the hull"), ("d", "Copying it from another craft")], "b"),
    ],
}
