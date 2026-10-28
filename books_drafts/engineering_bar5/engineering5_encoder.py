"""Encoders, Resolution and Position Feedback: absolute and incremental encoders, resolution, interpolation, backlash and calibration."""
CODE = "engineering5_encoder"
BOOK = {
    "title": "Encoders, Resolution and Position Feedback",
    "subtitle": "How a machine knows where its parts are",
    "chapters": [
        ("What an encoder does",
         "An encoder measures the position or turning angle of a shaft and reports it as a signal. The controller uses this feedback to know where the machine is. Without it, the machine could only be run blind."),
        ("Absolute and incremental",
         "An absolute encoder gives a unique position code at every angle, so it knows where it is as soon as it powers up. An incremental encoder counts marks as the shaft moves, so it must be homed to find its starting point. Each type suits different jobs."),
        ("Resolution",
         "Resolution is the smallest change in position that an encoder can detect. It is often stated as counts per turn. Higher resolution gives finer control, but it also costs more and demands faster electronics."),
        ("Interpolation",
         "Many encoders output a sine-shaped signal, and interpolation divides each cycle into finer steps. This reads positions far finer than the raw count of lines on the disc. It must be set up carefully, or the readings become uneven."),
        ("Backlash",
         "Backlash is the play, or small gap, between meshing gears or other moving parts. When the direction of motion reverses, the parts must cross this gap before the load moves. A sensor on the motor side may miss this lost motion, so the design must account for it."),
        ("Calibration",
         "Calibration checks that the encoder's readings match the true position of the machine. Engineers compare the readings with a known reference, such as a precise gauge or laser. Regular checks catch drift and damage before they cause scrap."),
    ],
    "test": [
        ("What does an absolute encoder report?",
         [("a", "Its exact position as soon as it powers up, without homing"), ("b", "Its colour"), ("c", "The speed of the sun"), ("d", "The number of cups of coffee")], "a"),
        ("What is resolution in an encoder?",
         [("a", "Brightness of its light"), ("b", "Its paint finish"), ("c", "The smallest position change it can detect"), ("d", "Its price")], "c"),
        ("What is backlash?",
         [("a", "A type of bearing"), ("b", "Play or a gap between meshing parts that causes lost motion"), ("c", "A type of paint"), ("d", "A fuse")], "b"),
        ("What is interpolation in encoder reading?",
         [("a", "Painting between the lines"), ("b", "A kind of cable"), ("c", "A type of fuse"), ("d", "Dividing a sine signal to read positions finer than the raw line count")], "d"),
        ("Why calibrate an encoder?",
         [("a", "To make its readings match the true position"), ("b", "To paint the case"), ("c", "To change its colour"), ("d", "To make it heavier")], "a"),
    ],
}
