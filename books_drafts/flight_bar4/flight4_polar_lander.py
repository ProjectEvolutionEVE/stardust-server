"""Case Study: Mars Polar Lander, 1999. A planned landing, leg sensors, an early engine cut-off and no data."""
CODE = 'flight4_polar_lander'
BOOK = {
    "title": "Case Study: Mars Polar Lander, 1999",
    "subtitle": "Leg sensors, an early engine cut-off and what the review found",
    "chapters": [
        ("A planned landing",
         "Mars Polar Lander was sent to land near the south pole of Mars in December 1999. It was meant to dig into the soil and look for water ice."),
        ("The leg sensors",
         "As the lander came down, its legs were meant to open and touch the surface. Sensors on the legs sent signals that may have been read as a touchdown too early."),
        ("The likely cause",
         "The most likely cause was that false signals from the leg sensors told the engines to shut off too soon, while the craft was still above the ground. The team could never confirm this, because the lander stayed silent."),
        ("No data",
         "Contact was never made after the landing attempt. The mission was lost, and no science came back. It was a painful blow to the team."),
        ("The review",
         "A review board studied the loss and looked at how the tests had been planned. It found that the tests had not covered every case that could happen."),
        ("Lessons",
         "Polar Lander teaches that a sensor's signal must be tested under the conditions it will really meet. A small assumption can cost a whole mission."),
    ],
    "test": [
        ("What was Mars Polar Lander going to look for?",
         [("a", "Water ice"), ("b", "Gold"), ("c", "Radio stations"), ("d", "Birds")], "a"),
        ("Which sensors were involved in the likely cause?",
         [("a", "Cloud sensors"), ("b", "Engine sensors"), ("c", "Eye sensors"), ("d", "Leg sensors")], "d"),
        ("What may have happened to the engines?",
         [("a", "They shut off too soon"), ("b", "They grew bigger"), ("c", "They painted themselves"), ("d", "They sang")], "a"),
        ("What happened after the landing attempt?",
         [("a", "Contact was made"), ("b", "No contact was ever made"), ("c", "It flew home"), ("d", "It made music")], "b"),
        ("What is the main lesson?",
         [("a", "Never send landers"), ("b", "Sensors do not matter"), ("c", "Test sensors under the conditions they will meet"), ("d", "Mars is safe")], "c"),
    ],
}
