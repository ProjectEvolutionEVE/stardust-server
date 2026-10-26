"""A Day in the Life of a Ship's Captain: rounds, checks, paperwork and decisions in a working day at sea."""
CODE = "flight5_h_captain_day"
BOOK = {
    "title": "A Day in the Life of a Ship's Captain",
    "subtitle": "Rounds, checks, paperwork and decisions in a working day at sea",
    "chapters": [
        ("Morning",
         "A ship's captain often starts early by reviewing the night's log, the weather and the course. The information gathered here shapes everything that follows."),
        ("Watch checks",
         "The captain confirms that each watch is staffed and that the officers know the plan. Good handovers prevent mistakes at shift changes."),
        ("Rounds",
         "Captains walk the ship to see its condition and speak with the crew. Being seen and listening keeps standards high."),
        ("Paperwork",
         "Logs, reports, certificates and orders take a good share of the day. Accurate records protect people and the ship."),
        ("Crew time",
         "Captains make time for their crew, from meals to training to personal troubles. Trust grows when people feel heard."),
        ("End of day",
         "The day ends with a final check, a review of tomorrow's plan and a handover to the night watch. A calm end keeps the next day steady."),
    ],
    "test": [
        ("What does a captain review in the morning?",
         [("a", "Sports scores"), ("b", "Recipes"), ("c", "The night's log, the weather and the course"), ("d", "Films")], "c"),
        ("Why are handovers important?",
         [("a", "They are a celebration"), ("b", "They prevent mistakes at shift changes"), ("c", "They save paper"), ("d", "They stop the ship")], "b"),
        ("What do logs and reports help protect?",
         [("a", "Paint"), ("b", "Music"), ("c", "Fuel prices"), ("d", "People and the ship")], "d"),
        ("What does walking the ship achieve?",
         [("a", "Seeing its condition and speaking with the crew"), ("b", "Losing weight"), ("c", "Counting seagulls"), ("d", "Cleaning the windows")], "a"),
        ("How does a captain build trust?",
         [("a", "By ignoring the crew"), ("b", "By making time to listen"), ("c", "By shouting orders"), ("d", "By hiding plans")], "b"),
    ],
}
