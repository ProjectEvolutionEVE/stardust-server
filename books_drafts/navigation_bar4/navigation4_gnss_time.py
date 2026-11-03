"""GNSS time transfer: how navigation satellites distribute time, offsets between time scales, and calibration."""
CODE = "navigation4_gnss_time"
BOOK = {
    "title": "GNSS Time Transfer",
    "subtitle": "How satellites carry the time, and how receivers keep it",
    "chapters": [
        ("Time from satellites", "Navigation satellites carry very accurate atomic clocks. Their signals tell a receiver the exact time, so a receiver can act as a clock too. This is called time transfer."),
        ("Offsets between systems", "Each satellite system keeps its own time scale. GPS time, for example, does not add leap seconds, so it differs from UTC by a whole number of seconds. Receivers must apply the offset to report the time correctly."),
        ("The receiver as a clock", "A receiver's own clock is not as good as the satellite clocks, so it drifts. The receiver estimates its clock error along with its position. A good receiver can then give a steady time signal."),
        ("The link to UTC", "UTC is the world's standard time, kept by national laboratories working together. Satellite systems publish their offsets from UTC, so users can convert. Correct conversion needs the current offset."),
        ("Who uses precise time", "Telecom networks, power grids, banks and science labs all depend on accurate time. For these users timing can matter more than position. A fixed antenna can be a very stable timing source."),
        ("Calibration", "A timing receiver is calibrated against a known reference. Checks against national time services show whether it is on track. Regular checks catch drift before it causes harm."),
    ],
    "test": [
        ("What does GNSS time transfer take from the satellites?", [("a", "Free water and power"), ("b", "Photographs of the ground"), ("c", "The exact time carried in their signals"), ("d", "The colour of the sky")], "c"),
        ("Why does GPS time differ from UTC?", [("a", "GPS time runs on a different calendar day"), ("b", "The satellites sit in a different time zone"), ("c", "The receiver always adds an hour"), ("d", "GPS time does not add leap seconds, so it is offset by a whole number of seconds")], "d"),
        ("What does a receiver usually estimate along with its position?", [("a", "Its own clock error"), ("b", "The number of birds nearby"), ("c", "The colour of the antenna"), ("d", "The price of the receiver")], "a"),
        ("Who keeps the world's standard time, UTC?", [("a", "Shipping companies"), ("b", "Weather services"), ("c", "A single private company"), ("d", "National time laboratories working together")], "d"),
        ("Which of these depends on accurate time?", [("a", "A paper map"), ("b", "Telecom networks and power grids"), ("c", "A wooden boat"), ("d", "A kitchen recipe")], "b"),
    ],
}
