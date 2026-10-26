"""Case Study: Apollo 11's Landing. Program alarms, a boulder field, a hand-flown descent and a tight fuel margin."""
CODE = 'flight4_apollo11_alarms'
BOOK = {
    "title": "Case Study: Apollo 11's Landing",
    "subtitle": "Alarms, a rough landing site and a calm team",
    "chapters": [
        ("Descent",
         "On 20 July 1969 the lunar module Eagle began its descent toward the Moon. The planned landing site was rougher than expected, with large boulders, so the crew had to look for a new spot."),
        ("The alarms",
         "During the descent the guidance computer kept showing program alarms, which meant it was overloaded. Mission controllers judged the alarms safe to continue, because the computer kept doing the essential tasks. The team had trained for this kind of warning."),
        ("The boulder field",
         "Armstrong took over steering by hand and flew the craft past a crater with boulders. He searched for a flat and safe area. Every second of that search used up fuel."),
        ("The fuel margin",
         "The lander had very little fuel left when it touched down. The margin was tight. Good planning and calm flying made the difference."),
        ("Calm control",
         "In Mission Control the team stayed calm, gave clear calls and made fast decisions. The flight director used a short poll to confirm that everyone agreed to continue."),
        ("What the landing teaches",
         "The landing shows the value of training for alarms, trusting the team, and keeping your head when the plan changes. A calm pilot and a calm team made the choice a safe one."),
    ],
    "test": [
        ("What was the lunar module called?",
         [("a", "Columbia"), ("b", "Eagle"), ("c", "Gemini"), ("d", "Challenger")], "b"),
        ("What did the computer keep showing during the descent?",
         [("a", "Program alarms"), ("b", "Weather reports"), ("c", "Music"), ("d", "Menus")], "a"),
        ("Who took over steering by hand?",
         [("a", "The flight doctor"), ("b", "Mission Control"), ("c", "Neil Armstrong"), ("d", "A robot")], "c"),
        ("What was tight at touchdown?",
         [("a", "The launch window"), ("b", "The fuel margin"), ("c", "The radio"), ("d", "The camera")], "b"),
        ("What did the flight director use to confirm agreement?",
         [("a", "A vote of the crew"), ("b", "A go or no-go poll"), ("c", "A letter"), ("d", "A song on the radio")], "b"),
    ],
}
