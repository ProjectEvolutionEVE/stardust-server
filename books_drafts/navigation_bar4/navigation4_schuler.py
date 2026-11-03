"""The Schuler period: the 84-minute natural period that shapes how inertial navigation errors behave, and how damping and tuning respond to it."""
CODE = "navigation4_schuler"
BOOK = {
    "title": "The Schuler Period",
    "subtitle": "An 84-minute rhythm inside every inertial system",
    "chapters": [
        ("An 84-minute pendulum", "Imagine a pendulum as long as the Earth's radius. It would swing back and forth in about 84 minutes. This is the Schuler period, and inertial systems share this natural rhythm."),
        ("Where the period comes from", "The period depends on Earth's radius and on the strength of gravity at its surface. It does not depend on the mass of the pendulum. With these numbers the value comes out close to 84 minutes."),
        ("Why errors oscillate", "A small tilt error in an inertial system does not grow steadily. Instead it swings back and forth at the Schuler period. Long-term errors therefore show up as slow oscillations."),
        ("Damping the error", "Damping reduces these oscillations so that the errors die away rather than repeat. Designers can add damping in the software that corrects the platform. A damped system is more stable on a long journey."),
        ("Tuning a system", "A navigation system is tuned so that its correcting loop matches the Schuler period. Tuning too strongly or too weakly causes problems. The right tuning gives good accuracy over many hours."),
        ("Design choices", "Engineers use the Schuler period when deciding how often to correct the system and how much weight to give outside aids. Understanding it helps a navigator judge when errors can be trusted. It is a core idea for anyone who designs or flies inertial systems."),
    ],
    "test": [
        ("What is the approximate Schuler period?", [("a", "About 24 hours"), ("b", "About 84 minutes"), ("c", "About 8 seconds"), ("d", "About 12 days")], "b"),
        ("Which two things set the Schuler period?", [("a", "The colour of the case and the day of the week"), ("b", "The mass of the pendulum"), ("c", "The number of satellites in view"), ("d", "Earth's radius and the strength of gravity")], "d"),
        ("How do errors in an inertial system behave?", [("a", "They swing back and forth at the Schuler period"), ("b", "They grow steadily without limit"), ("c", "They vanish the moment the unit is switched on"), ("d", "They stay exactly the same forever")], "a"),
        ("What is damping for?", [("a", "It makes the unit heavier"), ("b", "It turns the signal off during climbs"), ("c", "It makes the errors die away instead of repeating"), ("d", "It stops the satellites from moving")], "c"),
        ("Why is tuning important?", [("a", "It makes the paint dry faster"), ("b", "It gives good accuracy over many hours"), ("c", "It removes the need for any calibration"), ("d", "It makes the unit silent")], "b"),
    ],
}
