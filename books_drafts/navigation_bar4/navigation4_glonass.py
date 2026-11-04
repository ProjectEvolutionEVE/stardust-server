"""GLONASS and Frequency-Division Access: satellites sharing the sky by using different frequencies."""
CODE = "navigation4_glonass"
BOOK = {
    "title": "GLONASS and Frequency-Division Access",
    "subtitle": "Satellites sharing the sky by taking different frequencies",
    "chapters": [
        ("Frequency-division access", "GLONASS satellites use frequency-division access. Each satellite broadcasts on its own frequency channel. Receivers tune to the channel of each satellite they track."),
        ("Its history", "GLONASS was built by the Soviet Union and later run by Russia. It has gone through periods of decline and renewal. It is one of the main global satellite navigation systems."),
        ("Orbit slots", "GLONASS satellites occupy slots in three orbital planes. The slots are arranged so that the constellation covers the whole Earth. Each satellite has its own place in the plan."),
        ("Satellites sharing a frequency", "Some satellites can share the same frequency channel when they sit on opposite sides of the Earth. A receiver never sees both at once. This makes efficient use of the band."),
        ("The national system", "GLONASS is run by the Russian government. It works alongside other systems. Many receivers use several systems at once."),
        ("The receiver's task", "A receiver must tune to each satellite's channel. It then decodes the signals and works out its position. Multi-system receivers combine GLONASS with GPS and other systems."),
    ],
    "test": [
        ("What is frequency-division access?",
         [("a", "All satellites use one frequency"), ("b", "Satellites take turns at night"), ("c", "Each satellite broadcasts on its own frequency channel"), ("d", "Satellites send letters by post")], "c"),
        ("Which country built GLONASS?",
         [("a", "Japan"), ("b", "The Soviet Union"), ("c", "Brazil"), ("d", "Italy")], "b"),
        ("How many orbital planes does GLONASS use?",
         [("a", "Three"), ("b", "Ten"), ("c", "One"), ("d", "Thirty")], "a"),
        ("Why can some GLONASS satellites share a channel?",
         [("a", "They are the same satellite"), ("b", "They are very close together"), ("c", "They are switched off"), ("d", "They sit on opposite sides of the Earth")], "d"),
        ("What does a receiver do with the channels?",
         [("a", "It tunes to each satellite's channel"), ("b", "It paints the satellites"), ("c", "It stops listening"), ("d", "It sends letters")], "a"),
    ],
}
